#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
import os
import struct
import serial
import crc8
from pybuildit.const import *
from pybuildit.path import *
from pybuildit.log import *
import yaml


def to_deg(rawPosition):
    """位置情報の単位を[360/65536 * 度]から[度]に変換する
    """
    return round(rawPosition * 360.0 / float(0x10000), 2)


def from_deg(deg):
    """位置情報の単位を[度]から[360/65536 * 度]に変換する
    """
    return round(deg / 360.0 * 0x10000)


def to_rpm(rawVelocity):
    """速度情報の単位を[1/100 * rpm]から[rpm]に変換する
    """
    return rawVelocity / float(100)


def from_rpm(rpm):
    """速度情報の単位を[rpm]から[1/100 * rpm]に変換する
    """
    return round(rpm * 100)


def _from_unit_pos(v, unit):
    if unit == "raw":
        return int(v)
    elif unit == "deg":
        return from_deg(v)
    else:
        print("unit", unit)
        raise ValueError(unit)


def _from_unit_vel(v, unit):
    if unit == "raw":
        return int(v)
    elif unit == "rpm":
        return from_rpm(v)
    else:
        print("unit", unit)
        raise ValueError(unit)


def _to_unit_pos(v, unit):
    if unit == "raw":
        return int(v)
    elif unit == "deg":
        return to_deg(v)
    else:
        print("unit", unit)
        raise ValueError(unit)


def _to_unit_vel(v, unit):
    if unit == "raw":
        return int(v)
    elif unit == "rpm":
        return to_rpm(v)
    else:
        print("unit", unit)
        raise ValueError(unit)


class MCPError(Exception):
    """モーター制御プロトコルエラー用例外ベースクラス
    """
    pass


class MCPTransportError(MCPError):
    """通信層でのエラー用例外ベースクラス
    """
    pass


class MCPApplicationError(MCPError):
    """アプリケーション層でのエラー用例外ベースクラス
    """
    pass


class InvalidFormatError(MCPTransportError):
    """不正なメッセージファーマット例外"""
    pass


class InvalidCRCError(MCPTransportError):
    """不正なCRC例外"""
    pass


class UnexpectedMessageTypeError(MCPTransportError):
    """予想外のメッセージタイプ受信例外"""
    pass


class InvalidCommandPayloadSizeError(MCPTransportError):
    """不正なペイロードサイズ例外"""
    pass


class TimeoutError(MCPTransportError):
    """タイムアウト例外"""

    def __init__(self, e):
        self.args = [e]


class InvalidMessageTypeError(MCPApplicationError):
    """不正なメッセージタイプ例外"""
    pass


class InvalidCommandPayloadError(MCPApplicationError):
    """不正なペイロード例外"""
    pass


class InvalidOperationError(MCPApplicationError):
    """不正な操作例外"""

    def __init__(self, st):
        self.args = [st]


class OutOfPositionLimitError(MCPApplicationError):
    """位置範囲制限外エラー"""
    pass


class OtherError(MCPApplicationError):
    """その他の例外"""

    def __init__(self, e):
        self.args = [e]


class WaitUntilTimeoutError(Exception):
    """wait_untilメソッド用タイムアウト例外"""

    def __init__(self, e):
        self.args = [e]


class MCPStatus():
    """
    MCP status を抽象化したクラス
    """

    def __init__(self, status):
        """
        応答メッセージに含まれるMCP status を引数にとり、MCPStatusのオブジェクトを生成する
        """
        self._status = status

    def unnotified_error(self):
        """
        未通知のエラーが発生していれば1、そうでなければ0を返す
        """
        if self._status is None:
            return None
        return (self._status & 0b10000) > 0

    def state(self):
        """
        Buildit Actuatorの状態を返す
        """
        return (self._status) & 0xf

    def str_state(self):
        """
        Buildit Actuatorの状態を文字列で返す
        """
        return state2str(self.state())


class ServoStatus():
    """
    query servo status コマンドの結果を抽象化したクラス
    """

    def __init__(self, qssr):
        self._qssr = qssr

    def position(self, unit="raw"):
        """
        センサで計測された位置を指定された単位に換算して返す

        Parameters
        ----------
        unit : str, default "raw"
            "raw": [360/65536 * 度]
            "deg": [度]
        """
        return _to_unit_pos(self._qssr[QSSR_IDX_POS], unit)

    def velocity(self, unit="raw"):
        """
        センサで計測された速度を指定された単位に換算して返す

        Parameters
        ----------
        unit : str, default "raw"
            "raw": [1/100 * rpm]
            "rpm": [rpm]
        """
        return _to_unit_vel(self._qssr[QSSR_IDX_VEL], unit)

    def current(self):
        """
        センサで計測された電流値[mA]を返す
        """
        return self._qssr[QSSR_IDX_CUR]

    def ref(self):
        """
        現在の制御指令値を返す。ただし、制御状態でなければ 0 を返す
            - 位置制御の場合は[360/65536 * 度]
            - 速度制御の場合は[1/100 * rpm]
        """
        return self._qssr[QSSR_IDX_REF]

    def temperature(self):
        """
        センサで計測された温度[摂氏度]を返す
        """
        return self._qssr[QSSR_IDX_TEMP]

    def faults(self):
        """
        フォルト値(発生したフォルトに応じた値の論理和)を返す

        SERVO_FAULT_FOC_DURATION = 0x0001
        SERVO_FAULT_OVER_VOLT    = 0x0002
        SERVO_FAULT_UNDER_VOLT   = 0x0004
        SERVO_FAULT_OVER_TEMP    = 0x0008
        SERVO_FAULT_BREAK_IN     = 0x0040
        SERVO_FAULT_STOP_CONTROL_ERROR   = 0x0100
        SERVO_FAULT_STOP_TIMEOUT = 0x0200
        SERVO_FAULT_EXTERNAL     = 0x0800
        """
        return self._qssr[QSSR_IDX_FAULTS]

    def tuple(self):
        """
        位置、速度、指令値、温度、フォルトのタプルを返す
        """
        return self._qssr


