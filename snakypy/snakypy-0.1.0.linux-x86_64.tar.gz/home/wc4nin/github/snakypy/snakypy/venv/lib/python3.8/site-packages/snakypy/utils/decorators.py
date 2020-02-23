from functools import wraps
from snakypy.utils.exceptions import NotSupportWindows


def use_unix_system(func):
    """
    A decorator to force a function or method to run on Unix systems only.
    """
    from sys import platform

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Linux: startswith('linux')
        # OS X: startswith('darwin')
        # Windows: startswith('win')
        if platform.startswith('win'):
            msg = 'Invalid operating system "Windows". ' \
                  f'This function "{func.__name__}" is only compatible with ' \
                  'unix-based systems.'
            raise NotSupportWindows(msg)
        return func(*args, **kwargs)
    return wrapper


# DEPRECATED!
# def denying_win(*args, os='win'):
#     from sys import platform
#
#     # Linux: 'linux'
#     # OS X: 'darwin'
#     # Windows: 'win'
#
#     if args:
#         if (args != '') and platform.startswith(os):
#             raise Exception('>>> You cannot activate the color using Windows OS.')
#     else:
#         if platform.startswith(os):
#             msg = 'Invalid operating system (Windows). ' \
#                   f'This function "{__name__}" is compatible with ' \
#                   '"Linux" and "Mac OS X" systems only.'
#             raise Exception(msg)


__all__ = ['use_unix_system']
