from uuid import UUID

from sqlmodel import SQLModel


class UserIdentity(SQLModel):
    id: UUID
    name: str
    username: str
    mail: str


class UserPlacelist(SQLModel):
    id: UUID
    name: str
    author_name: str


class UserPlacelists(SQLModel):
    placelists: list[UserPlacelist]


class UserCompressed(SQLModel):
    id: UUID
    name: str
    username: str
