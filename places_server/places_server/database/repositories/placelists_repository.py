from abc import ABC
from abc import abstractmethod
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from places_server.database.entities import PlacelistEntity


class AbstractPlacelistsRepository(ABC):
    @abstractmethod
    async def get(self, session: AsyncSession, entity_id: UUID) -> PlacelistEntity | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_content(self, session: AsyncSession, content: str) -> list[PlacelistEntity]:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, session: AsyncSession, entity: PlacelistEntity) -> PlacelistEntity:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, session: AsyncSession, entity: PlacelistEntity) -> PlacelistEntity:
        raise NotImplementedError()


class PlacelistsRepository(AbstractPlacelistsRepository):
    async def get(self, session: AsyncSession, entity_id: UUID) -> PlacelistEntity | None:
        statement = (
            select(PlacelistEntity)
            .options(
                selectinload(PlacelistEntity.places),
                selectinload(PlacelistEntity.author),
                selectinload(PlacelistEntity.users),
            )
            .where(PlacelistEntity.id == entity_id)
        )
        result = await session.scalars(statement)
        return result.first()

    async def get_by_content(self, session: AsyncSession, content: str) -> list[PlacelistEntity]:
        statement = (
            select(PlacelistEntity).options(selectinload(PlacelistEntity.author)).where(PlacelistEntity.name.ilike(f"%{content}%"))
        )
        result = await session.scalars(statement)
        return list(result.all())

    async def create(self, session: AsyncSession, entity: PlacelistEntity) -> PlacelistEntity:
        session.add(entity)
        return entity

    async def delete(self, session: AsyncSession, entity: PlacelistEntity) -> PlacelistEntity:
        await session.delete(entity)
        return entity
