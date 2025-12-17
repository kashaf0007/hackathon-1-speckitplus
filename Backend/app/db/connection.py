# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker
# from app.core.config import settings

# DATABASE_URL = settings.neon_database_url

# engine = create_async_engine(DATABASE_URL, echo=True)
# AsyncSessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine,
#     class_=AsyncSession
# )

# async def get_db():
#     async with AsyncSessionLocal() as session:
#         yield session

import ssl
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Remove sslmode and channel_binding from URL as asyncpg handles SSL differently
db_url = settings.neon_database_url
if "?" in db_url:
    db_url = db_url.split("?")[0]

# Create SSL context for secure connection to Neon
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

engine = create_async_engine(
    db_url,
    echo=True,
    connect_args={"ssl": ssl_context},
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
