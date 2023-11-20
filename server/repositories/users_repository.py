from abc import ABC
from abc import abstractmethod
from uuid import UUID

from sqlalchemy.orm import selectinload
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from db.entities import User


class AbstractUsersRepository(ABC):
    @abstractmethod
    async def get(self, entity_id: UUID) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_mail(self, mail: str) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_mail_and_username(self, mail: str, username: str) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, entity: User) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, entity: User) -> User:
        raise NotImplementedError()


class UsersRepository(AbstractUsersRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get(self, entity_id: UUID) -> User:
        result = await self._session.scalars(select(User).where(User.id == entity_id).options(selectinload(User.placelists)))
        return result.one()

    async def get_by_mail(self, mail: str) -> User | None:
        result = await self._session.scalars(select(User).where(User.mail == mail))
        return result.first()

    async def get_by_mail_and_username(self, mail: str, username: str) -> User | None:
        result = await self._session.scalars(select(User).where(User.mail == mail, User.mail == username))
        return result.first()

    async def create(self, entity: User) -> User:
        self._session.add(entity)
        await self._session.commit()
        await self._session.refresh(entity)
        return entity

    async def update(self, entity: User) -> User:
        result = await self._session.get(User, entity.id)
        result.mail = entity.mail
        result.password = entity.password
        result.username = entity.username
        result.name = entity.name
        await self._session.commit()
        await self._session.refresh(entity)
        return entity
