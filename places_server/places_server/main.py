from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from places_server.app.api.api import api_router
from places_server.app.api.v1.dependencies import database
from places_server.configs import settings


@asynccontextmanager
async def lifespan(_: FastAPI):
    await database.create_tables()
    yield


app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(api_router)


def main() -> None:
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT)


if __name__ == "__main__":
    main()
