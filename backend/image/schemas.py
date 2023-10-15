from pydantic import BaseModel


class ImageId(BaseModel):
    file_id: str

    class Config:
        from_attributes = True
