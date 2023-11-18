from uuid import UUID

from fastapi import Request
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from starlette import status
from db.database import Database
from repositories.identity_repository import IdentityRepository
from repositories.users_repository import UsersRepository
from services.identity_service import IdentityService
from services.users_service import UsersService


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/identity/signin")

database = Database()

identity_repository = IdentityRepository(database)
identity_service = IdentityService(identity_repository)

users_repository = UsersRepository(database)
users_service = UsersService(users_repository)


async def get_current_user(request: Request):
    token = request.cookies.get('session_token')
    user = await identity_service.decode_token(token)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    return user
