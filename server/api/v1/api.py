from fastapi import APIRouter

from server.api.v1.endpoints.accounts import accounts_router
from server.api.v1.endpoints.placelists import placelists_router
from server.api.v1.endpoints.places import places_router
from server.api.v1.endpoints.users import users_router


api_router = APIRouter(prefix="/api/v1")

api_router.include_router(accounts_router)
api_router.include_router(placelists_router)
api_router.include_router(places_router)
api_router.include_router(users_router)
