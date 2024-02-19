from uuid import uuid4

from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from places_server.database.database import AbstractDatabase
from places_server.database.entities import Base
from places_server.database.entities import PlaceEntity
from places_server.database.entities import PlacelistEntity
from places_server.database.entities import UserEntity


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users_data = [
    {"name": "without_placelists", "mail": "m0", "username": "u0", "password": pwd_context.hash("p0")},
    {"name": "with_one_placelist", "mail": "m1", "username": "u1", "password": pwd_context.hash("p1")},
    {"name": "with_two_placelists", "mail": "m2", "username": "u2", "password": pwd_context.hash("p2")},
    {"name": "with_one_placelist_not_author", "mail": "m3", "username": "u3", "password": pwd_context.hash("p3")},
]


class FakeDatabase(AbstractDatabase):
    def __init__(self) -> None:
        self._engine = create_async_engine("sqlite+aiosqlite:///", echo=False, future=True)
        self.session_maker = async_sessionmaker(self._engine, expire_on_commit=False)
        self.users: list[UserEntity] = []
        self.places: list[PlaceEntity] = []
        self.placelists: list[PlacelistEntity] = []

    async def create_tables(self) -> None:
        async with self._engine.begin() as connection:
            await connection.run_sync(Base.metadata.drop_all)
            await connection.run_sync(Base.metadata.create_all)

        users: list[UserEntity] = []
        for user_data in users_data:
            users.append(
                UserEntity(
                    id=uuid4(),
                    name=user_data["name"],
                    mail=user_data["mail"],
                    username=user_data["username"],
                    password=user_data["password"],
                )
            )

        placelists_data = [
            {"name": "without_places", "author": users[1], "users": [users[1]]},
            {"name": "with_two_places", "author": users[2], "users": [users[1], users[2], users[3]]},
        ]
        placelists: list[PlacelistEntity] = []
        for placelist_data in placelists_data:
            placelists.append(
                PlacelistEntity(
                    id=uuid4(),
                    name=placelist_data["name"],
                    author=placelist_data["author"],
                    users=placelist_data["users"],
                )
            )

        places_data = [
            {"name": "Place1", "address": "a0", "latitude": 11.0, "longitude": 21.0, "placelists": [placelists[1]]},
            {"name": "Place2", "address": "a1", "latitude": 12.0, "longitude": 22.0, "placelists": [placelists[1]]},
        ]
        places: list[PlaceEntity] = []
        for place_data in places_data:
            places.append(
                PlaceEntity(
                    id=uuid4(),
                    name=place_data["name"],
                    address=place_data["address"],
                    latitude=place_data["latitude"],
                    longitude=place_data["longitude"],
                    placelists=place_data["placelists"],
                )
            )

        async with self.session_maker() as session:
            for user in users:
                session.add(user)

            for placelist in placelists:
                session.add(placelist)

            for place in places:
                session.add(place)

            await session.commit()

        self.users = users
        self.places = places
        self.placelists = placelists
