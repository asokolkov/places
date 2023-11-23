from abc import ABC
from abc import abstractmethod
from uuid import UUID

from db.entities import PlaceStatus
from db.entities import UserPlaceLink
from models.place import Place
from db.entities import Place as PlaceEntity
from models.place import PlaceCreate
from models.place import PlacesList
from db.entities import PlaceStatus as PlaceStatusEntity
from models.place import PlaceUpdate
from utils.unit_of_work import AbstractUnitOfWork


class AbstractPlacesService(ABC):
    @abstractmethod
    async def get_by_content(self, content: str, user_id: UUID) -> PlacesList:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, place_create: PlaceCreate) -> Place:
        raise NotImplementedError()

    @abstractmethod
    async def change_status(self, place_update: Place, user_id: UUID) -> Place | None:
        raise NotImplementedError()


class PlacesService(AbstractPlacesService):
    def __init__(self, uow: AbstractUnitOfWork):
        self._uow = uow

    async def get_by_content(self, content: str, user_id: UUID) -> PlacesList:
        async with self._uow as uow:
            result = PlacesList(places=[])
            places = await uow.places.get_by_content(content)
            for place in places:
                link = await uow.places.get_link(place.id, user_id)
                place_model = Place(**place.dict(), status=PlaceStatus.NEVER_BEEN if link is None else link.status)
                result.places.append(place_model)
            return result

    async def create(self, place_create: PlaceCreate) -> Place:
        async with self._uow as uow:
            entity_to_create = PlaceEntity.from_orm(place_create)
            created_entity = await uow.places.create(entity_to_create)
            result = Place(**created_entity.dict(), status=PlaceStatusEntity.NEVER_BEEN)
            await uow.commit()
            return result

    async def change_status(self, place_update: PlaceUpdate, user_id: UUID) -> Place | None:
        async with self._uow as uow:
            place_to_update = await uow.places.get(place_update.id)
            if place_to_update is None:
                return None
            link_to_update = await uow.places.get_link(place_update.id, user_id)
            if link_to_update is None:
                link = UserPlaceLink(place_id=place_update.id, user_id=user_id, status=PlaceStatusEntity(place_update.status.value))
                created_link = await uow.places.create_link(link)
                result = Place(**place_to_update.dict(), status=created_link.status)
                await uow.commit()
                return result
            else:
                updated_link = await uow.places.update_link(link_to_update, PlaceStatusEntity(place_update.status))
                result = Place(**place_to_update.dict(), status=updated_link.status)
                await uow.commit()
                return result
