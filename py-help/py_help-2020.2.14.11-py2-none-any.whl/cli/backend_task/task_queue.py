# -*- coding: utf-8 -*-

import sys

if sys.version_info < (3, 0):
    import Queue
else:
    import queue as Queue

import time
from .. import debug, info, warn, error
import pickle

# 任务的队列
task_queue = Queue.PriorityQueue()


class Task(object):

    def __init__(self, start_time, uuid, priority, url, kwargs, status_cbk, result_cbk):
        self.priority = priority
        self.url = url
        self.kwargs = kwargs
        self.start_time = start_time
        self.task_id = uuid
        self.task_status = None
        self.result = None
        self.status_cbk = status_cbk
        self.result_cbk = result_cbk
        return

    def __cmp__(self, other):
        if sys.version_info < (3, 0):
            return cmp(self.priority, other.priority)
        else:
            return (self.priority > other.priority) - (self.priority < other.priority)

    def __repr__(self):
        return "job[{}]: priority [{}] => kwargs {}".format(self.task_id, self.priority, self.kwargs)

    def do_result_cbk(self):
        self.result_cbk(self.task_id, pickle.dumps(self.result))

    def do_status_cbk(self, status_data):
        debug("需要设置 :{}".format(status_data))
        self.status_cbk(self.task_id, pickle.dumps(status_data))

    def do_task(self):
        debug("开始执行任务:{},url:{} args:{} ".format(self.task_id, self.url, self.kwargs))
        from ..router import router
        if not self.url.startswith('/'):
            self.url = "/{}".format(self.url)
        route = router.match_rule(self.url)
        if route is None:
            error("无法找到路由:{},运行任务失败".format(self.url))
            self.result = router.fail_msg("无法找到路由{}".format(self.url))
            self.do_result_cbk()
            return
        handler = route.get('handler')
        self.result = handler(**self.kwargs)
        debug("跑完返回 {} :{}".format(self.url, self.result))
        self.do_result_cbk()
