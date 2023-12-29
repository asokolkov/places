from datetime import datetime
from datetime import timezone

from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from app.models.user import User
from app.services.placelists_service import PlacelistsService
from app.services.places_service import PlacesService
from app.services.users_service import UsersService
from app.utils.cryptography import Cryptography
from database.database import Database
from database.repositories.placelists_repository import PlacelistsRepository
from database.repositories.places_repository import PlacesRepository
from database.repositories.users_repository import UsersRepository

database = Database()
cryptography = Cryptography()

users_repository = UsersRepository()
places_repository = PlacesRepository()
placelists_repository = PlacelistsRepository()

users_service = UsersService(database, placelists_repository, users_repository, places_repository, cryptography)
places_service = PlacesService(database, placelists_repository, users_repository, places_repository)
placelists_service = PlacelistsService(database, placelists_repository, users_repository, places_repository)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/signin")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    user = await cryptography.decode_token(token)
    if user is None or user.expiration_date < datetime.now(timezone.utc).timestamp():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return User.model_validate(user, from_attributes=True)
