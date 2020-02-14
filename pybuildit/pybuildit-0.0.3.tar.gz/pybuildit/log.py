#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import struct
from pybuildit.const import *

LOG_RECORED_BYTE_SIZE             = 16
GET_LOG_CMD_MAX_LOG_RECORED_SIZE  = 10

LOG_LEVEL_FATAL = 0x01
LOG_LEVEL_ERROR = 0x02
LOG_LEVEL_WARN  = 0x03
LOG_LEVEL_INFO  = 0x04

LOG_GROUP_SYSTEM                         = 0x01
LOG_GROUP_HANDLE_CMD                     = 0x04
LOG_GROUP_NACK                           = 0x05
LOG_GROUP_DOMAIN_BLDC_MOTOR_CONTROL      = 0x10
LOG_GROUP_DOMAIN_MCP_SERVER              = 0x14

LOG_SUB_GROUP_SYSTEM_POWER_ON            = 0x01
LOG_SUB_GROUP_SYSTEM_START_UP            = 0x02
LOG_SUB_GROUP_SYSTEM_ERROR               = 0x10
LOG_SUB_GROUP_SYSTEM_ASSERT              = 0x11
LOG_SUB_GROUP_BLDC_FAULT                 = 0x01
LOG_SUB_GROUP_BLDC_PROTECTION_STOP       = 0x02
LOG_SUB_GROUP_MCP_SERVER_UNNOTIFIED_ERROR = 0x01

LOG_RECORD_INFO_BYTE_SIZE   = 16
LOG_RECORD_BYTE_SIZE        = 16
LOG_RECORD_PAYLOAD_SIZE     = 8

def _err2str(e):
    """
    Builditユーザーマニュアルに記載されているエラーIDを引数に取り、文字列を返す関数
    """
    if e == MCP_SUCCESS:
        return "success"
    elif e == MCP_INVALID_FORMAT                :
        return "invalid_format"
    elif e == MCP_INVALID_CRC                   :
        return "invalid_crc"
    elif e == MCP_INVALID_COMMAND_PAYLOAD_SIZE  :
        return "invalid_command_payload_size"
    elif e == MCP_INVALID_MSG_TYPE              :
        return "invalid_msg_type"
    elif e == MCP_INVALID_COMMAND_PAYLOAD       :
        return "invalid_command_payload"
    elif e == MCP_INVALID_OPERATION             :
        return "invalid_operation"
    elif e == MCP_INVALID_MSG_SIZE              :
        return "invalid_msg_size"
    elif e == MCP_RECV_TIMEOUT                  :
        return "timeout"
    elif e == MCP_OUT_OF_POSITION_LIMIT         :
        return "out_of_position_limit"
    elif e == MCP_ABS_ENCODER_ERROR             :
        return "abs_encoder_error"
    elif e == MCP_INC_ENCODER_ERROR             :
        return "inc_encoder_error"
    elif e == MCP_MOTOR_ERROR                   :
        return "motor_error"
    elif e == MCP_OTHER_ERROR                   :
        return "other_error"
    else:
        return "unknown"


