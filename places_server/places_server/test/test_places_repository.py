from uuid import uuid4

import pytest
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database.entities import PlaceEntity
from database.entities import PlacelistEntity
from database.repositories.places_repository import AbstractPlacesRepository
from test.fake_classes import FakeDatabase


@pytest.mark.asyncio
async def test_get_existing_entity(fake_database: FakeDatabase, places_repository: AbstractPlacesRepository) -> None:
    async with fake_database.session_maker() as session:
        scalars = await session.scalars(select(PlaceEntity))
        places = list(scalars.all())

        entity = await places_repository.get(session, places[0].id)

        assert entity is not None
        assert entity.id == places[0].id


@pytest.mark.asyncio
async def test_get_non_existing_entity(
    fake_database: FakeDatabase, places_repository: AbstractPlacesRepository
) -> None:
    async with fake_database.session_maker() as session:
        entity = await places_repository.get(session, uuid4())

        assert entity is None


@pytest.mark.asyncio
async def test_get_by_content_valid(fake_database: FakeDatabase, places_repository: AbstractPlacesRepository) -> None:
    async with fake_database.session_maker() as session:
        scalars = await session.scalars(select(PlaceEntity))
        places = list(scalars.all())

        entities_by_name = await places_repository.get_by_content(session, places[0].name)
        entities_by_address = await places_repository.get_by_content(session, places[0].name)

        assert len(entities_by_name) == 1
        assert len(entities_by_address) == 1
        assert entities_by_name[0].id == places[0].id
        assert entities_by_address[0].id == places[0].id


@pytest.mark.asyncio
async def test_get_by_mail_invalid(fake_database: FakeDatabase, places_repository: AbstractPlacesRepository) -> None:
    name = "name_test"
    address = "address_test"

    async with fake_database.session_maker() as session:
        entities_by_name = await places_repository.get_by_content(session, name)
        entities_by_address = await places_repository.get_by_content(session, address)

        assert len(entities_by_name) == 0
        assert len(entities_by_address) == 0


@pytest.mark.asyncio
async def test_get_by_ids_valid(fake_database: FakeDatabase, places_repository: AbstractPlacesRepository) -> None:
    ids = [i.id for i in fake_database.places]

    async with fake_database.session_maker() as session:
        entities = await places_repository.get_by_ids(session, ids)

        assert len(entities) == 2


@pytest.mark.asyncio
async def test_get_by_ids_invalid(fake_database: FakeDatabase, places_repository: AbstractPlacesRepository) -> None:
    ids = [uuid4()]

    async with fake_database.session_maker() as session:
        entities = await places_repository.get_by_ids(session, ids)

        assert len(entities) == 0


@pytest.mark.asyncio
async def test_create(fake_database: FakeDatabase, places_repository: AbstractPlacesRepository) -> None:
    async with fake_database.session_maker() as session:
        places_scalars = await session.scalars(select(PlaceEntity))
        places = list(places_scalars.all())

        placelists_scalars = await session.scalars(
            select(PlacelistEntity).options(selectinload(PlacelistEntity.author))
        )
        placelists = list(placelists_scalars.all())

        new_place = PlaceEntity(
            id=uuid4(),
            name="New Place",
            address="New Address",
            latitude=101.0,
            longitude=102.0,
            placelists=[placelists[0]],
        )

        entity = await places_repository.create(session, new_place)

        new_places_scalars = await session.scalars(select(PlaceEntity))
        new_places = list(new_places_scalars.all())

        assert entity is not None
        assert entity.id not in [places.id for places in places]
        assert len(new_places) == len(places) + 1
        assert entity.placelists[0].id == placelists[0].id
        assert placelists[0].author.id == entity.placelists[0].author.id
