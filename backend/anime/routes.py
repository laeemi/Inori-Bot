from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.anime.models import Anime
from backend.anime.schemas import AnimeSize, AnimeTitle
from backend.core.postgres import get_session

router = APIRouter()


@router.get("/anime", response_model=AnimeSize)
async def get_anime(
        session: AsyncSession = Depends(get_session)
):
    return {"size": await Anime.get_size_of_list(session)}


@router.get("/send_a", response_model=AnimeTitle)
async def send_anime(
        episode: int, session: AsyncSession = Depends(get_session)
):
    return await Anime.get_anime_id(episode, session)


@router.post("/upload_anime")
async def upload_anime(
        episode: str, anime_id: str, session: AsyncSession = Depends(get_session)
):
    return await Anime.insert_anime(episode, anime_id, session)
