from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from database.entities import PlacelistEntity
from database.entities import UserEntity


class AbstractUsersRepository(ABC):
    @abstractmethod
    async def get(self, session: AsyncSession, entity_id: UUID) -> UserEntity | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_mail(self, session: AsyncSession, mail: str) -> UserEntity | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_username(self, session: AsyncSession, username: str) -> UserEntity | None:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, session: AsyncSession, entity: UserEntity) -> UserEntity:
        raise NotImplementedError()


class UsersRepository(AbstractUsersRepository):
    async def get(self, session: AsyncSession, entity_id: UUID) -> UserEntity | None:
        statement = (
            select(UserEntity)
            .where(UserEntity.id == entity_id)
            .options(selectinload(UserEntity.saved_placelists).selectinload(PlacelistEntity.author))
        )
        result = await session.scalars(statement)
        return result.first()

    async def get_by_mail(self, session: AsyncSession, mail: str) -> UserEntity | None:
        statement = select(UserEntity).where(UserEntity.mail == mail)
        result = await session.scalars(statement)
        return result.first()

    async def get_by_username(self, session: AsyncSession, username: str) -> UserEntity | None:
        statement = select(UserEntity).where(UserEntity.username == username)
        result = await session.scalars(statement)
        return result.first()

    async def create(self, session: AsyncSession, entity: UserEntity) -> UserEntity:
        session.add(entity)
        return entity
