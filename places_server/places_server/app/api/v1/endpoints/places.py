from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from starlette import status

from app.api.v1.dependencies import get_current_user
from app.api.v1.dependencies import places_service
from app.models.place import Place
from app.models.place import PlaceCreate
from app.models.place import PlacesList
from app.models.user import User


places_router = APIRouter(prefix="/places", tags=["Places"])


@places_router.get("/")
async def get_by_content(content: str) -> PlacesList:
    return await places_service.get_by_content(content)


@places_router.post("/")
async def create(place_create: PlaceCreate, user: User = Depends(get_current_user)) -> Place:
    place = await places_service.create(place_create, user.id)
    if place is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong while creating place",
        )
    return place
