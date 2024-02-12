from abc import ABC
from abc import abstractmethod
from uuid import UUID

from places_server.app.models.place import Place
from places_server.app.models.place import PlaceCreate
from places_server.app.models.place import PlacesList
from places_server.database.database import AbstractDatabase
from places_server.database.entities import PlaceEntity
from places_server.database.repositories.placelists_repository import AbstractPlacelistsRepository
from places_server.database.repositories.places_repository import AbstractPlacesRepository
from places_server.database.repositories.users_repository import AbstractUsersRepository


class AbstractPlacesService(ABC):
    @abstractmethod
    async def get(self, place_id: UUID) -> Place | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_content(self, content: str) -> PlacesList:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, place_create: PlaceCreate, user_id: UUID) -> Place | None:
        raise NotImplementedError()


class PlacesService(AbstractPlacesService):
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

    async def get(self, place_id: UUID) -> Place | None:
        async with self._database.session_maker() as session:
            place = await self._places_repository.get(session, place_id)
            if place is None:
                return None
            return Place.model_validate(place, from_attributes=True)

    async def get_by_content(self, content: str) -> PlacesList:
        async with self._database.session_maker() as session:
            places = await self._places_repository.get_by_content(session, content)
            places_models = [Place.model_validate(i, from_attributes=True) for i in places]
            return PlacesList(places=places_models)

    async def create(self, place_create: PlaceCreate, user_id: UUID) -> Place | None:
        async with self._database.session_maker() as session:
            user = await self._users_repository.get(session, user_id)
            if user is None:
                return None

            entity_to_create = PlaceEntity(**place_create.dict())
            created_entity = await self._places_repository.create(session, entity_to_create)

            await session.commit()

            return Place.model_validate(created_entity, from_attributes=True)
