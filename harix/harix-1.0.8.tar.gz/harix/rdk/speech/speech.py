#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
语音识别接口
"""

import grpc
from harix.rdk.proto.speech import enableSpeech_pb2_grpc, enableSpeech_pb2
from harix.rdk.tools import tools


class AsrSubscribe(object):

    def __init__(self, grpc_url,authority):
        """
        初始化方法

        :param grpc_url: gRPC服务器地址
        """
        print("AsrSubscribe init--")
        self.grpc_url = grpc_url
        channel = grpc.insecure_channel(grpc_url, options=[('grpc.default_authority', authority)])
        self.stub = enableSpeech_pb2_grpc.EnableSpeechStub(channel)

    def subscribe_asr(self, header, request):
        """
        订阅asr

        :param request: 参数
        :param header: robot基本信息
        :return:
        """

        common_req_info = tools.convert_header(header)
        enable_request = enableSpeech_pb2.EnableRequest(
            common_req_info=common_req_info,
            sub_type=request["sub_type"],
            enable=request["enable"],
            sub_addr=request["sub_addr"]
        )
        res_data = self.stub.enable(enable_request)
        return res_data



