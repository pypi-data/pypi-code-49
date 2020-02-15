import importlib
import pkgutil

from IQCommon.api.wrapper import api_exec_patcher
from IQCommon.utils import ObjectDict
from IQData.apis.authentication import *
import IQData.utils
from IQData.utils import (
    SERVICE_PATH,
    SERVICE_PREFIX,
    DEFAULT_SETTINGS
)
from IQData.utils.module_object import Module


def api_helper(config=None):
    """
    获取api字典
    :param config: 配置信息
    :type config: DictObject
    :return: api字典 {<module_name>:{<api_name>:api}}
    :rtype: dict
    """
    api_dict = {}
    if config is None:
        config = DEFAULT_SETTINGS
    else:
        if isinstance(config, ObjectDict):
            IQData.utils.settings = config

    try:
        service_settings = config.services
    except AttributeError:
        service_settings = None
    module_api = {}
    for loader, module_name, is_pkg in pkgutil.iter_modules(
            [
                SERVICE_PATH  # 注意 iter_modules的第一个地址参数为list
            ]
    ):

        if is_pkg:
            module_full_name = SERVICE_PREFIX + module_name
            try:
                service_module = importlib.import_module(
                    module_full_name
                )
                api_module = importlib.import_module(
                    module_full_name + '.api'
                )
            except ImportError:
                continue
            if service_settings:
                try:
                    module_settings = getattr(service_settings, module_name)
                except AttributeError:
                    pass
                else:
                    try:
                        service_module.settings.update(module_settings)
                    except AttributeError:
                        service_module.settings = module_settings
            try:
                module_api_dict = {}
                for api_method_name in api_module.__all__:
                    try:
                        api = getattr(api_module, api_method_name)
                    except AttributeError:
                        continue
                    module_api_dict[
                        api_method_name
                    ] = api
                if module_api_dict:
                    api_dict[module_name] = Module(
                        'IQData.' + module_name,
                        module_api_dict
                    )
                    module_api[module_name] = module_api_dict
            except AttributeError as e:
                continue
    try:
        shortcut_list = config.shortcut_module_list
    except AttributeError:
        pass
    else:
        for service_name in shortcut_list:
            if service_name in module_api:
                for api_name, api_object in module_api[service_name].items():
                    if api_name in api_dict and api_name != service_name:
                        continue
                    api_dict[api_name] = api_object
    return api_dict


def register_to_locales(
        locals_variable: dict = None,
        all_can_be_imported: list = None,
        config: ObjectDict = None
):
    """
    将api注册至作用域中
    :param locals_variable: 作用域
    :type locals_variable: dict / None
    :param all_can_be_imported: 可引用范围
    :type all_can_be_imported: list / None
    :param config: 配置信息
    :type config: ObjectDict
    :return: None
    """
    api_dict = api_helper(config)
    if locals_variable is not None:
        locals_variable.update(api_dict)
    if all_can_be_imported is not None:
        all_can_be_imported.extend(list(api_dict.keys()))
