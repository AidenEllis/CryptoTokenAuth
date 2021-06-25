from functools import wraps
from time import time


def processTime(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Process Time: {end_ if end_ > 0 else 0} ms")

    return _time_it
