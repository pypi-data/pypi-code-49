# -*- coding: utf-8 -*-
import json
import sys
import time
import pickle
import rpyc
import threading
from multiprocessing import Process
from .. import debug, info, warn, error
from py_help.lib.cache_obj_basic import CacheObjBasic
from .task_worker_service import TaskWorkerService
from rpyc.utils.server import ThreadPoolServer
from .task_queue import task_queue

try:
    from multiprocessing import set_executable
except ImportError as es:
    warn("导入 set_executable 出错，没有 python2.7 在linux下不支持")


    # 定义一个空函数
    def set_executable(executable):
        pass

MAX_STATUS_DATA = 1024
MAX_STORE_TRIGGER_CNT = 512  # 存储了512个任务后就会触发清空
MAX_STORE_TIME = 600  # 10分钟内没有收割的任务,就清空掉
INSIDE_RESULT = '__mark_unable_to_send_task_url__'


def run_service(run_port=50188, class_name='py_help.cli.router.Router', is_gevent=False, worker_id=0,
                shared_dict={}, shared_queue_list=[]):
    import importlib
    class_arr = class_name.split('.')
    class_name = class_arr[-1]
    module_name = '.'.join(class_arr[0:-1])
    if is_gevent:
        try:
            info("load gevent monkey")
            from gevent import monkey
            monkey.patch_all()
        except Exception as ex:
            error("加载gevent出现异常", ex)
    debug(
        "开始启动[{}] is_gevent:{} router backend_task service module_name:[{}],class_name:[{}],shared_dict:{},"
        "shared_queue_list:{}".format(
            run_port, is_gevent, module_name, class_name, len(shared_dict), len(shared_queue_list)))
    the_module = importlib.import_module(module_name)
    router = getattr(the_module, class_name)
    router().import_all_controller()
    router.backend_task_shared['worker_id'] = worker_id
    router.backend_task_shared['shared_dict'] = shared_dict
    router.backend_task_shared['shared_queue_list'] = shared_queue_list
    debug("start task worker service with port :{} is_import:{}".format(run_port, router.is_import_controller))
    the_server = ThreadPoolServer(TaskWorkerService, hostname='localhost', nbThreads=10, port=run_port,
                                  auto_register=False)
    from .task_worker import TaskWorker
    for w_id in range(10):
        wk = TaskWorker(w_id, task_queue)
        wk.setDaemon(True)
        wk.start()
    the_server.start()


