from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models import AccountToken


accounts_router = APIRouter(prefix="/accounts", tags=["Accounts"])


@accounts_router.post("/signin")
def signin(form_data: OAuth2PasswordRequestForm = Depends()) -> AccountToken:
    raise NotImplementedError()


@accounts_router.post("/signup")
def signup(form_data: OAuth2PasswordRequestForm = Depends()) -> AccountToken:
    raise NotImplementedError()
