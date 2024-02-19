from uuid import uuid4

import pytest
from sqlalchemy import select

from places_server.database.entities import UserEntity
from places_server.database.repositories.users_repository import AbstractUsersRepository
from places_server.test.fake_classes import FakeDatabase


@pytest.mark.asyncio
async def test_get_existing_entity(fake_database: FakeDatabase, users_repository: AbstractUsersRepository) -> None:
    async with fake_database.session_maker() as session:
        scalars = await session.scalars(select(UserEntity))
        users = list(scalars.all())

        entity = await users_repository.get(session, users[0].id)

        assert entity is not None
        assert entity.id == users[0].id


@pytest.mark.asyncio
async def test_get_non_existing_entity(fake_database: FakeDatabase, users_repository: AbstractUsersRepository) -> None:
    async with fake_database.session_maker() as session:
        entity = await users_repository.get(session, uuid4())

        assert entity is None


@pytest.mark.asyncio
async def test_get_by_mail_valid(fake_database: FakeDatabase, users_repository: AbstractUsersRepository) -> None:
    async with fake_database.session_maker() as session:
        scalars = await session.scalars(select(UserEntity))
        users = list(scalars.all())

        entity = await users_repository.get_by_mail(session, users[0].mail)

        assert entity is not None
        assert entity.id == users[0].id


@pytest.mark.asyncio
async def test_get_by_mail_invalid(fake_database: FakeDatabase, users_repository: AbstractUsersRepository) -> None:
    mail = "mail_test"

    async with fake_database.session_maker() as session:
        entity = await users_repository.get_by_mail(session, mail)

        assert entity is None


@pytest.mark.asyncio
async def test_get_by_username_valid(fake_database: FakeDatabase, users_repository: AbstractUsersRepository) -> None:
    async with fake_database.session_maker() as session:
        scalars = await session.scalars(select(UserEntity))
        users = list(scalars.all())

        entity = await users_repository.get_by_username(session, users[0].username)

        assert entity is not None
        assert entity.id == users[0].id


@pytest.mark.asyncio
async def test_get_by_username_invalid(fake_database: FakeDatabase, users_repository: AbstractUsersRepository) -> None:
    username = "username_test"

    async with fake_database.session_maker() as session:
        entity = await users_repository.get_by_username(session, username)

        assert entity is None


@pytest.mark.asyncio
async def test_create(fake_database: FakeDatabase, users_repository: AbstractUsersRepository) -> None:
    new_user = UserEntity(
        id=uuid4(), name="New UserEntity", mail="New Mail", username="New Username", password="New Password"
    )

    async with fake_database.session_maker() as session:
        scalars = await session.scalars(select(UserEntity))
        users = list(scalars.all())

        entity = await users_repository.create(session, new_user)

        new_scalars = await session.scalars(select(UserEntity))
        new_users = list(new_scalars.all())

        assert entity is not None
        assert entity.id not in [user.id for user in users]
        assert len(new_users) == len(users) + 1
