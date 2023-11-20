from abc import ABC, abstractmethod
from datetime import datetime

from db.entities import User as UserEntity
from models.identity import IdentitySignin, IdentitySignup
from models.user import UserIdentity
from utils.cryptography import AbstractCryptography
from utils.unit_of_work import AbstractUnitOfWork


class AbstractIdentityService(ABC):
    @abstractmethod
    async def signin(
        self, identity: IdentitySignin
    ) -> (UserIdentity | None, str | None, datetime | None):
        raise NotImplementedError()

    @abstractmethod
    async def signup(
        self, identity: IdentitySignup
    ) -> (UserIdentity | None, str | None, datetime | None):
        raise NotImplementedError()


class IdentityService(AbstractIdentityService):
    def __init__(self, uow: AbstractUnitOfWork, cryptography: AbstractCryptography):
        self._uow = uow
        self._cryptography = cryptography

    async def signin(
        self, identity_signin: IdentitySignin
    ) -> (UserIdentity | None, str | None, datetime | None):
        async with self._uow as uow:
            entity = await uow.users.get_by_mail(identity_signin.mail)
            if entity is None:
                return None, None, None
            if not await self._cryptography.similar_hashes(
                identity_signin.password, entity.password
            ):
                return None, None, None
            return await self._build_entity_with_token(entity)

    async def signup(
        self, identity_signup: IdentitySignup
    ) -> (UserIdentity | None, str | None, datetime | None):
        async with self._uow as uow:
            entity = await uow.users.get_by_mail_and_username(
                identity_signup.mail, identity_signup.username
            )
            if entity is not None:
                return None, None, None
            entity_to_create = UserEntity.from_orm(identity_signup)
            entity_to_create.password = await self._cryptography.hash(
                entity_to_create.password
            )
            created_entity = await uow.users.create(entity_to_create)
            await uow.commit()
            return await self._build_entity_with_token(created_entity)

    async def _build_entity_with_token(self, entity):
        result = UserIdentity.from_orm(entity)
        expiration_date = await self._cryptography.get_expiration_date()
        token = await self._cryptography.encode_token(entity.dict(), expiration_date)
        return result, token, expiration_date
