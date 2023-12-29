from uuid import uuid4

import pytest

from app.models.user import UserSignup
from app.models.user import UserUpdate
from app.services.users_service import AbstractUsersService
from database.entities import UserEntity


@pytest.mark.asyncio
async def test_get_valid(users_service: AbstractUsersService, fake_database_users: list[UserEntity]) -> None:
    user_id = fake_database_users[0].id

    user = await users_service.get(user_id)

    assert user is not None
    assert user.id == user_id


@pytest.mark.asyncio
async def test_get_invalid(users_service: AbstractUsersService) -> None:
    user_id = uuid4()

    user = await users_service.get(user_id)

    assert user is None


@pytest.mark.asyncio
async def test_get_placelists_valid(users_service: AbstractUsersService, fake_database_users: list[UserEntity]) -> None:
    user_id = fake_database_users[1].id

    placelists = await users_service.get_placelists(user_id)

    assert placelists is not None
    assert len(placelists.placelists) == 2


@pytest.mark.asyncio
async def test_get_placelists_invalid(users_service: AbstractUsersService) -> None:
    user_id = uuid4()

    placelists = await users_service.get_placelists(user_id)

    assert placelists is not None
    assert len(placelists.placelists) == 0


@pytest.mark.asyncio
async def test_signup_valid(users_service: AbstractUsersService) -> None:
    user_signup = UserSignup(name="A", mail="A", username="A", password="A")

    user = await users_service.signup(user_signup)

    assert user is not None
    assert user.name == user_signup.name


@pytest.mark.asyncio
async def test_signup_invalid_mail(users_service: AbstractUsersService) -> None:
    user_signup = UserSignup(name="A", mail="m0", username="A", password="A")

    user = await users_service.signup(user_signup)

    assert user is None


@pytest.mark.asyncio
async def test_signup_invalid_username(users_service: AbstractUsersService) -> None:
    user_signup = UserSignup(name="A", mail="A", username="u1", password="A")

    user = await users_service.signup(user_signup)

    assert user is None


@pytest.mark.asyncio
async def test_signin_valid(users_service: AbstractUsersService, fake_database_users: list[UserEntity]) -> None:
    mail = "m0"
    password = "p0"

    user = await users_service.signin(mail, password)

    assert user is not None


@pytest.mark.asyncio
async def test_signin_invalid_mail_or_password(
    users_service: AbstractUsersService, fake_database_users: list[UserEntity]
) -> None:
    mail = "m0"
    password = "p1"

    user = await users_service.signin(mail, password)

    assert user is None


@pytest.mark.asyncio
async def test_update_valid(users_service: AbstractUsersService, fake_database_users: list[UserEntity]) -> None:
    user_id = fake_database_users[0].id
    user_update = UserUpdate(name="A", mail="A", username="A", password="A", old_password="p0")

    user = await users_service.update(user_update, user_id)

    assert user is not None
    assert user.id == user_id
    assert user.name == user_update.name
    assert user.token is not None


@pytest.mark.asyncio
async def test_update_invalid_user_id(users_service: AbstractUsersService) -> None:
    user_id = uuid4()
    user_update = UserUpdate(name="A", mail="A", username="A", password="A", old_password="p0")

    user = await users_service.update(user_update, user_id)

    assert user is None


@pytest.mark.asyncio
async def test_update_invalid_password(
    users_service: AbstractUsersService, fake_database_users: list[UserEntity]
) -> None:
    user_id = fake_database_users[0].id
    user_update = UserUpdate(name="A", mail="A", username="A", password="A", old_password="A")

    user = await users_service.update(user_update, user_id)

    assert user is None


@pytest.mark.asyncio
async def test_update_invalid_mail(users_service: AbstractUsersService, fake_database_users: list[UserEntity]) -> None:
    user_id = fake_database_users[0].id
    user_update = UserUpdate(name="A", mail="m1", username="A", password="A", old_password="p0")

    user = await users_service.update(user_update, user_id)

    assert user is None


@pytest.mark.asyncio
async def test_update_invalid_username(
    users_service: AbstractUsersService, fake_database_users: list[UserEntity]
) -> None:
    user_id = fake_database_users[0].id
    user_update = UserUpdate(name="A", mail="A", username="u1", password="A", old_password="p0")

    user = await users_service.update(user_update, user_id)

    assert user is None
