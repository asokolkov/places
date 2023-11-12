from pydantic import BaseModel

from .place import Place
from .user import User


class Placelist(BaseModel):
    name: str
    public_id: str
    author: User
    places: list[Place]


class PlacelistCompressed(BaseModel):
    name: str
    public_id: str
    author_name: str


class PlacelistCreate(BaseModel):
    name: str
