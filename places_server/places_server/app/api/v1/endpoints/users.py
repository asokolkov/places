from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from places_server.app.models.user import UserWithToken
from places_server.app.api.v1.dependencies import get_current_user
from places_server.app.api.v1.dependencies import users_service
from places_server.app.models.user import User
from places_server.app.models.user import UserCompressed
from places_server.app.models.user import UserPlacelists
from places_server.app.models.user import UserSignup
from places_server.app.models.user import UserToken
from places_server.app.models.user import UserUpdate


users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.get("/current")
async def get_current(user: User = Depends(get_current_user)) -> User:
    return user


@users_router.get("/current/placelists")
async def get_current_placelists(user: User = Depends(get_current_user)) -> UserPlacelists:
    return await users_service.get_placelists(user.id)


@users_router.get("/{user_id}")
async def get_by_id(user_id: UUID) -> UserCompressed:
    user = await users_service.get(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@users_router.post("/signin")
async def signin(form_data: OAuth2PasswordRequestForm = Depends()) -> UserToken:
    token = await users_service.signin(form_data.username, form_data.password)
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    return token


@users_router.post("/signup")
async def signup(user_signup: UserSignup) -> User:
    signed_user = await users_service.signup(user_signup)
    if signed_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User already registered",
        )
    return signed_user


@users_router.put("/current")
async def update(user_update: UserUpdate, user: User = Depends(get_current_user)) -> UserWithToken:
    updated_user = await users_service.update(user_update, user.id)
    if updated_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong while updating user",
        )
    return updated_user
