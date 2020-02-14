#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pybuildit.const import *
from pybuildit.lib import *

class UnsafeBuildit(Buildit):
    """
    デバッグビルドファーム用拡張機能
    """

    def __init__(self, port=os.environ.get('BUILDIT_PORT', "/dev/ttyUSB0"), baud=os.environ.get('BUILDIT_BAUD', 115200), timeout_ms=3000):
        super().__init__(port, baud, timeout_ms)

    def get_prot_stop_pin_timeout(self, devId):
        """
        保護停止ピンによる停止間上限[ms]を取得する
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_PROTECTION_STOP_PIN_TIMEOUT), ackfmt='H')[0]

    def get_stop_control_error_threshold(self, devId):
        """
        停止異常閾値を取得する[360/65536 * 度]
        """
        return self._rpc(MSG_TYPE_GET_PARAM_CMD, devId, payload=struct.pack('<B', PARAM_ID_STOP_CONTROL_ERROR_THRESHOLD), ackfmt='I')[0]

    def set_prot_stop_pin_timeout(self, devId, v):
        """
        保護停止ピンによる停止間上限[ms]を設定する
        """
        return self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<BH', PARAM_ID_PROTECTION_STOP_PIN_TIMEOUT, int(v)), ackfmt='')

    def set_stop_control_error_threshold(self, devId, v):
        """
        停止異常閾値を設定する
        """
        return self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<BI', PARAM_ID_STOP_CONTROL_ERROR_THRESHOLD, int(v)), ackfmt='')

    def reset(self, devId):
        """
        ソフトウェアリセットする
        """
        return self._rpc(MSG_TYPE_RESET_CMD, devId, ackfmt='')

    def debug(self, devId, mode):
        """
        デバッグイベント発生

        Parameters
        ----------

        devId : int
            デバイスID

        mode : int
            モード(0:none, 1:position, 2:velocity)

        """
        return self._rpc(MSG_TYPE_DEBUG_CMD, devId, payload=struct.pack('H', int(mode)), ackfmt='')

    def clear_log(self, devId):
        """
        devIdで指定されたBuildit Actuatorのログを消去する
        """
        return self._rpc(MSG_TYPE_CLEAR_LOG_CMD, devId, ackfmt='')

    def clear_power_on_time(self, devId):
        """
        devIdで指定されたBuildit Actuatorの累計通電時間を0リセットする

        Parameters
        ----------

        devId : int
            デバイスID

        """
        return self._rpc(MSG_TYPE_CLEAR_LIFE_LOG_CMD, devId, payload=struct.pack('<B', LIFE_LOG_PARAM_ID_POWER_ON_TIME), ackfmt='')

    def set_calibration_data(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの補正値を設定する
        """
        return self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<BH', PARAM_ID_CALIBRATION, int(v)), ackfmt='')

    def set_position_sys_offset(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの位置センサのシステムオフセットを設定する [360/65536 * 度]
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<BH', PARAM_ID_POSITION_SYS_OFFSET, int(v)), ackfmt='')

    def set_current_KP(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの電流制御用比例ゲインを設定する
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bh', PARAM_ID_CURRENT_KP, int(v)), ackfmt='')

    def set_current_KI(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの電流制御用積分ゲインを設定する
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bh', PARAM_ID_CURRENT_KI, int(v)), ackfmt='')

    def set_current_max_Iterm(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの電流制御用積分項の上限値を設定する
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bi', PARAM_ID_CURRENT_MAX_ITERM, int(v)), ackfmt='')

    def set_current_min_Iterm(self, devId, v):
        """
        devIdで指定されたBuildit Actuatorの電流制御用積分項の下限値を設定する
        """
        self._rpc(MSG_TYPE_SET_PARAM_CMD, devId, payload=struct.pack('<Bi', PARAM_ID_CURRENT_MIN_ITERM, int(v)), ackfmt='')

    def _get_servo_params(self, devId):

        unsafeparams = dict(
            PARAM_ID_CURRENT_KP = self.get_current_KP(devId),
            PARAM_ID_CURRENT_KI = self.get_current_KI(devId),
            PARAM_ID_CURRENT_MAX_ITERM = self.get_current_max_Iterm(devId),
            PARAM_ID_CURRENT_MIN_ITERM = self.get_current_min_Iterm(devId),
            PARAM_ID_CURRENT_MAX_LIMIT = self.get_current_max_limit(devId),
            PARAM_ID_CURRENT_MIN_LIMIT = self.get_current_min_limit(devId),
        )

        return dict(super()._get_servo_params(devId), **unsafeparams)

    def _set_servo_params(self, devId, params):

        self.set_current_KP(devId, params['PARAM_ID_CURRENT_KP'])
        self.set_current_KI(devId, params['PARAM_ID_CURRENT_KI']),
        self.set_current_max_Iterm(devId, params['PARAM_ID_CURRENT_MAX_ITERM']),
        self.set_current_min_Iterm(devId, params['PARAM_ID_CURRENT_MIN_ITERM']),

        super()._set_servo_params(devId, params)
