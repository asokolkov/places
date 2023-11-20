from fastapi import Request
from fastapi import HTTPException
from starlette import status
from repositories.unit_of_work import UnitOfWork
from services.identity_service import IdentityService
from services.users_service import UsersService

uow = UnitOfWork()
users_service = UsersService(uow)
identity_service = IdentityService(uow)


async def get_current_user(request: Request):
    token = request.cookies.get('session_token')
    user = await identity_service.decode_token(token)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    return user
