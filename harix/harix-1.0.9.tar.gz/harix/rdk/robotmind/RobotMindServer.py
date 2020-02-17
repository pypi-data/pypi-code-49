#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
接受Robot通知服务
"""
from harix.rdk.proto.robot_mind import robotskill_pb2_grpc
from concurrent import futures
from harix.rdk.robotmind.RobotMindService import RobotMindService
import grpc


class RobotMindServer(object):

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
        robotskill_pb2_grpc.add_RobotSkillServiceServicer_to_server(RobotMindService(self.callback), server)
        server.add_insecure_port(self.host_port)
        server.start()
        print("robot mind server start")
        server.wait_for_termination()
        print("terminate")