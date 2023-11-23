import enum
from uuid import UUID

from sqlmodel import SQLModel


class PlaceStatus(enum.Enum):
    NOT_VISITED = 0
    SCHEDULED = 1
    VISITED = 2
    NOT_INTERESTED = 3


class Place(SQLModel):
    id: UUID
    name: str
    address: str
    status: PlaceStatus


class PlacesList(SQLModel):
    places: list[Place]


class PlaceCreate(SQLModel):
    name: str
    address: str
    latitude: float
    longitude: float


class PlaceUpdate(SQLModel):
    id: UUID
    status: PlaceStatus
