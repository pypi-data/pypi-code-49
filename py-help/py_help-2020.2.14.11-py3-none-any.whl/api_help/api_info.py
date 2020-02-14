# -*- coding: utf-8 -*-
import re
import json
from .validator import validator
from .schema_generator import schema_generator
from ..lib.CommonLogger import debug, info, warn, error


class ApiInfo:
    """
    用于生成需要的对接数据结构
    """

    def __init__(self, cfg_dict):
        self.cfg = cfg_dict
        self.generate_validator()

    def __getitem__(self, item):
        return self.cfg.get(item)

    def __setitem__(self, key, value):
        return self.cfg.__setitem__(key, value)

    @property
    def is_empty_api(self):
        return len(self.cfg) == 0

    def get(self, item, default=None):
        return self.cfg.get(item, default)

    def is_cli(self):
        if self.cfg.get('is_cli'):
            return True
        else:
            return False

    def call_api(self, *args, **kwargs):
        api_func = self.cfg.get('api')
        if self.cfg.get('validator'):
            valid_args = validator.validate(self.cfg.get('validator'), kwargs)
        else:
            valid_args = kwargs
        debug("api 调用: url=> [{}],api:{}".format(self.cfg.get('url'), api_func))
        return api_func(*args, **valid_args)

    def generate_validator(self):
        if self.cfg.get('params'):
            api_validator = schema_generator.generate_schema(self.cfg.get('params'))
            debug("获得的 api {} validator => {} ".format(self.cfg.get('url'), api_validator))
            self.cfg['validator'] = api_validator

    @property
    def uniq_url(self):
        method = self.cfg.get('method')
        url = self.cfg.get('url')
        if method is None:
            return url
        else:
            return "{}/{}".format(url, method)
