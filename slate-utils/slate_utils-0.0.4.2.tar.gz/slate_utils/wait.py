from functools import wraps

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def wait_progress(function):
    """
    Decorator function that will wait for the progress indicator to disappear
    before and after the function is called.
    """

    @wraps(function)
    def decorator(d, *args, **kwargs):
        wait = WebDriverWait(d, 60)
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "progress_box")))
        function(d, *args, **kwargs)
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "progress_box")))

    return decorator


def wait_method(timeout=3):
    """
    Decorator for methods that will wait for the progress indicator to disappear
    before and after the function is called.
    """

    def decorator(function):
        @wraps(function)
        def wrapper(instance, *args, **kwargs):
            wait = WebDriverWait(instance.d, timeout)
            wait.until(EC.invisibility_of_element((By.CLASS_NAME, "progress_box")))
            r = function(instance, *args, **kwargs)
            wait.until(EC.invisibility_of_element((By.CLASS_NAME, "progress_box")))
            return r

        return wrapper

    return decorator
