import json
import threading
import os
from flask import Flask, jsonify

from .config import LibConfig
from .registration import Registration
from .filter.restful_filter import RestfulFilter
from .filter import Filter
from .response import ResponseBody
name = "Libras"


class ResponseAdvice(object):

    @staticmethod
    def before_write(rv):
        return ResponseBody(data=rv).__dict__


class Libras(Flask):
    config_class = LibConfig

    response_filters = []

    response_advice = ResponseAdvice

    def property(self, key: str):
        return self.config.property(key)

    def make_response(self, rv, types: iter = (dict, list, set)):
        status = 200
        for response_filter in self.response_filters:
            rv, status = response_filter.do_filter(rv, status)
        if status and status == 400:
            return super(Libras, self).handle_exception(Exception(rv))
        if isinstance(rv, types):
            rv = jsonify(self.response_advice.before_write(rv))
        return super(Libras, self).make_response(rv)

    def register_filter(self, response_filter: Filter):
        self.response_filters.append(response_filter)

    def responsefilter(self, filter_path):
        """

        :param filter_path:
        :return: 
        """
        def decorator(f):
            print(filter_path)
            # todo 扫描目录  自动注册过滤器
            # self.response_filters.append(RestfulFilter)
            return f
        return decorator


class Application(object):
    _instance_lock = threading.Lock()

    def __init__(self, packages: str = None, profile: str = None):
        self.app = Libras(__name__)
        self.initialization(packages=packages, profile=profile)

    def __new__(cls, *args, **kwargs):
        if not hasattr(Application, "_instance"):
            with Application._instance_lock:
                if not hasattr(Application, "_instance"):
                    Application._instance = object.__new__(cls)
        return Application._instance

    def initialization(self, packages: str = None, profile: str = None):
        self.app.config['ROOT_PATH'] = os.getcwd()
        self.app.config['JSON_AS_ASCII'] = False
        self.app.config['scan_packages'] = packages
        self.app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
        self.app.config.from_yaml(profile)
        Registration.register(self.app)

    def run(self, host=None, port=9003):
        self.app.run(host=host, port=port, debug=True)
