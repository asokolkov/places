from abc import ABC, abstractmethod
from datetime import datetime

from db.entities import User as UserEntity
from models.identity import IdentitySignin, IdentitySignup
from models.identity import IdentityUpdateMail
from models.identity import IdentityUpdateName
from models.identity import IdentityUpdatePassword
from models.identity import IdentityUpdateUsername
from models.user import UserIdentity
from utils.cryptography import AbstractCryptography
from utils.unit_of_work import AbstractUnitOfWork


class AbstractIdentityService(ABC):
    @abstractmethod
    async def signin(
        self, identity_signin: IdentitySignin
    ) -> (UserIdentity | None, str | None, datetime | None):
        raise NotImplementedError()

    @abstractmethod
    async def signup(
        self, identity_signup: IdentitySignup
    ) -> (UserIdentity | None, str | None, datetime | None):
        raise NotImplementedError()

    @abstractmethod
    async def update_mail(self, identity_update_mail: IdentityUpdateMail, user: UserIdentity) -> (UserIdentity | None, str | None, datetime | None):
        raise NotImplementedError()

    @abstractmethod
    async def update_username(self, identity_update_username: IdentityUpdateUsername, user: UserIdentity) -> (UserIdentity | None, str | None, datetime | None):
        raise NotImplementedError()

    @abstractmethod
    async def update_password(
            self, identity_update_password: IdentityUpdatePassword, user: UserIdentity
            ) -> (UserIdentity | None, str | None, datetime | None):
        raise NotImplementedError()

    @abstractmethod
    async def update_name(
            self, identity_update_name: IdentityUpdateName, user: UserIdentity
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
            result = await self._build_entity_with_token(entity)
            return result

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
            result = await self._build_entity_with_token(created_entity)
            await uow.commit()
            return result

    async def update_mail(self, identity_update_mail: IdentityUpdateMail, user: UserIdentity) -> (UserIdentity | None, str | None, datetime | None):
        async with self._uow as uow:
            entity = await uow.users.get(user.id)
            if entity is None:
                return None, None, None
            existing_entity = await uow.users.get_by_mail(identity_update_mail.new_mail)
            if existing_entity is not None:
                return None, None, None
            if not await self._cryptography.similar_hashes(identity_update_mail.password, entity.password):
                return None, None, None
            entity.mail = identity_update_mail.new_mail
            result = await self._build_entity_with_token(entity)
            await uow.commit()
            return result

    async def update_username(self, identity_update_username: IdentityUpdateUsername, user: UserIdentity) -> (UserIdentity | None, str | None, datetime | None):
        async with self._uow as uow:
            entity = await uow.users.get(user.id)
            if entity is None:
                return None, None, None
            existing_entity = await uow.users.get_by_username(identity_update_username.new_username)
            if existing_entity is not None:
                return None, None, None
            if not await self._cryptography.similar_hashes(
                    identity_update_username.password, entity.password
                    ):
                return None, None, None
            entity.username = identity_update_username.new_username
            result = await self._build_entity_with_token(entity)
            await uow.commit()
            return result

    async def update_password(
            self, identity_update_password: IdentityUpdatePassword, user: UserIdentity
            ) -> (UserIdentity | None, str | None, datetime | None):
        async with self._uow as uow:
            entity = await uow.users.get(user.id)
            if entity is None:
                return None, None, None
            if not await self._cryptography.similar_hashes(
                    identity_update_password.old_password, entity.password
            ):
                return None, None, None
            entity.password = await self._cryptography.hash(
                identity_update_password.new_password
            )
            result = await self._build_entity_with_token(entity)
            await uow.commit()
            return result

    async def update_name(
            self, identity_update_name: IdentityUpdateName, user: UserIdentity
    ) -> (UserIdentity | None, str | None, datetime | None):
        async with self._uow as uow:
            entity = await uow.users.get(user.id)
            if entity is None:
                return None, None, None
            entity.name = identity_update_name.new_name
            result = await self._build_entity_with_token(entity)
            await uow.commit()
            return result

    async def _build_entity_with_token(self, entity) -> (UserIdentity | None, str | None, datetime | None):
        result = UserIdentity.from_orm(entity)
        expiration_date = await self._cryptography.get_expiration_date()
        token = await self._cryptography.encode_token(result.dict(), expiration_date)
        return result, token, expiration_date
