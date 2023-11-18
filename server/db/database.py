import asyncio
from abc import ABC
from abc import abstractmethod

from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker


class AbstractDatabase(ABC):
    @abstractmethod
    def get_session_maker(self) -> sessionmaker:
        raise NotImplementedError


class Database(AbstractDatabase):
    def __init__(self):
        self._engine = AsyncEngine(create_engine("postgresql+asyncpg://postgres:postgres@localhost/test", echo=True, future=True))
        self._session_maker = sessionmaker(self._engine, class_=AsyncSession, expire_on_commit=False)
        # asyncio.run(self._create_tables())

    def get_session_maker(self) -> sessionmaker:
        return self._session_maker

    async def _create_tables(self):
        async with self._engine.begin() as connection:
            await connection.run_sync(SQLModel.metadata.drop_all)
            await connection.run_sync(SQLModel.metadata.create_all)
