from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.entities import PlaceEntity


class AbstractPlacesRepository(ABC):
    @abstractmethod
    async def get(self, session: AsyncSession, entity_id: UUID) -> PlaceEntity | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_content(self, session: AsyncSession, content: str) -> list[PlaceEntity]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_ids(self, session: AsyncSession, ids: list[UUID]) -> list[PlaceEntity]:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, session: AsyncSession, entity: PlaceEntity) -> PlaceEntity:
        raise NotImplementedError()


class PlacesRepository(AbstractPlacesRepository):
    async def get(self, session: AsyncSession, entity_id: UUID) -> PlaceEntity | None:
        return await session.get(PlaceEntity, entity_id)

    async def get_by_content(self, session: AsyncSession, content: str) -> list[PlaceEntity]:
        statement = select(PlaceEntity).where((PlaceEntity.name == content) | (PlaceEntity.address == content))
        result = await session.scalars(statement)
        return list(result.all())

    async def get_by_ids(self, session: AsyncSession, ids: list[UUID]) -> list[PlaceEntity]:
        statement = select(PlaceEntity).where(PlaceEntity.id.in_(ids))
        result = await session.scalars(statement)
        return list(result.all())

    async def create(self, session: AsyncSession, entity: PlaceEntity) -> PlaceEntity:
        session.add(entity)
        return entity
