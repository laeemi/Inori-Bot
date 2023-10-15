from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message


from aiohttp import ClientSession

from config import settings
from filters.admin_filter import AdminFilter

router = Router()
base_url = settings.base_url
router.message.filter(AdminFilter())


class UploadAnimeSeries(StatesGroup):
    choosing_series = State()
    sending_video = State()


@router.message(Command("upload_music"))
async def upload_music(message: Message):
    async with ClientSession(base_url) as session:
        async with session.post("/upload_music") as resp:
            await message.answer(f"Загрузка прошла успешно! - [{await resp.text()}]")


@router.message(Command("upload_img"))
async def upload_img(message: Message):
    async with ClientSession(base_url) as session:
        params = {"image_id": message.photo[0].file_id}
        async with session.post("/upload_img", params=params) as resp:
            await message.answer(f"Загрузка прошла успешно! - [{await resp.text()}]")


@router.message(Command("upload_anime"))
async def upload_anime(message: Message, state: FSMContext):
    await message.answer(f"Напишите номер серии:")
    await state.set_state(UploadAnimeSeries.choosing_series)


@router.message(
    UploadAnimeSeries.choosing_series
)
async def series_chosen(message: Message, state: FSMContext):
    try:
        if int(message.text) > 0:
            await state.update_data(chosen_series=message.text)
            await message.answer(
                text="Отправьте файл для загрузки"
            )
            await state.set_state(UploadAnimeSeries.sending_video)
        else:
            await message.answer(
                text="Неверныый номер серии"
            )
    except:
        await message.answer(
            text="Неверное значение серии"
        )


@router.message(
    UploadAnimeSeries.sending_video,
    F.video
)
async def video_sent(message: Message, state: FSMContext):
    async with ClientSession(base_url) as session:
        params = {
            "episode": state.get_data(),
            "anime_id": message.video.file_id
                  }
        async with session.post("/anime_upload", params=params) as resp:
            await message.answer(f"Загрузка прошла успешно! - [{await resp.text()}]")
            await state.clear()
