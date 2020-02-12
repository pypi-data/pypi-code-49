import redis
from django.conf import settings

from .exceptions import RedisSettingsNotFoundException, RedisConnectionNotInitialize
from .. import rg_logger


class RedisCache:
    __connection = None

    def __init__(self, redis_settings_key: str = "CACHING_REDIS_SETTINGS"):
        self.redis_settings_key = redis_settings_key

    def __get_connection(self):
        if not self.__connection:
            redis_settings = self.__get_redis_settings(self.redis_settings_key)
            redis_connection = self.__init_redis_connection_with_settings(redis_settings, self.redis_settings_key)
            self.__connection = redis_connection
        else:
            pass

        # rg_logger.info("settingKey: " + self.redis_settings_key)
        return self.__connection

    @classmethod
    def __init_redis_connection_with_settings(cls, redis_settings: dict, redis_setting_key: str):
        try:
            if not redis_settings and ("HOST" not in redis_settings or "PORT" not in redis_settings not in "DB" in redis_settings and "PASSWORD" not in redis_settings):
                raise RedisSettingsNotFoundException(redis_setting_key)

            connection = redis.Redis(host=redis_settings["HOST"], port=redis_settings["PORT"], db=redis_settings["DB"], password=redis_settings["PASSWORD"], decode_responses=True)

            if connection:
                rg_logger.info("Host:{}, Port:{}, DB:{}, SettingKey: {}".format(redis_settings["HOST"], redis_settings["PORT"], redis_settings["DB"], redis_setting_key))

            return connection
        except Exception as e:
            rg_logger.exception(e, "RedisCache.__init_redis_connection_with_host()->>")

        return None

    @staticmethod
    def __get_redis_settings(redis_setting_key: str) -> dict:
        redis_settings_dict = getattr(settings, "REDIS_SETTINGS", None)

        if redis_settings_dict and redis_setting_key in redis_settings_dict:
            return redis_settings_dict[redis_setting_key]
        else:
            raise RedisSettingsNotFoundException(redis_setting_key)

    def put_value_in_hash_set(self, redis_key: str, _hash_key: str, _hash_value: str):
        redis_connection = self.__get_connection()

        if redis_connection:
            try:
                redis_connection.hset(redis_key, _hash_key, str(_hash_value))
            except Exception as e:
                rg_logger.exception(e, "RedisCache.put_value_in_hash_set()->>")
                # raise e
        else:
            raise RedisConnectionNotInitialize(redis_key)

    def get_value_from_hash_set(self, redis_key: str, _key):
        redis_connection = self.__get_connection()

        if redis_connection:
            try:
                return redis_connection.hget(redis_key, _key)
            except Exception as e:
                rg_logger.exception(e, "RedisCache.get_value_from_hash_set()->>")
                # raise e
        else:
            raise RedisConnectionNotInitialize(redis_key)

    def get_all_values_from_hash_set(self, _redis_key: str):
        redis_connection = self.__get_connection()

        if redis_connection:
            try:
                return redis_connection.hgetall(_redis_key)
            except Exception as e:
                rg_logger.exception(e, "RedisCache.get_all_values_from_hash_set()->>")
                # raise e
        else:
            raise RedisConnectionNotInitialize(_redis_key)

    def remove_value_from_hash_set(self, _redis_key: str, _hash_key: str):
        redis_connection = self.__get_connection()

        if redis_connection:
            try:
                return redis_connection.hdel(_redis_key, _hash_key)
            except Exception as e:
                rg_logger.exception(e, "RedisCache.remove_value_from_hash_set()->>")
                # raise e
        else:
            raise RedisConnectionNotInitialize(_redis_key)

    def delete_key_from_cache(self, _redis_key: str):
        redis_connection = self.__get_connection()

        if redis_connection:
            try:
                return redis_connection.delete(_redis_key)
            except Exception as e:
                rg_logger.exception(e, "RedisCache.delete_key_from_cache()->>")
                # raise e
        else:
            raise RedisConnectionNotInitialize(_redis_key)

    def put_string_value(self, _redis_key: str, _value: str):
        redis_connection = self.__get_connection()

        if redis_connection:
            try:
                return redis_connection.set(_redis_key, _value)
            except Exception as e:
                rg_logger.exception(e, "RedisCache.put_string_value()->>")
                # raise e
        else:
            raise RedisConnectionNotInitialize(_redis_key)

    def get_string_value(self, _redis_key):
        redis_connection = self.__get_connection()

        if redis_connection:
            try:
                return redis_connection.get(_redis_key)
            except Exception as e:
                rg_logger.exception(e, "RedisCache.get_string_value()->>")
                # raise e
        else:
            raise RedisConnectionNotInitialize(_redis_key)

    def incr_value(self, _redis_key):
        redis_connection = self.__get_connection()

        if redis_connection:
            try:
                return redis_connection.incr(_redis_key)
            except Exception as e:
                rg_logger.exception(e, "RedisCache.get_string_value()->>")
                # raise e
        else:
            raise RedisConnectionNotInitialize(_redis_key)
