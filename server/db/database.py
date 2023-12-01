import asyncio

from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio.engine import AsyncEngine


ENGINE = AsyncEngine(
    create_engine(
        "postgresql+asyncpg://postgres:postgres@localhost/test", echo=True, future=True
    )
)
SESSION_MAKER = sessionmaker(ENGINE, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    async with ENGINE.begin() as connection:
        await connection.run_sync(SQLModel.metadata.drop_all)
        await connection.run_sync(SQLModel.metadata.create_all)


# asyncio.run(init_db())
