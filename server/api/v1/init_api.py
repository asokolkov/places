from fastapi import APIRouter

from api.v1.endpoints.identity import identity_router
from api.v1.endpoints.users import users_router


api_router = APIRouter(prefix="/api/v1")

api_router.include_router(identity_router)
# api_router.include_router(placelists_router)
# api_router.include_router(places_router)
api_router.include_router(users_router)
