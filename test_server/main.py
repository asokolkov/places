from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from data import placelists

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/placelists")
async def say_hello(query: str | None = None):
    if query is None:
        return placelists
    if len(query) < 3:
        return []
    lower_query = query.lower()
    return [i for i in placelists if lower_query in i['name'].lower() or lower_query in i['user'].lower()]
