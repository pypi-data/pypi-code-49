# -*- coding: utf-8 -*-
import os
from py_help.api_help.api_wrapper import Api
from py_help.cli.router import DAEMON_SET_FILE
from .. import debug, info, warn, error


@Api()
def set_daemon(**kwargs):
    """
    @api /py/daemon_run
    @name daemon模式
    @toolable
    @description 启动了daemon模式之后,后续的命令都是daemon模式运行,daemon模式运行执行速度会快很多(少了文件加载的动作)
    @author 王沃伦
    @params
        stop,name:关闭,type:b,required:false,default:false,desc:默认可以不设置这个,不设置就是启动daemon模式,设置了是就是关闭daemon模式
    @example
        usage:set daemon_run --stop,desc:关闭daemon运行
        usage:set daemon_run,desc:启动daemon运行
    @expect 成功|失败|NONE
    """
    is_stop = kwargs.get('stop', False)
    info('是否停止daemon::{stop}'.format(stop=is_stop))
    if is_stop and os.path.exists(DAEMON_SET_FILE):
        import threading
        if os.path.exists(DAEMON_SET_FILE):
            os.remove(DAEMON_SET_FILE)

        def sys_exit():
            import time
            time.sleep(0.2)
            if os.path.exists(DAEMON_SET_FILE):
                os.remove(DAEMON_SET_FILE)
            info("最终退出")
            os._exit(0)

        info('需要启动线程退出了::{stop}'.format(stop=is_stop))
        thr = threading.Thread(target=sys_exit)
        thr.daemon = True
        thr.start()
    else:
        info('set daemon ::{stop}'.format(stop=is_stop))
        if not os.path.exists(DAEMON_SET_FILE):
            with open(DAEMON_SET_FILE, 'w') as fp:
                fp.write("")
                fp.flush()
    return {'exit': 0, 'out': 'success'}
