import functools
from asyncio import current_task
from contextlib import contextmanager

from async_lru import alru_cache
from sqlalchemy.ext.asyncio import async_scoped_session
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from .entities import Base


async def get_session() -> AsyncSession:
    session_maker = await get_session_maker()
    async with session_maker() as session:
        yield session


@alru_cache()
async def get_session_maker():
    engine = create_async_engine("postgresql+asyncpg://postgres:postgres@localhost/test")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
