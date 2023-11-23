from fastapi import APIRouter, Depends
from fastapi import HTTPException
from starlette import status

from api.utils.dependencies import get_current_user
from api.utils.dependencies import places_service
from models.place import Place
from models.place import PlaceCreate
from models.place import PlacesList
from models.place import PlaceUpdate
from models.user import UserIdentity


CONTENT_MIN_LENGTH = 3


places_router = APIRouter(prefix="/places", tags=["Places"])


@places_router.get("/")
async def get_by_content(content: str, user: UserIdentity = Depends(get_current_user)) -> PlacesList:
    if len(content) < CONTENT_MIN_LENGTH:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Content length must be >= {CONTENT_MIN_LENGTH}",
        )
    return await places_service.get_by_content(content, user.id)


@places_router.post("/")
async def create(place_create: PlaceCreate, user: UserIdentity = Depends(get_current_user)) -> Place:
    return await places_service.create(place_create)


@places_router.put("/")
async def update(place: PlaceUpdate, user: UserIdentity = Depends(get_current_user)) -> Place:
    place = await places_service.change_status(place, user.id)
    if place is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Error on update happened',
        )
    return place
