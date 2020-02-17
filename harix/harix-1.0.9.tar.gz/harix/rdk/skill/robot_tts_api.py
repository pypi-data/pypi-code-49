#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
语言模块，本模块封装了机器人运动语音相关的类、方法、结构
"""

import grpc
from harix.rdk.proto.robot_skill_api import robot_tts_api_pb2, robot_tts_api_pb2_grpc
from harix.rdk.tools import tools

class RobotTtsService(object):
    """
    语音相关类
    """

    def __init__(self, grpc_url, authority):
        """
        初始化方法

        :param grpc_url: gRPC服务器地址
        """
        print("RobotTtsService init--")
        self.grpc_url = grpc_url
        channel = grpc.insecure_channel(grpc_url, options=[('grpc.default_authority', authority)])
        self.stub = robot_tts_api_pb2_grpc.RobotTtsServiceStub(channel)

    def Speak(self, header, request):
        """
        说一段话

        :param request: 语音相关信息
        :param header: robot基本信息
        :return:
        """

        tts = robot_tts_api_pb2.Tts(text=request["text"], lang=request["lang"])
        request = robot_tts_api_pb2.SpeakRequest(
            common_req_info=tools.convert_header(header),
            tts=[tts]
        )

        res_data = self.stub.Speak(request)
        return res_data
