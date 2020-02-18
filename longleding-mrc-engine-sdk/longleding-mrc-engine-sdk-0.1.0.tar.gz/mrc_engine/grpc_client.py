# -*- coding: utf-8 -*-
from contextlib import contextmanager
from typing import Tuple, List, Dict

import grpc
from google.protobuf.any_pb2 import Any
from google.protobuf.json_format import MessageToDict

from . import common_pb2 as c_pb
from . import models as md
from . import mrcEngine_pb2 as m_pb
from . import mrcEngine_pb2_grpc as m_grpc


class MRCEngineGRPCClient(object):

    def __init__(self, endpoint: str, src: str = ""):
        self._endpoint = endpoint
        self._src = src

    @contextmanager
    def _rpc_stub(self):
        with grpc.insecure_channel(self._endpoint) as channel:
            stub = m_grpc.MRCEngineStub(channel)
            try:
                yield stub
            except grpc.RpcError as e:
                raise md.MRCEngineException(str(e))

    def ocr_result_classify(self, ocr_result: str, hospital: str = "") -> Tuple[str, int, str]:
        with self._rpc_stub() as stub:
            data = Any()
            classify_request = m_pb.OCRResultClassifyRequest(ocr_result=ocr_result, hospital=hospital)
            data.Pack(classify_request)
            request = c_pb.RequestMessage(src=self._src, data=data)
            response = stub.OCRResultClassify(request)
            if response.code != 0:
                raise md.MRCEngineException("{} {}".format(str(response.code), response.msg))
            r_msg = m_pb.OCRResultClassifyResponse()
            response.data.Unpack(r_msg)
            return r_msg.hospital, r_msg.doc_type, r_msg.sub_doc_type

    def ocr_result_matching(self, ocr_result: str, hospital: str = "", doc_type: int = 0, sub_doc_type: str = "", fields: List[str] = []) -> Tuple[Dict[str, str], Dict]:
        with self._rpc_stub() as stub:
            data = Any()
            classify_request = m_pb.OCRResultMatchingRequest(
                ocr_result=ocr_result,
                hospital=hospital,
                doc_type=doc_type,
                sub_doc_type=sub_doc_type,
                fields=fields
            )
            data.Pack(classify_request)
            request = c_pb.RequestMessage(src=self._src, data=data)
            response = stub.OCRResultMatching(request)
            if response.code != 0:
                raise md.MRCEngineException("{} {}".format(str(response.code), response.msg))
            r_msg = m_pb.OCRResultMatchingResponse()
            response.data.Unpack(r_msg)
            return r_msg.values, {k: MessageToDict(v) for k, v in r_msg.bounds.items()}
