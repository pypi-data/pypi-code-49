# coding: utf-8
from multiprocessing import Process, freeze_support
from concurrent.futures import ProcessPoolExecutor
from threading import Thread
import time, socket, random
from flask import request, make_response
from urllib3 import PoolManager
from dophon import properties
from dophon_logger import *
from dophon.annotation import Bean
import requests as direct_r
from requests_toolbelt.multipart.encoder import MultipartEncoder
from dophon.boot import BeanScan

logger = get_logger(eval(properties.log_types))

logger.inject_logger(globals())

ports = []  # 记录监听端口

proxy_clusters = {}

pool = PoolManager()


def main_freeze():
    freeze_support()


def redirect_request():
    current_header = {}
    request_kwargs = {}
    form_boundary = None
    # 迁移当前请求头
    for k, v in request.headers.items():
        if v.startswith('multipart/form-data;'):
            form_header_info = v.split('boundary=')
            form_boundary = form_header_info[1] if len(form_header_info) > 1 else None
            continue
        current_header[k] = v
    # print(request.endpoint)
    if request.endpoint and not request.endpoint.startswith('_annotation_auto_reg'):
        pass
    elif not current_header.get('Outer'):
        choice_port = random.choice(ports)
        # 添加网关标识
        current_header['Outer'] = 'pass'
        logger.info(f'touch path: {request.path}, touch port: {choice_port} [success]')
        request_kwargs['headers'] = current_header
        request_fields = request.json if request.is_json else request.form
        if form_boundary:
            __file = request.files.to_dict()['file']
            request_kwargs['data'] = {k: v for k, v in request_fields.items()}
            request_kwargs['data']['file'] = (__file.filename, __file.stream, __file.content_type)
            request_kwargs['data'] = MultipartEncoder(fields=request_kwargs['data'])
            request_kwargs['headers']["Content-Type"] = request_kwargs['data'].content_type
            res = direct_r.request(
                request.method,
                f'http://127.0.0.1:{choice_port}{request.path}',
                **request_kwargs
            )
            cell_res = make_response(res.content, res.status_code)
        else:
            if request.content_type and request.content_type.startswith('application/json'):
                import json
                request_kwargs['data'] = request_fields
            else:
                request_kwargs['data'] = request_fields

            # res = pool.request(
            #     request.method,
            #     f'http://127.0.0.1:{choice_port}{request.path}',
            #     **request_kwargs
            # )
            res = direct_r.request(
                request.method,
                f'http://127.0.0.1:{choice_port}{request.path}',
                **request_kwargs
            )
            cell_res = make_response(res.content, res.status_code)
        # print(res)
        # 迁移转发的响应头
        for item in res.headers:
            # print(item)
            cell_res.headers[item] = res.headers[item]
        return cell_res


def outer_entity(boot):
    # 重写路由信息(修改为重定向路径)
    Bean('app').before_request(redirect_request)
    boot.d_web(host='0.0.0.0')(lambda x: x)(0)


process_pool = ProcessPoolExecutor()


def run_clusters(base_boot, clusters: int, outer_port: bool = False, start_port: int = 8800,
                 multi_static_fix: bool = False,
                 part_kwargs: dict = {}):
    """
    运行集群式服务器
    :param clusters: 集群个数
    :param outer_port: 是否开启外部端口映射(映射端口为用户配置文件中配置的端口)
    :param start_port: 集群起始监听端口
    :param multi_static_fix: 集群静态文件修复
    :param part_kwargs: 集群节点额外参数(会覆盖默认参数)
    :return:
    """
    from dophon import boot, webboot
    process_pool = ProcessPoolExecutor(max_workers=clusters)
    if base_boot.__name__ == webboot.__name__:
        for i in range(clusters):
            current_port = start_port + i
            create_cluster_web_cell(boot=base_boot, port=current_port, part_kwargs=part_kwargs,
                                    cell_static_fix=multi_static_fix)
            ports.append(current_port)
        while len(ports) != clusters:
            time.sleep(5)

        logger.info('启动检测端口监听')
        for port in ports:
            if check_socket(int(port)):
                continue
        logger.info('集群端口: %s ' % ports)
        if outer_port:
            logger.info('启动外部端口监听[%s]' % (properties.port))
            outer_entity(base_boot)


def action_webboot(boot, cell_static_fix: bool, port: int):
    try:
        boot.fix_static(enhance_power=cell_static_fix)
        boot.fix_template()
    except Exception as e:
        raise e
    return boot.run


def create_cluster_web_cell(boot, port, part_kwargs, cell_static_fix: bool):
    kwargs = {
        'host': '127.0.0.1',
        'port': port,
        'run_type': eval(f'boot.{part_kwargs["run_type"] if "run_type" in part_kwargs else "FLASK"}'),
        'n': 2
    }
    if part_kwargs:
        # 迁移参数
        for k, v in part_kwargs.items():
            if k not in kwargs:
                kwargs[k] = v
    cell_boot = action_webboot(boot, cell_static_fix, port)
    # print(cell_boot)
    # http协议
    from dophon.tools import is_not_windows
    # Linux使用多进程
    # Windows使用多线程
    proc = Process(target=cell_boot, kwargs=kwargs) if is_not_windows() else Thread(target=cell_boot, kwargs=kwargs)
    port_proc = Process(target=check_socket, args=(int(port),)) if is_not_windows() else Thread(target=check_socket,
                                                                                                args=(int(port),))
    proc.start()
    port_proc.start()
    port_proc.join()
    # process_pool.submit(cell_boot, **kwargs)


def check_socket(port: int):
    s = socket.socket()
    flag = True
    while flag:
        try:
            ex_code = s.connect_ex(('127.0.0.1', port))
            flag = False
            return int(ex_code) == 0
        except Exception as e:
            time.sleep(3)
            continue
