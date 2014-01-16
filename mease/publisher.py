import redis
from .settings import REDIS_HOST, REDIS_PORT

__all__ = ('publish',)

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)


def publish(channel, message):
    """
    Publishes a message on a channel
    """
    r.publish(channel, message)
