from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy import select
from sqlalchemy import or_
from sqlmodel.ext.asyncio.session import AsyncSession

from db.entities import Place
from db.entities import PlaceStatus
from db.entities import UserPlaceLink


class AbstractPlacesRepository(ABC):
    @abstractmethod
    async def get(self, entity_id: UUID) -> Place | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_link(self, entity_id: UUID, user_id: UUID) -> UserPlaceLink | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_content(self, content: str) -> list[Place]:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, entity: Place) -> Place:
        raise NotImplementedError()

    @abstractmethod
    async def create_link(self, entity: UserPlaceLink) -> UserPlaceLink:
        raise NotImplementedError()

    @abstractmethod
    async def update_link(self, entity: UserPlaceLink, status: PlaceStatus) -> UserPlaceLink:
        raise NotImplementedError()


class PlacesRepository(AbstractPlacesRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get(self, entity_id: UUID) -> Place | None:
        return await self._session.get(Place, entity_id)

    async def get_link(self, entity_id: UUID, user_id: UUID) -> UserPlaceLink | None:
        return await self._session.get(UserPlaceLink, {"user_id": user_id, "place_id": entity_id})

    async def get_by_content(self, content: str) -> list[Place]:
        result = await self._session.scalars(select(Place).where(or_(Place.name == content, Place.address == content)))
        return result.all()

    async def create(self, entity: Place) -> Place:
        self._session.add(entity)
        return entity

    async def create_link(self, entity: UserPlaceLink) -> UserPlaceLink:
        self._session.add(entity)
        return entity

    async def update_link(self, entity: UserPlaceLink, status: PlaceStatus) -> UserPlaceLink:
        entity.status = status
        return entity
