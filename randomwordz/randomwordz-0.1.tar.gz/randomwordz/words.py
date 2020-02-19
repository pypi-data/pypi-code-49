# https://stackoverflow.com/questions/6028000/how-to-read-a-static-file-from-inside-a-python-package

# see above how to read in words from the files...
try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

import data
from random import choice as randchoice
from random import shuffle

class WordGenerator:
    def __init__(self, debug=False):
        self.data = {}
        self.codes = [
            "ADJ", "ADP", "CONJ", "DET", "NOUN",
            "NUM", "PRON", "PRT", "VERB", "NAME"
        ]
        self.debug = debug

        self._load()

    def _load(self):
        for name in self.codes:
            self.data[name] = pkg_resources.read_text(
                data,
                f"{name}.txt"
            ).split('\n')

    def _debug_msg(self, code):
        if code not in self.data and self.debug:
            print(f"Code {code} is invalid, try one of these:")
            print(self.codes)

    def get_all(self, code):
        """Returns all of a certain word type"""
        code = code.upper()
        self._debug_msg(code)
        return list(self.data.get(code, []))

    def get_all_random(self, code):
        """Returns all of a certain word type, randomized"""
        code = code.upper()
        self._debug_msg(code)
        l = list(self.data.get(code, []))
        shuffle(l)
        return l

    def get_random(self, code):
        """Returns a random word from the specified code"""
        code = code.upper()
        self._debug_msg(code)
        try:
            return randchoice(self.data.get(code, []))
        except:
            return ""

