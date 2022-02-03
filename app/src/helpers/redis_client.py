import redis

from src.helpers.redis_manager import (
    get_redis_hostname
)


def get_redis_client():
    return redis.Redis(host=get_redis_hostname(),
                       port=6379,
                       decode_responses=True)
