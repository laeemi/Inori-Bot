from pydantic import BaseModel


class AnimeSize(BaseModel):
    size: int

    class Config:
        from_attributes = True


class AnimeTitle(BaseModel):
    file_id: str

    class Config:
        from_attributes = True