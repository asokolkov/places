from fastapi import APIRouter, Depends

from server.api.utils import get_current_user
from server.models import PlacelistCompressed, User


users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.get("/{public_id}")
def get_by_id(public_id: str) -> User:
    raise NotImplementedError()


@users_router.get("/current")
def get_current(user: User = Depends(get_current_user)) -> User:
    raise NotImplementedError()


@users_router.get("/current/placelists")
def get_current_placelists(
    user: User = Depends(get_current_user),
) -> list[PlacelistCompressed]:
    raise NotImplementedError()
