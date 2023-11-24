from abc import ABC
from abc import abstractmethod
from uuid import UUID

from db.entities import PlacelistPlaceLink
from db.entities import UserPlacelistLink
from models.placelist import Placelist
from models.placelist import PlacelistCompressed
from models.placelist import PlacelistCreate
from models.placelist import PlacelistPlace
from models.placelist import PlacelistPlaceAdd
from models.placelist import PlacelistPlaceCompressed
from models.placelist import PlacelistsList
from models.placelist import PlacelistUser
from models.placelist import PlaceStatus
from models.user import UserIdentity
from utils.unit_of_work import AbstractUnitOfWork

from db.entities import Placelist as PlacelistEntity


class AbstractPlacelistsService(ABC):
    @abstractmethod
    async def get_by_content(self, content: str) -> PlacelistsList:
        raise NotImplementedError()

    @abstractmethod
    async def get(self, placelist_id: UUID, user_id: UUID) -> Placelist | None:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, placelist_create: PlacelistCreate, user_id: UUID) -> Placelist:
        raise NotImplementedError()

    @abstractmethod
    async def add_place(
            self, placelist_id: UUID, place: PlacelistPlaceAdd, user_id: UUID
            ) -> Placelist:
        raise NotImplementedError()

    @abstractmethod
    async def copy(self, placelist_id: UUID, user_id: UUID) -> Placelist | None:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, placelist_id: UUID, user_id: UUID) -> Placelist | None:
        raise NotImplementedError()


class PlacelistsService(AbstractPlacelistsService):
    def __init__(self, uow: AbstractUnitOfWork):
        self._uow = uow

    async def get_by_content(self, content: str) -> PlacelistsList:
        async with self._uow as uow:
            result = PlacelistsList(placelists=[])
            placelists = await uow.placelists.get_by_content(content)
            for placelist in placelists:
                author = await uow.users.get(placelist.author_id)
                author_model = PlacelistUser.from_orm(author)
                compressed_placelist = PlacelistCompressed(**placelist.dict(), author=author_model)
                result.placelists.append(compressed_placelist)
            return result

    async def get(self, placelist_id: UUID, user_id: UUID) -> Placelist | None:
        async with self._uow as uow:
            entity = await uow.placelists.get(placelist_id)
            if entity is None:
                return None
            author = await uow.users.get(entity.author_id)
            author_model = PlacelistUser.from_orm(author)
            places: list[PlacelistPlace] = []
            for place in entity.places:
                link = await uow.places.get_user_link(place.id, user_id)
                places.append(PlacelistPlace(**place.dict(), status=link.status if link is not None else PlaceStatus.NOT_VISITED))
            result = Placelist(**entity.dict(), author=author_model, places=places)
            return result

    async def create(self, placelist_create: PlacelistCreate, user: UserIdentity) -> Placelist:
        async with self._uow as uow:
            entity_to_create = PlacelistEntity(**placelist_create.dict(), author_id=user.id)
            created_entity = await uow.placelists.create(entity_to_create)
            link = UserPlacelistLink(user_id=user.id, placelist_id=created_entity.id)
            created_link = await uow.placelists.create_user_link(link)
            author_model = PlacelistUser(id=user.id, name=user.name)
            result = Placelist(**created_entity.dict(), author=author_model, places=[])
            await uow.commit()
            return result

    async def add_place(self, placelist_id: UUID, place_id: UUID, user_id: UUID) -> Placelist | None:
        async with self._uow as uow:
            placelist = await uow.placelists.get(placelist_id)
            if placelist is None or placelist.author_id != user_id:
                return None
            link = await uow.placelists.get_place_link(placelist_id, place_id)
            if link is not None:
                return None
            place_entity = await uow.places.get(place_id)
            if place_entity is None:
                return None
            link_to_create = PlacelistPlaceLink(placelist_id=placelist_id, place_id=place_id)
            created_link = await uow.placelists.create_place_link(link_to_create)
            author = await uow.users.get(placelist.author_id)
            author_model = PlacelistUser.from_orm(author)
            place_entity = await uow.places.get(place_id)
            places: list[PlacelistPlaceCompressed] = [PlacelistPlaceCompressed.from_orm(place_entity)]
            for place in placelist.places:
                places.append(PlacelistPlaceCompressed.from_orm(place))
            result = Placelist(**placelist.dict(), author=author_model, places=places)
            await uow.commit()
            return result

    async def copy(self, placelist_id: UUID, user_id: UUID) -> Placelist | None:
        async with self._uow as uow:
            placelist = await uow.placelists.get(placelist_id)
            if placelist is None or placelist.author_id == user_id:
                return None
            link = await uow.placelists.get_user_link(placelist_id, user_id)
            if link is not None:
                return None
            link_to_create = UserPlacelistLink(placelist_id=placelist_id, user_id=user_id)
            created_link = await uow.placelists.create_user_link(link_to_create)
            author = await uow.users.get(placelist.author_id)
            author_model = PlacelistUser.from_orm(author)
            places: list[PlacelistPlace] = []
            for place in placelist.places:
                places.append(PlacelistPlace.from_orm(place))
            result = Placelist(**placelist.dict(), author=author_model, places=places)
            await uow.commit()
            return result

    async def delete(self, placelist_id: UUID, user_id: UUID) -> Placelist | None:
        async with self._uow as uow:
            placelist = await uow.placelists.get(placelist_id)
            if placelist is None or placelist.author_id != user_id:
                return None
            deleted_entity = await uow.placelists.delete(placelist)
            author = await uow.users.get(user_id)
            author_model = PlacelistUser.from_orm(author)
            places: list[PlacelistPlace] = []
            for place in placelist.places:
                places.append(PlacelistPlace.from_orm(place))
            result = Placelist(**deleted_entity.dict(), author=author_model, places=places)
            await uow.commit()
            return result
