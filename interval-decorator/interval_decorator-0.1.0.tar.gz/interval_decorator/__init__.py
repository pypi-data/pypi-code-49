__version__ = "0.1.0"
import time


def interval(time_interval,):
    def decorator(function):
        function.__last_run = 0

        def guard(*args, **kwargs):
            now = time.time()
            if now - function.__last_run >= time_interval:
                function.__last_run = now
                return function(*args, **kwargs)

        return guard

    return decorator

