import os

from config.celerybeat import (
    get_celerybeat_schedule
)
from src.helpers.redis_manager import (
    get_redis_hostname
)


CELERY_BROKER_URL = \
    f"redis://:@{get_redis_hostname()}:6379/0"
result_backend = \
    f"redis://:@{get_redis_hostname()}:6379/0"
accept_content = ['json']
task_serializer = 'json'
result_serializer = 'json'
redis_max_connections = 10
CELERYBEAT_SCHEDULE = get_celerybeat_schedule(
    os.getenv("CELERYBEAT_SCHEDULE")
)
