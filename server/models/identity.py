from sqlmodel import SQLModel


class IdentitySignin(SQLModel):
    mail: str
    password: str


class IdentitySignup(SQLModel):
    name: str
    username: str
    mail: str
    password: str
