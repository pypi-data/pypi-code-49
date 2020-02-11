import os


if os.path.isfile('custom.py'):
    from custom import *  # noqa F403


def _():
    pass
