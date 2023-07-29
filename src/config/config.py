from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_ID: int

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
