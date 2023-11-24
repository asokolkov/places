from sqlmodel import SQLModel


class IdentitySignin(SQLModel):
    mail: str
    password: str


class IdentitySignup(SQLModel):
    name: str
    username: str
    mail: str
    password: str


class IdentityUpdateMail(SQLModel):
    new_mail: str
    password: str


class IdentityUpdateUsername(SQLModel):
    new_username: str
    password: str


class IdentityUpdatePassword(SQLModel):
    old_password: str
    new_password: str


class IdentityUpdateName(SQLModel):
    new_name: str
