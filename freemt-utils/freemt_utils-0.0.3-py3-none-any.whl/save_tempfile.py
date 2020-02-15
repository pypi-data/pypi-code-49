# coding: utf-8
"""
save to tempfile.NamedTemporaryFile
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as f:
        # url = 'file://' + f.name
        f.write(html)
    webbrowser.open('file://' + f.name)

https://stackoverflow.com/questions/21437386/launch-html-code-in-browser-that-is-generated-by-beautifulsoup-straight-from-p

savetofile(text, filename='out.txt', encoding='utf-8', start=False)

Open file in firefox if set

based on savetofile
"""
import os
import pathlib
from pathlib import Path
import tempfile
import subprocess
import platform
import cchardet

# from nose.tools import (eq_, with_setup)

from loguru import logger as LOGGER


# def savetofile(text, filename='out.html', encoding='utf-8', start=False):
# def save_tempfile(text, filename=None, encoding='ascii', start=True):
def save_tempfile(text, filename=None, encoding='utf-8', start=True):  # pylint: disable=too-many-branches, too-many-return-statements
    """
    Save text (str) to file (default to tmp.txt) or filepath (Path(str))
    """
    if filename is None:
        filename = tempfile.NamedTemporaryFile('w', delete=False, suffix='.html').name

    if text is None:
        LOGGER.warning(f'Input is None, exiting...')
        return ''

    if isinstance(text, bytes):
        _ = cchardet.detect(text)
        enc = _['encoding']
        if enc is None:
            enc = 'UTF-8'

        text = text.decode(enc)

    if not isinstance(text, str):
        try:
            text = str(text)
        except Exception:
            LOGGER.warning(" Not a str, cant convert to a str, exiting")
            return ''

    if isinstance(filename, pathlib.Path):
        fpath = filename.absolute()
    else:
        try:
            fpath = Path(filename).absolute()
        except Exception as exc:
            LOGGER.error(" fpath = Path(filename).absolute() Exception: %s, exiting" % exc)
            return ''

    if encoding.lower() in ['utf8', 'utf-8']:
        encoding = 'utf-8'

    #  if encoding == 'ascii': ncr xmlcharrefreplace
    if encoding not in ['utf-8']:
        text = text.encode(encoding, errors='xmlcharrefreplace').decode(encoding)

    with open(str(fpath), 'w', encoding=encoding) as fhandle:
        fhandle.write(text)
        # LOGGER.info("\n\tSaved to %s (encoding: %s)", str(fpath), encoding)
        LOGGER.info("\n\tSaved to %s" % str(fpath))

    if start:
        # modi

        # 'start' only valid in Windows
        platform_ = platform.system()
        if not platform_ == 'Windows':
            LOGGER.info('Platform is %s, exiting...' % platform_)
            return fpath.__str__()

        try:
            os.startfile(str(fpath))
            return fpath.__str__()
        except Exception as exc:
            LOGGER.debug('startfile didnt work ...: %s' % exc)
            LOGGER.info("Trying firefox in C:...")

        proc = subprocess.Popen([r"C:\Program Files\Mozilla Firefox\firefox.exe", str(fpath)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        LOGGER.info("Opening file in Firefox...")
        err, out = proc.communicate()
        if err:
            LOGGER.error("Start file in firefox errors: %s, out: %s", err, out)

        return fpath.__str__()

    return str(fpath)


_ = '''
def my_setup(level=logging.DEBUG):
    """my_setup."""

    fmt = '%(name)s-%(filename)s[ln:%(lineno)d]:'
    fmt += '%(levelname)s: %(message)s'
    logging.basicConfig(format=fmt, level=level)


@with_setup(my_setup)
def test_():
    """test_+++."""

    out = 1
    eq_(1, out)
'''


def main():
    """main"""


if __name__ == "__main__":
    main()
