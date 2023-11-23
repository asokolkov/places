from fastapi import HTTPException, Request
from starlette import status

from models.user import UserIdentity
from services.identity_service import IdentityService
from services.places_service import PlacesService
from services.users_service import UsersService
from utils.cryptography import Cryptography
from utils.unit_of_work import UnitOfWork


uow = UnitOfWork()
cryptography = Cryptography()
users_service = UsersService(uow)
identity_service = IdentityService(uow, cryptography)
places_service = PlacesService(uow)


async def get_current_user(request: Request):
    token = request.cookies.get("session_token")
    user = await cryptography.decode_token(token)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    return UserIdentity(**user)
