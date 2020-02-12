from ..rg_exceptions import RGException


class RedisSettingsNotFoundException(RGException):
    def __init__(self, redis_settings_name: str):
        msg = 'Redis Settings not declared in settings.py file, please add settings for: ' + redis_settings_name
        RGException.__init__(self, msg, exception_type='RedisSettingsNotFoundException')


class RedisConnectionNotInitialize(RGException):
    def __init__(self, redis_settings_name: str):
        msg = 'Redis Connection  not initialized/ready for rg_redis instance: ' + redis_settings_name
        RGException.__init__(self, msg, exception_type='RedisConnectionNotReadyException')
