import enum
from uuid import UUID

from sqlmodel import SQLModel


class PlaceStatus(enum.Enum):
    NOT_VISITED = 0
    SCHEDULED = 1
    VISITED = 2
    NOT_INTERESTED = 3


class PlacelistUser(SQLModel):
    id: UUID
    name: str


class PlacelistCompressed(SQLModel):
    id: UUID
    name: str
    author: PlacelistUser


class PlacelistsList(SQLModel):
    placelists: list[PlacelistCompressed]


class PlacelistPlace(SQLModel):
    id: UUID
    name: str
    address: str
    status: PlaceStatus


class PlacelistPlaceCompressed(SQLModel):
    id: UUID
    name: str
    address: str


class Placelist(SQLModel):
    id: UUID
    name: str
    author: PlacelistUser
    places: list[PlacelistPlace] | list[PlacelistPlaceCompressed]


class PlacelistCreate(SQLModel):
    name: str


class PlacelistPlaceAdd(SQLModel):
    id: UUID
