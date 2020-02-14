# -*- coding: utf-8 -*-
import rpyc
import sys
import threading
import time
from .. import debug, info, warn, error
from .task_queue import Task, task_queue
import json
import uuid


class TaskWorkerService(rpyc.Service):

    def on_connect(self, conn):
        info("connect~! {}".format(conn))
        self.task_queue = task_queue

    def on_disconnect(self, conn):
        # code that runs when the connection has already closed
        # (to finalize the service, if needed)
        debug("disconn :{}".format(conn))

    def exposed_ping(self, *args):
        """
        检查alive
        :return:
        """
        return 'pong'

    # 对于服务端来说， 只有以"exposed_"打头的方法才能被客户端调用，所以要提供给客户端的方法都得加"exposed_"
    def exposed_put_one_task(self, priority, url, kwargs, status_cbk, result_cbk, add_task_cbk):
        kwargs = dict(kwargs)
        debug("需要添加任务:url:{},kwargs:{}".format(url, kwargs))
        the_task_id = str(uuid.uuid1())
        the_task = Task(time.time(), the_task_id, priority, url, kwargs, status_cbk,
                        result_cbk)
        add_task_cbk(the_task_id)
        self.task_queue.put(the_task)
        return the_task_id

    def exposed_stop_worker_service(self):
        info("worker_service [{}]开始退出".format(self))

        def sys_exit():
            import time
            import os
            time.sleep(1)
            os._exit(0)

        threading.Thread(target=sys_exit).start()
        return 'exit_ok'
