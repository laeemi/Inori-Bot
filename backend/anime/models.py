from sqlalchemy import Column, String, select, Integer, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped

from backend.core.postgres.base import BaseModel


class Anime(BaseModel):
    __tablename__ = "anime_list"

    episode: Mapped[int] = Column(Integer, primary_key=True, nullable=False)
    anime_id: Mapped[str] = Column(String, nullable=False)

    @staticmethod
    async def get_size_of_list(session: AsyncSession) -> int:
        query = select(Anime.episode)
        return len((await session.execute(query)).all())

    @staticmethod
    async def get_anime_id(episode: int, session: AsyncSession) -> "Anime":
        query = select(Anime.anime_id).where(Anime.episode == episode)
        return (await session.execute(query)).scalars().first()

    @staticmethod
    async def insert_anime(episode: str, anime_id: str, session: AsyncSession) -> "Anime":
        query = insert(Anime).values(episode=int(episode), anime_id=anime_id).returning(Anime.anime_id)
        return (await session.execute(query)).scalars().first()
