"""Import modules"""
import os
import sys
import logging
from pydantic_settings import SettingsConfigDict, BaseSettings
from aiogram import Bot, Dispatcher
from pydantic import SecretStr
from loguru import logger

class InterceptHandler(logging.Handler):
    """Intercept Handler for loguru and aiogram"""
    def emit(self, record):
        level = logger.level(record.levelname).name
        logger.log(level, record.getMessage())


class Settings(BaseSettings):
    """ Project settings """
    token: SecretStr

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')


LEVEL: str = "DEBUG"
SEPARATOR: str = ";"

logging.getLogger('aiogram').setLevel(LEVEL)
logging.getLogger('aiogram').addHandler(InterceptHandler())
logging.getLogger('asyncio').setLevel(LEVEL)
logging.getLogger('asyncio').addHandler(InterceptHandler())

logger.remove()
logger.add(os.path.join("logs", "log.log"),
           format="[{time:YYYY-MM-DD at HH:mm:ss}] [{level}]: {message}",
           level=LEVEL, retention="10 days")
logger.add(sys.stderr,
           format="<green>[{time:YYYY-MM-DD at HH:mm:ss}]</green> <cyan>[{level}]</cyan>: "
                  "<level>{message}</level>",
           level=LEVEL, colorize=True)

config = Settings() # type: ignore

bot = Bot(config.token.get_secret_value())
dp = Dispatcher()
