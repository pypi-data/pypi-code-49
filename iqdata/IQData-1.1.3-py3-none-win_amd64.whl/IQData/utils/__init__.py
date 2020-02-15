import os

import pandas as pd
import six

import IQData
from IQCommon.utils import read_config, ObjectDict

BASE_PATH = IQData.__path__[0]
SERVICE_PATH = os.path.join(BASE_PATH, 'services')

SERVICE_PREFIX = 'IQData.services.'

BASE_CONFIG = os.path.join(BASE_PATH, 'utils', 'default_config.yml')

DEFAULT_SETTINGS = settings = ObjectDict(read_config(BASE_CONFIG))


class BaseObject(object):
    _repr_attr_list = []

    def __repr__(self):
        return "<{class_name} {property}>".format(
            class_name=self.__class__.__name__,
            property={attr: getattr(self, attr, None)
                      for attr in self._repr_attr_list}
        )


def dict_to_dataframe(data):
    df = {}

    if len(data):

        for item in data[0].keys():
            df[item] = []
        for item in data:
            for k, v in item.items():
                df[k].append(v)

    return pd.DataFrame(df)


def update_settings(config):
    if isinstance(config, six.string_types):
        config = read_config(config)
    if isinstance(config, dict):
        config = ObjectDict(config)
    if isinstance(config, ObjectDict):
        settings.update(config)


def get_user_id():
    os.environ.get('JPY_USER')
