# -*- coding: utf-8 -*-
import inspect
from typing import Dict, List, Tuple

from .grpc_client import MRCEngineGRPCClient
from .models import MRCEngineException

__all__ = [
    "init_service",
    "MRCEngineException",
    "ocr_result_classify",
    "ocr_result_matching",
]
_client: MRCEngineGRPCClient


def _param_check(func):
    def wrapper(*args, **kwargs):
        global _client
        assert _client is not None, "ocr engine sdk must be init first"
        sig = inspect.signature(func)
        params = list(sig.parameters.values())
        for i, v in enumerate(args):
            p = params[i]
            assert p.annotation is inspect.Parameter.empty or isinstance(v, p.annotation), "{} must be {}.".format(p.name, str(p.annotation))
        return func(*args, **kwargs)
    return wrapper


def init_service(endpoint: str, src: str) -> None:
    global _client
    assert type(endpoint) == str, "endpoint must be a str"
    _client = MRCEngineGRPCClient(endpoint=endpoint, src=src)


@_param_check
def ocr_result_classify(ocr_result: str, hospital: str = "") -> Tuple[str, int, str]:
    return _client.ocr_result_classify(ocr_result, hospital)


@_param_check
def ocr_result_matching(ocr_result: str, hospital: str = "", doc_type: int = 0, doc_sub_type: str = "", fields: List = []) -> Tuple[Dict[str, str], Dict]:
    return _client.ocr_result_matching(ocr_result, hospital, doc_type, doc_sub_type, fields)
