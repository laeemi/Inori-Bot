from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.core.postgres import get_session
from backend.music.models import Music

router = APIRouter()


@router.get("/music")
async def get_music(
    session: AsyncSession = Depends(get_session)
):
    return await Music.get_all(session)


@router.get("/send_m")
async def send_music(
        title: str,
        session: AsyncSession = Depends(get_session)
):
    return await Music.get_music_by_title(title, session)


@router.post("/upload_music")
async def upload_music(
    music_id: str, title: str, session: AsyncSession = Depends(get_session)
):
    return await Music.insert_music(music_id, title, session)
