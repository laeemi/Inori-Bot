from typing import Sequence

from sqlalchemy import Column, String, select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped

from backend.core.postgres.base import BaseModel


class Music(BaseModel):
    __tablename__ = "music_list"

    music_id: Mapped[str] = Column(String, primary_key=True, nullable=False)
    title: Mapped[str] = Column(String, nullable=False)

    @staticmethod
    async def get_all(session: AsyncSession) -> Sequence:
        query = select(Music.title)
        return (await session.execute(query)).scalars().all()

    @staticmethod
    async def get_music_by_title(title: str, session: AsyncSession) -> "Music":
        query = select(Music.music_id).where(Music.title == title)
        return (await session.execute(query)).scalars().first()

    @staticmethod
    async def insert_music(music_id: str, title: str, session: AsyncSession) -> "Music":
        query = insert(Music).values(music_id=music_id, title=title).returning(Music.music_id)
        return (await session.execute(query)).scalars().first()
