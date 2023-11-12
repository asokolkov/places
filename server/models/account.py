from pydantic import BaseModel


class AccountToken(BaseModel):
    token: str
