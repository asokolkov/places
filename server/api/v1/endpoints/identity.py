from datetime import datetime
from datetime import timedelta
from datetime import timezone

from fastapi import APIRouter
from fastapi import HTTPException
from starlette import status
from fastapi import Response
from api.utils.dependencies import identity_service
from configs import JWT_TOKEN_EXPIRE_DAYS
from models.identity import IdentitySignin, IdentitySignup

identity_router = APIRouter(prefix="/identity", tags=["Identity"])


@identity_router.post("/signin")
async def signin(response: Response, identity_signin: IdentitySignin):
    user_identity, token = await identity_service.signin(identity_signin)
    if user_identity is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    response.set_cookie(
        key="session_token", value=token, httponly=True, samesite='lax',
        expires=datetime.now(timezone.utc) + timedelta(days=JWT_TOKEN_EXPIRE_DAYS)
    )
    return user_identity


@identity_router.post("/signup")
async def signup(response: Response, identity_signup: IdentitySignup):
    user_identity, token = await identity_service.signup(identity_signup)
    if user_identity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User already registered",
        )
    response.set_cookie(
        key="session_token", value=token, httponly=True, samesite='lax',
        expires=datetime.now(timezone.utc) + timedelta(days=JWT_TOKEN_EXPIRE_DAYS)
    )
    return user_identity
