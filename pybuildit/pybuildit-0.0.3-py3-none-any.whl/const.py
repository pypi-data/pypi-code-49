#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

MSG_MARK = 0xabccba

MSG_HEADER_SIZE = 8

ACK_BIT = 0b10000000

MSG_TYPE_IDX = 5

DEVICE_ID_DEFAULT = 1
DEVICE_ID_MAX     = 127

MAX_REF_VELOCITY = 5000
MIN_REF_VELOCITY = -5000
MAX_REF_CURRENT = 4000
MIN_REF_CURRENT = -4000


MCP_SUCCESS                        = 0x00
MCP_INVALID_FORMAT                 = 0x01
MCP_INVALID_CRC                    = 0x02
MCP_INVALID_COMMAND_PAYLOAD_SIZE   = 0x03
MCP_INVALID_MSG_TYPE               = 0x04
MCP_INVALID_COMMAND_PAYLOAD        = 0x05
MCP_INVALID_OPERATION              = 0x06
MCP_INVALID_MSG_SIZE               = 0x07
MCP_RECV_TIMEOUT                   = 0x08
MCP_OUT_OF_POSITION_LIMIT          = 0x09
MCP_ABS_ENCODER_ERROR              = 0x80
MCP_INC_ENCODER_ERROR              = 0x90
MCP_MOTOR_ERROR                    = 0xa0
MCP_OTHER_ERROR                    = 0xff


MSG_TYPE_QUERY_SERVO_STATUS_CMD = 0x01
MSG_TYPE_GET_LOG_INFO_CMD       = 0x05
MSG_TYPE_GET_LOG_CMD            = 0x06
MSG_TYPE_CLEAR_LOG_CMD          = 0x07
MSG_TYPE_CLEAR_LIFE_LOG_CMD     = 0x09
MSG_TYPE_READY_CMD              = 0x10
MSG_TYPE_FREE_CMD               = 0x11
MSG_TYPE_HOLD_CMD               = 0x12
MSG_TYPE_CLEAR_FAULT_CMD        = 0x13
MSG_TYPE_PROTECTION_STOP_CMD        = 0x14
MSG_TYPE_SET_REF_CURRENT_CMD    = 0x20
MSG_TYPE_GET_REF_CURRENT_CMD    = 0x21
MSG_TYPE_SET_REF_VELOCITY_CMD   = 0x22
MSG_TYPE_GET_REF_VELOCITY_CMD   = 0x23
MSG_TYPE_SET_REF_POSITION_CMD   = 0x24
MSG_TYPE_GET_REF_POSITION_CMD   = 0x25
MSG_TYPE_SET_PARAM_CMD          = 0x30
MSG_TYPE_GET_PARAM_CMD          = 0x31
MSG_TYPE_RESET_ROTATION_CMD     = 0x32
MSG_TYPE_RESET_CMD              = 0x3c
MSG_TYPE_FAULT_CMD              = 0x3d
MSG_TYPE_DEBUG_CMD              = 0x3f
MSG_TYPE_WRONG_CMD              = 0x7f
MSG_TYPE_NACK                   = 0xff

PARAM_ID_CURRENT_KP           = 0x10
PARAM_ID_CURRENT_KI           = 0x11
PARAM_ID_CURRENT_MAX_ITERM    = 0x12
PARAM_ID_CURRENT_MIN_ITERM    = 0x13
PARAM_ID_CURRENT_MAX_LIMIT    = 0x14
PARAM_ID_CURRENT_MIN_LIMIT    = 0x15

PARAM_ID_VELOCITY_KP          = 0x20
PARAM_ID_VELOCITY_KI          = 0x21
PARAM_ID_VELOCITY_KD          = 0x22
PARAM_ID_VELOCITY_MAX_ITERM   = 0x23
PARAM_ID_VELOCITY_MIN_ITERM   = 0x24
PARAM_ID_VELOCITY_MAX_LIMIT   = 0x25
PARAM_ID_VELOCITY_MIN_LIMIT   = 0x26

