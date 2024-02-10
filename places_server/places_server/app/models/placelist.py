from uuid import UUID

from pydantic import BaseModel


class PlacelistUser(BaseModel):
    id: UUID
    name: str


class PlacelistCompressed(BaseModel):
    id: UUID
    name: str
    author: PlacelistUser


class PlacelistsList(BaseModel):
    placelists: list[PlacelistCompressed]


class PlacelistPlace(BaseModel):
    id: UUID
    name: str
    address: str


class Placelist(BaseModel):
    id: UUID
    name: str
    author: PlacelistUser
    places: list[PlacelistPlace]


class PlacelistCreate(BaseModel):
    name: str


class PlacelistUpdate(BaseModel):
    name: str
    places_ids: list[UUID]
