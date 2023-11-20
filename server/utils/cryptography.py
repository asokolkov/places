from abc import ABC, abstractmethod
from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from passlib.context import CryptContext

from configs import JWT_ALGORITHM, JWT_SECRET_KEY, JWT_TOKEN_EXPIRE_DAYS


class AbstractCryptography(ABC):
    @abstractmethod
    async def decode_token(self, token: str) -> dict[str, Any] | None:
        raise NotImplementedError()

    @abstractmethod
    async def encode_token(
        self, data: dict[str, Any], expiration_date: datetime
    ) -> str:
        raise NotImplementedError()

    @abstractmethod
    async def get_expiration_date(self) -> datetime:
        raise NotImplementedError()

    @abstractmethod
    async def similar_hashes(self, target: str, source: str) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def hash(self, value: str) -> str:
        raise NotImplementedError()


class Cryptography(AbstractCryptography):
    def __init__(self):
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def decode_token(self, token: str) -> dict[str, Any] | None:
        try:
            return jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        except Exception as _:
            return None

    async def encode_token(
        self, data: dict[str, Any], expiration_date: datetime
    ) -> dict[str, Any]:
        data["id"] = str(data["id"])
        token = {**data, "expiration_date": expiration_date.timestamp()}
        return jwt.encode(token, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    async def get_expiration_date(self) -> datetime:
        return datetime.now(timezone.utc) + timedelta(days=JWT_TOKEN_EXPIRE_DAYS)

    async def similar_hashes(self, target: str, source: str) -> bool:
        try:
            return self._pwd_context.verify(target, source)
        except (ValueError, TypeError):
            return False

    async def hash(self, value: str) -> str:
        return self._pwd_context.hash(value)
