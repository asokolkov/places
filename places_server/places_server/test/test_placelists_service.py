from uuid import uuid4

import pytest

from app.models.placelist import PlacelistCreate
from app.models.placelist import PlacelistUpdate
from app.services.placelists_service import AbstractPlacelistsService
from database.entities import PlaceEntity
from database.entities import PlacelistEntity
from database.entities import UserEntity


@pytest.mark.asyncio
async def test_get_by_content_valid(
    placelists_service: AbstractPlacelistsService, fake_database_placelists: list[PlacelistEntity]
) -> None:
    name = fake_database_placelists[0].name

    placelists_list = await placelists_service.get_by_content(name)

    assert placelists_list is not None
    assert len(placelists_list.placelists) == 1
    assert name in [i.name for i in placelists_list.placelists]
    assert placelists_list.placelists[0].author is not None


@pytest.mark.asyncio
async def test_get_by_content_invalid(
    placelists_service: AbstractPlacelistsService, fake_database_placelists: list[PlacelistEntity]
) -> None:
    name = "test_name"

    placelists_list = await placelists_service.get_by_content(name)

    assert placelists_list is not None
    assert len(placelists_list.placelists) == 0


@pytest.mark.asyncio
async def test_get_valid(
    placelists_service: AbstractPlacelistsService, fake_database_placelists: list[PlacelistEntity]
) -> None:
    placelist_id = fake_database_placelists[0].id

    placelist = await placelists_service.get(placelist_id)

    assert placelist is not None
    assert placelist.id == placelist_id


@pytest.mark.asyncio
async def test_get_invalid(placelists_service: AbstractPlacelistsService) -> None:
    placelist_id = uuid4()

    placelist = await placelists_service.get(placelist_id)

    assert placelist is None


@pytest.mark.asyncio
async def test_update_valid(
    placelists_service: AbstractPlacelistsService,
    fake_database_placelists: list[PlacelistEntity],
    fake_database_places: list[PlaceEntity],
) -> None:
    placelist = fake_database_placelists[0]
    placelist_to_update = PlacelistUpdate(name="New Name", places_ids=[fake_database_places[0].id])
    user = fake_database_placelists[0].author

    updated_placelist = await placelists_service.update(placelist.id, placelist_to_update, user.id)

    assert updated_placelist is not None
    assert updated_placelist.name == "New Name"
    assert len(updated_placelist.places) == 1
    assert updated_placelist.places[0].id == fake_database_places[0].id


@pytest.mark.asyncio
async def test_update_invalid_user_id(
    placelists_service: AbstractPlacelistsService,
    fake_database_placelists: list[PlacelistEntity],
    fake_database_places: list[PlaceEntity],
) -> None:
    placelist = fake_database_placelists[0]
    placelist_to_update = PlacelistUpdate(name="New Name", places_ids=[fake_database_places[0].id])
    user_id = uuid4()

    updated_placelist = await placelists_service.update(placelist.id, placelist_to_update, user_id)

    assert updated_placelist is None


@pytest.mark.asyncio
async def test_update_invalid_places_ids(
    placelists_service: AbstractPlacelistsService, fake_database_placelists: list[PlacelistEntity]
) -> None:
    placelist = fake_database_placelists[0]
    placelist_to_update = PlacelistUpdate(name="New Name", places_ids=[uuid4()])
    user_id = fake_database_placelists[0].author.id

    updated_placelist = await placelists_service.update(placelist.id, placelist_to_update, user_id)

    assert updated_placelist is not None
    assert updated_placelist.name == "New Name"
    assert len(updated_placelist.places) == 0


@pytest.mark.asyncio
async def test_update_invalid_placelist_id(placelists_service: AbstractPlacelistsService) -> None:
    placelist_id = uuid4()
    placelist_to_update = PlacelistUpdate(name="New Name", places_ids=[uuid4()])
    user_id = uuid4()

    updated_placelist = await placelists_service.update(placelist_id, placelist_to_update, user_id)

    assert updated_placelist is None


@pytest.mark.asyncio
async def test_create_valid(
    placelists_service: AbstractPlacelistsService,
    fake_database_placelists: list[PlacelistEntity],
    fake_database_users: list[UserEntity],
) -> None:
    new_placelist = PlacelistCreate(name="New Placelist")
    user_id = fake_database_users[0].id

    placelist = await placelists_service.create(new_placelist, user_id)

    assert placelist is not None
    assert placelist.author.id == user_id


@pytest.mark.asyncio
async def test_create_invalid_user_id(
    placelists_service: AbstractPlacelistsService, fake_database_placelists: list[PlacelistEntity]
) -> None:
    new_placelist_name = "New Placelist"
    user_id = uuid4()

    placelist = await placelists_service.create(new_placelist_name, user_id)

    assert placelist is None


@pytest.mark.asyncio
async def test_delete_valid(
    placelists_service: AbstractPlacelistsService,
    fake_database_placelists: list[PlacelistEntity],
    fake_database_users: list[UserEntity],
) -> None:
    placelist_id = fake_database_placelists[0].id
    user_id = fake_database_placelists[0].author.id

    placelist = await placelists_service.delete(placelist_id, user_id)

    assert placelist is not None
    assert placelist.author.id == user_id


@pytest.mark.asyncio
async def test_delete_invalid_user_id(
    placelists_service: AbstractPlacelistsService, fake_database_placelists: list[PlacelistEntity]
) -> None:
    placelist_id = fake_database_placelists[0].id
    user_id = uuid4()

    placelist = await placelists_service.delete(placelist_id, user_id)

    assert placelist is None


@pytest.mark.asyncio
async def test_delete_invalid_not_same_user_id(
    placelists_service: AbstractPlacelistsService,
    fake_database_placelists: list[PlacelistEntity],
    fake_database_users: list[UserEntity],
) -> None:
    placelist_id = fake_database_placelists[0].id
    user_id = fake_database_users[0].id

    placelist = await placelists_service.delete(placelist_id, user_id)

    assert placelist is None


@pytest.mark.asyncio
async def test_delete_invalid_placelist_id(placelists_service: AbstractPlacelistsService) -> None:
    placelist_id = uuid4()
    user_id = uuid4()

    placelist = await placelists_service.delete(placelist_id, user_id)

    assert placelist is None
