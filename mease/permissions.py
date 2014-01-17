from functools import wraps
from .exceptions import PermissionError


def require_permission(perm_func):
    def decored(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not perm_func(*args, **kwargs):
                # TODO : Handle errors
                print("Not allowed")
                return
            func(*args, **kwargs)
        return wrapper
    return decored
