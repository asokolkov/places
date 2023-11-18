from uuid import UUID

from fastapi import APIRouter, Depends

from api.utils.dependencies import get_current_user
from api.utils.dependencies import users_service
from models.user import User
from models.user import UserCompressed
from models.user import UserIdentity
from models.user import UserPlacelist

users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.get("/current")
async def get_current(user: UserIdentity = Depends(get_current_user)) -> UserIdentity:
    return user


@users_router.get("/current/placelists")
async def get_current_placelists(
    user: User = Depends(get_current_user),
) -> list[UserPlacelist]:
    return await users_service.get_placelists(user.id)


@users_router.get("/{user_id}")
async def get_by_id(user_id: UUID) -> UserCompressed:
    user = await users_service.get(user_id)
    return user
