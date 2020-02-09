import gettext
import sys
import os


def handling(exctype, value, tb):
    print(value)


sys.excepthook = handling

lang_dir = os.path.dirname(os.path.realpath(__file__)) + "/locale"
lang = gettext.translation('base', localedir=lang_dir, languages=['en'])
lang.install()
_ = lang.gettext
