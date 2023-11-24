from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy.orm import joinedload
from sqlalchemy.orm import selectinload
from sqlalchemy.orm import subqueryload
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from db.entities import User


class AbstractUsersRepository(ABC):
    @abstractmethod
    async def get(self, entity_id: UUID) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_mail(self, mail: str) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_username(self, username: str) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_mail_and_username(self, mail: str, username: str) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, entity: User) -> User:
        raise NotImplementedError()


class UsersRepository(AbstractUsersRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get(self, entity_id: UUID) -> User | None:
        result = await self._session.scalars(
            select(User)
            .where(User.id == entity_id)
            .options(selectinload(User.placelists))
        )
        return result.first()

    async def get_by_mail(self, mail: str) -> User | None:
        result = await self._session.scalars(select(User).where(User.mail == mail))
        return result.first()

    async def get_by_username(self, username: str) -> User | None:
        result = await self._session.scalars(select(User).where(User.username == username))
        return result.first()

    async def get_by_mail_and_username(self, mail: str, username: str) -> User | None:
        result = await self._session.scalars(
            select(User).where(User.mail == mail, User.mail == username)
        )
        return result.first()

    async def create(self, entity: User) -> User:
        self._session.add(entity)
        return entity
