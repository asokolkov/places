from uuid import uuid4

import pytest

from app.models.place import PlaceCreate
from app.services.places_service import AbstractPlacesService
from database.entities import PlaceEntity
from database.entities import PlacelistEntity
from database.entities import UserEntity


@pytest.mark.asyncio
async def test_get_by_content_valid(
    places_service: AbstractPlacesService, fake_database_places: list[PlaceEntity]
) -> None:
    name = fake_database_places[0].name

    places_list = await places_service.get_by_content(name)

    assert places_list is not None
    assert len(places_list.places) == 1
    assert name in [i.name for i in places_list.places]


@pytest.mark.asyncio
async def test_get_by_content_invalid(places_service: AbstractPlacesService) -> None:
    name = "test_name"

    places_list = await places_service.get_by_content(name)

    assert places_list is not None
    assert len(places_list.places) == 0


@pytest.mark.asyncio
async def test_get_valid(places_service: AbstractPlacesService, fake_database_places: list[PlaceEntity]) -> None:
    place_id = fake_database_places[0].id

    place = await places_service.get(place_id)

    assert place is not None
    assert place.id == place_id


@pytest.mark.asyncio
async def test_get_invalid(places_service: AbstractPlacesService) -> None:
    place_id = uuid4()

    place = await places_service.get(place_id)

    assert place is None


@pytest.mark.asyncio
async def test_create_valid(
    places_service: AbstractPlacesService,
    fake_database_places: list[PlaceEntity],
    fake_database_placelists: list[PlacelistEntity],
    fake_database_users: list[UserEntity],
) -> None:
    new_place = PlaceCreate(name="New Place", address="New Address", latitude=101.0, longitude=102.0)
    user_id = fake_database_users[1].id

    place = await places_service.create(new_place, user_id)

    assert place is not None
    assert place.name == new_place.name


@pytest.mark.asyncio
async def test_create_invalid_user_id(
    places_service: AbstractPlacesService,
    fake_database_places: list[PlaceEntity],
    fake_database_placelists: list[PlacelistEntity],
    fake_database_users: list[UserEntity],
) -> None:
    new_place = PlaceCreate(name="New Place", address="New Address", latitude=101.0, longitude=102.0)
    user_id = uuid4()

    place = await places_service.create(new_place, user_id)

    assert place is None
