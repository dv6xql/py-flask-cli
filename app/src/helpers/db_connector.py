from src.app import create_app
from src.extensions import db


def get_connector():
    app = create_app()
    db.app = app

    return db
