# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     dubbo
   Description :
   Author :       zhangfujun
   date：          2020/2/12
-------------------------------------------------
   Change Activity:
                   2020/2/12:
-------------------------------------------------
"""
__author__ = 'zhangfujun'


import socket
import telnetlib


class Dubbo(telnetlib.Telnet):
    prompt = 'dubbo>'
    coding = 'utf-8'

    def __init__(self, host=None, port=0,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        super().__init__(host, port)
        self.write(b"\n")

    def command(self, flag, str_=""):
        data = self.read_until(flag.encode())
        self.write(str_.encode() + b"\n")
        return data

    def invoke(self, service_name, method_name, arg):
        command_str = "invoke {0}.{1}{2}".format(
            service_name, method_name, arg)  # 这个地方的arg不能写成json.dumps(arg)，即不能转换成string型，提高复用性，在调2个或2个以上的接口的方法的参数时
        self.command(Dubbo.prompt, command_str)
        data = self.command(Dubbo.prompt, "")
        data = data.decode(Dubbo.coding, errors='ignore').split('\n')[0].strip()
        return data

    def test(self, conn,interface,method, data):
        result = conn.invoke(interface, method, data)
        return result
