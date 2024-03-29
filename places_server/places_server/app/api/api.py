from fastapi import APIRouter

from places_server.app.api.v1.v1 import v1_router


api_router = APIRouter(prefix="/api")

api_router.include_router(v1_router)
