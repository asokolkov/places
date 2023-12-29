from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    id: UUID
    name: str
    username: str
    mail: str


class UserPlacelist(BaseModel):
    id: UUID
    name: str
    author: "UserCompressed"


class UserPlacelists(BaseModel):
    placelists: list[UserPlacelist]


class UserCompressed(BaseModel):
    id: UUID
    name: str
    username: str


class UserDecodedToken(BaseModel):
    id: UUID
    name: str
    username: str
    mail: str
    expiration_date: float


class UserSignup(BaseModel):
    name: str
    username: str
    mail: str
    password: str


class UserToken(BaseModel):
    type: str
    value: str


class UserWithToken(BaseModel):
    id: UUID
    name: str
    username: str
    mail: str
    token: UserToken


class UserUpdate(BaseModel):
    mail: str
    username: str
    password: str
    name: str
    old_password: str
