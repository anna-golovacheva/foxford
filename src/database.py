import os
from typing import AsyncGenerator
from sqlalchemy import MetaData
from sqlalchemy.orm import registry, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from src.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


DATABASE_URL = os.environ.get("DATABASE_URL")

mapper_registry = registry()
Base = mapper_registry.generate_base()
metadata = Base.metadata

engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
