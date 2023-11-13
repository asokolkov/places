import enum

from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class PlaceStatus(int, enum.Enum):
    NEVER_BEEN = 0
    SCHEDULED = 1
    VISITED = 2
    NOT_INTERESTED = 3


class Base(DeclarativeBase):
    pass


class UserPlacelistAssociationTable(Base):
    __tablename__ = 'user_placelist_association'
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True)
    placelist_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('placelists.id'), primary_key=True)


class UserPlaceAssociationTable(Base):
    __tablename__ = 'user_place_association'
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True)
    place_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('places.id'), primary_key=True)
    status: Mapped[PlaceStatus] = mapped_column(Enum(PlaceStatus))


class PlacePlacelistAssociationTable(Base):
    __tablename__ = 'place_placelist_association'
    place_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('places.id'), primary_key=True)
    placelist_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('placelists.id'), primary_key=True)


class UserTable(Base):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    public_id: Mapped[str] = mapped_column(String(8), unique=True)
    mail: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))
    placelists: Mapped[list["PlacelistTable"]] = relationship(
        secondary=UserPlacelistAssociationTable.__tablename__, back_populates="users", lazy="joined"
    )
    places: Mapped[list["PlaceTable"]] = relationship(
        secondary=UserPlaceAssociationTable.__tablename__, back_populates="users", lazy="joined"
    )


class PlacelistTable(Base):
    __tablename__ = "placelists"
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    public_id: Mapped[str] = mapped_column(String(8), unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    author_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), unique=True)
    users: Mapped[list["UserTable"]] = relationship(
        secondary=UserPlacelistAssociationTable.__tablename__, back_populates="placelists", lazy="joined"
    )
    places: Mapped[list["PlaceTable"]] = relationship(
        secondary=PlacePlacelistAssociationTable.__tablename__, back_populates="placelists", lazy="joined"
    )


class PlaceTable(Base):
    __tablename__ = "places"
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    public_id: Mapped[str] = mapped_column(String(8), unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    users: Mapped[list["UserTable"]] = relationship(
        secondary=UserPlaceAssociationTable.__tablename__, back_populates="places", lazy="joined"
    )
    placelists: Mapped[list["PlacelistTable"]] = relationship(
        secondary=PlacePlacelistAssociationTable.__tablename__, back_populates="places",
        lazy="joined"
    )
