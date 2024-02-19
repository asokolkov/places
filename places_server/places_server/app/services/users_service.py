from abc import ABC
from abc import abstractmethod
from uuid import UUID

from places_server.app.models.user import User
from places_server.app.models.user import UserCompressed
from places_server.app.models.user import UserPlacelist
from places_server.app.models.user import UserPlacelists
from places_server.app.models.user import UserSignup
from places_server.app.models.user import UserToken
from places_server.app.models.user import UserUpdate
from places_server.app.models.user import UserWithToken
from places_server.app.utils.cryptography import AbstractCryptography
from places_server.database.database import AbstractDatabase
from places_server.database.entities import UserEntity
from places_server.database.repositories.placelists_repository import AbstractPlacelistsRepository
from places_server.database.repositories.places_repository import AbstractPlacesRepository
from places_server.database.repositories.users_repository import AbstractUsersRepository


class AbstractUsersService(ABC):
    @abstractmethod
    async def get(self, user_id: UUID) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_placelists(self, user_id: UUID) -> UserPlacelists:
        raise NotImplementedError()

    @abstractmethod
    async def signup(self, user_signup: UserSignup) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    async def signin(self, mail: str, password: str) -> UserToken | None:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, user_update: UserUpdate, user_id: UUID) -> UserWithToken | None:
        raise NotImplementedError()


class UsersService(AbstractUsersService):
    def __init__(
        self,
        database: AbstractDatabase,
        placelists_repository: AbstractPlacelistsRepository,
        users_repository: AbstractUsersRepository,
        places_repository: AbstractPlacesRepository,
        cryptography: AbstractCryptography,
    ) -> None:
        self._database = database
        self._placelists_repository = placelists_repository
        self._users_repository = users_repository
        self._places_repository = places_repository
        self._cryptography = cryptography

    async def get(self, user_id: UUID) -> User | None:
        async with self._database.session_maker() as session:
            user = await self._users_repository.get(session, user_id)
            if user is None:
                return None
            return User.model_validate(user, from_attributes=True)

    async def get_placelists(self, user_id: UUID) -> UserPlacelists:
        async with self._database.session_maker() as session:
            user = await self._users_repository.get(session, user_id)
            if user is None:
                return UserPlacelists(placelists=[])

            placelists = []
            for placelist in user.saved_placelists:
                author = UserCompressed.model_validate(placelist.author, from_attributes=True)
                placelist_dict = placelist.__dict__
                placelist_dict["author"] = author
                placelists.append(UserPlacelist.model_validate(placelist_dict, from_attributes=True))
            return UserPlacelists(placelists=placelists)

    async def signup(self, user_signup: UserSignup) -> User | None:
        async with self._database.session_maker() as session:
            user_by_mail = await self._users_repository.get_by_mail(session, user_signup.mail)
            if user_by_mail is not None:
                return None

            user_by_username = await self._users_repository.get_by_username(session, user_signup.username)
            if user_by_username is not None:
                return None

            user_signup.password = await self._cryptography.hash(user_signup.password)

            entity_to_create = UserEntity(**user_signup.dict())
            created_entity = await self._users_repository.create(session, entity_to_create)

            await session.commit()

            return User.model_validate(created_entity, from_attributes=True)

    async def signin(self, mail: str, password: str) -> UserToken | None:
        async with self._database.session_maker() as session:
            user = await self._users_repository.get_by_mail(session, mail)
            if user is None:
                return None

            hashes_similar = await self._cryptography.similar_hashes(password, user.password)
            if not hashes_similar:
                return None

            user_model = User.model_validate(user, from_attributes=True)
            token = UserToken(access_token=await self._cryptography.encode_token(user_model), token_type="bearer")

            return token

    async def update(self, user_update: UserUpdate, user_id: UUID) -> UserWithToken | None:
        async with self._database.session_maker() as session:
            user = await self._users_repository.get(session, user_id)
            if user is None:
                return None

            hashes_similar = await self._cryptography.similar_hashes(user_update.old_password, user.password)
            if not hashes_similar:
                return None

            existing_entity_by_mail = await self._users_repository.get_by_mail(session, user_update.mail)
            if existing_entity_by_mail is not None and existing_entity_by_mail.id != user.id:
                return None

            existing_entity_by_username = await self._users_repository.get_by_username(session, user_update.username)
            if existing_entity_by_username is not None and existing_entity_by_username.id != user.id:
                return None

            hashed_password = await self._cryptography.hash(user_update.password)

            user.mail = user_update.mail
            user.username = user_update.username
            user.name = user_update.name
            user.password = hashed_password

            await session.commit()

            user_model = User.model_validate(user, from_attributes=True)
            token = UserToken(access_token=await self._cryptography.encode_token(user_model), token_type="bearer")

            return UserWithToken(**user_model.dict(), token=token)
