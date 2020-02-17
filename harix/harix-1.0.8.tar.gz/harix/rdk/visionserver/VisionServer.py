#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
接收图片识别后上传的消息
"""
from harix.rdk.proto.serviceapp import recognizeVision_pb2_grpc
from concurrent import futures
from harix.rdk.visionserver.VisionService import VisionService
import grpc

class VisionServer(object):

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
        recognizeVision_pb2_grpc.add_VisionServicer_to_server(VisionService(self.callback), server)
        server.add_insecure_port(self.host_port)
        server.start()
        print("vision server start")
        server.wait_for_termination()
        print("terminate")