PARAM_ID_POSITION_KP          = 0x30
PARAM_ID_POSITION_KI          = 0x31
PARAM_ID_POSITION_KD          = 0x32
PARAM_ID_POSITION_MAX_ITERM   = 0x33
PARAM_ID_POSITION_MIN_ITERM   = 0x34
PARAM_ID_POSITION_MAX_LIMIT   = 0x35
PARAM_ID_POSITION_MIN_LIMIT   = 0x36
PARAM_ID_POSITION_OFFSET      = 0x3a

PARAM_ID_DEVICE_ID            = 0x80
PARAM_ID_FIRMWARE_VERSION     = 0x81
PARAM_ID_POWER_ON_TIME        = 0x82

PARAM_ID_CALIBRATION          = 0xa0
PARAM_ID_POSITION_SYS_OFFSET  = 0xa1

PARAM_ID_PROTECTION_STOP_PIN_TIMEOUT     = 0xd0
PARAM_ID_STOP_CONTROL_ERROR_THRESHOLD    = 0xd1


STATE_HOLD = 0
STATE_FREE = 1
STATE_READY = 2
STATE_CURRENT_SERVO = 3
STATE_VELOCITY_SERVO = 4
STATE_POSITION_SERVO = 5
STATE_PROTECTION_STOPPING = 12
STATE_PROTECTION_STOP     = 13
STATE_FAULT_FREE = 14
STATE_FAULT_HOLD = 15
STATE_UNKNOWN = 16


SERVO_FAULT_FOC_DURATION = 0x0001
SERVO_FAULT_OVER_VOLT    = 0x0002
SERVO_FAULT_UNDER_VOLT   = 0x0004
SERVO_FAULT_OVER_TEMP    = 0x0008
SERVO_FAULT_OVER_POSITION_LIMIT  = 0x0010
SERVO_FAULT_BREAK_IN     = 0x0040
SERVO_FAULT_STOP_CONTROL_ERROR   = 0x0100
SERVO_FAULT_STOP_TIMEOUT = 0x0200
SERVO_FAULT_EXTERNAL     = 0x0800


QSSR_IDX_POS = 0
QSSR_IDX_VEL = 1
QSSR_IDX_CUR = 2
QSSR_IDX_REF = 3
QSSR_IDX_TEMP = 4
QSSR_IDX_FAULTS = 5


def state2str(s):
    """状態IDを文字列に変換する"""
    if s == STATE_HOLD:
        return "STATE_HOLD"
    elif s == STATE_FREE:
        return "STATE_FREE"
    elif s == STATE_READY:
        return "STATE_READY"
    elif s == STATE_CURRENT_SERVO:
        return "STATE_CURRENT_SERVO"
    elif s == STATE_FAULT_FREE:
        return "STATE_FAULT_FREE"
    elif s == STATE_FAULT_HOLD:
        return "STATE_FAULT_HOLD"
    elif s == STATE_VELOCITY_SERVO:
        return "STATE_VELOCITY_SERVO"
    elif s == STATE_POSITION_SERVO:
        return "STATE_POSITION_SERVO"
    elif s == STATE_PROTECTION_STOPPING:
        return "STATE_PROTECTION_STOPPING"
    elif s == STATE_PROTECTION_STOP:
        return "STATE_PROTECTION_STOP"
    else:
        return "STATE_UNKNOWN"


def faults2str(s):
    """フォルト情報を文字列に変換する"""
    ret = []
    if s & SERVO_FAULT_FOC_DURATION:
        ret.append("SERVO_FAULT_FOC_DURATION")
    if s & SERVO_FAULT_OVER_VOLT   :
        ret.append("SERVO_FAULT_OVER_VOLT")
    if s & SERVO_FAULT_UNDER_VOLT  :
        ret.append("SERVO_FAULT_UNDER_VOLT")
    if s & SERVO_FAULT_OVER_TEMP   :
        ret.append("SERVO_FAULT_OVER_TEMP")
    if s & SERVO_FAULT_OVER_POSITION_LIMIT   :
        ret.append("SERVO_FAULT_OVER_POSITION_LIMIT")
    if s & SERVO_FAULT_STOP_TIMEOUT  :
        ret.append("SERVO_FAULT_STOP_TIMEOUT")
    if s & SERVO_FAULT_BREAK_IN    :
        ret.append("SERVO_FAULT_BREAK_IN")
    if s & SERVO_FAULT_STOP_CONTROL_ERROR    :
        ret.append("SERVO_FAULT_STOP_CONTROL_ERROR")
    if s & SERVO_FAULT_EXTERNAL    :
        ret.append("SERVO_FAULT_EXTERNAL")

    if len(ret) == 0:
        return "NO_FAULTS"
    else:
        return ", ".join(ret)