class TaskProcess(CacheObjBasic):
    rpyc_backend_thread = None
    rpyc_conn = None
    is_dead = False
    my_proc = None
    router_class_name = None
    is_need_auto_start = True
    multiprocessing_lock = threading.Lock()

    @classmethod
    def get_uniq_id(cls, *args, **kwargs):
        if len(args) > 0:
            uniq_id = 'port:{}'.format(args[0])
        else:
            if kwargs.get('port') is None:
                uniq_id = 'port:50188'
            else:
                uniq_id = 'port:{}'.format(kwargs.get('port'))
        return uniq_id

    def __init__(self, port=50188, is_gevent=False, worker_id=0, shared_dict={}, shared_queue_list=[],
                 router_class_name=None, executable=None):
        if not self._is_init:
            self.rpyc_conn = None
            self.rpyc_backend_thread = None
            self.task_port = port
            self.is_dead = False
            self.worker_id = worker_id
            self.shared_dict = shared_dict
            self.shared_queue_list = shared_queue_list
            self.my_proc = None
            self.is_need_auto_start = True
            self.router_class_name = router_class_name
            self.is_gevent = is_gevent
            self._is_init = True
            self.lock = threading.Lock()
            self.task_running_data = {}
            if executable is None:
                executable = sys.executable
            if executable != sys.executable and sys.version_info < (3, 0) and 'linux' in sys.platform:
                warn("linux 下的 python2 不支持多解析器模式")
                executable = sys.executable
            info("启动任务进程:{}".format(executable))
            self.executable = executable

    def _get_rpyc_conn(self):
        if self.rpyc_conn is None:
            info("尝试连接 rpyc {}".format(self.task_port))
            self.rpyc_conn = rpyc.connect('127.0.0.1', self.task_port, config={"allow_public_attrs": True})
            self.rpyc_backend_thread = rpyc.BgServingThread(self.rpyc_conn, callback=self.rpyc_disconn_callback)
        return self.rpyc_conn

    def rpyc_disconn_callback(self):
        warn("进程端口:{} proc:{} 连接断开".format(self.task_port, self.my_proc))
        if self.is_need_auto_start:
            info("需要拉起,进行快速拉起")
            self.trigger_start()

    def _reset_rpc_conn(self):
        if self.rpyc_backend_thread is not None:
            thr = self.rpyc_backend_thread
            self.rpyc_backend_thread = None
            del thr
        try:
            self.rpyc_conn = None
            self._get_rpyc_conn()
            return True
        except Exception as ex:
            warn("无法连接进程端口: {} {}".format(self.task_port, ex))
        return False

    def get_one_result(self, task_id, max_try=3):
        ret_data = None
        try:
            the_task_running_data = self.get_running_data(task_id)
            the_result = the_task_running_data.get('result')
            ret_data = the_result.get('data')
            if ret_data is None:
                cur_thread = threading.current_thread()
                if cur_thread.__dict__.get('result_padding_event') is None:
                    cur_thread.__dict__['result_padding_event'] = threading.Event()
                cur_thread.__dict__['result_padding_event'].clear()
                the_result['thread'] = cur_thread
                if cur_thread.__dict__['result_padding_event'].wait(max_try):
                    ret_data = the_result.get('data')
                    debug("{} 成功获取到数据 :{}".format(task_id, ret_data))
                    del self.task_running_data[task_id]
                else:
                    debug("{} 没有获取到数据,最终超时了".format(task_id))
        except EOFError:
            self._reset_rpc_conn()
        except Exception as e:
            error("出现异常,没有获取结果", e)
        return ret_data

    def get_one_status(self, task_id, max_try=3):
        ret_data = []
        try:
            the_task_running_data = self.get_running_data(task_id)
            the_status = the_task_running_data.get('status')
            the_status_data = the_status.get('data')
            if len(the_status_data) == 0:
                cur_thread = threading.current_thread()
                if cur_thread.__dict__.get('status_padding_event') is None:
                    cur_thread.__dict__['status_padding_event'] = threading.Event()
                cur_thread.__dict__['status_padding_event'].clear()
                the_status['thread'] = cur_thread
                if cur_thread.__dict__['status_padding_event'].wait(max_try):
                    debug("成功获取到数据 :{}".format(the_status_data))
                else:
                    debug("self:{} 没有获取到数据,最终超时了 {}".format(self, the_task_running_data))
            ret_data.extend(the_status_data)
            del the_status_data[:]
        except EOFError:
            self._reset_rpc_conn()
        except Exception as e:
            error("出现异常,没有获取状态", e)
        return ret_data

    def _trigger_clean_task_data(self):
        if len(self.task_running_data) > MAX_STORE_TRIGGER_CNT:
            now = time.time()
            need_del_ids = []
            for run_id, data in self.task_running_data.items():
                start_time = data.get('start_time')
                if now - start_time > MAX_STORE_TIME:
                    warn("需要删除任务 {} 结果数据,开始时间是 {}".format(run_id, time.localtime(start_time)))
                    need_del_ids.append(run_id)
            for one_id in need_del_ids:
                try:
                    del self.task_running_data[one_id]
                except Exception:
                    pass

    def task_status_update_cbk(self, task_id, status_data):
        status_data = pickle.loads(status_data)
        the_task_running_data = self.get_running_data(task_id)
        debug("self:{} 添加状态:{},the_task_running_data:{}".format(self, status_data, the_task_running_data))
        the_status = the_task_running_data.get('status')
        the_status.get('data').append(status_data)
        if len(the_status['data']) > MAX_STATUS_DATA:
            the_status['data'].pop(0)
        if the_status.get('thread') is None:
            self._trigger_clean_task_data()
        else:
            the_status.get('thread').__dict__.get('status_padding_event').set()

    def task_result_update_cbk(self, task_id, result_data):
        result_data = pickle.loads(result_data)
        the_task_running_data = self.get_running_data(task_id)
        debug("返回结果:{}".format(result_data))
        the_result = the_task_running_data.get('result')
        the_result['data'] = result_data
        if the_result.get('thread') is None:
            self._trigger_clean_task_data()
        else:
            the_result.get('thread').__dict__.get('result_padding_event').set()

    def get_running_data(self, task_id):
        if self.task_running_data.get(task_id) is None:
            self.task_running_data[task_id] = {
                'result': {},
                'start_time': time.time(),
                'status': {'data': []}
            }
        return self.task_running_data[task_id]

    def add_task_cbk(self, task_id):
        # debug("任务添加了:{}".format(task_id))
        self.get_running_data(task_id)

    def send_one_task(self, priority, url, kwargs, max_try=3):
        """
        触发后台任务进程执行一个任务
        :param priority: int, 任务的优先级,越大优先级越高.
        :param url: string, 需要触发的任务的url.
        :param kwargs: dict, 需要发送的参数字典.
        :param max_try: int, 最大尝试次数(避免偶然性出错).
        :return: json, 任务uuid
        """
        try_time = max_try
        try:
            ret = self._get_rpyc_conn().root.put_one_task(priority=priority, url=url, kwargs=kwargs,
                                                          status_cbk=self.task_status_update_cbk,
                                                          result_cbk=self.task_result_update_cbk,
                                                          add_task_cbk=self.add_task_cbk)
            debug("运行返回:{}".format(ret))
            self.add_task_cbk(ret)
            return ret
        except Exception as ex:
            if try_time > 0:
                info("出现异常,重试:", ex)
            else:
                error("try_time {t} is over get exception again".format(t=try_time))
                return None

        if self.check_is_alive():
            self._reset_rpc_conn()
        else:
            self.trigger_start()
        return self.send_one_task(priority, url, kwargs, try_time - 1)

    def send_task_get_result(self, priority, url, kwargs, max_try=3, max_timeout=120):
        ret = self.send_one_task(priority, url, kwargs, max_try)
        if ret:
            result = self.get_one_result(ret, max_timeout)
            debug("请求任务 url:{}, params:{}\n返回结果:{}".format(url, kwargs, result))
            return result
        else:
            warn("无法发送任务 url:{}".format(url))
            return INSIDE_RESULT

    def check_is_alive(self):
        for i in range(2):
            try:
                if self.my_proc is None:
                    debug("进程都没有启动过")
                    return False
                else:
                    if self.my_proc.is_alive():
                        debug("进程存活:{}".format(self.my_proc))
                    ret = self._get_rpyc_conn().root.ping()
                    if ret == 'pong':
                        return True
                    else:
                        return False
            except EOFError:
                self._reset_rpc_conn()
                debug("连接问题,重试一次")
            except Exception as ex:
                warn("检查出错 {}".format(ex))
                return False

    def trigger_start(self):
        with self.lock:
            if not self.is_need_auto_start:
                debug("无需自动启动")
                return
            if self.check_is_alive():
                debug("进程已经起来")
            else:
                if self.my_proc:
                    if self.my_proc.is_alive():
                        warn("前一个进程都还存在 pid:{},尝试杀掉进程".format(self.my_proc.pid))
                        try:
                            self.my_proc.terminate()
                            self.my_proc = None
                        except Exception:
                            pass

                self.my_proc = Process(target=run_service,
                                       args=(
                                           self.task_port, self.router_class_name, self.is_gevent, self.worker_id,
                                           self.shared_dict,
                                           self.shared_queue_list))
                self.my_proc.daemon = True
                if self.executable != sys.executable:
                    with self.multiprocessing_lock:
                        try:
                            set_executable(self.executable)
                            self.my_proc.start()
                        except Exception as ex:
                            error("出现异常，启动进程失败", ex)
                        finally:
                            set_executable(sys.executable)
                else:
                    self.my_proc.start()
                for i in range(5):
                    if self.my_proc.is_alive():
                        if self._reset_rpc_conn():
                            debug(
                                "成功启动进程: port:{} pid:{} router_class:{}".format(self.task_port, self.my_proc.pid,
                                                                                self.router_class_name))
                            return True
                        else:
                            time.sleep(1)
                    else:
                        warn("进程异常:{}".format(self.my_proc))
                warn(
                    "启动进程超时: port:{} pid:{} router_class:{}".format(self.task_port, self.my_proc.pid,
                                                                    self.router_class_name))
                return False

    def trigger_stop_proc(self):
        with self.lock:
            self.is_need_auto_start = False
            if not self.check_is_alive():
                is_alive_proc = False
                try:
                    debug('触发进程停止 port:{}'.format(self.task_port))
                    if self.my_proc:
                        if self.my_proc.is_alive():
                            debug("进程存活:{}".format(self.my_proc))
                            is_alive_proc = True
                            self.my_proc.terminate()
                            self.my_proc = None
                    ret = self._get_rpyc_conn().root.stop_worker_service()
                    debug("停止进程返回 ret:{}".format(ret))
                    if ret == 'exit_ok':
                        return True
                    else:
                        return False
                except EOFError as eof_ex:
                    if is_alive_proc:
                        debug("网络断开了,应该是terminate的效果")
                        return True
                    else:
                        debug("检查出错 {}".format(eof_ex))
                        return False
                except Exception as ex:
                    debug("检查出错 {}".format(ex))
                    return False
