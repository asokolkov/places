from abc import ABC

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from places_server.configs import settings
from places_server.database.entities import Base


class AbstractDatabase(ABC):
    _engine: AsyncEngine
    session_maker: async_sessionmaker[AsyncSession]


class Database(AbstractDatabase):
    def __init__(self) -> None:
        self._engine = create_async_engine(settings.DATABASE_URL, echo=settings.DATABASE_ECHO, future=True)
        self.session_maker = async_sessionmaker(self._engine, expire_on_commit=False)

    async def create_tables(self) -> None:
        async with self._engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)

