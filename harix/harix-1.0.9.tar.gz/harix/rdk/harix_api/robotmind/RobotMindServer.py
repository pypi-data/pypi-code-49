#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
接受Robot通知服务
"""
from harix.rdk.proto.robot_mind import robotskill_pb2_grpc
from concurrent import futures
from harix.rdk.harix_api.robotmind.RobotMindService import RobotMindService
import grpc


class RobotMindServer(object):

    def __init__(self, host_port, enable_callback, action_callback ):
        """
        初始化方法

        :param host_port: gRPC服务器地址
        :param callback: 反馈函数
        """
        self.enable_callback = enable_callback
        self.action_callback = action_callback
        self.host_port = host_port

    def StartServer(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        robotskill_pb2_grpc.add_RobotSkillServiceServicer_to_server(RobotMindService(self.enable_callback, self.action_callback), server)
        server.add_insecure_port(self.host_port)
        server.start()
        print("robot mind server start")
        server.wait_for_termination()
        print("terminate")