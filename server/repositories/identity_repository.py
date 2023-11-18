from abc import ABC
from abc import abstractmethod

from sqlmodel import select

from db.database import AbstractDatabase
from db.entities import User


class AbstractIdentityRepository(ABC):
    @abstractmethod
    async def get_by_mail(self, mail: str) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_mail_and_username(self, mail: str, username: str) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, entity: User) -> User:
        raise NotImplementedError()


class IdentityRepository(AbstractIdentityRepository):
    def __init__(self, db: AbstractDatabase) -> None:
        self._db = db

    async def get_by_mail(self, mail: str) -> User | None:
        async with self._db.get_session_maker()() as session:
            result = await session.scalars(select(User).where(User.mail == mail))
            return result.first()

    async def get_by_mail_and_username(self, mail: str, username: str) -> User | None:
        async with self._db.get_session_maker()() as session:
            result = await session.scalars(select(User).where(User.mail == mail).where(User.mail == username))
            return result.first()

    async def create(self, entity: User) -> User:
        async with self._db.get_session_maker()() as session:
            session.add(entity)
            await session.commit()
            result = await session.scalars(select(User).where(User.id == entity.id))
            return result.one()
