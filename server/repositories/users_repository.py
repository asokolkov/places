from abc import ABC
from abc import abstractmethod
from uuid import uuid4

from sqlalchemy.orm import selectinload
from sqlmodel import select

from db.database import AbstractDatabase
from db.entities import User as UserEntity


class AbstractUsersRepository(ABC):
    @abstractmethod
    async def get(self, entity_id: uuid4) -> UserEntity:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_username(self, username: str) -> UserEntity:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, entity: UserEntity) -> UserEntity:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, entity: UserEntity) -> UserEntity:
        raise NotImplementedError()


class UsersRepository(AbstractUsersRepository):
    def __init__(self, db: AbstractDatabase):
        self._db = db

    async def get(self, entity_id: uuid4) -> UserEntity:
        async with self._db.get_session_maker()() as session:
            result = await session.scalars(select(UserEntity).where(UserEntity.id == entity_id).options(selectinload(UserEntity.placelists)))
            return result.one()

    async def get_by_username(self, username: str) -> UserEntity:
        async with self._db.get_session_maker()() as session:
            result = await session.scalars(select(UserEntity).where(UserEntity.username == username))
            return result.one()

    async def create(self, entity: UserEntity) -> UserEntity:
        async with self._db.get_session_maker()() as session:
            session.add(entity)
            await session.commit()
            result = await session.scalars(select(UserEntity).where(UserEntity.id == entity.id).options(selectinload(UserEntity.placelists)))
            return result.one()

    async def update(self, entity: UserEntity) -> UserEntity:
        async with self._db.get_session_maker()() as session:
            result = await session.get(UserEntity, entity.id)
            result.mail = entity.mail
            result.password = entity.password
            result.username = entity.username
            result.name = entity.name
            await session.commit()
            result = await session.scalars(
                select(UserEntity).where(UserEntity.id == entity.id).options(
                    selectinload(UserEntity.placelists)
                    )
                )
            return result.one()
