"""Import modules"""
import asyncio
from pydantic_settings import SettingsConfigDict, BaseSettings
from aiogram import Bot, Dispatcher
from pydantic import SecretStr

class Settings(BaseSettings):
    """ Project settings """
    token: SecretStr

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

config = Settings() # type: ignore
loop = asyncio.get_event_loop()

bot = Bot(config.token.get_secret_value())
dp = Dispatcher(loop=loop)
