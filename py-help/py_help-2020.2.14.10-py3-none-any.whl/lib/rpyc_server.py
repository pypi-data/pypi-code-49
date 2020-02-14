# -*- coding: utf-8 -*-
import rpyc
import sys
import os
from rpyc.utils.server import ThreadedServer
from .CommonLogger import debug, info, warn, error
import json
from ..cli.router import DAEMON_PORT, DAEMON_SET_FILE


class RpycServer(rpyc.Service):
    is_import_controller = False

    def on_connect(self, *args):
        info("connect~!")
        # code that runs when a connection is created
        # (to init the serivce, if needed)
        pass

    def on_disconnect(self, *args):
        # code that runs when the connection has already closed
        # (to finalize the service, if needed)
        pass

    # 对于服务端来说， 只有以"exposed_"打头的方法才能被客户端调用，所以要提供给客户端的方法都得加"exposed_"
    def exposed_run_the_cmd(self, argv_hash_str, the_stderr=None):
        import importlib
        # 这里搞一波动态加载,否则貌似会创建错误的类
        argv_hash = json.loads(argv_hash_str)
        class_name = argv_hash.get('class_name', 'py_help.cli.router.Router')
        argv = argv_hash.get('argv', [])
        class_arr = class_name.split('.')
        class_name = class_arr[-1]
        module_name = '.'.join(class_arr[0:-1])
        info("module_name:{},class_name:{}".format(module_name, class_name))
        the_module = importlib.import_module(module_name)
        router = getattr(the_module, class_name)
        info("class_name:{},router:{}".format(class_name, router))
        router.is_run_in_daemon = True
        old_std_out = sys.stdout
        old_std_err = sys.stderr
        if the_stderr is not None:
            sys.stderr = the_stderr
        ret = router().run_orig(argv, False)
        sys.stdout = old_std_out
        sys.stderr = old_std_err
        return json.dumps(ret)


def run_service():
    debug("start rpyc service set daemon  pid:{}".format(os.getpid()))
    with open(DAEMON_SET_FILE, 'w') as fp:
        fp.write("{}".format(os.getpid()))
        fp.flush()
    the_server = ThreadedServer(RpycServer, port=DAEMON_PORT, hostname="localhost", auto_register=False)
    the_server.start()
