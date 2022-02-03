import logging
import logging.config

from flask import Flask
from celery import Celery
from dotenv import load_dotenv

from config.logging import get_logging_config
from src.extensions import db

from config.celery import (
    CELERY_BROKER_URL,
    result_backend,
    accept_content,
    task_serializer,
    result_serializer,
    redis_max_connections,
    CELERYBEAT_SCHEDULE
)


CELERY_TASK_LIST = [
    'src.tasks',
]


def create_celery_app(app=None):
    """
    Create a new Celery object and tie together the Celery config to the app's
    config. Wrap all tasks in the context of the application.

    :param app: Flask app
    :return: Celery app
    """
    app = app or create_app()

    celery = Celery(
        app.import_name,
        broker=CELERY_BROKER_URL,
        include=CELERY_TASK_LIST
    )

    celery.conf.update({
        "CELERY_BROKER_URL": CELERY_BROKER_URL,
        "result_backend": result_backend,
        "accept_content": accept_content,
        "task_serializer": task_serializer,
        "result_serializer": result_serializer,
        "redis_max_connections": redis_max_connections,
        "beat_schedule": CELERYBEAT_SCHEDULE
    })
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    load_dotenv(".env", verbose=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    # Override settings
    if settings_override:
        app.config.update(settings_override)

    # Configure logging
    logging.getLogger()
    logging.config.dictConfig(get_logging_config())

    extensions(app)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    db.init_app(app)

    return None
