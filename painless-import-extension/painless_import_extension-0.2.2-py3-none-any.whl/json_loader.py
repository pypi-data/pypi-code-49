from pathlib import Path
from sys import version_info
from pie import LoaderForBetterLife
import json
import pickle


class JsonLoader(LoaderForBetterLife[dict]):
    def load_program(self, b: bytes):
        return pickle.loads(b)

    def dump_program(self, prog) -> bytes:
        return pickle.dumps(prog)

    if version_info < (3, 6):
        encoding = 'utf-8'

        def source_to_prog(self, src: bytes, path: Path) -> dict:
            return json.loads(src.decode(self.encoding))
    else:

        def source_to_prog(self, src: bytes, path: Path) -> dict:
            return json.loads(src)

    def suffix(self) -> str:
        return '.json'
