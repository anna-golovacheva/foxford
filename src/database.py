import os
from typing import AsyncGenerator
from sqlalchemy import MetaData
from sqlalchemy.orm import registry
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


DATABASE_URL = os.environ.get("DATABASE_URL")

mapper_registry = registry()
Base = mapper_registry.generate_base()
metadata = Base.metadata

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
