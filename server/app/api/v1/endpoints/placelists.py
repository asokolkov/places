from fastapi import APIRouter, Depends

from api.utils import get_current_user
from models import Place, Placelist, PlacelistCompressed, PlacelistCreate, User


placelists_router = APIRouter(prefix="/placelists", tags=["Placelists"])


@placelists_router.get("/")
def get_by_query(query: str | None) -> list[PlacelistCompressed]:
    raise NotImplementedError()


@placelists_router.get("/{public_id}")
def get(public_id: str, user: User = Depends(get_current_user)) -> Placelist:
    raise NotImplementedError()


@placelists_router.post("/")
def create(
    placelist_create: PlacelistCreate, user: User = Depends(get_current_user)
) -> Placelist:
    raise NotImplementedError()


@placelists_router.post("/{public_id}/places")
def add_place(
    public_id: str, place: Place, user: User = Depends(get_current_user)
) -> Placelist:
    raise NotImplementedError()


@placelists_router.post("/{public_id}/copy")
def copy(public_id: str, user: User = Depends(get_current_user)) -> Placelist:
    raise NotImplementedError()


@placelists_router.delete("/{public_id}")
def delete(public_id: str, user: User = Depends(get_current_user)) -> Placelist:
    raise NotImplementedError()
