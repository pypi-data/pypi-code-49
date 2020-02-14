# -*- coding: utf-8 -*-
from contextlib import contextmanager

import grpc
from google.protobuf.any_pb2 import Any

from . import common_pb2 as c_pb
from . import models as md
from . import ocrEngine_pb2 as o_pb
from . import ocrEngine_pb2_grpc as o_grpc


class OcrEngineGRPCClient(object):

    def __init__(self, endpoint: str, src: str = ""):
        self._endpoint = endpoint
        self._src = src

    @contextmanager
    def _rpc_stub(self):
        with grpc.insecure_channel(self._endpoint) as channel:
            stub = o_grpc.OCREngineStub(channel)
            try:
                yield stub
            except grpc.RpcError as e:
                raise md.OCREngineException(str(e))

    def _ocr_request(self, ocr_request: o_pb.GetOCRResultRequest):
        with self._rpc_stub() as stub:
            data = Any()
            data.Pack(ocr_request)
            request = c_pb.RequestMessage(src=self._src, data=data)
            response = stub.GetOCRResult(request)
            if response.code != 0:
                raise md.OCREngineException("{} {}".format(str(response.code), response.msg))
            unpacked_msg = o_pb.GetOCRResultResponse()
            response.data.Unpack(unpacked_msg)
            return unpacked_msg.ocr_result

    def ocr_result_with_image_oss_path(self, oss_path: str = None) -> str:
        req = o_pb.GetOCRResultRequest(image_oss_path=oss_path)
        return self._ocr_request(req)

    def ocr_result_with_image_url(self, image_url: str = None) -> str:
        req = o_pb.GetOCRResultRequest(image_url=image_url)
        return self._ocr_request(req)

    def ocr_result_with_image(self, image: bytes = None) -> str:
        req = o_pb.GetOCRResultRequest(image=image)
        return self._ocr_request(req)
