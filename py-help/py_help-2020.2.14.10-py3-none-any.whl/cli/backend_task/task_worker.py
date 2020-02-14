# -*- coding: utf-8 -*-
import threading
from .. import debug, info, warn, error


class TaskWorker(threading.Thread):
    worker_status = threading.local()

    def __init__(self, wk_id, queue):
        super(TaskWorker, self).__init__()
        self.worker_id = wk_id
        self.wk_queue = queue
        self.is_start = True

    def run(self):
        debug("start Worker[{}]".format(self.worker_id))
        while self.is_start:
            try:
                one_task = self.wk_queue.get()
                debug("worker:{} 运行任务:{}".format(self.worker_id, one_task))
                self.worker_status.task = one_task
                one_task.do_task()
            except Exception as e:
                error("处理任务出错::", e)

    def stop(self):
        self.is_start = False

    @classmethod
    def set_task_status(cls, status_data):
        the_task_id = cls.worker_status.task.task_id
        debug("设置[{}] => status [{}]".format(the_task_id, status_data))
        cls.worker_status.task.do_status_cbk(status_data)

    @classmethod
    def get_task_id(cls):
        try:
            return cls.worker_status.task.task_id
        except Exception as ex:
            info("task 不存在")
            return None
