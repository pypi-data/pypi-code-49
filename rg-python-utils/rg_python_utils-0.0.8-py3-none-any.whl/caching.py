from django.core.cache import caches

from .rg_exceptions import RGUtilCacheException


class _Caching:

    @classmethod
    def get_string_from_cache(cls, _key, _default_value: str):
        return cls.__get_value_from_cache(_key, _default_value)

    @classmethod
    def put_string_in_cache(cls, _key, _value: str):
        cls.__put_value_in_cache(_key, _value)

    @classmethod
    def __get_cache(cls) -> caches:
        return caches["rg_plugin_util_cache"]

    @classmethod
    def __put_value_in_cache(cls, _key: str, _value: str):
        cache = cls.__get_cache()

        if cache:
            caches.set(_key, _value)
        else:
            error = "please define cache entry for rg plugins util cache, "
            "'rg_plugin_util_cache': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache','LOCATION': 'unique-snowflake' }"

            raise RGUtilCacheException(error)

    @classmethod
    def __get_value_from_cache(cls, _key, _default_value: str) -> str:
        cache = cls.__get_cache()

        if cache:
            return caches.get(_key, _default_value)
        else:
            error = "please define cache entry for rg plugins util cache, "
            "'rg_plugin_util_cache': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache','LOCATION': 'unique-snowflake' }"

            raise RGUtilCacheException(error)
