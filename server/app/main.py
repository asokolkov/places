from fastapi import FastAPI

from api.v1.api import api_router
from configs import API_VERSION, APP_NAME


app = FastAPI(title=APP_NAME, version=API_VERSION)
app.include_router(api_router)
