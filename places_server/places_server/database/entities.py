from uuid import UUID
from uuid import uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class UserSavedPlacelistLinkEntity(Base):
    __tablename__ = "user_saved_placelist_link"
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"), primary_key=True)
    placelist_id: Mapped[UUID] = mapped_column(ForeignKey("placelist.id"), primary_key=True)


class UserCreatedPlacelistLinkEntity(Base):
    __tablename__ = "user_created_placelist_link"
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"), primary_key=True)
    placelist_id: Mapped[UUID] = mapped_column(ForeignKey("placelist.id"), primary_key=True)


class PlacelistPlaceLinkEntity(Base):
    __tablename__ = "placelist_place_link"
    placelist_id: Mapped[UUID] = mapped_column(ForeignKey("placelist.id"), primary_key=True)
    place_id: Mapped[UUID] = mapped_column(ForeignKey("place.id"), primary_key=True)


class UserEntity(Base):
    __tablename__ = "user"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    mail: Mapped[str]
    username: Mapped[str]
    name: Mapped[str]
    password: Mapped[str]
    created_placelists: Mapped[list["PlacelistEntity"]] = relationship(
        "PlacelistEntity", secondary=UserCreatedPlacelistLinkEntity.__tablename__, back_populates="author"
    )
    saved_placelists: Mapped[list["PlacelistEntity"]] = relationship(
        "PlacelistEntity", secondary=UserSavedPlacelistLinkEntity.__tablename__, back_populates="users"
    )


class PlacelistEntity(Base):
    __tablename__ = "placelist"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str]
    author: Mapped["UserEntity"] = relationship(
        "UserEntity", secondary=UserCreatedPlacelistLinkEntity.__tablename__, back_populates="created_placelists"
    )
    users: Mapped[list["UserEntity"]] = relationship(
        "UserEntity", secondary=UserSavedPlacelistLinkEntity.__tablename__, back_populates="saved_placelists"
    )
    places: Mapped[list["PlaceEntity"]] = relationship(
        "PlaceEntity", secondary=PlacelistPlaceLinkEntity.__tablename__, back_populates="placelists"
    )


class PlaceEntity(Base):
    __tablename__ = "place"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str]
    address: Mapped[str]
    latitude: Mapped[float]
    longitude: Mapped[float]
    placelists: Mapped[list["PlacelistEntity"]] = relationship(
        "PlacelistEntity", secondary=PlacelistPlaceLinkEntity.__tablename__, back_populates="places"
    )
