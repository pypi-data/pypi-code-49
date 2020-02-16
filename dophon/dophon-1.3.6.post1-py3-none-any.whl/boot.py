# coding: utf-8
import functools
import os
import sys
import re

from dophon import pre_boot

pre_boot.check_modules()

from dophon import properties, blue_print

from dophon_logger import *

logger = get_logger(eval(properties.log_types))

logger.inject_logger(globals())

from werkzeug import _internal

_internal._logger = logger

from . import tools


def load_banner():
    """
    加载header-banner文件
    :return:
    """
    file_root = properties.project_root
    file_path = file_root + os.path.sep + 'header.txt'
    if os.path.exists(file_path):
        with open(file_path, encoding='utf8') as banner:
            for line in banner.readlines():
                sys.stdout.write(line)
    else:
        tools.show_banner()
    sys.stdout.flush()


def load_footer():
    """
    加载footer-banner文件
    :return:
    """
    file_root = properties.project_root
    file_path = file_root + os.path.sep + 'footer.txt'
    if os.path.exists(file_path):
        with open(file_path, encoding='utf8') as banner:
            for line in banner.readlines():
                sys.stdout.write(line)
    sys.stdout.flush()


def BeanScan(scan_path: list = []):
    def method(f):
        @functools.wraps(f)
        def method_args(*args, **kwargs):
            logger.debug('mapping beans')
            __scan_path = scan_path if scan_path else properties.components_path
            for bean_path in __scan_path:
                is_project_root = os.path.abspath(properties.project_root + bean_path) == os.path.abspath(
                    properties.project_root)
                if is_project_root:
                    # 若配置项目自身路径则提示警告
                    logger.warning(f'扫描路径(components_path)存在项目根路径的配置会导致项目异常启动,请注意')
                map_bean(bean_path)
            return f(*args, **kwargs)

        return method_args

    return method


def map_bean(bean_path: str, is_project_root: bool = False):
    __project_root = properties.project_root.replace("\\", "/")
    bean_dir = re.sub('(\\\\|/)', '', bean_path)
    # 不存在路由定义
    # print(f'bean_path: {bean_path}')
    try:
        for root, dirs, files in os.walk(f'{__project_root}{bean_path}'):
            relative_path = re.sub(f'{__project_root}', '', root)
            # 若处于路由定义则跳过
            # 相对路径为根路径也跳过
            # 强制指定为项目根路径也跳过
            if relative_path in properties.blueprint_path \
                    or relative_path == '/' \
                    or relative_path.endswith('__') \
                    or is_project_root:
                continue
            # 校验忽略注入的配置
            __pass_component_flag = False
            __uncomponents_path = [
                i.replace(f'{os.path.sep}', '')
                for i in (properties.uncomponents_path if hasattr(properties, 'uncomponents_path') else [])
            ]
            __uncomponents_path.append(f'/site-packages')
            __uncomponents_path.append(f'/.package_cache')
            for __up_items in __uncomponents_path:
                if relative_path.startswith(__up_items):
                    __pass_component_flag = True
                    break
            if __pass_component_flag:
                continue
            logger.debug(f'scan path {relative_path}')
            # exec(f'from {re.sub("/", ".", __bean_dir)} import {module_path.split(".")[-1]}')
            # print(f'{root} => {relative_path} => {dirs} => {files}')
            # print(__dirs)
            for file in files:
                file_short_name = os.path.basename(file).split(".")[0]
                if not file.endswith('.py') or re.match('__.+__', file_short_name):
                    # 不是python脚本文件
                    continue
                # 获取内部文件路径
                __file_path = f'{relative_path}/{file_short_name}'
                # 整理成包形式
                __file_package = re.sub('(\\\\|/)', '.', __file_path)
                # print(__file_package)
                __file_package_part = __file_package.split('.')[1:]
                # print(__file_package_part)
                __exec_code = f'from {".".join(__file_package_part[:-1])} import {__file_package_part[-1]}'
                # print(__exec_code)
                logger.debug(f'mapping bean {__file_package_part[-1]} {__exec_code}')
                try:
                    exec(__exec_code)
                except Exception as e:
                    logger.error(f'{__file_package_part[-1]} inject failed, reason: {e}')
        __import__(bean_dir, fromlist=bean_dir)
    except Exception as e:
        # raise e
        pass


@BeanScan()
def d_app(f):
    load_banner()

    @functools.wraps(f)
    def __d_app(*arg, **kwargs):
        return f(*arg, **kwargs) if callable(f) else None

    load_footer()
    return __d_app
