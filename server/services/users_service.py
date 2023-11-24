from abc import ABC, abstractmethod
from uuid import UUID

from models.user import UserIdentity, UserPlacelists
from models.user import UserPlacelist
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
            if entity is None:
                return None
            return UserIdentity.from_orm(entity)

    async def get_placelists(self, model_id: UUID) -> UserPlacelists:
        async with self._uow as uow:
            entity = await uow.users.get(model_id)
            if entity is None:
                return UserPlacelists(placelists=[])
            placelists: list[UserPlacelist] = []
            for placelist in entity.placelists:
                placelists.append(UserPlacelist(id=placelist.id, name=placelist.name, author_name=entity.name))
            return UserPlacelists(placelists=placelists)
