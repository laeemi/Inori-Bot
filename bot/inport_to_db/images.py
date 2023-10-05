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
    file = open("../../res/images/id")
    images_list = file.readlines()

    for img in images_list:
        values = await conn.execute('''
            INSERT INTO images_list (image_id) VALUES ($1)
            ''', img.strip("\n")
                                    )

        print(values)
    await conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
