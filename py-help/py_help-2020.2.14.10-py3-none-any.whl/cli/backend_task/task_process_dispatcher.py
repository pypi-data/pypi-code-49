# -*- coding: utf-8 -*-
import threading
import sys
import uuid
from apscheduler.schedulers.background import BackgroundScheduler  # 导入调度器
from .. import debug, info, warn, error


class TaskProcessDispatcher(object):
    task_proc_match = {}

    def __init__(self, proc_monitor):
        self.proc_monitor = proc_monitor
        self.cur_idx = 0
        self.process_call_match_dict = {}
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.once_timers = {}

    def get_dispatcher_process(self, one_executable=None):
        if one_executable is None or one_executable == sys.executable:
            the_process = self.proc_monitor.process_list[self.cur_idx % self.proc_monitor.process_list_len]
        else:
            process_list = self.proc_monitor.executable_map.get(one_executable, [])
            the_process = process_list[self.cur_idx % len(process_list)]
        self.cur_idx += 1
        self.cur_idx %= 4096
        return the_process

    def send_task_get_result(self, *args, **kwargs):
        task_id = kwargs.get('task_id')
        if task_id is None:
            return self.get_dispatcher_process(kwargs.pop('_executable')).send_task_get_result(*args, **kwargs)
        else:
            if 'task_id' in kwargs:
                del kwargs['task_id']
            the_process = self.process_call_match_dict.get(task_id)
            if the_process is None:
                error("没有任务[{}]的dispatcher记录".format(task_id))
                return None
            else:
                debug("对指定task_id:{}的进程来发起请求".format(task_id))
                return the_process.send_task_get_result(*args, **kwargs)

    def send_one_task(self, *args, **kwargs):
        """
        发送任务到任务子进程里执行
        :param args: 参数是 py_help.cli.backend_task.task_process 里的 send_one_task
        :param kwargs: 有内置的task_id,_executable 这两个内置参数
        :return:
        """
        task_id = kwargs.get('task_id')
        if task_id is None:
            the_process = self.get_dispatcher_process(kwargs.get('_executable'))
        else:
            the_process = self.process_call_match_dict.get(task_id)

        if 'task_id' in kwargs:
            del kwargs['task_id']
        if '_executable' in kwargs:
            del kwargs['_executable']
        if the_process is None:
            error("没有任务[{}]的dispatcher记录".format(task_id))
            return None
        else:
            wk_id = the_process.send_one_task(*args, **kwargs)
            self.process_call_match_dict[wk_id] = the_process
            return wk_id

    def _do_timer_task(self, *args, **kwargs):
        debug("开始定时任务: args:{} kwargs:{}".format(args, kwargs))
        ret = self.send_one_task(*args, **kwargs)
        self._clean_once_timer()
        if ret is not None and ret in self.process_call_match_dict:
            del self.process_call_match_dict[ret]

    def _get_one_timer(self, timer_id):
        once_timer = self.once_timers.get(timer_id)
        if once_timer is None:
            return self.scheduler.get_job(timer_id)
        else:
            return once_timer

    def _clean_once_timer(self):
        need_del = []
        for k, v in self.once_timers.items():
            if not v.is_alive():
                need_del.append(k)
        for one in need_del:
            try:
                del self.once_timers[one]
            except Exception:
                pass

    def start_timer_task(self, timer_type, func=None, args=[], kwargs={}, job_kwargs={}):
        job_uuid = str(uuid.uuid1())
        debug("添加任务类型 {} job_kwargs:{} id:{}".format(timer_type, job_kwargs, job_uuid))
        if func is None:
            func = self._do_timer_task
        if timer_type == 'once':
            seconds = job_kwargs.get('seconds', 0)
            the_timer = threading.Timer(function=func, interval=seconds, args=args, kwargs=kwargs)
            self.once_timers[job_uuid] = the_timer
            the_timer.start()
            return job_uuid
        the_job = self.scheduler.add_job(func, timer_type, id=job_uuid, args=args, kwargs=kwargs, **job_kwargs)
        if the_job is not None:
            self.scheduler.wakeup()
            return job_uuid
        else:
            error("触发任务出现异常 job是空")
            return None

    def pause_timer_task(self, task_id):
        the_job = self._get_one_timer(task_id)
        if the_job is None:
            error("异常,无法获取到任务 :{}".format(task_id))
            return False
        else:
            if isinstance(the_job, threading.Timer):
                the_job.cancel()
                del self.once_timers[task_id]
            else:
                the_job.pause()
            return True

    def cancel_timer_task(self, task_id):
        the_job = self._get_one_timer(task_id)
        if the_job is None:
            error("异常,无法获取到任务 :{}".format(task_id))
            return False
        else:
            if sys.version_info < (3, 0):
                timer_class = threading.Thread
            else:
                timer_class = threading.Timer
            if isinstance(the_job, timer_class):
                the_job.cancel()
                del self.once_timers[task_id]
            else:
                the_job.remove()
            return True

    def broadcast_one_task(self, *args, **kwargs):
        wk_ids = []
        for the_process in self.proc_monitor.process_list:
            wk_id = the_process.send_one_task(*args, **kwargs)
            self.process_call_match_dict[wk_id] = the_process
            wk_ids.append(wk_id)
        return wk_ids

    def get_one_status(self, task_id, max_try=3):
        """
        获取任务的返回信息
        :param task_id: 任务启动时的任务ID
        :param max_try: 重试次数
        :return:
        """
        the_process = self.process_call_match_dict.get(task_id)
        if the_process is None:
            error("没有任务[{}]的dispatcher记录".format(task_id))
            return None
        else:
            return the_process.get_one_status(task_id, max_try)

    def get_one_result(self, task_id, max_try=3):
        the_process = self.process_call_match_dict.get(task_id)
        if the_process is None:
            error("没有任务[{}]的dispatcher记录".format(task_id))
            return None
        else:
            result = the_process.get_one_result(task_id, max_try)
            if result is not None:
                # 不是空才可以删掉,是空就是超时的
                del self.process_call_match_dict[task_id]
            return result
