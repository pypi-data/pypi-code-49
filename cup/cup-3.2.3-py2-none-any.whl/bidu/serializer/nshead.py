#!/usr/bin/env python
# -*- coding: utf-8 -*
# #############################################################
#
#  Copyright (c) Baidu.com, Inc. All Rights Reserved
#
# #############################################################

"""
:author:
    Guannan Ma @mythmgn
    lishoujun 2019
"""
import cup
import socket
import time
import struct


from cup import err
# from cup import unittest
HEADER_LEN = 36  # 2*short + 4*int + 1*char*16 = 36


class NsheadError(err.BaseCupException):
    """
    Nshead类用到的Error
    """
    def __init__(self, msg):
        super(NsheadError, self).__init__(msg)


class Nshead(object):
    """
    Nshead类，封装了Nshead的各类操作.用法如下
    ::
        from __future__ import print_function
        from cup.bidu.serializer import nshead
        from cup import unittest
        head = nshead.Nshead(
            {
                'id': 888,
                'version': 2,
                'log_id': 111,
                'provider': 'cup-cup',
                'magic_num': 0xfb709394,
                'reserved': 0,
                'body_len': 99999
            }
        )
        binary = head.dump()
        print(binary)
        head2 = Nshead()
        head2.load_from_binary(binary)
        binary2 = head2.dump()
        unittest.assert_eq(binary, binary2)
    """
    __FORMAT = 'HHI16sIII'
    __MAGIC_NUM = 0xfb709394

    def __init__(self, dict_head=None):
        """
        :param dict_head:
            用来初始化的数据的dict, 如果dict_head不设置

            后续请使用load_from_binary函数载入数据
        """
        self.__inited = False
        self.__head = {}
        self._struct_obj = struct.Struct(self.__FORMAT)
        if dict_head is None:
            pass
        else:
            assert type(dict_head) == dict, 'head should be None or a dict'

            self.__head['id'] = dict_head.get('id', 0)
            self.__head['version'] = dict_head.get('version', 0)
            self.__head['log_id'] = dict_head.get('log_id', 0)
            self.__head['provider'] = dict_head.get('provider', 'pynshead')
            self.__head['reserved'] = dict_head.get('reserved', 0)
            self.__head['body_len'] = dict_head.get('body_len', 0)
            self.__head['magic_num'] = self.__MAGIC_NUM
            self.__inited = True

    def load_from_binary(self, binary_data):
        """
        从序列化后的二进制读取数据来进行该类的object设置.
        如果读取失败，会raise NsheadError

        """
        self.__head['id'], self.__head['version'], self.__head['log_id'], \
            self.__head['provider'], self.__head['magic_num'], \
            self.__head['reserved'], self.__head['body_len'] = \
            self._struct_obj.unpack(binary_data)
        if self.__head['magic_num'] != self.__MAGIC_NUM:
            raise NsheadError(
                'magic_num is wrong. Shoule be %s' % str(self.__MAGIC_NUM)
            )
        else:
            self.__inited = True

    def get_dict(self):
        """
        获得ns_head dict的数据, 请不要直接修改该回返dict
        """
        return self.__head

    def dump(self):
        """
        将该nshead进行序列化并回返序列化后的数据, 如果序列化失败会
        raise NsheadError
        """
        if self.__inited:
            return self._struct_obj.pack(
                self.__head['id'], self.__head['version'],
                self.__head['log_id'], self.__head['provider'],
                self.__head['magic_num'], self.__head['reserved'],
                self.__head['body_len']
            )
        else:
            raise NsheadError('Has not initialized yet.')

    def nshead_write(self, sock, info, log_id=0):
        """
        send nshead data by socket

        :param sock:
            sock info like:
            Server = ("127.0.0.1", 8080)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(Server)

        :param info:
            message to send

        :param log_id:
            a 32bit log id

        :return：
            size of sent data

        :raise:
            raise cup.err.NetException when socket connection broken
        """
        body_len = len(info)
        self.__init__({'provider': 'pythonclient',
                       'log_id': log_id, 'body_len': body_len})
        send_nshead_info = self.dump()
        msglen = len(send_nshead_info + info)
        totalsent = 0
        while totalsent < msglen:
            sent = sock.send(send_nshead_info + info[totalsent:])
            if sent == 0:
                raise cup.err.NetException('socket connection broken')
            totalsent = totalsent + sent
        return totalsent

    def nshead_read(self, sock):
        """
        read nshead data from socket

        :param sock:
            sock info like:
            Server = ("127.0.0.1", 8080)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(Server)

        :return：
            data read from socket

        :raise:
            raise cup.err.NetException when socket connection broken
        """
        msg = ''
        info = sock.recv(HEADER_LEN)
        if info == '':
            raise cup.err.NetException('socket connection broken')
        self.load_from_binary(info)
        body_len = self.get_dict()['body_len']
        while(len(msg) < body_len):
            recever_buf = sock.recv(body_len)
            if recever_buf == '':
                raise cup.err.NetException('socket connection broken')
            msg = msg + recever_buf
        return msg

    def put(self, HOSTNAME, PORT, send_pack, logid=int(time.time())):
        """
        quick request nshead use hostname port and data.

        :param
            HOSTNAME: '127.0.0.1'
            PORT: 80
            send_pack: '{"data":"something"}'
            logid: 20191019

        :return：
            data read from server

        :raise:
            raise NsheadError if any exception happen
        """
        try:
            _sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            _sock.settimeout(10)
            _sock.connect((HOSTNAME, PORT))

            self.nshead_write(_sock, send_pack, logid)
            response = self.nshead_read(_sock)
            _sock.close()
        except socket.error as e:
            err_msg = e
            _sock.close()
            raise NsheadError(err_msg)
        return response


