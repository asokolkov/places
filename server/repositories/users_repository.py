from abc import ABC
from abc import abstractmethod
from uuid import UUID

from sqlalchemy.orm import selectinload
from sqlmodel import select

from db.database import AbstractDatabase
from db.entities import User


class AbstractUsersRepository(ABC):
    @abstractmethod
    async def get(self, entity_id: UUID) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_username(self, username: str) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, entity: User) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, entity: User) -> User:
        raise NotImplementedError()


class UsersRepository(AbstractUsersRepository):
    def __init__(self, db: AbstractDatabase):
        self._db = db

    async def get(self, entity_id: UUID) -> User:
        async with self._db.get_session_maker()() as session:
            result = await session.scalars(select(User).where(User.id == entity_id).options(selectinload(User.placelists)))
            return result.one()

    async def get_by_username(self, username: str) -> User:
        async with self._db.get_session_maker()() as session:
            result = await session.scalars(select(User).where(User.username == username))
            return result.one()

    async def create(self, entity: User) -> User:
        async with self._db.get_session_maker()() as session:
            session.add(entity)
            await session.commit()
            result = await session.scalars(select(User).where(User.id == entity.id).options(selectinload(User.placelists)))
            return result.one()

    async def update(self, entity: User) -> User:
        async with self._db.get_session_maker()() as session:
            result = await session.get(User, entity.id)
            result.mail = entity.mail
            result.password = entity.password
            result.username = entity.username
            result.name = entity.name
            await session.commit()
            result = await session.scalars(
                select(User).where(User.id == entity.id).options(
                    selectinload(User.placelists)
                    )
                )
            return result.one()
