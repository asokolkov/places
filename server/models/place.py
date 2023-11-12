import enum

from pydantic import BaseModel


class PlaceStatus(enum.Enum):
    NOT_VISITED = 0
    SCHEDULED = 1
    VISITED = 2
    NOT_INTERESTED = 3


class Place(BaseModel):
    name: str
    public_id: str
    address: str
    visited: bool


class PlaceCreate(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float
