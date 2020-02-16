from pathlib import Path
from pie import LoaderForBetterLife, T
import yaml
import pickle


class YamlLoader(LoaderForBetterLife[dict]):
    def load_program(self, b: bytes) -> T:
        return pickle.loads(b)

    def dump_program(self, prog: T) -> bytes:
        return pickle.dumps(prog)

    def source_to_prog(self, src: bytes, path: Path) -> dict:
        return yaml.load(src, yaml.SafeLoader)

    def suffix(self):
        return '.yml', '.yaml'
