# -*- coding: utf-8 -*-
import threading
import time
import sys
from multiprocessing import Manager
from .. import debug, info, warn, error
from .task_process import TaskProcess


class TaskProcessMonitor(threading.Thread):
    process_status = {}

    def __init__(self, start_port, process_cnt, the_router_class, is_gevent=False, executable_list=None):
        super(TaskProcessMonitor, self).__init__()
        self.start_port = start_port
        self.process_cnt = process_cnt
        self.is_start = True
        self.is_gevent = is_gevent
        self.manager = Manager()
        self.shared_dict = self.manager.dict()
        self.shared_queue_list = []
        self.process_list = []
        self.running_router_class_name = "{}.{}".format(the_router_class.__module__, the_router_class.__name__)
        if executable_list is None:
            executable_list = [sys.executable]
        self.executable_list = executable_list
        self.executable_map = {}
        self.is_monitor = True

        self.worker_id = 0

        for idx in range(len(executable_list)):
            one_executable = executable_list[idx]
            self.do_start_one_executable(self.start_port + (idx * self.process_cnt), one_executable)
        self.ensure_all_process_start()
        self.process_list_len = len(self.process_list)

    def ensure_all_process_start(self):
        threads = []
        for one_process in self.process_list:
            one_thr = threading.Thread(target=one_process.trigger_start)
            one_thr.daemon = True
            one_thr.start()
            threads.append(one_thr)
        for one_thr in threads:
            one_thr.join()

    def do_start_one_executable(self, start_port, one_executable):
        if self.executable_map.get(one_executable) is None:
            self.executable_map[one_executable] = []
        for port in range(start_port, start_port + self.process_cnt):
            self.shared_queue_list.append(self.manager.Queue(2048))
            proc = TaskProcess(port=port, is_gevent=self.is_gevent, worker_id=self.worker_id,
                               shared_dict=self.shared_dict, executable=one_executable,
                               shared_queue_list=self.shared_queue_list,
                               router_class_name=self.running_router_class_name)
            self.process_list.append(proc)
            self.executable_map[one_executable].append(proc)
            self.worker_id += 1

    def run(self):
        debug("start Monitor {} router:{}".format(self.process_list, self.running_router_class_name))
        time.sleep(15)  # 这里先等一下,保证进程起来
        while self.is_start:
            try:
                if self.is_monitor:
                    for one_process in self.process_list:
                        if not one_process.check_is_alive():
                            info("进程不存活:{},启动router:{}".format(one_process, self.running_router_class_name))
                            one_process.trigger_start()
                time.sleep(1)
            except Exception as e:
                error("监控任务出错::", e)
                time.sleep(5)

    def pause_mon(self):
        self.is_monitor = False
        self.stop_process()

    def stop(self):
        debug("开始停止")
        self.is_start = False
        self.stop_process()

    def stop_process(self):
        for one_process in self.process_list:
            if one_process.check_is_alive():
                try:
                    one_process.trigger_stop_proc()
                except Exception as ex:
                    error("退出时出错了", ex)
