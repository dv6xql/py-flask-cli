import os
from pathlib import Path

from dotenv import load_dotenv

from src.helpers.app_environment import (
    get_dotenv_path,
    get_app_env
)


load_dotenv(dotenv_path=get_dotenv_path())

# Flask App
APP_ENV = get_app_env()
DEBUG = os.getenv('APP_DEBUG')
LOG_LEVEL = os.getenv('LOG_LEVEL')

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://" \
                          f"{os.getenv('DB_USER')}:" \
                          f"{os.getenv('DB_PASSWORD')}@" \
                          f"{os.getenv('DB_HOST')}:" \
                          f"{os.getenv('DB_PORT')}/" \
                          # f"{os.getenv('DB_NAME')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Other variables
DOTENV_PATH = str(Path('.') / '.env')
LOGS_DIR = str(Path('.') / 'logs')
LOGS_FILENAME = "logs.json"
Path(LOGS_DIR).mkdir(parents=True, exist_ok=True)
