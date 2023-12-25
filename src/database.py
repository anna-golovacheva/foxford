import os
from typing import AsyncGenerator
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import registry, sessionmaker, Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from src.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


DATABASE_URL = os.environ.get('DATABASE_URL').replace("://", "ql+asyncpg://", 1)

mapper_registry = registry()
Base = mapper_registry.generate_base()
metadata = Base.metadata


# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

# DATABASE_URL_SYNC = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_URL_SYNC = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
engine_sync = create_engine(DATABASE_URL_SYNC)
SessionLocalSync = sessionmaker(autocommit=False, autoflush=False, bind=engine_sync)

def get_sync_session() -> Session:
    session = SessionLocalSync()
    return session