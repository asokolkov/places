from abc import ABC
from abc import abstractmethod
from uuid import uuid5

from sqlalchemy import delete
from sqlalchemy import insert
from sqlalchemy import select

from db.database import session_maker
from db.entities import PlacelistEntity


class AbstractPlacelistsRepository(ABC):
    @abstractmethod
    async def get(self, entity_id: uuid5) -> PlacelistEntity:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_content(self, content: str) -> list[PlacelistEntity]:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, entity: PlacelistEntity) -> PlacelistEntity:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, entity_id: uuid5) -> PlacelistEntity:
        raise NotImplementedError()


class PlacelistsRepository(AbstractPlacelistsRepository):
    _entity = PlacelistEntity

    async def get(self, entity_id: uuid5) -> PlacelistEntity:
        async with session_maker.begin() as session:
            return await session.get(self._entity, entity_id)

    async def get_by_content(self, content: str) -> list[PlacelistEntity]:
        async with session_maker.begin() as session:
            statement = select(self._entity).filter(
                self._entity.id.icontains(content) |
                self._entity.name.icontains(content)
            )
            result = await session.execute(statement)
            return result.scalar_one()

    async def create(self, entity: PlacelistEntity) -> PlacelistEntity:
        async with session_maker.begin() as session:
            statement = insert(self._entity).values(entity.dict()).returning(self._entity)
            result = await session.execute(statement)
            return result.scalar_one()

    async def delete(self, entity_id: uuid5) -> PlacelistEntity:
        async with session_maker.begin() as session:
            statement = delete(self._entity).filter_by(id=entity_id).returning(self._entity)
            result = await session.execute(statement)
            return result.scalar_one()
