from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_ID: int
    OAUTH_TOKEN: str
    CATALOG_ID: str

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

bot = Bot(token=settings.BOT_TOKEN, parse_mode=ParseMode.HTML)
