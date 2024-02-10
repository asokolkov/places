from uuid import UUID

from pydantic import BaseModel


class PlacesList(BaseModel):
    places: list["Place"]


class Place(BaseModel):
    id: UUID
    name: str
    address: str
    latitude: float
    longitude: float


class PlaceCreate(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float
