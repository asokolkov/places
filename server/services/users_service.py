from abc import ABC
from abc import abstractmethod
from uuid import UUID

from pydantic import parse_obj_as

from db.entities import User as UserEntity
from models.user import User
from models.user import UserCompressed
from models.user import UserIdentity
from models.user import UserPlacelist
from models.user import UserUpdate
from repositories.users_repository import AbstractUsersRepository


class AbstractUsersService(ABC):
    @abstractmethod
    async def get(self, model_id: UUID) -> UserCompressed:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_username(self, username: str) -> UserCompressed:
        raise NotImplementedError()

    @abstractmethod
    async def get_placelists(self, model_id: UUID) -> list[UserPlacelist]:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, model: UserUpdate) -> User:
        raise NotImplementedError()


class UsersService(AbstractUsersService):
    def __init__(self, repository: AbstractUsersRepository):
        self._repository = repository

    async def get(self, model_id: UUID) -> UserIdentity:
        result = await self._repository.get(model_id)
        return UserIdentity.from_orm(result)

    async def get_by_username(self, username: str) -> UserCompressed:
        result = await self._repository.get_by_username(username)
        return UserCompressed.from_orm(result)

    async def get_placelists(self, model_id: UUID) -> list[UserPlacelist]:
        result = await self._repository.get(model_id)
        return parse_obj_as(list[UserPlacelist], result.placelists)

    async def update(self, model: UserUpdate) -> User:
        entity = parse_obj_as(UserEntity, model)
        result = await self._repository.update(entity)
        return User.from_orm(result)