def paramid2str(s):
    if s == PARAM_ID_CURRENT_KP                   :
        return "PARAM_ID_CURRENT_KP"
    elif s == PARAM_ID_CURRENT_KI                   :
        return "PARAM_ID_CURRENT_KI"
    elif s == PARAM_ID_CURRENT_MAX_ITERM            :
        return "PARAM_ID_CURRENT_MAX_ITERM"
    elif s == PARAM_ID_CURRENT_MIN_ITERM            :
        return "PARAM_ID_CURRENT_MIN_ITERM"
    elif s == PARAM_ID_CURRENT_MAX_LIMIT            :
        return "PARAM_ID_CURRENT_MAX_LIMIT"
    elif s == PARAM_ID_CURRENT_MIN_LIMIT            :
        return "PARAM_ID_CURRENT_MIN_LIMIT"
    elif s == PARAM_ID_VELOCITY_KP                  :
        return "PARAM_ID_VELOCITY_KP"
    elif s == PARAM_ID_VELOCITY_KI                  :
        return "PARAM_ID_VELOCITY_KI"
    elif s == PARAM_ID_VELOCITY_KD                  :
        return "PARAM_ID_VELOCITY_KD"
    elif s == PARAM_ID_VELOCITY_MAX_ITERM           :
        return "PARAM_ID_VELOCITY_MAX_ITERM"
    elif s == PARAM_ID_VELOCITY_MIN_ITERM           :
        return "PARAM_ID_VELOCITY_MIN_ITERM"
    elif s == PARAM_ID_VELOCITY_MAX_LIMIT           :
        return "PARAM_ID_VELOCITY_MAX_LIMIT"
    elif s == PARAM_ID_VELOCITY_MIN_LIMIT           :
        return "PARAM_ID_VELOCITY_MIN_LIMIT"
    elif s == PARAM_ID_POSITION_KP                  :
        return "PARAM_ID_POSITION_KP"
    elif s == PARAM_ID_POSITION_KI                  :
        return "PARAM_ID_POSITION_KI"
    elif s == PARAM_ID_POSITION_KD                  :
        return "PARAM_ID_POSITION_KD"
    elif s == PARAM_ID_POSITION_MAX_ITERM           :
        return "PARAM_ID_POSITION_MAX_ITERM"
    elif s == PARAM_ID_POSITION_MIN_ITERM           :
        return "PARAM_ID_POSITION_MIN_ITERM"
    elif s == PARAM_ID_POSITION_MAX_LIMIT           :
        return "PARAM_ID_POSITION_MAX_LIMIT"
    elif s == PARAM_ID_POSITION_MIN_LIMIT           :
        return "PARAM_ID_POSITION_MIN_LIMIT"
    elif s == PARAM_ID_POSITION_OFFSET              :
        return "PARAM_ID_POSITION_OFFSET"
    elif s == PARAM_ID_DEVICE_ID                    :
        return "PARAM_ID_DEVICE_ID"
    elif s == PARAM_ID_FIRMWARE_VERSION             :
        return "PARAM_ID_FIRMWARE_VERSION"
    elif s == PARAM_ID_POWER_ON_TIME                :
        return "PARAM_ID_POWER_ON_TIME"
    elif s == PARAM_ID_CALIBRATION                  :
        return "PARAM_ID_CALIBRATION"
    elif s == PARAM_ID_POSITION_SYS_OFFSET          :
        return "PARAM_ID_POSITION_SYS_OFFSET"
    elif s == PARAM_ID_PROTECTION_STOP_PIN_TIMEOUT  :
        return "PARAM_ID_PROTECTION_STOP_PIN_TIMEOUT"
    elif s == PARAM_ID_STOP_CONTROL_ERROR_THRESHOLD :
        return "PARAM_ID_STOP_CONTROL_ERROR_THRESHOLD"
    else:
        return "PARAM_ID_UNKNOWN"
