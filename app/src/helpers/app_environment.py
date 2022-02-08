import os
from pathlib import Path

from dotenv import load_dotenv


def get_app_env() -> str:
    return os.getenv('APP_ENV')


def is_production() -> bool:
    return get_app_env() == "production"


def is_testing() -> bool:
    return get_app_env() == "testing"


def get_dotenv_path() -> Path:
    return Path('.') / '.env'


load_dotenv(dotenv_path=get_dotenv_path())
