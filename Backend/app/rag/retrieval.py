from typing import List, Optional
from qdrant_client.models import ScoredPoint
from fastembed import TextEmbedding
from app.rag.qdrant import search_vectors
from app.core.config import settings
import numpy as np

# Initialize FastEmbedding model (BAAI/bge-small-en-v1.5 - 384 dimensions)
embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

async def generate_embedding(text: str) -> List[float]:
    # FastEmbed returns a generator, so we need to get the first result
    embeddings = list(embedding_model.embed([text]))
    return embeddings[0].tolist()

async def semantic_search(query: str, limit: int = 5) -> List[ScoredPoint]:
    query_vector = await generate_embedding(query)
    search_result = await search_vectors(query_vector, limit)
    return search_result

async def hybrid_search(query: str, selected_text: str, limit: int = 5) -> List[ScoredPoint]:
    query_vector = await generate_embedding(query)
    selected_text_vector = await generate_embedding(selected_text)
    
    # Simple combination: average the vectors
    combined_vector = np.mean([query_vector, selected_text_vector], axis=0).tolist()
    
    search_result = await search_vectors(combined_vector, limit)
    return search_result


async def retrieve_context(query: str, selected_text: Optional[str] = None, limit: int = 5) -> List[dict]:
    if selected_text:
        search_results = await hybrid_search(query, selected_text, limit)
    else:
        search_results = await semantic_search(query, limit)
    
    context_with_sources = []
    for point in search_results:
        if point.payload:
            context_with_sources.append({
                "content": point.payload.get("content", ""),
                "source": point.payload.get("source", "unknown")
            })
    return context_with_sources