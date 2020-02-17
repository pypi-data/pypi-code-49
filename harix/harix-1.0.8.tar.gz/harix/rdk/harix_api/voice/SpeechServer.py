#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
接受ASR语音文字数据的服务
"""
from harix.rdk.proto.serviceapp import recognizeSpeech_pb2_grpc
from concurrent import futures
from harix.rdk.harix_api.voice.SpeechService import SpeechService
import grpc


class SpeechServer(object):

    def __init__(self, host_port, callback):
        """
        初始化方法

        :param host_port: gRPC服务器地址
        :param callback: 反馈函数
        """
        self.callback = callback
        self.host_port = host_port

    def StartServer(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        recognizeSpeech_pb2_grpc.add_SpeechServicer_to_server(SpeechService(self.callback), server)
        server.add_insecure_port(self.host_port)
        server.start()
        print("speech server start")
        server.wait_for_termination()
        print("terminate")












