from abc import ABC

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from configs.local import DATABASE_ECHO
from configs.local import DATABASE_URL


class AbstractDatabase(ABC):
    _engine: AsyncEngine
    session_maker: async_sessionmaker[AsyncSession]


class Database(AbstractDatabase):
    def __init__(self) -> None:
        self._engine = create_async_engine(DATABASE_URL, echo=DATABASE_ECHO, future=True)
        self.session_maker = async_sessionmaker(self._engine, expire_on_commit=False)
