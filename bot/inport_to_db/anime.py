import asyncpg
import asyncio

from backend.config import settings
from bot.config import settings


async def run():
    conn = await asyncpg.connect(
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        database=settings.POSTGRES_DATABASE,
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT
    )
    file = open("../../res/anime/id")
    anime_list = file.readlines()

    for anime in anime_list:
        temp = anime.split(" ", 1)
        values = await conn.execute('''
            INSERT INTO anime_list (episode, anime_id) VALUES ($1, $2)
            ''', int(temp[0]), temp[1].strip("\n")
                                    )
        print(values)
    await conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
