import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from places_server.configs import settings
from places_server.app.api.api import api_router


app = FastAPI(title=settings.APP_NAME)

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
