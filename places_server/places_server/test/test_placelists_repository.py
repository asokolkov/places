from uuid import uuid4

import pytest
from sqlalchemy import select

from places_server.database.entities import PlacelistEntity
from places_server.database.entities import UserEntity
from places_server.database.repositories.placelists_repository import AbstractPlacelistsRepository
from places_server.test.fake_classes import FakeDatabase


@pytest.mark.asyncio
async def test_get_existing_entity(
    fake_database: FakeDatabase, placelists_repository: AbstractPlacelistsRepository
) -> None:
    async with fake_database.session_maker() as session:
        scalars = await session.scalars(select(PlacelistEntity))
        placelists = list(scalars.all())

        entity = await placelists_repository.get(session, placelists[0].id)

        assert entity is not None
        assert entity.id == placelists[0].id


@pytest.mark.asyncio
async def test_get_non_existing_entity(
    fake_database: FakeDatabase, placelists_repository: AbstractPlacelistsRepository
) -> None:
    async with fake_database.session_maker() as session:
        entity = await placelists_repository.get(session, uuid4())

        assert entity is None


@pytest.mark.asyncio
async def test_get_by_content_valid(
    fake_database: FakeDatabase, placelists_repository: AbstractPlacelistsRepository
) -> None:
    async with fake_database.session_maker() as session:
        scalars = await session.scalars(select(PlacelistEntity))
        placelists = list(scalars.all())

        entities = await placelists_repository.get_by_content(session, placelists[0].name)

        assert len(entities) == 1
        assert entities[0].id == placelists[0].id


@pytest.mark.asyncio
async def test_get_by_content_invalid(
    fake_database: FakeDatabase, placelists_repository: AbstractPlacelistsRepository
) -> None:
    name = "name_test"

    async with fake_database.session_maker() as session:
        entities = await placelists_repository.get_by_content(session, name)

        assert len(entities) == 0


@pytest.mark.asyncio
async def test_create(fake_database: FakeDatabase, placelists_repository: AbstractPlacelistsRepository) -> None:
    async with fake_database.session_maker() as session:
        placelists_scalars = await session.scalars(select(PlacelistEntity))
        placelists = list(placelists_scalars.all())

        users_scalars = await session.scalars(select(UserEntity))
        user = users_scalars.first()

        new_placelist = PlacelistEntity(id=uuid4(), name="New Placelist", author=user, users=[user])

        entity = await placelists_repository.create(session, new_placelist)

        new_placelists_scalars = await session.scalars(select(PlacelistEntity))
        new_placelists = list(new_placelists_scalars.all())

        assert entity is not None
        assert entity.id not in [placelist.id for placelist in placelists]
        assert len(new_placelists) == len(placelists) + 1
        assert entity.author.id == user.id
        assert user in entity.users


@pytest.mark.asyncio
async def test_delete(fake_database: FakeDatabase, placelists_repository: AbstractPlacelistsRepository) -> None:
    async with fake_database.session_maker() as session:
        scalars = await session.scalars(select(PlacelistEntity))
        placelists = list(scalars.all())

        entity = await placelists_repository.delete(session, placelists[0])

        new_scalars = await session.scalars(select(PlacelistEntity))
        new_placelists = list(new_scalars.all())

        assert entity is not None
        assert entity.id not in [placelist.id for placelist in new_placelists]
