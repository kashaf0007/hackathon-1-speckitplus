from qdrant_client import QdrantClient, models
from app.core.config import settings

client = QdrantClient(
    url=settings.qdrant_url,
    api_key=settings.qdrant_api_key,
)

COLLECTION_NAME = "rag_documents"

async def create_qdrant_collection():
    current_collections = await client.get_collections()
    if COLLECTION_NAME not in [c.name for c in current_collections.collections]:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
        )

async def upsert_vectors(vectors: list, payloads: list):
    client.upsert(
        collection_name=COLLECTION_NAME,
        wait=True,
        points=models.Batch(
            vectors=vectors,
            payloads=payloads,
        ),
    )

async def search_vectors(query_vector: list, limit: int = 5) -> list:
    search_result = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=limit,
    )
    return search_result

async def delete_points(point_ids: list):
    client.delete(
        collection_name=COLLECTION_NAME,
        points_selector=models.PointIdsList(
            points=point_ids,
        ),
    )