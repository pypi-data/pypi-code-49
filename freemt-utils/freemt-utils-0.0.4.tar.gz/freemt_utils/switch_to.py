'''
switch_to path contextmanager (with)
http://ralsina.me/weblog/posts/BB963.html
'''
import os
import pathlib
from contextlib import contextmanager
from loguru import logger


@contextmanager
def switch_to(path=pathlib.Path().home()):
    '''
    switch to path

    with switch_to(path):
        pass  # do stuff
    '''
    old_dir = os.getcwd()

    try:
        path = pathlib.Path(path)
    except Exception as exc:
        logger.error(exc)
        raise

    if not path.is_dir():  # pragma: no cover
        msg = '*{}* is not a directory or does not exist.'
        raise Exception(msg.format(path))

    os.chdir(path)
    yield
    os.chdir(old_dir)
