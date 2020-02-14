# -*- coding: utf-8 -*-
import sys
import os
from .CommonLogger import debug, info, warn, error, get_buffer_data
from ..cli.router import router
import threading
import time

if sys.version_info < (3, 0):
    from Queue import Queue
    from SimpleXMLRPCServer import SimpleXMLRPCServer
    from SocketServer import ThreadingMixIn
else:
    from queue import Queue
    from xmlrpc.server import SimpleXMLRPCServer
    from socketserver import ThreadingMixIn


class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass


class CacheBuffer:
    def __init__(self, msg_queue):
        self.msg_queue = msg_queue

    def write(self, data):
        debug("来写入数据:{}".format(data))
        self.msg_queue.put(data)

    def read(self):
        self.msg_queue.get()


kw_status_match = {
    'return': 2,
    'success': 1,
    'failure': 0,
    'error': -1,
}


class KeywordRunThread(threading.Thread):
    def __init__(self, thread_id, name, kw_data, server):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.kw_data = kw_data
        self.server = server

    def run(self):
        debug("开始启动任务:{} {} kw_data:{}".format(self.thread_id, self.name, self.kw_data))
        try:
            # 调用路由目标，并将返回值打印到控制台，并指定程序的退出码
            handler = self.kw_data['kw_info']['handler']
            time_before = time.time()
            ret = handler(**self.kw_data.get('params'))
            time_after = time.time()
            info('finish, time spend {}s'.format(round(time_after - time_before, 2)))
            debug("call url:{url},ret:{ret}".format(url=self.kw_data['kw_info']['rule'], ret=ret))
            result_arr = None
            if isinstance(ret, dict) and ret.get('exit') is not None and ret.get('out') is not None:
                result_success = ret.get('exit') == 0
                if result_success:
                    act_result = '成功'
                else:
                    act_result = '失败'
                status = kw_status_match['success']
                if act_result != self.kw_data['expected']:
                    status = kw_status_match['failure']
                result_arr = [result_success, {
                    'data': {
                        'value': ret.get('out'),
                        'expected': self.kw_data['expected'],
                        'actual': act_result
                    },
                    'status': status,
                    'archives': {},
                    'logs': []
                }]
            else:
                act_result = '成功'
                result_arr = [act_result == self.kw_data['expected'], {
                    'data': {
                        'value': ret.get('out'),
                        'expected': self.kw_data['expected'],
                        'actual': act_result
                    },
                    'status': kw_status_match['return'],
                    'archives': {},
                    'logs': []
                }]
            self.server.kw_result = result_arr
            return ret
        except Exception as es:
            error("运行关键字出现异常:{}".format(self.name), es)


class XmlRpcServer:
    host_ip = '0.0.0.0'
    port = 8080
    url = '/RPC2'
    kw_result = None

    def __init__(self, host_ip='0.0.0.0', port=8080, url='/RPC2'):
        self.host_ip = host_ip
        self.port = port
        self.url = url
        self.kw_id = 0
        self.result_queue = Queue(1024)
        self.log_queue = Queue(1024)
        self.server_instance = ThreadXMLRPCServer((host_ip, port), allow_none=True)
        self.server_instance.register_instance(self)
        self.home = os.path.expanduser('~')
        self.running_keyword = None

    def _parse_keyword_str(self, kw_str, kw_args):
        kw_arr = kw_str.split(',')
        kw_name = kw_arr[0].replace('[', '').replace(']', '')
        rule_dict = router.get_rule_by_name(kw_name)
        if rule_dict is None:
            msg = "无法找到keyword:{}".format(kw_name)
            warn(msg)
            return None
        else:
            params_info = rule_dict.get('route_info').get('params')
            kw_expected = '成功'
            for one_kw_k in kw_arr:
                if '期望结果:' in one_kw_k:
                    kw_expected = one_kw_k.replace('期望结果:', '').strip()
            key_params = {}
            for one_param_info in params_info:
                if one_param_info.get('name') in kw_args:
                    key_params[one_param_info.get('id')] = kw_args[one_param_info.get('name')]
            return {
                'kw_name': kw_name,
                'params': key_params,
                'expected': kw_expected,
                'kw_info': rule_dict
            }

    def start_server(self):
        self.server_instance.serve_forever()

    def ping(self):
        # debug("来了 ping")
        return 'pong'

    def get_home(self):
        debug("来了 get home {}".format(self.home))
        return self.home

    def realtime_read(self):
        ret_data = {
            "over": False,
            "log": get_buffer_data(),
            "result": self.kw_result
        }
        if self.running_keyword.is_alive():
            debug("关键字还没跑完 {}".format(self.running_keyword.name))
        else:
            info("关键字已经跑完:{}".format(self.running_keyword.name))
            ret_data['over'] = True
        debug("来了 realtime_read 返回的数据是:{}".format(ret_data))
        return ret_data

    def read(self):
        debug("来了 read")
        return ''

    def run_keyword(self, keyword, timeout, kw_args, is_async):
        debug("要运行keyword:【{}】,参数是:{},timeout:{},async:{}".format(keyword, kw_args, timeout, is_async))
        kw_data = self._parse_keyword_str(keyword, kw_args)
        if kw_data is None:
            msg = "无法找到keyword:{}".format(keyword)
            warn(msg)
            return False, msg
        else:
            self.kw_result = None
            self.running_keyword = KeywordRunThread(self.kw_id, "kw_{}_{}".format(keyword, self.kw_id),
                                                    kw_data, self)
            if is_async:
                self.running_keyword.start()
            else:
                self.running_keyword.run()
            return True, "成功启动关键字:【{}】".format(keyword)

    def stop_keyword(self):
        debug("stop keyword")
        pass

    def shutdown(self):
        debug("shutdown")
        self.server_instance.shutdown()
        return 'done'
