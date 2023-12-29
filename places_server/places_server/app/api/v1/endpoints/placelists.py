from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi import HTTPException
from starlette import status

from app.api.v1.dependencies import get_current_user
from app.api.v1.dependencies import placelists_service
from app.models.placelist import Placelist
from app.models.placelist import PlacelistCreate
from app.models.placelist import PlacelistsList
from app.models.placelist import PlacelistUpdate
from app.models.user import User

placelists_router = APIRouter(prefix="/placelists", tags=["Placelists"])


@placelists_router.get("/")
async def get_by_content(content: str) -> PlacelistsList:
    return await placelists_service.get_by_content(content)


@placelists_router.get("/{placelist_id}")
async def get(placelist_id: UUID) -> Placelist:
    placelist = await placelists_service.get(placelist_id)
    if placelist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Placelist not found",
        )
    return placelist


@placelists_router.put("/{placelist_id}")
async def update(
    placelist_id: UUID, placelist_update: PlacelistUpdate, user: User = Depends(get_current_user)
) -> Placelist:
    placelist = await placelists_service.update(placelist_id, placelist_update, user.id)
    if placelist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong while updating placelist",
        )
    return placelist


@placelists_router.post("/")
async def create(placelist_create: PlacelistCreate, user: User = Depends(get_current_user)) -> Placelist:
    placelist = await placelists_service.create(placelist_create, user.id)
    if placelist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong while creating placelist",
        )
    return placelist


@placelists_router.delete("/{placelist_id}")
async def delete(placelist_id: UUID, user: User = Depends(get_current_user)) -> Placelist:
    placelist = await placelists_service.delete(placelist_id, user.id)
    if placelist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong while deleting placelist",
        )
    return placelist
