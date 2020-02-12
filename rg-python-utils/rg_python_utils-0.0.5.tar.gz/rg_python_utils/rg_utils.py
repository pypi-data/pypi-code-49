import json
import time
import os
from numbers import Number
from datetime import datetime
from json import JSONEncoder

from django.db import connection

from . import rg_logger
from .rg_enum_base import Enum
from django.forms.models import model_to_dict


class RGJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        elif isinstance(obj, Enum):
            return obj.name
        elif isinstance(obj, datetime):
            return str(obj)
        else:
            return JSONEncoder.default(self, obj)


class Util:

    @classmethod
    def convert_model_to_dict(cls, _model) -> dict:
        if _model:
            return model_to_dict(_model)
        else:
            pass

    @classmethod
    def read_flag_from_django_config(cls, _key: str, _default_value):
        return os.getenv(_key, _default_value)

    @classmethod
    def read_request_header_field(cls, request, _key: str):
        if request and request.headers and _key in request.headers:
            return request.headers[_key]
        else:
            pass

    @staticmethod
    def to_json_string(_dict: dict) -> str:
        _dict = Util.remove_null_and_empty_values_from_dict(_dict)
        return json.dumps(_dict, cls=RGJsonEncoder)

    @staticmethod
    def from_json_string(_str: dict) -> dict:
        return json.loads(_str)

    @staticmethod
    def is_date_string_valid(date_string: str) -> bool:
        try:
            datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
            return True
        except ValueError as e:
            return False

    @classmethod
    def get_date_time_from_millis(cls, _millis: int):
        return datetime.fromtimestamp(_millis / 1000.0)

    @staticmethod
    def get_current_time_millis() -> int:
        return int(round(time.time() * 1000))

    @classmethod
    def get_current_time(cls) -> datetime:
        return datetime.utcnow()

    @classmethod
    def get_current_time_str(cls) -> str:
        return str(datetime.utcnow())

    @staticmethod
    def get_time_to_millis(datetime_obj: datetime) -> int:
        epoch_time = (datetime_obj - datetime(1970, 1, 1, tzinfo=datetime_obj.tzinfo)).total_seconds()
        return int(epoch_time * 1000)

    @staticmethod
    def get_str_time_to_millis(date_string: str) -> int:
        time_obj = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
        epoch_time = (time_obj - datetime(1970, 1, 1, tzinfo=time_obj.tzinfo)).total_seconds()
        return int(epoch_time * 1000)

    @staticmethod
    def get_week_number_of_current_year() -> int:
        return datetime.now().isocalendar()[1]

    @staticmethod
    def get_day_number_of_current_year() -> int:
        return datetime.now().timetuple().tm_yday

    @staticmethod
    def get_current_year() -> int:
        return datetime.now().timetuple().tm_yday

    @staticmethod
    def get_string_from_dict(value_dict: dict, key: str, default_value=None) -> str:
        try:
            if value_dict and key in value_dict:
                _value = value_dict[key]
                return str(_value) if _value else default_value
        except Exception as e:
            rg_logger.exception(e, log_message="rg_utils.get_string_from_dict()->>")
        return default_value

    @staticmethod
    def get_int_from_dict(value_dict: dict, key: str, default_value=0) -> int:
        try:
            if value_dict and key in value_dict and isinstance(value_dict[key], int):
                return int(default_value) if not value_dict[key] else int(value_dict[key])
        except Exception as e:
            rg_logger.exception(e, log_message="rg_utils.get_int_from_dict()->>")
        return int(default_value)

    @staticmethod
    def get_float_from_dict(value_dict: dict, key: str, default_value=0) -> float:
        try:
            if value_dict and key in value_dict and Util.is_instance_of_number(value_dict[key]):
                return float(default_value) if not value_dict[key] else float(value_dict[key])
        except Exception as e:
            rg_logger.exception(e, log_message="rg_utils.get_int_from_dict()->>")
        return float(default_value)

    @staticmethod
    def get_bool_from_dict(value_dict: dict, key: str) -> bool:
        try:
            if value_dict and key in value_dict:
                return bool(value_dict[key])
        except Exception as e:
            rg_logger.exception(e, log_message="rg_utils.get_bool_from_dict()->>")
        return False

    @staticmethod
    def get_list_from_dict(value_dict: dict, key: str) -> list:
        try:
            if value_dict and key in value_dict:
                return list(value_dict[key])
        except Exception as e:
            rg_logger.exception(e, log_message="rg_utils.get_list_from_dict()->>")
        return []

    @staticmethod
    def get_value_from_dict(value_dict: dict, key: str, default_value=None):
        try:
            if value_dict and key in value_dict:
                val = value_dict[key]
                return default_value if not val else val
        except Exception as e:
            rg_logger.exception(e, log_message="rg_utils.get_value_from_dict()->>")
        return default_value

    @staticmethod
    def compare_dictionary(first_dict: dict, second_dict: dict) -> bool:
        try:
            if not first_dict and not second_dict:
                return False

            if not second_dict or not first_dict:
                return True

            for key in first_dict:
                if key in second_dict:
                    if second_dict[key] != first_dict[key]:
                        return True
                else:
                    return True
        except Exception as e:
            pass

        return False

    @classmethod
    def is_dict_equal(cls, first_dict: dict, second_dict: dict, excluded_keys: dict = None) -> bool:
        if not first_dict or not second_dict:
            return False

        for _key, _value in first_dict.items():
            if excluded_keys and _key in excluded_keys:
                continue

            try:
                if _value != second_dict[_key]:
                    return False
            except Exception as e:
                pass

        return True

    @staticmethod
    def remove_null_and_empty_values_from_dict(_dict: dict) -> dict:
        if _dict:
            new_dict = {}
            for _key in _dict:
                if _dict[_key]:
                    new_dict[_key] = _dict[_key]

            return new_dict
        else:
            pass

    @staticmethod
    def remove_null_and_empty_values_within_dict(_dict: dict):
        keys_to_delete = []
        if _dict:
            for _key in _dict:
                if not _dict[_key]:
                    keys_to_delete.append(_key)

            if keys_to_delete:
                for _key in keys_to_delete:
                    del _dict[_key]
        else:
            pass

    @staticmethod
    def remove_null_and_empty_from_dict_list(_dict_list: list):
        if _dict_list:
            for _item in _dict_list:
                Util.remove_null_and_empty_values_from_dict(_item)
        else:
            pass

    @staticmethod
    def remove_keys_from_dict(_dict: dict, keys: list):
        for key in keys:
            Util.remove_key_from_dict(_dict, key)

    @staticmethod
    def remove_key_from_dict(_dict: dict, key):
        if _dict and key in _dict:
            del _dict[key]

    @staticmethod
    def subtract_dictionaries(_dict_1: dict, _dict_2: dict) -> dict:
        if _dict_1:
            if _dict_2:
                return {key: _dict_1[key] - _dict_2.get(key, 0) for key in _dict_1.keys()}
            else:
                pass
        else:
            pass

    @staticmethod
    def is_instance_of_number(obj):
        return [isinstance(obj, Number)]

    @staticmethod
    def is_table_exist_in_db(table_name: str) -> bool:

        try:
            return table_name in connection.introspection.table_names()
        except Exception as e:
            rg_logger.logger("PlayerData.create_table_if_not_exist->>Exception: " + getattr(e, 'message', repr(e)))
        return False
