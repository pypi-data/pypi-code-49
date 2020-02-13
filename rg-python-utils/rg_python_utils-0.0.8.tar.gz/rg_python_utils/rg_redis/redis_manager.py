import redis
from django.conf import settings
from .. import rg_logger

from . import exceptions


class RedisManager:
    __connection_cache = {}

    def __init__(self, redis_setting_key: str):
        if self.__connection_cache and redis_setting_key in self.__connection_cache and self.__connection_cache[redis_setting_key]:
            raise Exception("RedisManager->>Already exist rg_redis key in  db, key: " + redis_setting_key)
        else:
            redis_settings = self.__get_redis_settings(redis_setting_key)
            redis_connection = self.__init_redis_connection_with_settings(redis_settings, redis_setting_key)
            self.__connection_cache[redis_setting_key] = redis_connection

    @staticmethod
    def __init_redis_connection_with_settings(redis_settings: dict, redis_setting_key: str):
        try:
            if not redis_settings and ("HOST" not in redis_settings or "PORT" not in redis_settings not in "DB" in redis_settings and "PASSWORD" not in redis_settings):
                raise exceptions.RedisSettingsNotFoundException(redis_setting_key)

            return redis.Redis(host=redis_settings["HOST"], port=redis_settings["PORT"], db=redis_settings["DB"], password=redis_settings["PASSWORD"], decode_responses=True)
        except Exception as e:
            rg_logger.exception(e, "RedisLeaderboard.__init_redis_connection_with_host()->>")

        return None

    @staticmethod
    def get_redis_connection(redis_setting_key: str):
        connection = None

        if RedisManager.__connection_cache and redis_setting_key in RedisManager.__connection_cache:
            connection = RedisManager.__connection_cache[redis_setting_key]

        if not connection:
            RedisManager(redis_setting_key)

        if not connection and RedisManager.__connection_cache and redis_setting_key in RedisManager.__connection_cache:
            connection = RedisManager.__connection_cache[redis_setting_key]

        return connection

    @staticmethod
    def set_value_to_redis_set(redis_key: str, value, redis_setting_key: str) -> bool:
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                return redis_connection.set(redis_key, value) == 1
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.update_value()->>")
                raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(redis_key)

    @staticmethod
    def get_value_from_redis_set(redis_key: str, redis_setting_key: str) -> str:
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                return redis_connection.get(redis_key)
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.update_value()->>")
                raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(redis_key)

    @staticmethod
    def update_value_to_sorted_set(_key: str, key: str, value, redis_setting_key: str) -> bool:
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                return redis_connection.zadd(_key, {key: value}) == 1
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.update_value_to_sorted_set()->>")
                raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(_key)

    @staticmethod
    def get_value_from_sorted_set(_key: str, _value, redis_setting_key: str) -> float:
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                return redis_connection.zscore(_key, _value)
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.get_value_from_sorted_set()->>")
                raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(redis_setting_key)

    @staticmethod
    def get_rank_from_sorted_set(redis_key: str, _id: str, redis_setting_key: str, rev_rank: bool = True) -> int:
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                if rev_rank:
                    rank = redis_connection.zrevrank(redis_key, _id)
                else:
                    rank = redis_connection.zrank(redis_key, _id)

                if isinstance(rank, int) and rank >= 0:
                    return rank + 1
                else:
                    pass

            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.get_rank_from_sorted_set()->>")
                raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(redis_key)

    @staticmethod
    def get_value_from_sorted_set_with_range(_key: str, min_range: int, max_range: int, descending: bool, redis_setting_key: str) -> [tuple]:
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                return redis_connection.zrange(_key, min_range, max_range, withscores=True, desc=descending)
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.get_value_from_sorted_set_with_range()->>")
                raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(_key)

    @staticmethod
    def delete_key_from_redis(_key: str, redis_setting_key: str):
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                redis_connection.delete(_key)
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.delete_key_from_redis()->>")
                raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(_key)

    @staticmethod
    def get_value_for_key(redis_key: str, key: str, redis_setting_key: str):
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                redis_connection.get(key)
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.get_value_for_key()->>")
                raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(redis_key)

    @staticmethod
    def get_all_value_of_hset(_key: str, redis_setting_key: str):
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                return redis_connection.hgetall(_key)
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.get_all_value_of_hset()->>")
                # raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(_key)

        return None

    # @staticmethod
    # def get_value_from_hset_for_key(_key: str, key: str, redis_setting_key: str):
    #     redis_connection = RedisManager.get_redis_connection(redis_setting_key)
    #
    #     if redis_connection:
    #         try:
    #             return redis_connection.get(_key, key)
    #         except Exception as e:
    #             rg_logger.exception(e, "RedisLeaderboard.get_value_from_hset_for_key()->>")
    #             # raise e
    #     else:
    #         raise exceptions.RedisConnectionNotInitialize(_key)
    #
    #     return None

    @staticmethod
    def delete_key_from_hset(hash_key: str, redis_key: str, redis_setting_key: str):
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                redis_connection.hdel(redis_key, hash_key)
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.delete_key_from_hset()->>")
                # raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(hash_key)

    @staticmethod
    def delete_all_value_from_hset(_key: str, redis_setting_key: str):
        RedisManager.delete_key_from_redis(_key, redis_setting_key)

    @staticmethod
    def set_value_to_redis_hash_set(redis_key: str, _key, _value, redis_setting_key: str):
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                redis_connection.hset(redis_key, _key, _value)
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.delete_key_from_hset()->>")
                # raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(redis_key)

    @staticmethod
    def get_value_from_redis_hash_set(redis_key: str, _key, redis_setting_key: str):
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                return redis_connection.hget(redis_key, _key)
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.delete_key_from_hset()->>")
                # raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(redis_key)

    @staticmethod
    def get_values_from_hash_set_for_multiple_key(hash_key: str, _keys_list: [], redis_setting_key: str):
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                if _keys_list:
                    return redis_connection.hmget(hash_key, _keys_list)
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.delete_key_from_hset()->>")
                # raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(redis_setting_key)

    @staticmethod
    def get_total_value_count_from_sorted_set(redis_key: str, redis_setting_key: str) -> int:
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                max_score = redis_connection.zrevrange(redis_key, 0, 0)
                if max_score:
                    max_score = max_score[0]
                    return redis_connection.zcount(redis_key, 0, max_score)

                return 0
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.delete_key_from_hset()->>")
                # raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(redis_setting_key)

    @staticmethod
    def get_multiple_values(_keys_list: [], redis_setting_key: str):
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                if _keys_list:
                    return redis_connection.mget(_keys_list)

                    # pipe = redis_connection.pipeline()
                    # for _key in _keys_list:
                    #     pipe.hgetall(_key)
                    #
                    # return pipe.execute()
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.delete_key_from_hset()->>")
                # raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(redis_setting_key)

    @staticmethod
    def set_multiple_values_to_hash(hash_key: str, _values_dict: dict, redis_setting_key: str):
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                redis_connection.hmset(hash_key, _values_dict)
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.delete_key_from_hset()->>")
                # raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(redis_setting_key)

    @staticmethod
    def set_multiple_values(_values_dict: dict, redis_setting_key: str):
        redis_connection = RedisManager.get_redis_connection(redis_setting_key)

        if redis_connection:
            try:
                if _values_dict:
                    redis_connection.mset(_values_dict)
            except Exception as e:
                rg_logger.exception(e, "RedisLeaderboard.delete_key_from_hset()->>")
                # raise e
        else:
            raise exceptions.RedisConnectionNotInitialize(redis_setting_key)

    @staticmethod
    def __get_redis_settings(redis_setting_key: str) -> dict:
        redis_settings_dict = getattr(settings, "REDIS_SETTINGS", None)

        if redis_settings_dict and redis_setting_key in redis_settings_dict:
            return redis_settings_dict[redis_setting_key]
        else:
            raise exceptions.RedisSettingsNotFoundException(redis_setting_key)
