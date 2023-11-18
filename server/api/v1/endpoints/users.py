from uuid import UUID

from fastapi import APIRouter, Depends

from api.utils.dependencies import get_current_user
from api.utils.dependencies import users_repository
from models.user import User
from models.user import UserPlacelist

users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.get("/{user_id}")
async def get_by_id(user_id: UUID) -> User:
    user = await users_repository.get(user_id)
    return user


@users_router.get("/current")
async def get_current(user: User = Depends(get_current_user)) -> User:
    return user


@users_router.get("/current/placelists")
async def get_current_placelists(
    user: User = Depends(get_current_user),
) -> list[UserPlacelist]:
    return await users_repository.get_placelists(user)
