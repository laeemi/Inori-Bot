import random
from typing import Sequence

from sqlalchemy import Column, String, select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped

from core.postgres.base import BaseModel


class Image(BaseModel):
    __tablename__ = "image"

    file_id: Mapped[str] = Column(String, primary_key=True, nullable=False)

    @staticmethod
    async def get_random_image(session: AsyncSession) -> "Image":
        query = select(Image.file_id)
        result = (await session.execute(query)).all()
        return random.choice(result)

    @staticmethod
    async def insert_image(file_id: str, session: AsyncSession) -> "Image":
        query = insert(Image).values(file_id=file_id).returning(Image.file_id)
        return (await session.execute(query)).scalars().first()
