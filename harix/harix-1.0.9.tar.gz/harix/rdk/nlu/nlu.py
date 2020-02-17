#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
自然语言识别接口
"""

import grpc
from harix.rdk.proto.nlu import nlu_pb2, nlu_pb2_grpc
from harix.rdk.tools import tools


class NluService(object):

    def __init__(self, grpc_url, authority):
        """
        初始化方法

        :param grpc_url: gRPC服务器地址
        """
        print("NluService init--")
        self.grpc_url = grpc_url
        # channel = grpc.insecure_channel(grpc_url, options=[('grpc.default_authority', 'harix-skill-nlu.harix-allinone3')])
        channel = grpc.insecure_channel(grpc_url,
                                        options=[('grpc.default_authority', authority)])
        self.stub = nlu_pb2_grpc.NLUStub(channel)

    def nlu_detect(self, header, request):
        """
        自然语言识别

        :param request: 参数
        :param header: robot基本信息
        :return:
        """
        common_req_info = tools.convert_header(header)
        text_request = nlu_pb2.TextRequest(
            common_req_info=common_req_info,
            body=request
        )
        res_data = self.stub.Detect(text_request)
        return res_data







