from abc import ABC
from abc import abstractmethod
from uuid import uuid4

from pydantic import parse_obj_as

from db.entities import User as UserEntity
from models.user import UserCreate
from models.user import User
from models.user import UserCompressed
from models.user import UserPlacelist
from models.user import UserUpdate
from repositories.users_repository import AbstractUsersRepository


class AbstractUsersService(ABC):
    @abstractmethod
    async def get(self, model_id: uuid4) -> UserCompressed:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_username(self, username: str) -> UserCompressed:
        raise NotImplementedError()

    @abstractmethod
    async def get_placelists(self, model_id: uuid4) -> list[UserPlacelist]:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, model: UserCreate) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, model: UserUpdate) -> User:
        raise NotImplementedError()


class UsersService(AbstractUsersService):
    def __init__(self, repository: AbstractUsersRepository):
        self._repository = repository

    async def get(self, model_id: uuid4) -> UserCompressed:
        result = await self._repository.get(model_id)
        return UserCompressed.from_orm(result)

    async def get_by_username(self, username: str) -> UserCompressed:
        result = await self._repository.get_by_username(username)
        return UserCompressed.from_orm(result)

    async def get_placelists(self, model_id: uuid4) -> list[UserPlacelist]:
        result = await self._repository.get(model_id)
        return parse_obj_as(list[UserPlacelist], result.placelists)

    async def create(self, model: UserCreate) -> User:
        entity = parse_obj_as(UserEntity, model)
        result = await self._repository.create(entity)
        return User.from_orm(result)

    async def update(self, model: UserUpdate) -> User:
        entity = parse_obj_as(UserEntity, model)
        result = await self._repository.update(entity)
        return User.from_orm(result)
