from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from backend.image.models import Image
from backend.core.postgres import get_session
from backend.image.schemas import ImageId

router = APIRouter()


@router.get("/img", response_model=ImageId)
async def send_random_image(
        session: AsyncSession = Depends(get_session)
):
    return await Image.get_random_image(session)


@router.post("/upload_img")
async def upload_image(
        file_id: str, session: AsyncSession = Depends(get_session)
):
    return await Image.insert_image(file_id, session)
