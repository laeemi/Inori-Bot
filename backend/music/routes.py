from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.postgres import get_session
from music.models import Music
from music.schemas import MusicFull

router = APIRouter()


@router.get("/music", response_model=list[str])
async def get_music(
        session: AsyncSession = Depends(get_session)
):
    return await Music.get_all(session)


@router.get("/send_m", response_model=MusicFull)
async def send_music(
        title: str,
        session: AsyncSession = Depends(get_session)
):
    return await Music.get_music_by_title(title, session)


@router.post("/upload_music", status_code=status.HTTP_201_CREATED, response_model=MusicFull)
async def upload_music(
        file_id: str, title: str, session: AsyncSession = Depends(get_session)
):
    return await Music.insert_music(file_id, title, session)
