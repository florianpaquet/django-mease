from functools import wraps
from .exceptions import PermissionError


def require_permission(perm_func):
    def decored(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not perm_func(*args, **kwargs):
                raise PermissionError()
        return wrapper
    return decored
