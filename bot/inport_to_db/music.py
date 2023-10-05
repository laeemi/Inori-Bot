import asyncpg
import asyncio

from backend.config import settings


async def run():
    conn = await asyncpg.connect(
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        database=settings.POSTGRES_DATABASE,
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT
    )
    file = open("../../res/music/id")
    music_list = file.readlines()

    for music in music_list:
        temp = music.split(" ", 1)
        values = await conn.execute('''
            INSERT INTO music_list (music_id, title) VALUES ($1, $2)
            ''', temp[0], temp[1].strip("\n")
                                    )
        print(values)
    await conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
