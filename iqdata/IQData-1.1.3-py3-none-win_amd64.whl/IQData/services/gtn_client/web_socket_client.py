# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c)2018, 恒生电子股份有限公司
# All rights reserved.
#
# 文件名称：WebSocketClinet.py
# 摘    要：面向WebSocket的客户端
#
# 当前版本：V1.0.0
# 作    者：
# 完成日期：2018-12-19
# 备    注：
###############################################################################
import threading

import websocket

# from IQData.utils.logger import system_log

class WSClient(object):
    """
    这个类使用了第三方包websocket
    """
    def __init__(self, url, **kwargs):
        self.ws = websocket.WebSocketApp(url)
        on_open = kwargs.get('on_open', None)
        on_close = kwargs.get('on_close', None)
        on_message = kwargs.get('on_message', None)
        on_error = kwargs.get('on_error', None)
        # 连接成功时调用的函数
        self.ws.on_open = on_open if on_open else lambda ws: system_log.info('#### open ####')
        # 连接关闭时调用的函数
        self.ws.on_close = on_close if on_close else lambda ws: system_log.info('#### close ####')
        # 收到信息时调用的函数
        self.ws.on_message = on_message if on_message else lambda ws, message: system_log.info(message)
        # 连接发送异常时嗲用的函数
        self.ws.on_error = on_error if on_error else lambda ws, error: system_log.error(error)
        # 启动客户端
        self.run()

    def run(self):
        t = threading.Thread(target=self.ws.run_forever)
        t.setDaemon(True)
        t.start()

    def send(self, data):
        self.ws.send(data)


if __name__ == '__main__':
    # 测试websocket
    import time
    # 连接到服务器之后就会触发on_open事件
    def on_open(ws):
        req = '{"event":"subscribe", "channel":"btc_usdt.deep"}'
        # print(req)
        ws.send(req)
    channel = WSClient("wss://i.cg.net/wi/ws", on_open=on_open)
    time.sleep(10)
