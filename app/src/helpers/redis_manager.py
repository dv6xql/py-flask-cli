import json

from src.helpers.app_environment import (
    get_app_env
)
from config.redis import (
    REDIS_HOSTNAME,
    REDIS_KEY_EXPIRES_AFTER_HOUR
)


def get_redis_hostname() -> str:
    return REDIS_HOSTNAME


def get_redis_key(redis, key: str):
    if not redis.get(key):
        return None

    value = redis.get(key)

    try:
        json_results = json.loads(value)
        print(f"{len(json_results)} {key} found in Redis.")

        return json_results
    except Exception as e:
        print(e)

    return value


def set_redis_key(redis, key: str, value: str, expire: int = None):
    if not expire:
        expire = REDIS_KEY_EXPIRES_AFTER_HOUR

    redis.set(name=f"{key}", value=value, ex=expire)
