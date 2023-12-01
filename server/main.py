import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.init_api import api_router
from configs import API_VERSION, APP_NAME


app = FastAPI(title=APP_NAME, version=API_VERSION)
app.include_router(api_router)

origins = [
   "http://localhost:8000",
   "http://localhost:5173",
]

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
   expose_headers=["set-cookie"]
)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
