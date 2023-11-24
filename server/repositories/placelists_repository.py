from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlmodel import select

from db.entities import Placelist
from db.entities import PlacelistPlaceLink
from db.entities import UserPlacelistLink


class AbstractPlacelistsRepository(ABC):
    @abstractmethod
    async def get(self, entity_id: UUID) -> Placelist | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_content(self, content: str) -> list[Placelist]:
        raise NotImplementedError()

    @abstractmethod
    async def get_place_link(self, placelist_id: UUID, place_id: UUID) -> PlacelistPlaceLink | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_user_link(self, placelist_id: UUID, user_id: UUID) -> UserPlacelistLink | None:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, entity: Placelist) -> Placelist:
        raise NotImplementedError()

    @abstractmethod
    async def create_place_link(self, entity: PlacelistPlaceLink) -> PlacelistPlaceLink:
        raise NotImplementedError()

    @abstractmethod
    async def create_user_link(self, entity: UserPlacelistLink) -> UserPlacelistLink:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, entity: Placelist) -> Placelist:
        raise NotImplementedError()


class PlacelistsRepository(AbstractPlacelistsRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get(self, entity_id: UUID) -> Placelist | None:
        result = await self._session.scalars(select(Placelist).where(Placelist.id == entity_id).options(selectinload(Placelist.places)))
        return result.first()

    async def get_by_content(self, content: str) -> list[Placelist]:
        result = await self._session.scalars(select(Placelist).where(Placelist.name == content))
        return result.all()

    async def get_place_link(self, placelist_id: UUID, place_id: UUID) -> PlacelistPlaceLink | None:
        return await self._session.get(PlacelistPlaceLink, {"placelist_id": placelist_id, "place_id": place_id})

    async def get_user_link(self, placelist_id: UUID, user_id: UUID) -> UserPlacelistLink | None:
        return await self._session.get(UserPlacelistLink, {"placelist_id": placelist_id, "user_id": user_id})

    async def create(self, entity: Placelist) -> Placelist:
        self._session.add(entity)
        return entity

    async def create_place_link(self, entity: PlacelistPlaceLink) -> PlacelistPlaceLink:
        self._session.add(entity)
        return entity

    async def create_user_link(self, entity: UserPlacelistLink) -> UserPlacelistLink:
        self._session.add(entity)
        return entity

    async def delete(self, entity: Placelist) -> Placelist:
        await self._session.delete(entity)
        return entity
