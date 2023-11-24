from fastapi import APIRouter, HTTPException, Response
from fastapi import Depends
from starlette import status

from api.utils.dependencies import get_current_user
from api.utils.dependencies import identity_service
from models.identity import IdentitySignin, IdentitySignup
from models.identity import IdentityUpdateMail
from models.identity import IdentityUpdateName
from models.identity import IdentityUpdatePassword
from models.identity import IdentityUpdateUsername
from models.user import UserIdentity

identity_router = APIRouter(prefix="/identity", tags=["Identity"])


@identity_router.post("/signin")
async def signin(response: Response, identity_signin: IdentitySignin):
    user_identity, token, expiration = await identity_service.signin(identity_signin)
    if user_identity is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        samesite="lax",
        expires=expiration,
    )
    return user_identity


@identity_router.post("/signup")
async def signup(response: Response, identity_signup: IdentitySignup):
    user_identity, token, expiration = await identity_service.signup(identity_signup)
    if user_identity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User already registered",
        )
    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        samesite="lax",
        expires=expiration,
    )
    return user_identity


@identity_router.post("/mail")
async def update_mail(response: Response, identity_update_mail: IdentityUpdateMail, user: UserIdentity = Depends(get_current_user)):
    user_identity, token, expiration = await identity_service.update_mail(identity_update_mail, user)
    if user_identity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong while updating mail",
        )
    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        samesite="lax",
        expires=expiration,
    )
    return user_identity


@identity_router.post("/password")
async def update_password(response: Response, identity_update_password: IdentityUpdatePassword, user: UserIdentity = Depends(get_current_user)):
    user_identity, token, expiration = await identity_service.update_password(identity_update_password, user)
    if user_identity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong while updating password",
        )
    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        samesite="lax",
        expires=expiration,
    )
    return user_identity


@identity_router.post("/username")
async def update_password(response: Response, identity_update_username: IdentityUpdateUsername, user: UserIdentity = Depends(get_current_user)):
    user_identity, token, expiration = await identity_service.update_username(identity_update_username, user)
    if user_identity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong while updating username",
        )
    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        samesite="lax",
        expires=expiration,
    )
    return user_identity


@identity_router.post("/name")
async def update_password(response: Response, identity_update_name: IdentityUpdateName, user: UserIdentity = Depends(get_current_user)):
    user_identity, token, expiration = await identity_service.update_name(identity_update_name, user)
    if user_identity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong while updating name",
        )
    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        samesite="lax",
        expires=expiration,
    )
    return user_identity
