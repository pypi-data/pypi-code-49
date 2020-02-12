from . import rg_utils


class RGException(Exception):

    def __init__(self, error: str, exception_type: str = None, json_data_received: dict = None, **kwargs):
        self.error = error
        self.extra_args = {"error": error, "exception_type": exception_type}
        self.json_data_received = json_data_received

        if kwargs:
            for key, value in kwargs.items():
                if key == 'kwargs':
                    continue
                self.extra_args[key] = value

    def get_dict(self) -> dict:
        if self.json_data_received:
            self.extra_args["json_data_received"] = self.json_data_received

        return rg_utils.Util.remove_null_and_empty_values_from_dict(self.extra_args)


class RGUtilCacheException(RGException):
    def __init__(self, error: str):
        RGException.__init__(self, error, exception_type='RGUtilCacheException')


class JSONDataNotInCorrectFormat(RGException):
    def __init__(self, error, json_data_received: dict = None):
        RGException.__init__(self, error, json_data_received=json_data_received, exception_type="JSONDataNotInCorrectFormat")


class SQLQueryException(RGException):
    def __init__(self, sql, json_error: str):
        msg = "Error in executing sql query, query: error_message: " + json_error + ", sql: " + str(sql)
        RGException.__init__(self, msg, exception_type='SQLQueryException')


class RGLZMAException(RGException):
    def __init__(self, error: str):
        RGException.__init__(self, error, exception_type='RGLZMAException')
