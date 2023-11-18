from uuid import UUID
from sqlmodel import SQLModel


class UserSignup(SQLModel):
    name: str


class UserCreate(SQLModel):
    name: str
    username: str
    mail: str
    password: str


class UserUpdate(SQLModel):
    id: UUID
    name: str
    username: str
    mail: str
    password: str


class UserCompressed(SQLModel):
    id: UUID
    name: str
    username: str


class UserPlacelist(SQLModel):
    id: UUID
    name: str
    author_name: str


class UserIdentity(SQLModel):
    id: UUID
    name: str
    username: str
    mail: str


class User(SQLModel):
    id: UUID
    name: str
    username: str
    mail: str
    placelists: list[UserPlacelist]
