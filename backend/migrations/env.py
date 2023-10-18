import asyncio
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import create_async_engine

from alembic import context

from config import settings
from core.postgres import Base
from anime.models import Anime
from music.models import Music
from image.models import Image

config = context.config

target_metadata = Base.metadata


def run_sync_migrations(connection: Connection):
    context.configure(
        connection=connection, target_metadata=target_metadata, compare_type=True
    )
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations(engine):
    async with engine.connect() as connection:
        await connection.run_sync(run_sync_migrations)
    await engine.dispose()


def run_migrations_online() -> None:
    engine = create_async_engine(
        settings.DATABASE_URL.unicode_string(), echo=True, future=True
    )

    asyncio.run(run_migrations(engine))


run_migrations_online()
