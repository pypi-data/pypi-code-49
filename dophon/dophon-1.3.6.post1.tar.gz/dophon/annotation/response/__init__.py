# 响应返回数据修饰器(跳过视图解析器)
# 响应体形式返回
# (自带AutoParam) <------暂未完成
import functools
from dophon import properties
from dophon_logger import *
from flask import jsonify, render_template
import re

logger = get_logger(eval(properties.log_types))

logger.inject_logger(globals())


def response_body():
    def method(f):
        @functools.wraps(f)
        def arg(*args, **kwargs):
            obj = f(*args, **kwargs)
            try:
                result = jsonify(obj)
            except TypeError as te:
                result = {k: getattr(obj, k) for k in dir(obj) if not re.match('__.+__', k)}
                # result = obj.__dict__
                # result = None
            finally:
                return result if result else {}

        return arg

    return method


# 返回web模板
def response_template(template: list):
    """
    返回模板页面
    :param template: 模板页面路径
    :return:
    """

    def method(f):
        @functools.wraps(f)
        def args(*args, **kwargs):
            page_param = f(*args, **kwargs)
            if isinstance(page_param, type({})):
                return render_template(template, **page_param)
            else:
                logger.error('页面参数错误!')
                raise KeyError('页面参数错误!')

        return args

    return method
