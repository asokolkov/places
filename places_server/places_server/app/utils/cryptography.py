from abc import ABC
from abc import abstractmethod
from datetime import datetime
from datetime import timedelta
from datetime import timezone

import jwt
from passlib.context import CryptContext

from places_server.configs import settings
from places_server.app.models.user import User
from places_server.app.models.user import UserDecodedToken


class AbstractCryptography(ABC):
    @abstractmethod
    async def decode_token(self, token: str) -> UserDecodedToken | None:
        raise NotImplementedError()

    @abstractmethod
    async def encode_token(self, user: User) -> str:
        raise NotImplementedError()

    @abstractmethod
    async def similar_hashes(self, target: str, source: str) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def hash(self, value: str) -> str:
        raise NotImplementedError()


class Cryptography(AbstractCryptography):
    def __init__(self) -> None:
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def decode_token(self, token: str) -> UserDecodedToken | None:
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            return UserDecodedToken.model_validate(decoded_token, from_attributes=True)
        except Exception as _:
            return None

    async def encode_token(self, user: User) -> str:
        dict_user = user.dict()
        dict_user["id"] = str(dict_user["id"])
        expiration_date = datetime.now(timezone.utc) + timedelta(days=settings.JWT_TOKEN_EXPIRE_DAYS)
        dict_user["expiration_date"] = expiration_date.timestamp()
        return jwt.encode(dict_user, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    async def similar_hashes(self, target: str, source: str) -> bool:
        try:
            hashes_similar: bool = self._pwd_context.verify(target, source)
            return hashes_similar
        except (ValueError, TypeError):
            return False

    async def hash(self, value: str) -> str:
        result: str = self._pwd_context.hash(value)
        return result
