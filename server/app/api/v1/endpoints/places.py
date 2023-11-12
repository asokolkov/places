from fastapi import APIRouter, Depends

from api.utils import get_current_user
from models import Place, PlaceCreate, PlaceStatus, User


places_router = APIRouter(prefix="/places", tags=["Places"])


@places_router.get("/")
def get_by_query(query: str | None) -> list[Place]:
    raise NotImplementedError()


@places_router.post("/{public_id}/status")
def change_status(
    public_id: str, place_status: PlaceStatus, user: User = Depends(get_current_user)
) -> Place:
    raise NotImplementedError()


@places_router.post("/")
def create(place_create: PlaceCreate, user: User = Depends(get_current_user)) -> Place:
    raise NotImplementedError()
