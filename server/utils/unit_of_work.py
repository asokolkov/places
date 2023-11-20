from abc import ABC, abstractmethod
from typing import Self

from db.database import SESSION_MAKER
from repositories.users_repository import AbstractUsersRepository, UsersRepository


class AbstractUnitOfWork(ABC):
    users: AbstractUsersRepository

    @abstractmethod
    async def __aenter__(self) -> Self:
        raise NotImplementedError()

    @abstractmethod
    async def __aexit__(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError()


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self) -> None:
        self._session_maker = SESSION_MAKER

    async def __aenter__(self) -> AbstractUnitOfWork:
        self._session = self._session_maker()
        self.users = UsersRepository(self._session)
        return self

    async def __aexit__(self, *args) -> None:
        await self._session.rollback()
        await self._session.close()

    async def commit(self) -> None:
        await self._session.commit()
