import asyncio

import pytest

from places_server.app.services.placelists_service import AbstractPlacelistsService
from places_server.app.services.placelists_service import PlacelistsService
from places_server.app.services.places_service import AbstractPlacesService
from places_server.app.services.places_service import PlacesService
from places_server.app.services.users_service import AbstractUsersService
from places_server.app.services.users_service import UsersService
from places_server.app.utils.cryptography import AbstractCryptography
from places_server.app.utils.cryptography import Cryptography
from places_server.database.entities import PlaceEntity
from places_server.database.entities import PlacelistEntity
from places_server.database.entities import UserEntity
from places_server.database.repositories.placelists_repository import AbstractPlacelistsRepository
from places_server.database.repositories.placelists_repository import PlacelistsRepository
from places_server.database.repositories.places_repository import AbstractPlacesRepository
from places_server.database.repositories.places_repository import PlacesRepository
from places_server.database.repositories.users_repository import AbstractUsersRepository
from places_server.database.repositories.users_repository import UsersRepository
from places_server.test.fake_classes import FakeDatabase


@pytest.fixture(scope="function")
def fake_database() -> FakeDatabase:
    database = FakeDatabase()
    asyncio.run(database.create_tables())
    return database


@pytest.fixture(scope="function")
def fake_database_users(fake_database: FakeDatabase) -> list[UserEntity]:
    users: list[UserEntity] = fake_database.users
    return users


@pytest.fixture(scope="function")
def fake_database_places(fake_database: FakeDatabase) -> list[PlaceEntity]:
    places: list[PlaceEntity] = fake_database.places
    return places


@pytest.fixture(scope="function")
def fake_database_placelists(fake_database: FakeDatabase) -> list[PlacelistEntity]:
    placelists: list[PlacelistEntity] = fake_database.placelists
    return placelists


@pytest.fixture(scope="function")
def users_repository() -> AbstractUsersRepository:
    return UsersRepository()


@pytest.fixture(scope="function")
def placelists_repository() -> AbstractPlacelistsRepository:
    return PlacelistsRepository()


@pytest.fixture(scope="function")
def places_repository() -> AbstractPlacesRepository:
    return PlacesRepository()


@pytest.fixture(scope="function")
def cryptography() -> AbstractCryptography:
    return Cryptography()


@pytest.fixture(scope="function")
def users_service(
    fake_database: FakeDatabase,
    placelists_repository: AbstractPlacelistsRepository,
    places_repository: AbstractPlacesRepository,
    users_repository: AbstractUsersRepository,
    cryptography: AbstractCryptography,
) -> AbstractUsersService:
    return UsersService(fake_database, placelists_repository, users_repository, places_repository, cryptography)


@pytest.fixture(scope="function")
def placelists_service(
    fake_database: FakeDatabase,
    placelists_repository: AbstractPlacelistsRepository,
    places_repository: AbstractPlacesRepository,
    users_repository: AbstractUsersRepository,
) -> AbstractPlacelistsService:
    return PlacelistsService(fake_database, placelists_repository, users_repository, places_repository)


@pytest.fixture(scope="function")
def places_service(
    fake_database: FakeDatabase,
    placelists_repository: AbstractPlacelistsRepository,
    places_repository: AbstractPlacesRepository,
    users_repository: AbstractUsersRepository,
) -> AbstractPlacesService:
    return PlacesService(fake_database, placelists_repository, users_repository, places_repository)
