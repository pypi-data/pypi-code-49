#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
接收vision图片识别的消息
"""
from harix.rdk.proto.serviceapp import recognizeVision_pb2, recognizeVision_pb2_grpc
from harix.rdk.proto.common import common_pb2
import _thread

class VisionService(recognizeVision_pb2_grpc.VisionServicer):

    def __init__(self, callback):
        """
        初始化方法

        :param callback: 反馈函数
        """
        self.callback = callback




    def BeforeRecognize(self, request, context):

        header = {
            "tenant_id": request.common_req_info.tenant_id,
            "user_id": request.common_req_info.user_id,
            "robot_id": request.common_req_info.robot_id,
            "robot_type": request.common_req_info.robot_type,
            "service_code": request.common_req_info.service_code,
            "seq": request.common_req_info.seq
        }

        self.callback(header, request.body)

        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )
        return recognizeVision_pb2.RecognitionResponse(
            common_rsp_info=common_resp_info,
            propose={
                "do_recognize": True
            }
        )

    def CompleteRecognize(self, request, context):

        print("enter CompleteRecognize")
        header = {
            "tenant_id": request.common_req_info.tenant_id,
            "user_id": request.common_req_info.user_id,
            "robot_id": request.common_req_info.robot_id,
            "robot_type": request.common_req_info.robot_type,
            "service_code": request.common_req_info.service_code,
            "seq": request.common_req_info.seq
        }

        return_type = request.WhichOneof("result_oneof")
        print(return_type)
        image_obj = {}
        if return_type == "nothing":
            image_obj = request.nothing
        elif return_type == "ocr":
            image_obj = request.ocr
        elif return_type == "money":
            image_obj = request.Money
        elif return_type == "car_plate":
            image_obj = request.car_plate
        elif return_type == "object":
            image_obj = request.object
        elif return_type == "face":
            image_obj = request.face
        elif return_type == "face_attr":
            image_obj = request.face_attr
        elif return_type == "caption":
            image_obj = request.caption
        elif return_type == "classify":
            image_obj = request.classify
        elif return_type == "fall":
            image_obj = request.fall
        elif return_type == "compare":
            image_obj = request.compare
        elif return_type == "vending":
            image_obj = request.vending

        try:
            _thread.start_new_thread(self.callback, (header, request.image_info, return_type, image_obj))
        except Exception as err:
            print("Error: 无法启动vision callback线程")
            print(err)

        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )

        return recognizeVision_pb2.VisionResponse(
            common_resp_info=common_resp_info,
            nothing="true"
        )

    def OcrEvent(self, request, context):
        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )
        return recognizeVision_pb2.EventResponse(
            common_rsp_info=common_resp_info
        )

    def MoneyEvent(self, request, context):
        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )
        return recognizeVision_pb2.EventResponse(
            common_rsp_info=common_resp_info
        )

    def CarPlateEvent(self, request, context):
        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )
        return recognizeVision_pb2.EventResponse(
            common_rsp_info=common_resp_info
        )

    def ObjectEvent(self, request, context):
        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )
        return recognizeVision_pb2.EventResponse(
            common_rsp_info=common_resp_info
        )

    def FaceEvent(self, request, context):
        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )
        return recognizeVision_pb2.EventResponse(
            common_rsp_info=common_resp_info
        )

    def FaceAttrEvent(self, request, context):
        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )
        return recognizeVision_pb2.EventResponse(
            common_rsp_info=common_resp_info
        )

    def CaptionEvent(self, request, context):
        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )
        return recognizeVision_pb2.EventResponse(
            common_rsp_info=common_resp_info
        )

    def ClassifyEvent (self, request, context):
        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )
        return recognizeVision_pb2.EventResponse(
            common_rsp_info=common_resp_info
        )

    def FallEvent(self, request, context):
        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )
        return recognizeVision_pb2.EventResponse(
            common_rsp_info=common_resp_info
        )

    def CompareEvent(self, request, context):
        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )
        return recognizeVision_pb2.EventResponse(
            common_rsp_info=common_resp_info
        )

    def VendingEvent(self, request, context):
        common_resp_info = common_pb2.CommonRspInfo(
            err_code=0
        )
        return recognizeVision_pb2.EventResponse(
            common_rsp_info=common_resp_info
        )