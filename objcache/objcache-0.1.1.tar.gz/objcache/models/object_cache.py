from typing import Any, Sequence
import transaction
import ZODB, ZODB.FileStorage
from objcache.logic.seed import seed_db_if_needed
from objcache.logic.subpath import get_result_subpath
from BTrees.OOBTree import OOBTree


class ObjectCache:
    """
    Store Python objects on the filesystem and load them later. Built on top of ZoDB but provides
    an easier to use interface.

    :Examples:

        >>> from objcache import ObjectCache
        >>> cache = ObjectCache('cache.zodb', ('a', 'b'))
        >>> cache.store(5)
        >>> # Later session
        >>> cache = ObjectCache('cache.zodb', ('a', 'b'))
        >>> result = cache.get()
        >>> print(result)
        5
    """
    _root = None
    _db = None

    def __init__(self, db_path: str, cache_path: Sequence[str]):
        self.cache_path = cache_path
        self.db_path = db_path
        self._validate()

    @property
    def db(self):
        if self._db is None:
            self._storage = ZODB.FileStorage.FileStorage(self.db_path)
            self._db = ZODB.DB(self._storage)
            seed_db_if_needed(self._db)
        return self._db

    @property
    def db_root(self):
        if self._root is None:
            self._open_transaction()
        return self._root

    def store(self, result: Any) -> None:
        """
        Store Python object on the filesystem
        """
        try:
            result_subpath = get_result_subpath(self.db_root, self.cache_path, create_oobtree=True)
            result_subpath[self.cache_path[-1]] = result
        except Exception as e:
            raise e
        finally:
            self._close_transaction()

    def get(self) -> Any:
        """
        Get Python object from the filesystem
        """
        try:
            result_subpath = get_result_subpath(self.db_root, self.cache_path)
            result = result_subpath[self.cache_path[-1]]
            if isinstance(result, OOBTree):
                # DB won't remain in a session to use collection, so don't return it
                raise CantLoadCollectionException(f'{self.cache_path} is a collection, not an item. '
                                                  f'Provide an item path')
            return result
        except Exception as e:
            raise e
        finally:
            self._close_transaction()

    def delete(self) -> None:
        """
        Delete previously stored Python object from the filesystem
        """
        try:
            result_subpath = get_result_subpath(self.db_root, self.cache_path)
            del result_subpath[self.cache_path[-1]]
        except Exception as e:
            raise e
        finally:
            self._close_transaction()

    def exists(self) -> bool:
        """
        Check whether there is already a Python object stored on the filesystem for this cache path
        """
        try:
            result = self.get()
        except KeyError:
            return False
        return True

    def _close_transaction(self):
        transaction.commit()
        self.db.close()
        self._conn = None
        self._root = None
        self._db = None

    def _open_transaction(self):
        self._conn = self.db.open()
        self._root = self._conn.root.main

    def _validate(self):
        if len(self.cache_path) == 0:
            raise ValueError(f'must pass non empty items in cache path, got {self.cache_path}')


class CantLoadCollectionException(Exception):
    pass