def nshead_write(sock, info, log_id=0):
    """
    send nshead data by socket

    :param sock:
        sock info like:
        Server = ("127.0.0.1", 8080)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(Server)

    :param info:
        message to send

    :param log_id:
        a 32bit log id

    :return：
        size of sent data

    :raise:
        raise RuntimeError when socket connection broken
    """
    body_len = len(info)
    send_nshead = Nshead({'provider': 'pythonclient',
                          'log_id': log_id, 'body_len': body_len})
    send_nshead_info = send_nshead.dump()
    msglen = len(send_nshead_info + info)
    totalsent = 0
    while totalsent < msglen:
        sent = sock.send(send_nshead_info + info[totalsent:])
        if sent == 0:
            raise RuntimeError('socket connection broken')
        totalsent = totalsent + sent
    return totalsent


def nshead_read(sock):
    """
    read nshead data from socket

    :param sock:
        sock info like:
        Server = ("127.0.0.1", 8080)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(Server)

    :return：
        data read from socket

    :raise:
        raise RuntimeError when socket connection broken
    """
    msg = ''
    info = sock.recv(HEADER_LEN)
    if info == '':
        raise RuntimeError('socket connection broken')
    receive_nshead = Nshead()
    receive_nshead.load_from_binary(info)
    body_len = receive_nshead.get_dict()['body_len']
    while(len(msg) < body_len):
        recever_buf = sock.recv(body_len)
        if recever_buf == '':
            raise RuntimeError('socket connection broken')
        msg = msg + recever_buf
    return msg

# if __name__ == '__main__':
#     head = Nshead(
#         {
#             'id': 888,
#             'version': 2,
#             'log_id': 111,
#             'provider': 'cup-cup',
#             'magic_num': 0xfb709394,
#             'reserved': 0,
#             'body_len': 99999
#         }
#     )
#     binary = head.dump()
#     head2 = Nshead()
#     head2.load_from_binary(binary)
#     binary2 = head2.dump()
#     unittest.assert_eq(binary, binary2)
