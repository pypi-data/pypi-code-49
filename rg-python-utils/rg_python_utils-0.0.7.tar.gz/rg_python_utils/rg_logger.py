import logging

from .rg_redis.redis_cache import RedisCache


class RGLoggerCache:
    __cache_connection = None

    @classmethod
    def _get_cache(cls) -> RedisCache:
        if not cls.__cache_connection:
            cls.__cache_connection = RedisCache()

        return cls.__cache_connection

    @classmethod
    def _get_redis_key(cls):
        return "{}:".format("rg_logger_status")

    @classmethod
    def is_debug_enabled(cls) -> bool:
        redis_value = cls._get_cache().get_string_value(cls._get_redis_key())

        return True if redis_value == "true" else False

    @classmethod
    def set_debug_state(cls, is_enabled: bool):
        cls._get_cache().put_string_value(cls._get_redis_key(), "true" if is_enabled else "false")


logger = logging.getLogger('debug')


def info(msg):
    if RGLoggerCache.is_debug_enabled():
        logger.info(msg)


def exception(e, log_message: str = "", can_print_stacktrace: bool = False):
    logger.error(log_message + "%s, ExceptionMessage:%s", log_message, get_exception_msg(e), exc_info=can_print_stacktrace)


def get_exception_msg(e) -> str:
    return getattr(e, 'message', repr(e))
