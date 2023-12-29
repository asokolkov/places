from fastapi import APIRouter

from app.api.v1.endpoints.placelists import placelists_router
from app.api.v1.endpoints.places import places_router
from app.api.v1.endpoints.users import users_router


v1_router = APIRouter(prefix="/v1")

v1_router.include_router(placelists_router)
v1_router.include_router(places_router)
v1_router.include_router(users_router)
