from typing import Optional, List, Dict

from pydantic import BaseModel


class MusicFull(BaseModel):
    file_id: str

    class Config:
        from_attributes = True


class MusicTitles(BaseModel):
    titles: List[str]

    class Config:
        from_attributes = True


class MusicCreate(BaseModel):
    file_id: str
    title: str
