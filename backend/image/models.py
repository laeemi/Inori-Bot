import random
from typing import Sequence

from sqlalchemy import Column, String, select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped

from backend.core.postgres.base import BaseModel


class Image(BaseModel):
    __tablename__ = "images_list"

    image_id: Mapped[str] = Column(String, primary_key=True, nullable=False)

    @staticmethod
    async def get_random_image(session: AsyncSession) -> "Image":
        query = select(Image.image_id)
        result = (await session.execute(query)).scalars().all()
        return random.choice(result)

    @staticmethod
    async def insert_image(image_id: str, session: AsyncSession) -> "Image":
        query = insert(Image).values(image_id=image_id).returning(Image.image_id)
        return (await session.execute(query)).scalars().first()
