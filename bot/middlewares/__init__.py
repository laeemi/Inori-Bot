import logging
from datetime import datetime, timedelta
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, CallbackQuery, Update, Video


class LogMiddleware(BaseMiddleware):
    @staticmethod
    def message_bot_log(message: Message, update: Update) -> None:
        log = (f'-------------------------------------------------------------------------------\n'
               f'Пользователь: {message.from_user.full_name}\n'
               f'Написал: {message.text}\n'
               f'Chat_ID(ID): {message.chat.id}\n'
               f'Ссылка: {message.from_user.username}\n'
               f'Время: {datetime.utcnow() + timedelta(hours=3)}\n'
               f'Время сообщения: {message.date + timedelta(hours=3)}\n'
               f'Update id={update.update_id}\n'
               )

        if message.video is not None:
            log += f'\nПользователь прислал видео {message.video.file_id}\n'
        if message.photo is not None:
            log += f'\nПользователь прислал фото:'
            for photo in message.photo:
                log += photo.file_id + " | "

        log += "-------------------------------------------------------------------------------\n"
        logging.info(log)

    @staticmethod
    def callback_bot_log(callback: CallbackQuery, update: Update) -> None:
        logging.info(f'-------------------------------------------------------------------------------\n'
                     f'Пользователь: {callback.from_user.full_name}\n'
                     f'Отправил callback: {callback.data}\n'
                     f'Chat_ID(ID): {callback.from_user.id}\n'
                     f'Ссылка: {callback.from_user.username}\n'
                     f'Время: {datetime.utcnow() + timedelta(hours=3)}\n'
                     f'Update id={update.update_id}'
                     f'-------------------------------------------------------------------------------\n'
                     )

    @staticmethod
    def event_bot_log(update: Update) -> None:
        logging.info(f'-------------------------------------------------------------------------------\n'
                     f'Пользователь: {update.from_user.full_name}\n'
                     f'Отправил нераспознанный апдейт!!\n'
                     f'Chat_ID(ID): {update.from_user.id}\n'
                     f'Ссылка: {update.from_user.username}\n'
                     f'Время: {datetime.utcnow() + timedelta(hours=3)}\n'
                     f'Update id={update.update_id}'
                     f'-------------------------------------------------------------------------------\n'
                     )

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if isinstance(event, Update):
            if event.message is not None:
                self.message_bot_log(event.message, event)
            elif event.callback_query is not None:
                self.callback_bot_log(event.callback_query, event)
            else:
                self.event_bot_log(event)

        res = await handler(event, data)
        return res
