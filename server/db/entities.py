import enum
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel


class PlaceStatus(int, enum.Enum):
    NEVER_BEEN = 0
    SCHEDULED = 1
    VISITED = 2
    NOT_INTERESTED = 3


class UserPlacelistLink(SQLModel, table=True):
    user_id: UUID | None = Field(default=None, foreign_key="user.id", primary_key=True)
    placelist_id: UUID | None = Field(
        default=None, foreign_key="placelist.id", primary_key=True
    )


class User(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    mail: str
    username: str
    name: str
    password: str
    placelists: list["Placelist"] = Relationship(link_model=UserPlacelistLink)


class Placelist(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    name: str
    author_id: UUID
    users: list["User"] = Relationship(
        link_model=UserPlacelistLink, back_populates="placelists"
    )


# class PlaceEntity(Base):
#     __tablename__ = "places"
#     id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
#     name: Mapped[str] = mapped_column(String(255), nullable=False)
#     address: Mapped[str] = mapped_column(String(255), nullable=False)
#     latitude: Mapped[float] = mapped_column(Float, nullable=False)
#     longitude: Mapped[float] = mapped_column(Float, nullable=False)
#     # users: Mapped[list["UserEntity"]] = relationship(
#     #     secondary=UserPlaceAssociationEntity.__tablename__,
#     #     back_populates=__tablename__,
#     #     lazy="joined"
#     # )
#     # placelists: Mapped[list["PlacelistEntity"]] = relationship(
#     #     secondary=PlacePlacelistAssociationEntity.__tablename__,
#     #     back_populates=__tablename__,
#     #     lazy="joined"
#     # )
#

#
#
# class UserPlaceAssociationEntity(Base):
#     __tablename__ = 'user_place_association'
#     user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey(UserEntity.id), primary_key=True)
#     place_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey(PlaceEntity.id), primary_key=True)
#     status: Mapped[PlaceStatus] = mapped_column(Enum(PlaceStatus))
#
#
# class PlacePlacelistAssociationEntity(Base):
#     __tablename__ = 'place_placelist_association'
#     place_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey(PlaceEntity.id), primary_key=True)
#     placelist_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey(PlacelistEntity.id), primary_key=True)
