import re
import json
from functools import wraps
from inspect import getfullargspec, signature, _empty
from dophon import properties
from dophon.tools.sys_utils import to_dict

DESC_INFO = {}
TRANSLATE_TYPES = ['int', 'set']
SPECIAL_TRANSLATE_TYPES = ['list', 'dict']
RETURN_TYPE_DESC = {
    'dict': {}, 'list': [], set: [], 'tuple': [], 'str': "\"\"", 'int': 0
}


def try_str(obj):
    try:
        return json.dumps(obj, ensure_ascii=False)
    except:
        try:
            return to_dict(obj)
        except:
            return str(obj)


def desc(
        operation: str = 'None',
        param_des: dict = {},
        demo: dict = None,
        return_demo=None,
        remark: str = None,
):
    """
    函数描述装饰器
    自动添加请求属性配对
    :return:
    """
    if properties.load_desc:
        def inner_method(f):
            # 获取方法的参数名集合
            # FullArgSpec(args=['test_arg1'], varargs=None, varkw=None, defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={})
            full_arg_spec = getfullargspec(f)
            func_return_type = signature(f).return_annotation
            func_return_type = func_return_type if func_return_type != _empty else None
            __own_doc = getattr(f, '__doc__')  # 自身定义的文档
            __args = full_arg_spec.args  # 通过函数定义的属性名集合
            __defaults = full_arg_spec.defaults  # 通过函数定义参数默认值
            __defaults = __defaults if __defaults else ()
            # 处理无默认值参数
            if __defaults and len(__args) > len(__defaults):
                __pre_defaults = list(__defaults)
                for count in range(len(__args) - len(__defaults)):
                    __pre_defaults.insert(0, None)
                __defaults = tuple(__pre_defaults)
            # print(__defaults)
            __annotations = full_arg_spec.annotations  # 通过函数定义的参数修饰
            # print(full_arg_spec)
            # 处理参数信息,放入参数信息列
            __function_arg_info = {}
            __func_info = {
                'own_doc': re.sub('(\n)', '<br />', __own_doc) if __own_doc else operation
            }
            for __inner_arg_index in range(len(__args)):
                __function_arg_type = __annotations[__args[__inner_arg_index]].__name__ \
                    if __annotations and __args[__inner_arg_index] in __annotations else 'any'
                __function_arg_dvalue = (eval(
                    f"""{__function_arg_type}""" + \
                    f"""("{__defaults[
                        __inner_arg_index]}")""") \
                    if __function_arg_type in TRANSLATE_TYPES else (__defaults[__inner_arg_index] \
                    if __function_arg_type in SPECIAL_TRANSLATE_TYPES else (try_str(__defaults[__inner_arg_index]) \
                    if __defaults and __inner_arg_index < len(
                    __defaults) else None))) \
                    if __defaults and __inner_arg_index < len(__defaults) else None
                __function_arg_info[__args[__inner_arg_index]] = {
                    'name': __args[__inner_arg_index],
                    'desc': param_des.get(__args[__inner_arg_index]) if __args[
                                                                            __inner_arg_index] in param_des else None,
                    # 获取参数上的默认值
                    # 隐藏对象地址
                    'default_value': re.sub(' at.*>', '>', __function_arg_dvalue
                                            ) if isinstance(__function_arg_dvalue, str) else __function_arg_dvalue
                    if __defaults and __inner_arg_index < len(__defaults) else None,
                    # 获取参数上的类型修饰
                    'type': __annotations[__args[__inner_arg_index]].__name__
                    if __annotations and __args[__inner_arg_index] in __annotations
                    else 'any',
                }
            __func_info['remark'] = remark
            __func_info['args_info'] = __function_arg_info
            __func_return_type_desc = func_return_type.__name__ \
                if func_return_type \
                else 'any'
            __func_info['demo'] = demo
            __func_info['returns'] = {
                'type': __func_return_type_desc,
                'demo': return_demo
                if return_demo else (RETURN_TYPE_DESC[__func_return_type_desc]
                                     if __func_return_type_desc in RETURN_TYPE_DESC else to_dict(
                    func_return_type.__init__()))
            }
            DESC_INFO[f'{getattr(f, "__module__")}.{getattr(f, "__name__")}'] = __func_info

            @wraps(f)
            def inner_args(*args, **kwargs):
                return f(*args, **kwargs)

            return inner_args

        return inner_method
    else:
        def pass_inner_method(f):
            @wraps(f)
            def pass_inner_args(*args, **kwargs):
                return f(*args, **kwargs)

            return pass_inner_args

        return pass_inner_method
