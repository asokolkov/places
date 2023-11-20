from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from api.utils.dependencies import get_current_user, users_service
from models.user import UserCompressed, UserIdentity, UserPlacelists


users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.get("/current")
async def get_current(user: UserIdentity = Depends(get_current_user)) -> UserIdentity:
    return user


@users_router.get("/current/placelists")
async def get_current_placelists(
    user: UserIdentity = Depends(get_current_user),
) -> UserPlacelists:
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