def _cmd2str(c):
    """
    Builditユーザーマニュアルに記載されているメッセージタイプIDを引数に取り、文字列を返す関数
    """

    if c == MSG_TYPE_QUERY_SERVO_STATUS_CMD :
        return "query_servo_status"
    elif c == MSG_TYPE_READY_CMD              :
        return "ready"
    elif c == MSG_TYPE_FREE_CMD               :
        return "free"
    elif c == MSG_TYPE_HOLD_CMD               :
        return "hold"
    elif c == MSG_TYPE_CLEAR_FAULT_CMD        :
        return "clear_fault"
    elif c == MSG_TYPE_PROTECTION_STOP_CMD    :
        return "protection_stop"
    elif c == MSG_TYPE_SET_REF_CURRENT_CMD    :
        return "set_ref_current"
    elif c == MSG_TYPE_GET_REF_CURRENT_CMD    :
        return "get_ref_current"
    elif c == MSG_TYPE_SET_REF_VELOCITY_CMD   :
        return "set_ref_velocity"
    elif c == MSG_TYPE_GET_REF_VELOCITY_CMD   :
        return "get_ref_velocity"
    elif c == MSG_TYPE_SET_REF_POSITION_CMD   :
        return "set_ref_position"
    elif c == MSG_TYPE_GET_REF_POSITION_CMD   :
        return "get_ref_position"
    elif c == MSG_TYPE_RESET_ROTATION_CMD     :
        return "reset_rotation"
    elif c == MSG_TYPE_SET_PARAM_CMD          :
        return "set_param"
    elif c == MSG_TYPE_GET_PARAM_CMD          :
        return "get_param"
    elif c == MSG_TYPE_RESET_CMD              :
        return "reset"
    elif c == MSG_TYPE_FAULT_CMD              :
        return "fault"
    elif c == MSG_TYPE_DEBUG_CMD              :
        return "debug"
    elif c == MSG_TYPE_GET_LOG_INFO_CMD       :
        return "get_log_info"
    elif c == MSG_TYPE_GET_LOG_CMD            :
        return "get_log"
    elif c == MSG_TYPE_CLEAR_LOG_CMD          :
        return "clear_log"
    else:
        return "unknown(" + hex(c) + ")"


def log_level2str(lv):
    """
    ログレベルを受け取り、文字列を返す
    """
    if lv == LOG_LEVEL_FATAL:
        return "FATAL"
    elif lv == LOG_LEVEL_ERROR :
        return "ERROR"
    elif lv == LOG_LEVEL_WARN  :
        return "WARN"
    elif lv == LOG_LEVEL_INFO  :
        return "INFO"
    else:
        return "UNKNOWN"

def log_record2str(lv, g, sg, c, payload):
    """
    ログレコードを受け取り、文字列を返す
    """


    s0 = hex(g)
    s1 = hex(sg)
    s2 = hex(c)
    s3 = "[" + " ".join(['0x{:02x}'.format(c) for c in payload]) + "]"

    if g == LOG_GROUP_SYSTEM                           :
        s = "system"
        if sg == LOG_SUB_GROUP_SYSTEM_POWER_ON            :
            return (s, "power_on", s2, s3)
        elif sg == LOG_SUB_GROUP_SYSTEM_START_UP            :
            return (s, "start_up", s2, s3)
        elif sg == LOG_SUB_GROUP_SYSTEM_ERROR               :
            return (s, "error", s2, s3)
        elif sg == LOG_SUB_GROUP_SYSTEM_ASSERT              :
            if lv == LOG_LEVEL_FATAL:
                hd = struct.unpack('<6sH', payload)
                filename = hd[0].decode('ascii')
                fileline = hd[1]
                ext = "(.c)" if c == 0 else "(.h)"
                return (s, "assert", s2, "file:" + filename + ext + ", line:" + str(fileline))
            else:
                return (s, "assert", s2, s3)
        else:
            return (s, s1, s2, s3)
    elif g == LOG_GROUP_HANDLE_CMD                     :
        return ("cmd_handler", 'cmd_' + _cmd2str(sg), s2, s3)
    elif g == LOG_GROUP_NACK                     :
        return ("nack", "-", _err2str(c), s3)
    elif g == LOG_GROUP_DOMAIN_BLDC_MOTOR_CONTROL      :
        s = "domain_bldcmc"
        if sg == LOG_SUB_GROUP_BLDC_FAULT                 :
            faults = struct.unpack('<H', payload[0:2])[0]
            return (s, "bldc_fault", "-", faults2str(faults))
        elif sg == LOG_SUB_GROUP_BLDC_PROTECTION_STOP       :
            return (s, "bldc_protection_stop", s2, s3)
        else:
            return (s, s1, s2, s3)
    elif g == LOG_GROUP_DOMAIN_MCP_SERVER              :
        if sg == LOG_SUB_GROUP_MCP_SERVER_UNNOTIFIED_ERROR:
            return ("domain_mcp_server", "unnotified_error", _err2str(c), s3)
        return ("domain_mcp_server", s1, s2, s3)
    else:
        return (s0, s1, s2, s3)
