from abc import ABC
from abc import abstractmethod
from uuid import UUID

from places_server.app.models.placelist import Placelist
from places_server.app.models.placelist import PlacelistCompressed
from places_server.app.models.placelist import PlacelistCreate
from places_server.app.models.placelist import PlacelistsList
from places_server.app.models.placelist import PlacelistUpdate
from places_server.database.database import AbstractDatabase
from places_server.database.entities import PlacelistEntity
from places_server.database.repositories.placelists_repository import AbstractPlacelistsRepository
from places_server.database.repositories.places_repository import AbstractPlacesRepository
from places_server.database.repositories.users_repository import AbstractUsersRepository


class AbstractPlacelistsService(ABC):
    @abstractmethod
    async def get_by_content(self, content: str) -> PlacelistsList:
        raise NotImplementedError()

    @abstractmethod
    async def get(self, placelist_id: UUID) -> Placelist | None:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, placelist_id: UUID, placelist_update: PlacelistUpdate, user_id: UUID) -> Placelist | None:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, placelist_create: PlacelistCreate, user_id: UUID) -> Placelist | None:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, placelist_id: UUID, user_id: UUID) -> Placelist | None:
        raise NotImplementedError()


class PlacelistsService(AbstractPlacelistsService):
    def __init__(
        self,
        database: AbstractDatabase,
        placelists_repository: AbstractPlacelistsRepository,
        users_repository: AbstractUsersRepository,
        places_repository: AbstractPlacesRepository,
    ) -> None:
        self._database = database
        self._placelists_repository = placelists_repository
        self._users_repository = users_repository
        self._places_repository = places_repository

    async def get_by_content(self, content: str) -> PlacelistsList:
        async with self._database.session_maker() as session:
            placelists = await self._placelists_repository.get_by_content(session, content)
            compressed_placelists = [
                PlacelistCompressed.model_validate(placelist, from_attributes=True) for placelist in placelists
            ]
            return PlacelistsList(placelists=compressed_placelists)

    async def get(self, placelist_id: UUID) -> Placelist | None:
        async with self._database.session_maker() as session:
            entity = await self._placelists_repository.get(session, placelist_id)
            if entity is None:
                return None

            return Placelist.model_validate(entity, from_attributes=True)

    async def update(self, placelist_id: UUID, placelist_update: PlacelistUpdate, user_id: UUID) -> Placelist | None:
        async with self._database.session_maker() as session:
            placelist = await self._placelists_repository.get(session, placelist_id)
            if placelist is None or placelist.author.id != user_id:
                return None

            placelist.name = placelist_update.name
            new_places = await self._places_repository.get_by_ids(session, placelist_update.places_ids)
            placelist.places = new_places

            await session.commit()

            return Placelist.model_validate(placelist, from_attributes=True)

    async def create(self, placelist_create: PlacelistCreate, user_id: UUID) -> Placelist | None:
        async with self._database.session_maker() as session:
            user = await self._users_repository.get(session, user_id)
            if user is None:
                return None

            entity_to_create = PlacelistEntity(name=placelist_create.name, author=user, places=[], users=[user])
            created_entity = await self._placelists_repository.create(session, entity_to_create)

            await session.commit()

            return Placelist.model_validate(created_entity, from_attributes=True)

    async def delete(self, placelist_id: UUID, user_id: UUID) -> Placelist | None:
        async with self._database.session_maker() as session:
            placelist = await self._placelists_repository.get(session, placelist_id)
            if placelist is None:
                return None

            user = await self._users_repository.get(session, user_id)
            if user is None:
                return None

            if placelist.author.id != user_id:
                return None

            deleted_entity = await self._placelists_repository.delete(session, placelist)

            await session.commit()

            return Placelist.model_validate(deleted_entity, from_attributes=True)
