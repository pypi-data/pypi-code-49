#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
语音识别接口
"""

import grpc
from harix.rdk.proto.vision import enableVision_pb2, enableVision_pb2_grpc
from harix.rdk.tools import tools


class VisionSubscribe(object):

    def __init__(self, grpc_url, authority):
        """
        初始化方法

        :param grpc_url: gRPC服务器地址
        """
        print("VisionSubscribe init--")
        self.grpc_url = grpc_url
        channel = grpc.insecure_channel(grpc_url,
                                        options=[('grpc.default_authority', authority)])
        self.stub = enableVision_pb2_grpc.EnableVisionStub(channel)

    def subscribe_vision(self, header, request):
        """
        订阅vision

        :param request: 参数
        :param header: robot基本信息
        :return:
        """
        common_req_info = tools.convert_header(header)
        enable_request = enableVision_pb2.EnableRequest(
            common_req_info=common_req_info,
            sub_type=request["sub_type"],
            enable=request["enable"],
            sub_addr=request["sub_addr"]
        )

        if "faceset_id" in request:
            enable_request.faceset_id = request["faceset_id"]

        res_data = self.stub.enable(enable_request)
        return res_data





