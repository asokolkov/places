from abc import ABC
from abc import abstractmethod

from db.database import SESSION_MAKER
from repositories.users_repository import AbstractUsersRepository
from repositories.users_repository import UsersRepository


class AbstractUnitOfWork(ABC):
    users: AbstractUsersRepository

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError()

    @abstractmethod
    async def __aexit__(self, *args):
        raise NotImplementedError()

    @abstractmethod
    async def commit(self):
        raise NotImplementedError()


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self._session_maker = SESSION_MAKER

    async def __aenter__(self):
        self._session = self._session_maker()
        self.users = UsersRepository(self._session)
        return self

    async def __aexit__(self):
        await self._session.rollback()
        await self._session.close()

    async def commit(self):
        await self._session.commit()
