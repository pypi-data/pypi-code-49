#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
自然语言识别接口
"""

from harix.rdk.proto.common import common_pb2
import time
import uuid


def convert_header(input_header):

    t = time.time()
    timestamp = int(round(t * 1000))
    common_req_info = common_pb2.CommonReqInfo(
        tenant_id=input_header["tenant_id"],
        version="3.0",
        user_id=input_header["user_id"],
        robot_id=input_header["robot_id"],
        robot_type=input_header["robot_type"],
        service_code=input_header["service_code"],
        seq=input_header["seq"],
        guid=str(uuid.uuid4()),
        root_guid=str(uuid.uuid4()),
        timestamp=timestamp,
    )

    if "version" in input_header:
        common_req_info.version = input_header["version"]

    print(common_req_info)




    return common_req_info
