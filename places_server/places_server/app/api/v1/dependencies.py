from datetime import datetime
from datetime import timezone

from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from places_server.app.models.user import User
from places_server.app.services.placelists_service import PlacelistsService
from places_server.app.services.places_service import PlacesService
from places_server.app.services.users_service import UsersService
from places_server.app.utils.cryptography import Cryptography
from places_server.database.database import Database
from places_server.database.repositories.placelists_repository import PlacelistsRepository
from places_server.database.repositories.places_repository import PlacesRepository
from places_server.database.repositories.users_repository import UsersRepository


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