class Buildit(object):
    """
    モーター制御プロトコルをカプセル化し、Buildit Actuatorと通信する為のクラス

    Examples
    ---------
    >>> from pybuildit import *
    >>> buildit = Buildit(port="/dev/ttyUSB0", timeout_ms=3000) #for Linux
    >>> buildit = Buildit(port="COM8", timeout_ms=3000) #for Win
    >>> deviceId = 1
    >>> qss = buildit.query_servo_status(deviceId)
    >>> print("position[deg]: ", qss.position(unit="deg"))
    >>> print("velocity[rpm]: ", qss.velocity(unit="rpm"))
    >>> print("temperature[℃]: ", qss.temperature())
    >>> print("state: ", buildit.last_mcp_status.str_state())
    >>> #buildit.clear_fault(deviceId)
    >>> buildit.ready(deviceId)
    >>> buildit.set_ref_velocity(deviceId, from_rpm(42.5))
    >>> buildit.set_ref_position(deviceId, to_deg(180))
    """

    def _write(self, msg):
        sendedSize = self._ser.write(msg)
        assert sendedSize == len(msg), "serial write error"

    def _read(self, msg_size):
        return self._ser.read(msg_size)

    def _calcCRC(self, s):
        hash = crc8.crc8()
        hash.update(s)

        return int(hash.hexdigest(), 16)

    def __init__(self, port=os.environ.get('BUILDIT_PORT', "/dev/ttyUSB0"), baud=os.environ.get('BUILDIT_BAUD', 115200), timeout_ms=3000):
        """

        指定されたパラメーターでシリアルポートをオープンする

        Parameters
        ----------
        baud : int, default 115200
            ボーレート
        port : str, default "/dev/ttyUSB0"
            シリアルポートの名前(例: Linuxなら/dev/ttyUSB0, WindowsならCOM8等)
        timeout_ms : int, default 3000
            タイムアウト(ミリ秒) 負の値であればはタイムアウトしない

        """
        if timeout_ms < 0:
            self._ser = serial.Serial(port, baud)
        else:
            self._ser = serial.Serial(port, baud, timeout=timeout_ms / 1000.0)
        if self.is_open():
            self._ser.reset_input_buffer()
            self._ser.reset_output_buffer()
        self._last_mcp_status = None

    def is_open(self):
        """
        シリアルポートがオープンされていればTrue、そうでなければFalseを返す
        """
        return self._ser.is_open

    def open(self, port=os.environ.get('BUILDIT_PORT', "/dev/ttyUSB0"), baud=os.environ.get('BUILDIT_BAUD', 115200)):
        """
        シリアルポートをオープンする

        Parameters
        ----------

        baud : int, default 115200
            ボーレート
        port : str, default "/dev/ttyUSB0"
            シリアルポートの名前(例: Linuxなら/dev/ttyUSB0, WindowsならCOM8等)
        """
        self._ser.baudrate = baud
        self._ser.port = port
        self._ser.open()
        self._ser.reset_input_buffer()
        self._ser.reset_output_buffer()

    def close(self):
        """
        シリアルポートをクローズする
        """
        self._ser.close()

    def _receive_ack(self):

        header = self._read(MSG_HEADER_SIZE)
        if len(header) != MSG_HEADER_SIZE:
            raise TimeoutError((header, len(header)))

        (mark1, mark2, mark3, crc, devId, msgType, payloadSize) = struct.unpack('BBBBBBB', header[0:7])
        mark = (mark1 << 16) + (mark2 << 8) + mark3

        if mark != MSG_MARK:
            raise InvalidFormatError

        payload = self._read(payloadSize)

        if len(payload) != payloadSize:
            raise TimeoutError((payload, len(payload)))

        if crc != self._calcCRC(header[4:8] + payload):
            raise InvalidCRCError

        # print "recv:", struct.unpack('B' * len(header), header)

        return (msgType, payload)

    def _nack2exception(self, payload):

        (status, err) = struct.unpack('HB', payload)
        self._last_mcp_status = status
        if err == MCP_INVALID_COMMAND_PAYLOAD:
            return InvalidCommandPayloadError
        elif err == MCP_INVALID_COMMAND_PAYLOAD_SIZE:
            return InvalidCommandPayloadSizeError
        elif err == MCP_INVALID_OPERATION:
            return InvalidOperationError(self.last_mcp_status().str_state())
        elif err == MCP_INVALID_MSG_TYPE:
            return InvalidMessageTypeError
        elif err == MCP_OUT_OF_POSITION_LIMIT:
            return OutOfPositionLimitError
        else:
            return OtherError(err)

    def _rpc_raw(self, msg, ackfmt):

        self._write(msg)
        (ackType, payload) = self._receive_ack()

        cmdType = struct.unpack('B' * len(msg), msg)[MSG_TYPE_IDX]

        if ackType == MSG_TYPE_NACK:
            raise self._nack2exception(payload)
        elif ackType == (ACK_BIT | cmdType):
            bs = struct.unpack('<H' + ackfmt, payload)
            self._last_mcp_status = bs[0]
            return bs[1:]
        else:
            raise UnexpectedMessageTypeError

    def _rpc_log_raw(self, msg, ackfmt):

        self._write(msg)
        (ackType, payload) = self._receive_ack()

        cmdType = struct.unpack('B' * len(msg), msg)[MSG_TYPE_IDX]

        if ackType == MSG_TYPE_NACK:
            raise self._nack2exception(payload)
        elif ackType == (ACK_BIT | cmdType):
            status = struct.unpack('<H', payload[0:2])[0]
            startIndex = struct.unpack('<H', payload[2:4])[0]
            readSize = struct.unpack('<H', payload[4:6])[0]

            logRecords = []
            for i in range(readSize):
                index = 6 + i * LOG_RECORD_BYTE_SIZE
                recordBytes = payload[index:(index + LOG_RECORD_BYTE_SIZE)]
                hd = struct.unpack('<IBBBB', recordBytes[0:LOG_RECORD_BYTE_SIZE - LOG_RECORD_PAYLOAD_SIZE])
                logIndex = hd[0]
                logLevel = hd[1]
                group    = hd[2]
                subGroup = hd[3]
                code     = hd[4]
                payload_data = recordBytes[LOG_RECORD_BYTE_SIZE - LOG_RECORD_PAYLOAD_SIZE:LOG_RECORD_BYTE_SIZE]
                (g, sg, c, data) = log_record2str(logLevel, group, subGroup, code, payload_data)
                logRecord = {'index': logIndex, 'level': log_level2str(logLevel), 'group': g, 'subGroup': sg, 'code': c, 'payload': data}
                logRecords.append(logRecord)

            self._last_mcp_status = status

            logData = {'startIndex': startIndex, 'readSize': readSize, 'logRecords': logRecords}
            return logData
        else:
            raise UnexpectedMessageTypeError

    def _rpc_make_msg(self, msgType, devId, payloadSize = None, mark=MSG_MARK, crc = None, payload=bytes()):

        if payloadSize is None:
            payloadSize = len(payload)

        m = struct.pack('BBB', mark >> 16 & 0xff, mark >> 8 & 0xff, mark & 0xff)

        header = struct.pack('BBH', devId, msgType, payloadSize)

        if crc is None:
            crc = struct.pack('B', self._calcCRC(header + payload))
        else:
            crc = struct.pack('B', crc)

        msg = m + crc + header + payload

        return msg

    def _rpc(self, msgType, devId, payloadSize=None, mark=MSG_MARK, crc=None, payload=bytes(), ackfmt=''):

        msg = self._rpc_make_msg(msgType, devId, payloadSize, mark, crc, payload)

        if os.environ.get('AMARETTO_TRACE_COMMAND_BYTE', 0):
            print(["{:02x}".format(x) for x in msg])

        return self._rpc_raw(msg, ackfmt)

    def _rpc_log(self, msgType, devId, payloadSize=None, mark=MSG_MARK, crc=None, payload=bytes(), ackfmt=''):

        msg = self._rpc_make_msg(msgType, devId, payloadSize, mark, crc, payload)

        return self._rpc_log_raw(msg, ackfmt)

    def last_mcp_status(self):
        """
        最新の応答に含まれるMCPStatusを返します(ただし、一度も通信していなければNone)
        """
        if self._last_mcp_status is None:
            return None
        return MCPStatus(self._last_mcp_status)

    def wait_until(self, devId, pred, timeout_ms = -1):
        """
        Buildit Actuatorがユーザーが指定した状態になるか、タイムアウトするまでブロッキングする。
        ブロッキング解除条件はquery_servo_status(devId)の結果がpred関数の戻り値をTrueにすることである。

        Examples
        ------------

        位置が0より大きくなるまで待つ例

        >>> amaretto.wait_until(devId, lambda state,query_status_result: query_status_result.position() > 0)

        Parameters
        ----------

        devId : int
            デバイスID
        pred : function
            第一引数としてBuildit Actuatorの状態、第二引数としてquery_servo_statusの結果を受け取ってTrueもしくはFalseを返す関数
        timeout_ms : int
            タイムアウト値(ミリ秒)。ただし、タイムアウト値に負の値を指定した場合はタイムアウト処理は行われない

        """

        starttime = time.time()
        timeout_sec = timeout_ms / 1000.0

        while True:
            q = self.query_servo_status(devId)
            if pred(self.last_mcp_status().state(), q):
                break
            if timeout_sec >= 0 and time.time() - starttime > timeout_sec:
                raise WaitUntilTimeoutError((self.last_mcp_status().str_state(), q))

    def wait_until_state(self, devId, targetState, timeout_ms = -1):
        """
        devIdで指定されたBuildit Actuatorの状態遷移完了をポーリングで待つ

        Parameters
        ----------

        devId : int
            デバイスID
        s : int
            状態ID
        timeout_ms : int
            タイムアウト値(ミリ秒)

        """

        self.wait_until(devId, lambda s, q: s == targetState, timeout_ms)

    def wait_until_stop(buildit, dev_id, timeout, vel_thres=10, vel_unit="raw"):
        """
        devIdで指定された位置制御状態にあるBuildit Actuatorがposで指定された位置で停止されるまでブロックする

        Parameters
        ----------

        devId : int
            デバイスID
        pos : int
            停止予定位置
        timeout_ms : int
            タイムアウト値(ミリ秒)
        vel_thres : float
            停止速度の許容誤差
        vel_unit : str, default "raw"
            vel_thres の単位
            "raw": [360/65536 * 度]
            "deg": [度]

        """
        def has_stopped(state, qssr):
            if abs(qssr.velocity(vel_unit)) > vel_thres:
                return False
            return state != STATE_FAULT_HOLD

        buildit.wait_until(dev_id, has_stopped)

    def wait_until_stop_at(buildit, dev_id, pos, timeout, pos_thres=10, pos_unit="raw", vel_thres=10, vel_unit="raw"):
        """
        devIdで指定された位置制御状態にあるBuildit Actuatorがposで指定された位置で停止されるまでブロックする

        Parameters
        ----------

        devId : int
            デバイスID
        pos : int
            停止予定位置
        timeout_ms : int
            タイムアウト値(ミリ秒)
        pos_thres : float
            停止位置の許容誤差
        pos_unit : str, default "raw"
            pos 及び pos_thres の単位
            "raw": [360/65536 * 度]
            "deg": [度]
        vel_thres : float
            停止速度の許容誤差
        vel_unit : str, default "raw"
            vel_thres の単位
            "raw": [360/65536 * 度]
            "deg": [度]

        """
        def has_stopped(state, qssr):
            if abs(qssr.position(pos_unit) - pos) > pos_thres:
                return False
            if abs(qssr.velocity(vel_unit)) > vel_thres:
                return False
            return state != STATE_FAULT_HOLD

        buildit.wait_until(dev_id, has_stopped)

    # フィールドアクセス可能なオブジェクトにして返すべき
    def query_servo_status(self, devId):
        """
        devIdで指定されたBuildit Actuatorの状態を問い合わせる

        Parameters
        ----------

        devId : int
            デバイスID

        Returns
        -------
        ServoStatus のオブジェクトを返す
        """

        return ServoStatus(self._rpc(MSG_TYPE_QUERY_SERVO_STATUS_CMD, devId, ackfmt='ihhiBH'))

    def hold(self, devId):
        """
        devIdで指定された、ブレーキ保持状態、ブレーキ解除状態、レディ状態のいずれかの状態にあるBuildit Actuatorをブレーキ保持状態に遷移させる

        Parameters
        ----------

        devId : int
            デバイスID

        """
        return self._rpc(MSG_TYPE_HOLD_CMD, devId, ackfmt='')

    def ready(self, devId):
        """
        devIdで指定された、ブレーキ保持状態、ブレーキ解除状態、レディ状態のいずれかの状態にあるBuildit Actuatorをレディ状態に遷移させる

        Parameters
        ----------

        devId : int
            デバイスID

        """
        return self._rpc(MSG_TYPE_READY_CMD, devId, ackfmt='')

    def force_hold(self, devId):
        """
        devIdで指定された、Buildit Actuatorをブレーキ保持状態に遷移させる

        Parameters
        ----------

        devId : int
            デバイスID

        """
        self.query_servo_status(devId)
        s = self.last_mcp_status().state()

        if s in [STATE_CURRENT_SERVO, STATE_VELOCITY_SERVO, STATE_POSITION_SERVO]:
            self.stop(devId)
            self.wait_until_state(devId, STATE_READY, timeout_ms = 500)
            self.hold(devId)
        elif s in [STATE_FAULT_FREE, STATE_FAULT_HOLD]:
            self.clear_fault(devId)
            self.hold(devId)
        else:
            self.hold(devId)

    def force_ready(self, devId):
        """
        devIdで指定された、Buildit Actuatorをレディ状態に遷移させる

        Parameters
        ----------

        devId : int
            デバイスID

        """
        self.query_servo_status(devId)
        s = self.last_mcp_status().state()

        if s in [STATE_CURRENT_SERVO, STATE_VELOCITY_SERVO, STATE_POSITION_SERVO]:
            self.stop(devId)
            self.wait_until_state(devId, STATE_READY, timeout_ms = 500)
        elif s in [STATE_FAULT_FREE, STATE_FAULT_HOLD]:
            self.clear_fault(devId)
            self.ready(devId)
        else:
            self.ready(devId)

    def force_free(self, devId):
        """
        devIdで指定された、Buildit Actuatorをブレーキ解除状態に遷移させる

        Parameters
        ----------

        devId : int
            デバイスID

        """
        self.query_servo_status(devId)
        s = self.last_mcp_status().state()

        if s in [STATE_CURRENT_SERVO, STATE_VELOCITY_SERVO, STATE_POSITION_SERVO]:
            self.stop(devId)
            self.wait_until_state(devId, STATE_READY, timeout_ms = 500)
            self.free(devId)
        elif s in [STATE_FAULT_FREE, STATE_FAULT_HOLD]:
            self.clear_fault(devId)
            self.free(devId)
        else:
            self.free(devId)

    def free(self, devId):
        """
        devIdで指定された、ブレーキ保持状態、ブレーキ解除状態、レディ状態のいずれかの状態にあるBuildit Actuatorをブレーキ解除状態に遷移させる
        Buildit Actuatorをfree状態に遷移させる

        Parameters
        ----------

        devId : int
            デバイスID

        """
        return self._rpc(MSG_TYPE_FREE_CMD, devId, ackfmt='')

    def stop(self, devId, timeout_ms=500):
        """
        devIdで指定された、電流制御状態、速度制御状態、位置制御状態、レディ状態のいずれかの状態にあるBuildit Actuatorに対して保護停止を行う。
        保護停止が成功した場合、Buildit Actuatorはレディ状態に遷移する。

        Parameters
        ----------

        devId : int
            デバイスID

        timeout_ms : int
            タイムアウト[ミリ秒]

        """
        return self._rpc(MSG_TYPE_PROTECTION_STOP_CMD, devId, payload=struct.pack('<H', timeout_ms), ackfmt='')

    def clear_fault(self, devId):
        """
        devIdで指定された、フォルト状態にあるBuildit Actuatorに対して復帰を試みる。
        ブレーキ解除フォルト状態であればブレーキ解除状態に ブレーキ保持フォルト状態であればブレーキ保持状態に遷移する。

        Parameters
        ----------

        devId : int
            デバイスID

        """
        return self._rpc(MSG_TYPE_CLEAR_FAULT_CMD, devId, ackfmt='')

    def reset_rotation(self, devId, rot = 0):
        """
        devIdで指定された、レディ状態、位置制御状態のいずれでもないBuildit Actuatorの電源投入後のの累計回転数を初期化する。

        Parameters
        ----------

        devId : int
            デバイスID
        rot   : int
            リセット後の回転数

        """
        return self._rpc(MSG_TYPE_RESET_ROTATION_CMD, devId, payload=struct.pack('<h', rot), ackfmt='')

    def set_ref_current(self, devId, cur):
        """
        devIdで指定された、電流制御状態、速度制御状態、位置制御状態、レディ状態のいずれかの状態にあるBuildit Actuatorを電流指令値を設定した上で電流制御状態に遷移させる

        Parameters
        ----------

        devId : int
            デバイスID

        cur : int
            電流指令値[mA]

        Returns
        -------
        cur : int
            センサで計測された電流値[mA]


        """
        return self._rpc(MSG_TYPE_SET_REF_CURRENT_CMD, devId, payload=struct.pack('h', int(cur)), ackfmt='h')[0]

    def get_ref_current(self, devId):
        """
        devIdで指定された、電流制御状態にあるBuildit Actuatorの電流指令値[mA]を取得する
        """
        return self._rpc(MSG_TYPE_GET_REF_CURRENT_CMD, devId, ackfmt='h')[0]

    def get_current_KP(self, devId):
        """
        devIdで指定されたBuildit Actuatorの電流制御用比例ゲインを取得する
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_CURRENT_KP), ackfmt='h')[0]

    def get_current_KI(self, devId):
        """
        devIdで指定されたBuildit Actuatorの電流制御用積分ゲインを取得する
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_CURRENT_KI), ackfmt='h')[0]

    def get_current_max_Iterm(self, devId):
        """
        devIdで指定されたBuildit Actuatorの電流制御用積分項の上限値を取得する(非推奨)
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_CURRENT_MAX_ITERM), ackfmt='i')[0]

    def get_current_min_Iterm(self, devId):
        """
        devIdで指定されたBuildit Actuatorの電流制御用積分項の下限値を取得する(非推奨)
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_CURRENT_MIN_ITERM), ackfmt='i')[0]

    def set_current_max_limit(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの電流指令値の上限値を設定する
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bh', PARAM_ID_CURRENT_MAX_LIMIT, int(v)), ackfmt='')

    def get_current_max_limit(self, devId):
        """
        devIdで指定されたBuildit Actuatorの電流指令値の上限値を取得する
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_CURRENT_MAX_LIMIT), ackfmt='h')[0]

    def set_current_min_limit(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの電流指令値の下限値を設定する
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bh', PARAM_ID_CURRENT_MIN_LIMIT, int(v)), ackfmt='')

    def get_current_min_limit(self, devId):
        """
        devIdで指定されたBuildit Actuatorの電流指令値の下限値を取得する
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_CURRENT_MIN_LIMIT), ackfmt='h')[0]

    def set_ref_velocity(self, devId, vel, unit="raw"):
        """
        devIdで指定された、電流制御状態、速度制御状態、位置制御状態、レディ状態のいずれかの状態にあるBuildit Actuatorを速度指令値velを設定して速度制御状態に遷移させる

        Parameters
        ----------

        devId : int
            デバイスID

        vel : int もしくは float
            速度指令値

        unit : str
            引数と戻り値の単位

            "raw": [1/100 * rpm]
            "rpm": [rpm]

        Returns
        -------
        vel : int
            センサで計測された速度
        """
        ref = _from_unit_vel(vel, unit)
        sen = self._rpc(MSG_TYPE_SET_REF_VELOCITY_CMD, devId, payload=struct.pack('h', ref), ackfmt='h')[0]
        return _to_unit_vel(sen, unit)

    def get_ref_velocity(self, devId, unit="raw"):
        """
        devIdで指定された、速度制御状態にあるBuildit Actuatorの速度指令値を取得する

        Parameters
        ----------

        devId : int
            デバイスID

        unit : str
            戻り値の単位

            "raw": [1/100 * rpm]
            "rpm": [rpm]

        """
        ref = self._rpc(MSG_TYPE_GET_REF_VELOCITY_CMD, devId, ackfmt='h')[0]
        return _to_unit_vel(ref, unit)

    def set_velocity_KP(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの速度制御用比例ゲインを設定する
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bh', PARAM_ID_VELOCITY_KP, int(v)), ackfmt='')

    def get_velocity_KP(self, devId):
        """
        devIdで指定されたBuildit Actuatorの速度制御用比例ゲインを取得する
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_VELOCITY_KP), ackfmt='h')[0]

    def set_velocity_KI(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの速度制御用積分ゲインを設定する
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bh', PARAM_ID_VELOCITY_KI, int(v)), ackfmt='')

    def get_velocity_KI(self, devId):
        """
        devIdで指定されたBuildit Actuatorの速度制御用積分ゲインを取得する
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_VELOCITY_KI), ackfmt='h')[0]

    def set_velocity_KD(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの速度制御用微分ゲインを設定する
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bh', PARAM_ID_VELOCITY_KD, int(v)), ackfmt='')

    def get_velocity_KD(self, devId):
        """
        devIdで指定されたBuildit Actuatorの速度制御用積微分ゲインを取得する
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_VELOCITY_KD), ackfmt='h')[0]

    def set_velocity_max_Iterm(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの速度制御用積分項の上限値を設定する(非推奨)
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bi', PARAM_ID_VELOCITY_MAX_ITERM, int(v)), ackfmt='')

    def get_velocity_max_Iterm(self, devId):
        """
        devIdで指定されたBuildit Actuatorの速度制御用積分項の上限値を取得する(非推奨)
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_VELOCITY_MAX_ITERM), ackfmt='i')[0]

    def set_velocity_min_Iterm(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの速度制御用積分項の下限値を設定する(非推奨)
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bi', PARAM_ID_VELOCITY_MIN_ITERM, int(v)), ackfmt='')

    def get_velocity_min_Iterm(self, devId):
        """
        devIdで指定されたBuildit Actuatorの速度制御用積分項の下限値を取得する(非推奨)
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_VELOCITY_MIN_ITERM), ackfmt='i')[0]

    def set_velocity_max_limit(self, devId, v, unit="raw"):
        """
        devIdで指定されたBuildit Actuatorの速度指令値の上限値を設定する

        Parameters
        ----------

        devId : int
            デバイスID

        v : int もしくは float
            速度制限値

        unit : str
            引数の単位

            "raw": [1/100 * rpm]
            "rpm": [rpm]

        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bh', PARAM_ID_VELOCITY_MAX_LIMIT, _from_unit_vel(v, unit)), ackfmt='')

    def get_velocity_max_limit(self, devId, unit="raw"):
        """
        devIdで指定されたBuildit Actuatorの速度指令値の上限値を取得する

        Parameters
        ----------

        devId : int
            デバイスID

        unit : str
            戻り値の単位

            "raw": [1/100 * rpm]
            "rpm": [rpm]

        """
        v = self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_VELOCITY_MAX_LIMIT), ackfmt='h')[0]
        return _to_unit_vel(v, unit)

    def set_velocity_min_limit(self, devId, v, unit="raw"):
        """
        devIdで指定されたBuildit Actuatorの速度指令値の下限値を設定する

        Parameters
        ----------

        devId : int
            デバイスID

        v : int もしくは float
            位置制限値

        unit : str
            引数の単位

            "raw": [1/100 * rpm]
            "rpm": [rpm]

        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bh', PARAM_ID_VELOCITY_MIN_LIMIT, _from_unit_vel(v, unit)), ackfmt='')

    def get_velocity_min_limit(self, devId, unit="raw"):
        """
        devIdで指定されたBuildit Actuatorの速度指令値の下限値を取得する

        Parameters
        ----------

        devId : int
            デバイスID

        unit : str
            戻り値の単位

            "raw": [1/100 * rpm]
            "rpm": [rpm]

        """
        v = self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_VELOCITY_MIN_LIMIT), ackfmt='h')[0]
        return _to_unit_vel(v, unit)

    def set_ref_position(self, devId, pos, unit="raw"):
        """
        devIdで指定された、電流制御状態、速度制御状態、位置制御状態、レディ状態のいずれかの状態にあるBuildit Actuatorを位置指令値posを設定して位置制御状態に遷移させる

        Parameters
        ----------

        devId : int
            デバイスID

        pos : int もしくは float
            位置指令値

        unit : str
            引数と戻り値の単位

            "raw": [360/65536 * 度]
            "deg": [度]


        Returns
        -------
        pos : int
            センサで計測された位置


        """
        ref = _from_unit_pos(pos, unit)
        sen = self._rpc(MSG_TYPE_SET_REF_POSITION_CMD, devId, payload=struct.pack('i', ref), ackfmt='i')[0]
        return _to_unit_pos(sen, unit)

    def get_ref_position(self, devId, unit="raw"):
        """
        devIdで指定された、位置制御状態にあるBuildit Actuatorの位置指令値[360/65536 * 度]を取得する

        Parameters
        ----------

        devId : int
            デバイスID

        unit : str
            戻り値の単位

            "raw": [360/65536 * 度]
            "deg": [度]

        """
        ref = self._rpc(MSG_TYPE_GET_REF_POSITION_CMD, devId, ackfmt='i')[0]
        return _to_unit_pos(ref, unit)

    def set_position_KP(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの位置制御用比例ゲインを設定する
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bh', PARAM_ID_POSITION_KP, int(v)), ackfmt='')

    def get_position_KP(self, devId):
        """
        devIdで指定されたBuildit Actuatorの位置制御用比例ゲインを取得する
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_POSITION_KP), ackfmt='h')[0]

    def set_position_KI(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの位置制御用積分ゲインを設定する
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bh', PARAM_ID_POSITION_KI, int(v)), ackfmt='')

    def get_position_KI(self, devId):
        """
        devIdで指定されたBuildit Actuatorの位置制御用積分ゲインを取得する
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_POSITION_KI), ackfmt='h')[0]

    def set_position_KD(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの位置制御用微分ゲインを設定する
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bh', PARAM_ID_POSITION_KD, int(v)), ackfmt='')

    def get_position_KD(self, devId):
        """
        devIdで指定されたBuildit Actuatorの位置制御用積微分ゲインを取得する
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_POSITION_KD), ackfmt='h')[0]

    def set_position_max_Iterm(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの位置制御用積分項の上限値を設定する(非推奨)
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bi', PARAM_ID_POSITION_MAX_ITERM, int(v)), ackfmt='')

    def get_position_max_Iterm(self, devId):
        """
        devIdで指定されたBuildit Actuatorの位置制御用積分項の上限値を取得する(非推奨)
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_POSITION_MAX_ITERM), ackfmt='i')[0]

    def set_position_min_Iterm(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの位置制御用積分項の下限値を設定する(非推奨)
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bi', PARAM_ID_POSITION_MIN_ITERM, int(v)), ackfmt='')

    def get_position_min_Iterm(self, devId):
        """
        devIdで指定されたBuildit Actuatorの位置制御用積分項の下限値を取得する(非推奨)
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_POSITION_MIN_ITERM), ackfmt='i')[0]

    def set_position_max_limit(self, devId, v, unit="raw"):
        """
        devIdで指定されたBuildit Actuatorの位置指令値の上限値を設定する

        Parameters
        ----------

        devId : int
            デバイスID

        v : int もしくは float
            位置制限値

        unit : str
            引数の単位

            "raw": [360/65536 * 度]
            "deg": [度]

        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bi', PARAM_ID_POSITION_MAX_LIMIT, _from_unit_pos(v, unit)), ackfmt='')

    def get_position_max_limit(self, devId, unit="raw"):
        """
        devIdで指定されたBuildit Actuatorの位置指令値の上限値を取得する

        Parameters
        ----------

        devId : int
            デバイスID

        unit : str
            戻り値の単位

            "raw": [360/65536 * 度]
            "deg": [度]

        """
        v = self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_POSITION_MAX_LIMIT), ackfmt='i')[0]
        return _to_unit_pos(v, unit)

    def set_position_min_limit(self, devId, v, unit="raw"):
        """
        devIdで指定されたBuildit Actuatorの位置指令値の下限値を設定する [360/65536 * 度]

        Parameters
        ----------

        devId : int
            デバイスID

        v : int もしくは float
            位置制限値

        unit : str
            引数の単位

            "raw": [360/65536 * 度]
            "deg": [度]

        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bi', PARAM_ID_POSITION_MIN_LIMIT, _from_unit_pos(v, unit)), ackfmt='')

    def get_position_min_limit(self, devId, unit="raw"):
        """
        devIdで指定されたBuildit Actuatorの位置指令値の下限値を取得する [360/65536 * 度]

        Parameters
        ----------

        devId : int
            デバイスID

        unit : str
            戻り値の単位

            "raw": [360/65536 * 度]
            "deg": [度]

        """
        v = self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_POSITION_MIN_LIMIT), ackfmt='i')[0]
        return _to_unit_pos(v, unit)

    def set_position_offset(self, devId, v, unit="raw"):
        """
        devIdで指定されたBuildit Actuatorの位置センサのユーザーオフセットを設定する [360/65536 * 度]
        """
        v = _from_unit_pos(v, unit)
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bh', PARAM_ID_POSITION_OFFSET, v), ackfmt='')

    def get_position_offset(self, devId, unit="raw"):
        """
        devIdで指定されたBuildit Actuatorの位置センサのユーザーオフセットを取得する [360/65536 * 度]
        """
        v = self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_POSITION_OFFSET), ackfmt='h')[0]
        return _to_unit_pos(v, unit)

    def set_device_id(self, devId, v):
        """
        devIdで指定されたBuildit ActuatorのデバイスIDを設定する
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<BB', PARAM_ID_DEVICE_ID, int(v)), ackfmt='')

    def get_device_id(self, devId):
        """
        devIdで指定されたBuildit ActuatorのデバイスIDを取得する
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_DEVICE_ID), ackfmt='B')[0]

    def find_device_id(self):
        """
        接続中の応答可能なデバイスのうち最も小さなデバイスIDを返す
        """
        timeout = self._ser.timeout
        self._ser.timeout = 0.05    # sec
        foundId = None
        try:
            for id in range(DEVICE_ID_MAX + 1):
                try:
                    self.query_servo_status(devId=id)
                    foundId = id
                    break
                except Exception as e:
                    pass
        finally:
            self._ser.timeout = timeout

        return foundId

    def _get_servo_params(self, devId):

        params = dict(
            PARAM_ID_VELOCITY_KP = self.get_velocity_KP(devId),
            PARAM_ID_VELOCITY_KI = self.get_velocity_KI(devId),
            PARAM_ID_VELOCITY_KD = self.get_velocity_KD(devId),
            PARAM_ID_VELOCITY_MAX_ITERM = self.get_velocity_max_Iterm(devId),
            PARAM_ID_VELOCITY_MIN_ITERM = self.get_velocity_min_Iterm(devId),
            PARAM_ID_VELOCITY_MAX_LIMIT = self.get_velocity_max_limit(devId),
            PARAM_ID_VELOCITY_MIN_LIMIT = self.get_velocity_min_limit(devId),

            PARAM_ID_POSITION_KP = self.get_position_KP(devId),
            PARAM_ID_POSITION_KI = self.get_position_KI(devId),
            PARAM_ID_POSITION_KD = self.get_position_KD(devId),
            PARAM_ID_POSITION_MAX_ITERM = self.get_position_max_Iterm(devId),
            PARAM_ID_POSITION_MIN_ITERM = self.get_position_min_Iterm(devId),
            PARAM_ID_POSITION_MAX_LIMIT = self.get_position_max_limit(devId),
            PARAM_ID_POSITION_MIN_LIMIT = self.get_position_min_limit(devId),

            PARAM_ID_POSITION_OFFSET = self.get_position_offset(devId)
        )
        # print(params)
        return params

    def _set_servo_params(self, devId, params):

        self.set_current_max_limit(devId, params['PARAM_ID_CURRENT_MAX_LIMIT']),
        self.set_current_min_limit(devId, params['PARAM_ID_CURRENT_MIN_LIMIT']),

        self.set_velocity_KP(devId, params['PARAM_ID_VELOCITY_KP']),
        self.set_velocity_KI(devId, params['PARAM_ID_VELOCITY_KI']),
        self.set_velocity_KD(devId, params['PARAM_ID_VELOCITY_KD']),
        self.set_velocity_max_Iterm(devId, params['PARAM_ID_VELOCITY_MAX_ITERM']),
        self.set_velocity_min_Iterm(devId, params['PARAM_ID_VELOCITY_MIN_ITERM']),
        self.set_velocity_max_limit(devId, params['PARAM_ID_VELOCITY_MAX_LIMIT']),
        self.set_velocity_min_limit(devId, params['PARAM_ID_VELOCITY_MIN_LIMIT']),

        self.set_position_KP(devId, params['PARAM_ID_POSITION_KP']),
        self.set_position_KI(devId, params['PARAM_ID_POSITION_KI']),
        self.set_position_KD(devId, params['PARAM_ID_POSITION_KD']),
        self.set_position_max_Iterm(devId, params['PARAM_ID_POSITION_MAX_ITERM']),
        self.set_position_min_Iterm(devId, params['PARAM_ID_POSITION_MIN_ITERM']),
        self.set_position_max_limit(devId, params['PARAM_ID_POSITION_MAX_LIMIT']),
        self.set_position_min_limit(devId, params['PARAM_ID_POSITION_MIN_LIMIT']),

        self.set_position_offset(devId, params['PARAM_ID_POSITION_OFFSET'])

    def save_servo_params(self, devId, fileName=None):
        """
        devIdで指定されたBuildit Actuatorのサーボパラメーターをファイルに保存する
        """

        if fileName is None:
            timestr = time.strftime("%Y%m%d-%H%M%S")
            fileName = "params-" + timestr + ".yml"

        with open(fileName, "w") as file:
            params = self._get_servo_params(devId)
            yaml.dump(params, file, default_flow_style=False)

    def load_servo_params(self, devId, filepath):
        """
        サーボパラメーターをファイルから読みだし、devIdで指定されたBuildit Actuatorに反映する
        """

        with open(filepath, "r") as stream:
            try:
                params = yaml.safe_load(stream)
                self._set_servo_params(devId, params)

            except yaml.YAMLError as exc:
                print(exc)

    def save_configuration(self, devId, fileName=None):
        """
        devIdで指定されたBuildit Actuatorの設定をファイルに保存する
        """

        if fileName is None:
            timestr = time.strftime("%Y%m%d-%H%M%S")
            fileName = "configuration-" + timestr + ".yml"

        with open(fileName, "w") as file:
            params = self._get_servo_params(devId)
            params = dict(params, **dict(
                PARAM_ID_POSITION_SYS_OFFSET = self.get_position_sys_offset(devId),
                PARAM_ID_CALIBRATION = self.get_calibration_data(devId),
                PARAM_ID_FIRMWARE_VERSION = self.get_firmware_version(devId),
            ))
            yaml.dump(params, file, default_flow_style=False)

    def move_with_period(self, devId, goal, period_ms, acc=0.2, dec=0.2, pos_thres=10, unit="raw"):
        """
        指定された期間で目標位置値で停止するように100Hzで移動命令を発行する

        PC側のシステムのシリアル通信のレイテンシを5ms以下に設定すること

        Parameters
        ----------

        devId : int
            デバイスID
        goal : float
            目標位置
        period_ms : float
            移動時間[ミリ秒]
        acc : float
            t1に対する開始加速期間の割合([0.1, 1])
        dec : float
            t1に対する終端減速期間の割合([0.1, 1])
        pos_thres: float
            停止位置の許容誤差
        unit : str
            goal, pos_thres の単位

        """
        period = period_ms / 1000
        sampling = 100
        start = self.query_servo_status(devId).position(unit)

        if self.last_mcp_status().state() not in [STATE_READY, STATE_CURRENT_SERVO, STATE_VELOCITY_SERVO, STATE_POSITION_SERVO]:
            raise InvalidOperationError(self.last_mcp_status().str_state())
        n = round(period * sampling)
        if n <= 0:
            n = 1
        span = period / float(n)
        t0 = time.time()
        path = BuilditPath([(0, start), (period, goal)], acc, dec)
        i = 1
        ref = 0
        while True:
            t = time.time()
            if (t - t0) < i * span:
                continue
            # print(t, ref)
            if t > t0 + period:
                sen = self.set_ref_position(devId, goal, unit)
                self.wait_until_stop_at(devId, goal, 1000, pos_thres, unit)
                sen = self.set_ref_position(devId, goal, unit)
                break
            tmp = path.interp(t - t0)
            if (tmp is not None):
                ref = int(tmp)
                i = i + 1
            sen = self.set_ref_position(devId, ref, unit)
        return sen

    def get_firmware_version(self, devId):
        """
        devIdで指定されたBuildit Actuatorのファームウェアのバージョン情報を取得する
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_FIRMWARE_VERSION), ackfmt='16s')[0].decode('ascii').replace('\0', '')

    def get_power_on_time(self, devId):
        """
        devIdで指定されたBuildit Actuatorの累計通電時間を取得する
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_POWER_ON_TIME), ackfmt='I')[0]

    def get_calibration_data(self, devId):
        """
        devIdで指定されたBuildit Actuatorの補正値を取得する
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_CALIBRATION), ackfmt='H')[0]

    def get_position_sys_offset(self, devId):
        """
        devIdで指定されたBuildit Actuatorの位置センサのシステムオフセットを取得する [360/65536 * 度]
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_POSITION_SYS_OFFSET), ackfmt='H')[0]

    def get_log_info(self, devId):
        """
        devIdで指定されたBuildit Actuatorのログ情報を取得する

        Parameters
        ----------

        devId : int
            デバイスID

        Returns
        -------
        readableSize : int
            取得可能なログレコード数


        """
        return self._rpc(MSG_TYPE_GET_LOG_INFO_CMD, devId, ackfmt='h')[0]

    def print_log(self, devId, startIndex = 0, readSize = -1):
        """
        devIdで指定されたBuildit Actuatorのログを出力する

        Parameters
        ----------

        devId : int
            デバイスID

        startIndex : int
            取得するログレコードの開始番号

        readSize : int
            取得するログレコードの個数

        """

        data = self.get_log(devId, startIndex, readSize)
        if len(data['logRecords']) > 0:
            print('startIndex:', data['startIndex'])
            print('readSize:', data['readSize'])
            for record in data['logRecords']:
                print("{index:10d}:\t{level:s}:\t{group:17s}\t{subGroup:17s}\t{code:s}\t{payload:s}".format(**record))

    def get_log(self, devId, startIndex = 0, readSize = -1):
        """
        devIdで指定されたBuildit Actuatorのログを取得する

        Parameters
        ----------

        devId : int
            デバイスID

        startIndex : int
            取得するログレコードの開始番号

        readSize : int
            取得するログレコードの個数

        Returns
        -------
        startIndex : int
            取得したログレコードの開始番号

        readSize : int
            取得したログレコードの個数

        logRecords : bytes
            取得したReadSize個分のログレコード
        """
        records = []
        numOfRecords = self.get_log_info(devId)

        if startIndex < 0 :
            startIndex = 0

        if readSize < 0:
            readSize = numOfRecords

        if startIndex + readSize > numOfRecords:
            readSize = min(readSize, numOfRecords - startIndex)

        offset = startIndex
        remain = readSize

        while remain > 0:
            size = min(remain, 10)
            tmp = self._rpc_log(MSG_TYPE_GET_LOG_CMD, devId, payload=struct.pack('hh', int(offset), int(size)), ackfmt='')
            records = records + tmp['logRecords']
            offset = offset + size
            remain = remain - size

        return {'startIndex': startIndex,
                'readSize'  : readSize,
                'logRecords': records}

    def fault(self, devId, is_fatal = False):
        """
        任意のフォルトを発生させる

        Parameters
        ----------

        devId : int
            デバイスID

        is_fatal : bool
            True  ならシステムフォルト(モーターの通電を止めてブレーキがかかる。そして再起動しない限りLEDの点灯以外は何も行わない)
            False ならフォルト状態に遷移させる(モーターの通電を止めてブレーキがかかる)


        """
        return self._rpc(MSG_TYPE_FAULT_CMD, devId, payload=struct.pack('H', int(is_fatal)), ackfmt='')
