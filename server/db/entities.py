import enum
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import Enum, Column


class PlaceStatus(int, enum.Enum):
    NEVER_BEEN = 0
    SCHEDULED = 1
    VISITED = 2
    NOT_INTERESTED = 3


class UserPlacelistLink(SQLModel, table=True):
    user_id: UUID | None = Field(default=None, foreign_key="user.id", primary_key=True)
    placelist_id: UUID | None = Field(default=None, foreign_key="placelist.id", primary_key=True)


class UserPlaceLink(SQLModel, table=True):
    user_id: UUID | None = Field(default=None, foreign_key="user.id", primary_key=True)
    place_id: UUID | None = Field(default=None, foreign_key="place.id", primary_key=True)
    status: PlaceStatus = Column(Enum(PlaceStatus))


class PlacelistPlaceLink(SQLModel, table=True):
    placelist_id: UUID | None = Field(default=None, foreign_key="placelist.id", primary_key=True)
    place_id: UUID | None = Field(default=None, foreign_key="place.id", primary_key=True)


class User(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    mail: str
    username: str
    name: str
    password: str
    placelists: list["Placelist"] = Relationship(link_model=UserPlacelistLink, back_populates="users")
    places: list["Place"] = Relationship(link_model=UserPlaceLink, back_populates="users")


class Placelist(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    name: str
    author_id: UUID
    users: list["User"] = Relationship(link_model=UserPlacelistLink, back_populates="placelists")
    places: list["Place"] = Relationship(link_model=PlacelistPlaceLink, back_populates="placelists")


class Place(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    name: str
    address: str
    latitude: float
    longitude: float
    users: list["User"] = Relationship(link_model=UserPlaceLink, back_populates="places")
    placelists: list["Placelist"] = Relationship(link_model=PlacelistPlaceLink, back_populates="places")
