from abc import ABC, abstractmethod
from uuid import UUID

from models.user import UserIdentity, UserPlacelists
from utils.unit_of_work import AbstractUnitOfWork


class AbstractUsersService(ABC):
    @abstractmethod
    async def get(self, model_id: UUID) -> UserIdentity | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_placelists(self, model_id: UUID) -> UserPlacelists:
        raise NotImplementedError()


class UsersService(AbstractUsersService):
    def __init__(self, uow: AbstractUnitOfWork):
        self._uow = uow

    async def get(self, model_id: UUID) -> UserIdentity | None:
        async with self._uow as uow:
            entity = await uow.users.get(model_id)
            return UserIdentity.from_orm(entity)

    async def get_placelists(self, model_id: UUID) -> UserPlacelists:
        async with self._uow as uow:
            entity = await uow.users.get(model_id)
            if entity is None:
                return UserPlacelists(placelists=[])
            return UserPlacelists.from_orm(entity)
