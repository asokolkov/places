from abc import ABC
from abc import abstractmethod

from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update

from db.database import session_maker
from db.entities import PlaceEntity


class AbstractPlacesRepository(ABC):
    @abstractmethod
    async def get_by_content(self, content: str) -> list[PlaceEntity]:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, entity: PlaceEntity) -> PlaceEntity:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, entity: PlaceEntity) -> PlaceEntity:
        raise NotImplementedError()


class PlacesRepository(AbstractPlacesRepository):
    _entity = PlaceEntity

    async def get_by_content(self, content: str) -> PlaceEntity:
        async with session_maker.begin() as session:
            statement = select(PlaceEntity).where(
                PlaceEntity.id.icontains(content) |
                PlaceEntity.name.icontains(content)
            )
            result = await session.execute(statement)
            return result.scalar_one()

    async def create(self, entity: PlaceEntity) -> PlaceEntity:
        async with session_maker.begin() as session:
            statement = insert(self._entity).values(entity.dict()).returning(self._entity)
            result = await session.execute(statement)
            return result.scalar_one()

    async def update(self, entity: PlaceEntity) -> PlaceEntity:
        async with session_maker.begin() as session:
            statement = update(self._entity).where(self._entity.id == entity.id).values(entity.dict()).returning(self._entity)
            result = await session.execute(statement)
            return result.scalar_one()
