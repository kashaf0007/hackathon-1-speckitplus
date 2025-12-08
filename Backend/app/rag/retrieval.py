from typing import List, Optional
from qdrant_client.models import ScoredPoint
from openai import OpenAI
from app.rag.qdrant import search_vectors
from app.core.config import settings
import numpy as np

openai_client = OpenAI(api_key=settings.GEMINI_API_KEY)

async def generate_embedding(text: str) -> List[float]:
    response = openai_client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

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