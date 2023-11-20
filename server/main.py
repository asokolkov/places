import uvicorn
from fastapi import FastAPI

from api.v1.init_api import api_router
from configs import API_VERSION, APP_NAME


app = FastAPI(title=APP_NAME, version=API_VERSION)
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
