from typing import Sequence, Any, Tuple

from sqlalchemy import Column, String, select, insert, Row, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped

from core.postgres.base import BaseModel


class Music(BaseModel):
    __tablename__ = "music"

    file_id: Mapped[str] = Column(String, primary_key=True, nullable=False)
    title: Mapped[str] = Column(String, nullable=False)

    @staticmethod
    async def get_all(session: AsyncSession) -> Sequence:
        query = select(Music.title)
        return (await session.execute(query)).scalars().all()

    @staticmethod
    async def get_music_by_title(title: str, session: AsyncSession) -> Row:
        query = select(Music.file_id).where(Music.title == title)
        return (await session.execute(query)).first()

    @staticmethod
    async def insert_music(file_id: str, title: str, session: AsyncSession) -> "Music":
        query = insert(Music).values(file_id=file_id, title=title).returning(Music)
        return (await session.execute(query)).scalars().first()
