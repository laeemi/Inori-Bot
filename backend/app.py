from fastapi import FastAPI
from config import settings
from music.routes import router as music_router
from anime.routes import router as anime_router
from image.routes import router as image_router


app = FastAPI(
    title=settings.app_name,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    redoc_url=None,
)

app.include_router(music_router)
app.include_router(anime_router)
app.include_router(image_router)


@app.get("/start")
async def start():
    return


@app.get("/menu")
async def menu():
    return


@app.get("/name")
async def menu():
    return


@app.get("/age")
async def age():
    return


@app.get("/about")
async def about():
    return

