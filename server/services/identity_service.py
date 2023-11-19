from abc import ABC
from abc import abstractmethod
from datetime import datetime
from datetime import timedelta
from datetime import timezone

import jwt
from passlib.context import CryptContext
from pydantic import parse_obj_as

from configs import JWT_ALGORITHM
from configs import JWT_SECRET_KEY
from configs import JWT_TOKEN_EXPIRE_DAYS
from db.entities import User as UserEntity
from models.identity import IdentitySignin, IdentitySignup
from models.user import UserIdentity
from repositories.identity_repository import AbstractIdentityRepository


class AbstractIdentityService(ABC):
    @abstractmethod
    async def signin(self, identity: IdentitySignin) -> (UserIdentity | None, str | None):
        raise NotImplementedError()

    @abstractmethod
    async def signup(self, identity: IdentitySignup) -> (UserIdentity | None, str | None):
        raise NotImplementedError()

    @abstractmethod
    async def decode_token(self, token: str) -> UserIdentity:
        raise NotImplementedError()


class IdentityService(AbstractIdentityService):
    def __init__(self, repository: AbstractIdentityRepository) -> None:
        self._repository = repository
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def signin(self, identity_signin: IdentitySignin) -> (UserIdentity | None, str | None):
        existing_entity = await self._repository.get_by_mail(identity_signin.mail)
        if existing_entity is None:
            return None, None
        if not await self._password_verified(identity_signin.password, existing_entity.password):
            return None, None
        user_identity = UserIdentity.from_orm(existing_entity)
        token = await self._create_token(user_identity)
        return UserIdentity.from_orm(existing_entity), token

    async def signup(self, identity_signup: IdentitySignup) -> (UserIdentity | None, str | None):
        existing_entity = await self._repository.get_by_mail_and_username(identity_signup.mail, identity_signup.username)
        if existing_entity is not None:
            return None, None
        entity = parse_obj_as(UserEntity, identity_signup)
        entity.password = self._pwd_context.hash(entity.password)
        result = await self._repository.create(entity)
        user_identity = UserIdentity.from_orm(result)
        token = await self._create_token(user_identity)
        return user_identity, token

    async def decode_token(self, token: str) -> UserIdentity:
        decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return UserIdentity(**decoded_token)

    async def _create_token(self, user_identifier: UserIdentity) -> str:
        expiration_date = datetime.now(timezone.utc) + timedelta(days=JWT_TOKEN_EXPIRE_DAYS)
        user_dictionary = user_identifier.dict()
        user_dictionary['id'] = str(user_dictionary['id'])
        token = {'expiration_date': expiration_date.timestamp(), **user_dictionary}
        return jwt.encode(token, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    async def _password_verified(self, password: str, hashed_password: str) -> bool:
        try:
            return self._pwd_context.verify(password, hashed_password)
        except (ValueError, TypeError):
            return False
