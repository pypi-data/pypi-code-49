import os
from typing import Optional, Sequence

from objcache import ObjectCache
from tests.utils import ObjectCacheForTesting, delete_object_cache_for_testing, ObjectClassForTesting, GENERATED_PATH


class TestObjectCache:
    cache: Optional[ObjectCache] = None
    test_cache_path: Sequence[str] = ('a', 'b')
    stored_result: ObjectClassForTesting = ObjectClassForTesting('abc')

    def setup_method(self):
        if not os.path.exists(GENERATED_PATH):
            os.makedirs(GENERATED_PATH)
        self.cache = ObjectCacheForTesting(self.test_cache_path)

    def teardown_method(self):
        self.cache = None
        delete_object_cache_for_testing()

    def test_store_and_get(self):
        self.cache.store(self.stored_result)
        self.cache = ObjectCacheForTesting(self.test_cache_path)  # reload cache
        gotten = self.cache.get()
        assert gotten == self.stored_result




