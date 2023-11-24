from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi import HTTPException
from starlette import status

from api.utils.dependencies import get_current_user
from api.utils.dependencies import placelists_service
from models.placelist import Placelist
from models.placelist import PlacelistCreate
from models.placelist import PlacelistPlaceAdd
from models.placelist import PlacelistsList
from models.user import UserIdentity


CONTENT_MIN_LENGTH = 3


placelists_router = APIRouter(prefix="/placelists", tags=["Placelists"])


@placelists_router.get("/")
async def get_by_content(content: str) -> PlacelistsList:
    if len(content) < CONTENT_MIN_LENGTH:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Content length must be >= {CONTENT_MIN_LENGTH}",
        )
    return await placelists_service.get_by_content(content)


@placelists_router.get("/{placelist_id}")
async def get(placelist_id: UUID, user: UserIdentity = Depends(get_current_user)) -> Placelist:
    placelist = await placelists_service.get(placelist_id, user.id)
    if placelist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Placelist not found",
        )
    return placelist


@placelists_router.post("/")
async def create(
    placelist_create: PlacelistCreate, user: UserIdentity = Depends(get_current_user)
) -> Placelist:
    return await placelists_service.create(placelist_create, user)


@placelists_router.post("/{placelist_id}/places")
async def add_place(
    placelist_id: UUID, place: PlacelistPlaceAdd, user: UserIdentity = Depends(get_current_user)
) -> Placelist:
    placelist = await placelists_service.add_place(placelist_id, place.id, user.id)
    if placelist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong while adding place to placelist",
        )
    return placelist


@placelists_router.post("/{placelist_id}/copy")
async def copy(placelist_id: UUID, user: UserIdentity = Depends(get_current_user)) -> Placelist:
    placelist = await placelists_service.copy(placelist_id, user.id)
    if placelist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong while copying placelist",
        )
    return placelist


@placelists_router.delete("/{placelist_id}")
async def delete(placelist_id: UUID, user: UserIdentity = Depends(get_current_user)) -> Placelist:
    placelist = await placelists_service.delete(placelist_id, user.id)
    if placelist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong while deleting placelist",
        )
    return placelist
