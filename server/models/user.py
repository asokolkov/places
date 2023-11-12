from pydantic import BaseModel


class User(BaseModel):
    public_id: str
    name: str
    username: str
