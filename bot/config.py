from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    token: str
    base_url: str
    admin_id: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings(extra="ignore")
