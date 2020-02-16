from abc import ABC, abstractmethod
from typing import Type, Generic, TypeVar, Tuple, Union
from pathlib import Path
from importlib.util import cache_from_source
from importlib.util import MAGIC_NUMBER
import hmac
import hashlib
__all__ = ['Header', 'DefaultHeader', 'LoaderForBetterLife']

T = TypeVar('T')


def source_hash(x):
    return hmac.new(MAGIC_NUMBER, x, hashlib.md5).digest()


class CacheValueError(ValueError):
    pass


class Header(ABC):
    """The header of code object representing the module to load
    This can be used for verifying the compiled code, or querying if
    the compiled code is out of date and needs re-compilation.
    Besides, one can also keep extra information in the header
    for applying other cache system, etc.
    """
    @abstractmethod
    def is_out_of_date(self, src_code: bytes) -> bool:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_source(cls, src_code: bytes) -> 'Header':
        """
        Produce the header from source code of "{self.name}.{self.suffix()}".
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_cache(cls, compiled_cache: bytes) -> 'Header':
        """
        Produce the header from cache contents of file
            `cache_from_source("{self.name}.{self.suffix()}")`.
        """
        raise NotImplementedError

    @abstractmethod
    def remove_header(self, prog_bytes: bytes) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def add_header(self, prog_bytes: bytes) -> bytes:
        raise NotImplementedError

    @classmethod
    def get_header_and_prog_bytes(cls, compiled_cache: bytes):
        header = cls.from_cache(compiled_cache)
        prog_bytes = header.remove_header(compiled_cache)
        return header, prog_bytes

    default = None  # type: Header


class DefaultHeader(Header):
    def is_out_of_date(self, src_code: bytes) -> bool:
        return self.hash != source_hash(src_code)

    def __init__(self, hash: bytes):
        self.hash = hash

    @classmethod
    def from_cache(cls, compiled_cache: bytes) -> Header:
        i = compiled_cache.find(b'\n')
        if i == -1:
            raise CacheValueError
        n = int(compiled_cache[:i])
        hash = compiled_cache[i + 1:i + 1 + n]
        header = cls(hash)
        return header

    @classmethod
    def from_source(cls, src_code: bytes) -> Header:
        hash = source_hash(src_code)
        return cls(hash)

    @classmethod
    def remove_header(cls, compiled_cache: bytes) -> bytes:
        i = compiled_cache.find(b'\n')
        if i == -1:
            raise CacheValueError
        n = int(compiled_cache[:i])
        b = compiled_cache[i + 1 + n:]
        return b

    def add_header(self, prog_bytes: bytes) -> bytes:
        b = bytearray()
        b.extend(str(len(self.hash)).encode())
        b.extend(b'\n')
        b.extend(self.hash)
        b.extend(prog_bytes)
        return bytes(b)


class LoaderForBetterLife(Generic[T]):
    def __init__(self, filename, qualified_name):
        self.file = Path(filename)
        self.qualified_name = qualified_name

    @abstractmethod
    def suffix(self) -> Union[str, Tuple[str, ...]]:
        """
        The suffix of extension file to load.
        e.g., ".json", ".pyd"
        As you see it should start with a dot.
        """
        raise NotImplementedError

    @abstractmethod
    def dump_program(self, prog: T) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def load_program(self, b: bytes) -> T:
        raise NotImplementedError

    @abstractmethod
    def source_to_prog(self, src: bytes, path: Path) -> T:
        raise NotImplementedError

    def load_header_and_prog(self) -> Tuple[Header, T]:
        suffix = self.suffix()
        searched = []
        suffixes = suffix if isinstance(suffix, tuple) else (suffix, )
        for suffix in suffixes:
            src_file = self.file.with_suffix(suffix)
            cache_file_path = cache_from_source(str(src_file.absolute()))
            cache_file = Path(cache_file_path).with_suffix('.pie.pyc')
            cache_file.parent.mkdir(exist_ok=True, parents=True)
            cache = None
            if cache_file.exists():
                with cache_file.open('rb') as f:
                    cache_bytes = f.read()
                    header, prog_bytes = self.header_cls(
                    ).get_header_and_prog_bytes(cache_bytes)
                    program = self.load_program(prog_bytes)
                    cache = header, program

            if src_file.exists():
                with src_file.open('rb') as f:
                    src = f.read()

                need_recompile = True
                if cache:
                    # verify cache
                    header, program = cache

                    if not header.is_out_of_date(src):
                        need_recompile = False

                if need_recompile:
                    header = self.header_cls().from_source(src)
                    program = self.source_to_prog(src, src_file)
                    with cache_file.open('wb') as f:
                        contents = self.dump_program(program)
                        contents = header.add_header(contents)
                        f.write(contents)

            else:
                searched.append(str(src_file.absolute()))
                continue

            # noinspection PyUnboundLocalVariable
            return header, program

        raise FileNotFoundError('any of\n- {}'.format('\n- '.join(searched)))

    def load(self):
        return self.load_header_and_prog()[1]

    def header_cls(_) -> Type[Header]:
        return DefaultHeader
