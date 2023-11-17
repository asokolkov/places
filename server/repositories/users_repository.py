from abc import ABC
from abc import abstractmethod
from uuid import uuid5

from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update

from db.database import session_maker
from db.entities import UserEntity


class AbstractUsersRepository(ABC):
    @abstractmethod
    async def get(self, entity_id: uuid5) -> UserEntity:
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


class UsersRepository:
    _entity = UserEntity

    async def get(self, entity_id: uuid5) -> UserEntity:
        async with session_maker.begin() as session:
            return await session.get(self._entity, entity_id)

    async def get_by_username(self, username: str) -> UserEntity:
        async with session_maker.begin() as session:
            statement = select(self._entity).where(self._entity.username == username)
            result = await session.execute(statement)
            return result.scalar_one()

    async def create(self, entity: UserEntity):
        async with session_maker.begin() as session:
            statement = insert(self._entity).values(entity.dict()).returning(self._entity)
            result = await session.execute(statement)
            return result.scalar_one()

    async def update(self, entity: UserEntity):
        async with session_maker.begin() as session:
            statement = update(self._entity).where(self._entity.id == entity.id).values(entity.dict()).returning(self._entity)
            result = await session.execute(statement)
            return result.scalar_one()
