from functools import wraps


def require_permission(perm_func):
    def decored(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not perm_func(*args, **kwargs):
                # TODO : Handle errors
                return
            func(*args, **kwargs)
        return wrapper
    return decored
