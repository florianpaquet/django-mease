import redis
import pickle
from .settings import REDIS_HOST, REDIS_PORT, REDIS_CHANNELS

__all__ = ('publish',)

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)


def publish(channels_list=None, *args, **kwargs):
    """
    Publishes a message on channels
    """
    channels_list = channels_list or REDIS_CHANNELS
    p = pickle.dumps((args, kwargs))

    if not isinstance(channels_list, list):
        channels_list = [channels_list]

    for channel in channels_list:
        r.publish(channel, p)
