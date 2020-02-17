# -*- coding: utf-8 -*-
# @Time    : 2017/3/11 15:44
# @Author  : Liu Gang
# @Site    : 
# @File    : ratb5.py
# @Software: PyCharm Community Edition
import socket
import struct
import logging.config
import ctypes
import time
from pyvat.compat import stdin_input, PY_VER, chrtobyte, sleep, compat_socket, gettime
from pyvat.vatbase import LOGGER_PATH
from math import modf

"""
modification history
--------------------
V1.00.00, 18May2018, Liu Gang written
V1.00.01, 12Jun2019, Liu Gang ,Add T900
V1.00.02, 06Aug2019, Liu Gang ,Add T900 RSSI Test
V1.00.03, 17Feb2020, Liu Gang ,Add T900 RSSI Test
--------------------
"""
RATB5_VER = "V1.00.03"

_ADDR = ("10.86.20.223", 8001)

RATB_DATT1_T900 = 0x02  # Bit0~5, datt N1, Bit6~11, datt N2
RATB_DATT2_T900 = 0x03  # Bit0~5, datt N5, Bit6~11, datt N3
RATB_DATT3 = 0x04
RATB_GPIO_VALUE = 0x09
RATB_GPIO_DIR = 0x10
RATB_ANT_SEL = 0x1A
RATB_INS_SEL = 0x1B
RATB_CODE_SEL = 0x1D
RATB_RATE_SEL = 0x1E
RATB_DATT_CFG = 0x1F
RATB_SEND_EN = 0x1C
RATB_FRAME_CNT = 0x20
RATB_FRAME_GAP = 0x21
RATB_RELAY_STAT = 0x22
RATB_PROTOCOL_SEL = 0x23
RATB_RS485_SEL = 0x25  # 0 for 6700, 1 for 6710. default 0

RATB_MOD1_EN = 0x28
RATB_MOD2_EN = 0x29
RATB_LNA_EN = 0x30
RATB_TX_DAC_SLEEP = 0x40
RATB_RX_DAC_SLEEP = 0x41
RATB_DAC_PHASE = 0x42
RATB_RX_K0 = 0x43
RATB_TX_K0 = 0x44
RATB_PLL_DATA_H = 0x50
RATB_PLL_DATA_L = 0x51
RATB_PLL_TRIG = 0x52
RATB_PLL_READY = 0x53
RATB_PLL_UNLOCK = 0x54
RATB_PLL_CE = 0x55
RATB_MOD_PD = 0x56
RATB_MOD_PD_RX = 0x57

RATB_EEPROM_W_CS = 0x60
RATB_EEPROM_R_CS = 0x61
RATB_EEPROM_ADDR = 0x62
RATB_EEPROM_W_DATA = 0x65
RATB_EEPROM_WP = 0x68
RATB_EEPROM_R_DATA = 0x69

RATB_PWR_FREQ = 0x70  # high 8bis for freq band, low 8bits for freq point
RATB_PWR_LEVEL = 0x71  # Power Value
RATB_PWR_EN = 0x72

RATB_ADC_VOL = 0x73  # Get ADC Voltage
RATB_DET_PWR = 0x74  # Get Power

RATB_RTC_CONF = 0x75  # RTC Config

RATB_SERIAL_LP = 0x80

PWR_FREQ_800 = 0x55
PWR_FREQ_900 = 0xAA

ANT_INS_SA = 1
ANT_INS_SG = 2

MAX_PLL_CHECK = 20
MX2541_R7_VAL = 0x00000017
MX2541_R13_VAL = 0x0000008d
MX2541_R12_VAL = 0x0000001c
MX2541_R9_VAL = 0x28001409
MX2541_R8_VAL = 0x0111ce58
MX2541_R6_VAL = 0x001f3326
MX2541_R5_VAL = 0xa0000005
MX2541_R3_VAL = 0x0d806003
MX2541_R2_VAL = 0x04000642

MX2541_R4_VAL_800 = 0x88043284
MX2541_R1_VAL_800 = 0x00051401
MX2541_R0_VAL_800 = 0x000067f0

MX2541_R4_VAL_900 = 0x88043264
MX2541_R1_VAL_900 = 0x00040d01
MX2541_R0_VAL_900 = 0x0000eff0

T800 = 0
T900 = 1
T1000 = 2
# EEPROM offset
CALI_CNT_OFFSET = 0xf
CALI_TABLE_OFFSET = 0x10


class TagRatbMsg:
    def __init__(self):
        self.ucRW = 0x00
        self.ucAddr = 0x00
        self.ucHData = 0x00
        self.ucLData = 0x00


class RATB5:
    def __init__(self):
        # self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s = compat_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.req = TagRatbMsg()
        self.rev = TagRatbMsg()
        self.pll_cfg_flag = True
        self.pll_cfg_freq = 0
        self.datt1 = 13.0
        self.power_table = list()
        logging.config.fileConfig(LOGGER_PATH)
        self.logger = logging.getLogger("ratb")

        self.ratb_ver = T800  # T800 0, T900 1, T1000 2

    def __del__(self):
        self.s.close()

    def set_ratb_ver(self, ver):
        """
        Set Version
        :param ver: 0, T800; 1, T900
        :return:None
        """
        ver_list = ["T800", "T900", "T1000"]
        self.ratb_ver = ver
        self.logger.debug("Set RATB Type:{0}".format(ver_list[ver]))

    def msg_gen(self, addr, data=0x00, mod=1):
        if mod == 1:
            self.req.ucRW = 0xC0
            self.req.ucAddr = addr
            self.req.ucHData = (data >> 8) & 0xFF
            self.req.ucLData = data & 0xFF
        if mod == 0:
            self.req.ucRW = 0xA0
            self.req.ucAddr = addr
            self.req.ucHData = 0x00
            self.req.ucLData = 0x00

        req_list = list()
        req_list.append(self.req.ucRW)
        req_list.append(self.req.ucAddr)
        req_list.append(self.req.ucHData)
        req_list.append(self.req.ucLData)
        for x in range(28):
            req_list.append(0x00)

        return chrtobyte(req_list)

    def rev_gen(self, data_list):
        self.rev.ucRW = data_list[0]
        self.rev.ucAddr = data_list[1]
        self.rev.ucHData = data_list[2]
        self.rev.ucLData = data_list[3]

    def data_read(self, tsec):
        self.s.settimeout(tsec)
        try:
            data, addr = self.s.recvfrom(1024)
            ret_list = []
            if PY_VER == 3:
                for s in data:
                    ret_list.append(s)
            else:
                for s in data:
                    ret_list.append(struct.unpack('B', s)[0])
            # self.logger.debug(ret_list)
            return ret_list
        except Exception as e:
            self.logger.debug(e.args[0])
            return None

    def send_msg(self, addr, data, timeout=1):
        global _ADDR
        c = self.s.sendto(self.msg_gen(addr, data), _ADDR)
        if c <= 0:
            self.logger.debug("Fail")
            return False

        if self.ratb_ver == T1000:
            revlist = self.data_read(timeout)
            if revlist is None:
                return False
            else:
                self.rev_gen(revlist)
                if self.rev.ucAddr != addr:
                    return False

    def query_msg(self, addr, timeout=1):
        global _ADDR
        c = self.s.sendto(self.msg_gen(addr, mod=0), _ADDR)
        if c <= 0:
            self.logger.debug("Send Fail")
            return None

        revlist = self.data_read(timeout)
        if revlist is None:
            return None
        else:
            self.rev_gen(revlist)

        return (self.rev.ucHData << 8) | self.rev.ucLData

    def sw_ant(self, ant, ins):
        """
        181218 Liugang Add T900
        :param ant: Ant Number
        :param ins: Instrument Code
        :return:
        """
        if self.ratb_ver == T800:
            self.send_msg(RATB_ANT_SEL, 0x01 << (ant - 1))
        elif self.ratb_ver == T900:
            ant_list = [0x02, 0x03, 0x00, 0x01]
            self.send_msg(RATB_ANT_SEL, ant_list[ant - 1])
        elif self.ratb_ver == T1000:
            self.send_msg(RATB_ANT_SEL, ant)

        sleep(0.02)
        self.send_msg(RATB_INS_SEL, ins)
        sleep(0.02)

    def set_gpio(self, value):
        self.send_msg(RATB_GPIO_DIR, 0x01)  # set GPIO output dir
        sleep(0.02)
        self.send_msg(RATB_GPIO_VALUE, value)
        sleep(0.02)

    def read_gpio(self):
        self.send_msg(RATB_GPIO_DIR, 0x00)  # set GPIO input dir
        sleep(0.02)
        return self.query_msg(RATB_GPIO_VALUE, 5)  # read GPIO value ,5s timeout

    def set_rssi_rate(self, rate):
        # req = 0x00
        if rate == 64:
            req = 0x01
        elif rate == 174:
            req = 0x02
        elif rate == 320:
            req = 0x04
        elif rate == 640:
            req = 0x08
        elif rate == 160:
            req = 0x09
        elif rate == 274:
            req = 0x0B
        elif rate == 80:
            req = 0x0A
        else:
            return False

        self.send_msg(RATB_RATE_SEL, req)
        return True

    def set_frame_gap(self, gap):
        self.send_msg(RATB_FRAME_GAP, gap)
        return True

    def set_protocol(self, pro):
        """

        :param pro:1 , 6C   .2, HangBiao
        :return:
        """
        self.send_msg(RATB_PROTOCOL_SEL, pro)
        return True

    def set_rssi_code(self, code):
        """

        :param code: 1,FM0 2,Miller2
        :return:
        """
        self.send_msg(RATB_CODE_SEL, code)
        return True

    def set_rssi_datt(self, datt):
        self.send_msg(RATB_DATT_CFG, datt)
        return True

    def set_frame_cnt(self, cnt):
        self.send_msg(RATB_FRAME_CNT, cnt)
        return True

    def rssi_send_en(self):
        self.send_msg(RATB_SEND_EN, 0x01)
        return True

    def datt_cal(self, datt=float()):
        """

        :param datt: dbm to  attenuate
        :return:datt config for RATB5
        """
        f_datt = self.datt1
        i_target0 = int(f_datt)
        hdatt = i_target0 << 1
        f_gap0 = f_datt - i_target0
        if f_gap0 >= 0.75:
            hdatt += 2
        elif 0.75 > f_gap0 >= 0.25:
            hdatt += 1
        hdatt = ~hdatt & 0xff
        hdatt &= 0x3f

        datt -= f_datt

        i_target = int(datt)
        ldatt = i_target << 1
        f_gap = datt - i_target
        if f_gap >= 0.75:
            ldatt += 2
        elif 0.75 > f_gap >= 0.25:
            ldatt += 1
        ldatt = ~ldatt & 0xff
        ldatt &= 0x3f

        return ((hdatt << 6) | ldatt) & 0xfff

    def rs485_sel(self, sel):
        """
        Sel Rs485 test mode
        :param sel:1 for 6710, 0 is default,for 6700
        :return:
        """
        self.send_msg(RATB_RS485_SEL, sel)
        return True

    def set_eeprom(self, woffset, wdatalen, data):
        """

        :param woffset:
        :param wdatalen:
        :param data:
        :return:
        """
        if wdatalen == 1:
            try:
                data = data[0]
            except Exception:
                pass

            self.send_msg(RATB_EEPROM_ADDR, woffset)
            sleep(0.001)
            self.send_msg(RATB_EEPROM_W_DATA, data)
            sleep(0.001)
            self.send_msg(RATB_EEPROM_W_CS, 0x00)
            sleep(0.001)
            self.send_msg(RATB_EEPROM_W_CS, 0x01)
            self.logger.debug("EEPROM W--Offset:0x%03X,Len:%d,Data:%02X" % (woffset, wdatalen, data))
        else:
            eedata = ""
            for offset in range(wdatalen):
                c_offset = woffset + offset
                c_data = data[offset]
                self.send_msg(RATB_EEPROM_ADDR, c_offset)
                sleep(0.001)
                self.send_msg(RATB_EEPROM_W_DATA, c_data)
                sleep(0.001)
                self.send_msg(RATB_EEPROM_W_CS, 0x00)
                sleep(0.001)
                self.send_msg(RATB_EEPROM_W_CS, 0x01)
                eedata += "{0:02X}".format(data[offset])
                sleep(0.001)

            self.logger.debug("EEPROM W--Offset:%03X,Len:%d,Data:%s" % (woffset, wdatalen, eedata))

    def get_eeprom(self, woffset, wdatalen):
        ret_list = list()
        eedata = ""
        for offset in range(wdatalen):
            c_offset = woffset + offset
            self.send_msg(RATB_EEPROM_ADDR, c_offset)
            sleep(0.001)
            self.send_msg(RATB_EEPROM_R_CS, 0x00)
            sleep(0.001)
            self.send_msg(RATB_EEPROM_R_CS, 0x01)
            sleep(0.001)
            ret = self.query_msg(RATB_EEPROM_R_DATA)
            if ret is None:
                return False
            else:
                ret_list.append(ret)
                sleep(0.001)
                eedata += "{0:02X}".format(ret)

        self.logger.debug("EEPROM R--Offset:0x%03X,Len:%d,Data:%s" % (woffset, wdatalen, eedata))
        if wdatalen == 1:
            ret_list = ret_list[0]
        return ret_list

    def send_check(self, addr, data):
        self.send_msg(addr, data)
        ret = self.query_msg(addr)
        if ret != data:
            return False
        else:
            return True

    def pll_reg_cfg(self, dw_data):
        check_times = 0
        self.send_msg(RATB_PLL_DATA_H, dw_data >> 16)
        self.send_msg(RATB_PLL_DATA_L, dw_data & 0xffff)
        self.send_msg(RATB_PLL_TRIG, 0x00)
        self.send_msg(RATB_PLL_TRIG, 0x01)
        self.logger.debug("Config PLL REG,0x{0:08X}".format(dw_data))
        ret = 0
        while ret != 1 and check_times < MAX_PLL_CHECK:
            ret = self.query_msg(RATB_PLL_READY)
            sleep(0.2)
            check_times += 1

        if check_times >= MAX_PLL_CHECK:
            self.logger.error("PLL REG Config check {0} times, Fail!".format(check_times))
            return False
        else:
            self.logger.debug("PLL REG Config check {0} times, Success!".format(check_times))
            return True

    def pll_chip_cfg(self, dw_freq, b_need_rst=True):
        """

        :param dw_freq:
        :param b_need_rst:
        :return:
        """

        if dw_freq == self.pll_cfg_freq:
            self.logger.debug("Alread Config Freq {0}".format(dw_freq))
        else:
            if b_need_rst:
                self.pll_reg_cfg(MX2541_R7_VAL)
                self.pll_reg_cfg(MX2541_R13_VAL)
                self.pll_reg_cfg(MX2541_R12_VAL)
                self.pll_reg_cfg(MX2541_R9_VAL)
                self.pll_reg_cfg(MX2541_R8_VAL)
                self.pll_reg_cfg(MX2541_R6_VAL)
                self.pll_reg_cfg(MX2541_R5_VAL)
                if dw_freq > 900000:
                    self.pll_reg_cfg(MX2541_R4_VAL_900)
                else:
                    self.pll_reg_cfg(MX2541_R4_VAL_800)
                self.pll_reg_cfg(MX2541_R3_VAL)
                self.pll_reg_cfg(MX2541_R2_VAL)

            f_frac = float(dw_freq) * 3 / 125
            pll_n = int(f_frac)
            r0_data = pll_n << 4 & 0xffff
            # if dw_freq > 900000:
            #     pll_r = 26000 / 125
            # else:
            #     pll_r = 40000 / 125
            pll_r = 26000 / 125

            r1_data = ((pll_n & 0xf000) << 4) | (pll_r << 4) | 0x01
            self.logger.debug("pll_n:0x{0:04X},r0:{1:08X},r1:{2:08X}".format(pll_n, r0_data, r1_data))
            self.pll_reg_cfg(r1_data)
            self.pll_reg_cfg(r0_data)

        ret = 0
        check_times = 0
        while ret != 1 and check_times < MAX_PLL_CHECK:
            ret = self.query_msg(RATB_PLL_UNLOCK)
            sleep(0.2)
            check_times += 1

        if check_times >= MAX_PLL_CHECK:
            self.logger.error("PLL Lock check {0} times, Fail!".format(check_times))
            self.pll_cfg_flag = True
            return False
        else:
            self.pll_cfg_freq = dw_freq
            self.pll_cfg_flag = False
            self.logger.debug("PLL Lock check {0} times, Success!".format(check_times))
            return True

    def pll_chip_en(self, reg_data):
        self.send_msg(RATB_PLL_CE, reg_data)
        self.logger.debug("Set PLL CE:0x{0:02X}".format(reg_data))

    def lna_chip_en(self, reg_data):
        self.send_msg(RATB_LNA_EN, reg_data)
        self.logger.debug("Set LNA EN:0x{0:02X}".format(reg_data))

    def mod_pd(self, reg_data):
        self.send_msg(RATB_MOD_PD, reg_data)
        self.logger.debug("Set MOD PD:0x{0:02X}".format(reg_data))

    def rx_mod_pd(self, reg_data):
        self.send_msg(RATB_MOD_PD_RX, reg_data)
        self.logger.debug("Set RX MOD PD:0x{0:02X}".format(reg_data))

    def set_tx_dac_sleep(self, sleep_en):
        self.send_msg(RATB_TX_DAC_SLEEP, sleep_en)
        self.logger.debug("Set TX DAC Sleep:{0}".format(sleep_en))

    def set_rx_dac_sleep(self, sleep_en):
        self.send_msg(RATB_RX_DAC_SLEEP, sleep_en)
        self.logger.debug("Set RX DAC Sleep:{0}".format(sleep_en))

    def set_datt_n1(self, att_val):
        ret = self.query_msg(RATB_DATT1_T900)
        if ret is None:
            self.logger.error("DATT0 Reg Read Fail!")
            return False

        datt_n2 = (ret >> 6) & 0x3f

        i_target = int(att_val)
        datt_n1 = i_target << 1
        f_gap = att_val - i_target
        if f_gap >= 0.75:
            datt_n1 += 2
        elif 0.75 > f_gap >= 0.25:
            datt_n1 += 1
        datt_n1 = ~datt_n1 & 0xff
        datt_n1 &= 0x3f
        datt_val = ((datt_n2 << 6) | datt_n1) & 0xfff
        self.logger.debug("datt_n2:{1:06b}, datt_n1:{0:06b}".format(datt_n1, datt_n2))
        self.send_msg(RATB_DATT1_T900, datt_val)

    def set_datt_n2(self, att_val):
        ret = self.query_msg(RATB_DATT1_T900)
        if ret is None:
            self.logger.error("DATT0 Reg Read Fail!")
            return False
        # b' 0000 0011 1111
        datt_n1 = ret & 0x03f

        i_target = int(att_val)
        datt_n2 = i_target << 1
        f_gap = att_val - i_target
        if f_gap >= 0.75:
            datt_n2 += 2
        elif 0.75 > f_gap >= 0.25:
            datt_n2 += 1
        datt_n2 = ~datt_n2 & 0xff
        datt_n2 &= 0x3f
        datt_val = ((datt_n2 << 6) | datt_n1) & 0xfff
        self.logger.debug("datt_n2:{1:06b}, datt_n1:{0:06b}".format(datt_n1, datt_n2))
        self.send_msg(RATB_DATT1_T900, datt_val)

    def set_datt_n3(self, att_val):
        ret = self.query_msg(RATB_DATT2_T900)
        if ret is None:
            self.logger.error("DATT1 Reg Read Fail!")
            return False
        # b' 0000 0011 1111
        datt_n5 = ret & 0x03f

        i_target = int(att_val)
        datt_n3 = i_target << 1
        f_gap = att_val - i_target
        if f_gap >= 0.75:
            datt_n3 += 2
        elif 0.75 > f_gap >= 0.25:
            datt_n3 += 1
        datt_n3 = ~datt_n3 & 0xff
        datt_n3 &= 0x3f
        datt_val = ((datt_n3 << 6) | datt_n5) & 0xfff
        self.logger.debug("datt_n3:{1:06b}, datt_n5:{0:06b}".format(datt_n5, datt_n3))
        self.send_msg(RATB_DATT2_T900, datt_val)

    def set_datt_n5(self, att_val):
        ret = self.query_msg(RATB_DATT2_T900)
        if ret is None:
            self.logger.error("DATT1 Reg Read Fail!")
            return False

        datt_n3 = (ret >> 6) & 0x3f

        i_target = int(att_val)
        datt_n5 = i_target << 1
        f_gap = att_val - i_target
        if f_gap >= 0.75:
            datt_n5 += 2
        elif 0.75 > f_gap >= 0.25:
            datt_n5 += 1
        datt_n5 = ~datt_n5 & 0xff
        datt_n5 &= 0x3f
        datt_val = ((datt_n3 << 6) | datt_n5) & 0xfff
        self.logger.debug("datt_n3:{1:06b}, datt_n5:{0:06b}".format(datt_n5, datt_n3))
        self.send_msg(RATB_DATT2_T900, datt_val)

    def set_tx_k0(self, k0_val):
        self.send_msg(RATB_TX_K0, k0_val)
        self.logger.debug("Set Tx K0:0x{0:04X}".format(k0_val))

    def set_rx_k0(self, k0_val):
        self.send_msg(RATB_RX_K0, k0_val)
        self.logger.debug("Set Tx K0:0x{0:04X}".format(k0_val))

    def set_dac_phase(self, phase):
        self.send_msg(RATB_DAC_PHASE, phase)
        self.logger.debug("Set DAC Phase:{0}".format(phase))

    def get_power_config(self, power_val):
        """
        :param power_val: -8 ~ 15
        :return:
        """
        if power_val > 15 or power_val < -8:
            self.logger.error("Power Set Out of Range!{0}".format(power_val))
            return False

        power_table = self.power_table
        power_step_list = [x[0] for x in power_table]
        # print(power_step_list)

        diff = 15
        config_step = 0
        for step in power_step_list:
            cal_diff = abs(power_val - step)
            if cal_diff < diff:
                diff = cal_diff
                config_step = step

        set_k0 = power_table[power_step_list.index(config_step)][1]
        set_datt = power_table[power_step_list.index(config_step)][2]
        config_diff = power_val - config_step
        float_diff = config_diff - int(config_diff)
        if abs(float_diff) > 0.5:
            if float_diff > 0:
                set_datt = set_datt - int(config_diff) - 0.5
                set_k0 = set_k0 + (float_diff - 0.5) * 10 * 0x100  # K0 0x100 ~ 0.1dB
            else:
                set_datt = set_datt - int(config_diff) + 0.5
                set_k0 = set_k0 + (float_diff + 0.5) * 10 * 0x100  # K0 0x100 ~ 0.1dB
        else:
            set_datt = set_datt - int(config_diff)
            set_k0 = set_k0 + float_diff * 10 * 0x100
        set_k0 = int(set_k0)
        self.logger.debug("Power:{0},Set K0:0x{1:04X},Datt:{2}".format(power_val, set_k0, set_datt))
        return [set_k0, set_datt]

    def set_cali_cnt(self, cnt):
        self.set_eeprom(CALI_CNT_OFFSET, 1, cnt)
        self.logger.debug("Calibration Cnt Set: {0}".format(cnt))

    def get_cali_cnt(self):
        ret = self.get_eeprom(CALI_CNT_OFFSET, 1)
        if ret is False:
            self.logger.error("Calibration Cnt Get Fail!")
            return False
        self.logger.debug("Calibration Cnt Get: {0}".format(ret))
        return ret

    def set_cali_table(self, index, power, k0, datt):
        max_index = self.get_cali_cnt() - 1
        if index > max_index:
            return False

        if power < 0:
            power_i = abs(int(power)) | 0x80
            power_f = 0 - 100 * round(modf(power)[0], 2)
        else:
            power_i = int(power)
            power_f = 100 * round(modf(power)[0], 2)

        power_f = int(power_f)

        k0_h = (k0 >> 8) & 0xff
        k0_l = k0 & 0xff

        datt_i = int(datt)
        datt_f = 100 * (datt - datt_i)
        datt_f = int(datt_f)

        value_list = [power_i, power_f, k0_h, k0_l, datt_i, datt_f]
        self.set_eeprom(CALI_TABLE_OFFSET + 6 * index, len(value_list), value_list)
        self.logger.debug("Set Calibration table:{0},{1},0x{2:04X},{3:.2f}".format(index, power, k0, datt))

    def get_cali_talbe(self):
        cnt = self.get_eeprom(CALI_CNT_OFFSET, 1)
        if cnt is False:
            return False
        power_table_list = list()
        for index in range(cnt):
            ret_list = self.get_eeprom(CALI_TABLE_OFFSET + 6 * index, 6)
            if ret_list is False:
                return False
            if (ret_list[0] >> 7) & 0x01 == 1:
                # self.logger.debug("It's a minus!")
                ret_list[0] = 0 - (ret_list[0] & 0x7f)
                p_float = 0 - float(ret_list[1]) / 100
            else:
                p_float = float(ret_list[1]) / 100

            cali_list = [ret_list[0] + p_float, (ret_list[2] << 8) | ret_list[3],
                         ret_list[4] + float(ret_list[5]) / 100]

            power_table_list.append(cali_list)

        return power_table_list

    def set_rx_mod1_en(self, mod_en):
        """
        01: MOD
        10: NOMOD
        :param mod_en:
        :return:
        """
        self.send_msg(RATB_MOD1_EN, mod_en)
        self.logger.debug("Set Rx MOD1 EN:{0}".format(mod_en))

    def set_rx_mod2_en(self, mod_en):
        """
        10: MOD
        01: NOMOD
        :param mod_en:
        :return:
        """
        self.send_msg(RATB_MOD2_EN, mod_en)
        self.logger.debug("Set Rx MOD2 EN:{0}".format(mod_en))

    def set_datt1(self, att_val):
        i_target = int(att_val)
        datt_n = i_target << 1
        f_gap = att_val - i_target
        if f_gap >= 0.75:
            datt_n += 2
        elif 0.75 > f_gap >= 0.25:
            datt_n += 1
        datt_n = ~datt_n & 0xff
        datt_n &= 0x3f
        self.logger.debug("set datt_n1:{0:06b}".format(datt_n))
        self.send_msg(RATB_DATT1_T900, datt_n)

    def set_datt2(self, att_val):
        i_target = int(att_val)
        datt_n = i_target << 1
        f_gap = att_val - i_target
        if f_gap >= 0.75:
            datt_n += 2
        elif 0.75 > f_gap >= 0.25:
            datt_n += 1
        datt_n = ~datt_n & 0xff
        datt_n &= 0x3f
        self.logger.debug("set datt_n2:{0:06b}".format(datt_n))
        self.send_msg(RATB_DATT2_T900, datt_n)

    def set_datt3(self, att_val):
        i_target = int(att_val)
        datt_n = i_target << 1
        f_gap = att_val - i_target
        if f_gap >= 0.75:
            datt_n += 2
        elif 0.75 > f_gap >= 0.25:
            datt_n += 1
        datt_n = ~datt_n & 0xff
        datt_n &= 0x3f
        self.logger.debug("set datt_n3:{0:06b}".format(datt_n))
        self.send_msg(RATB_DATT3, datt_n)

    def get_datt3(self):
        datt_n = self.query_msg(RATB_DATT3)
        self.logger.debug("get datt_n3:{0:06b}".format(datt_n))

    def get_adc_voltage(self):
        vol = self.query_msg(RATB_ADC_VOL)
        self.logger.debug("Get Voltage:{0}".format(vol))
        return vol

    def detect_power(self):
        pwr = ctypes.c_int16(self.query_msg(RATB_DET_PWR)).value
        self.logger.debug("Power Detected:{0}".format(pwr))
        print(type(pwr), pwr)
        return pwr

    def set_pwr_freq(self, freq_band, freq_point):
        """

        :param freq_band:
        :param freq_point:
        :return:
        """
        self.send_msg(RATB_PWR_FREQ, (freq_band << 8) | (freq_point & 0xff))

    def set_pwr_level(self, power_value):
        """

        :param power_value: 1dBm = 1000
        :return:
        """
        power_value = power_value
        self.send_msg(RATB_PWR_LEVEL, power_value)

    def set_pwr_onoff(self, onoff):
        """

        :param onoff: 1 On, 0 Off
        :return:
        """
        self.send_msg(RATB_PWR_EN, onoff)

    def clear_serial_buf(self):
        self.send_msg(RATB_SERIAL_LP, 0)

    def rtc_conf(self):
        time_data = time.localtime(time.time())
        self.send_msg(RATB_RTC_CONF, 0x3000 | time_data.tm_sec)
        self.send_msg(RATB_RTC_CONF, 0x2000 | time_data.tm_min)
        self.send_msg(RATB_RTC_CONF, 0x1000 | time_data.tm_hour)

        self.send_msg(RATB_RTC_CONF, 0x0300 | time_data.tm_mday)
        self.send_msg(RATB_RTC_CONF, 0x0200 | time_data.tm_mon)
        self.send_msg(RATB_RTC_CONF, 0x0100 | (time_data.tm_year - 2000))


def signal_gen():
    ue = RATB5()
    ue.set_ratb_ver(T900)
    ret = ue.query_msg(RATB_GPIO_VALUE)
    if ret is None:
        ue.logger.error("no response,please check connection.")
        return

    ue.logger.debug("RATB Connect success!")
    disp_power_table(ue)
    while True:
        print("1, Set K0.\n2, Set Datt.\n3, Set Freq.\n4, PA ONOFF.\n5, Power Out Test.\n0, Exit.")
        sel = input("Input your selection:")
        if sel == 0:
            ue.pll_chip_en(0x00)
            ue.lna_chip_en(0x00)
            break
        elif sel == 1:
            ret = ue.query_msg(RATB_TX_K0)
            k0 = stdin_input("Input K0(0x{0:04X}):0x".format(ret))
            k0 = int(k0, base=16)
            ue.set_tx_k0(k0)
        elif sel == 2:
            datt = stdin_input("Input Datt(dB):")
            datt = float(datt)
            ue.set_datt_n3(datt)
        elif sel == 3:
            def disp_freq(cfg_freq):
                if cfg_freq == 0:
                    return 922625
                else:
                    return cfg_freq

            freq = stdin_input("Input Freq({0:.3f}Mhz -> {1}):".format(float(disp_freq(ue.pll_cfg_freq)) / 1000,
                                                                       disp_freq(ue.pll_cfg_freq)))
            freq = int(freq)
            ue.pll_chip_en(0x01)
            ue.pll_chip_cfg(freq, ue.pll_cfg_flag)
        elif sel == 4:
            option = stdin_input("Input Operation, 0, OFF; 1, ON:")
            option = int(option)
            ue.lna_chip_en(option)
            ue.pll_chip_en(option)
        elif sel == 5:
            freq = stdin_input("Input Freq(922.265Mhz -> 922625):")
            freq = int(freq)
            power = stdin_input("Input the Power(-8~15):")
            power = float(power)
            ret_list = ue.get_power_config(power)
            if ret_list is False:
                print("Error!")
                stdin_input("Any Key to Continue!")
                continue
            ue.set_tx_k0(ret_list[0])
            ue.set_datt_n3(ret_list[1])
            ue.pll_chip_en(0x01)
            ue.pll_chip_cfg(freq, ue.pll_cfg_flag)
            ue.lna_chip_en(0x01)

    stdin_input("Any Key to Exit!")


def eeprom_test(ue):
    while True:
        print("1, EEPROM Read\n2, EEPROM Set\n0, Exit!")
        sel = input("Input your selection:")
        sel = int(sel)
        if sel == 0:
            break
        elif sel == 1:
            offset = stdin_input("Input The offset:0x")
            offset = int(offset, base=16)
            length = stdin_input("Input the Length:")
            length = int(length)
            ue.get_eeprom(offset, length)
        elif sel == 2:
            offset = stdin_input("Input The offset:0x")
            offset = int(offset, base=16)
            data_str = stdin_input("Input the data str(00 01 02 FF 0E):")
            data_list = data_str.split(" ")
            data_list = [int(data, base=16) for data in data_list]
            ue.set_eeprom(offset, len(data_list), data_list)


def disp_power_table(ue):
    table = ue.get_cali_talbe()

    if table is False:
        ue.logger.error("Tabel get error!")
        return False

    ue.power_table = table
    print("___________________________")
    print("Index\tPower\tK0    \tDatt")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    index = 0
    for values in table:
        print("{3}\t{0}\t0x{1:04X}\t{2:.2f}".format(values[0], values[1], values[2], index))
        index += 1
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")


def power_table_opr(ue):
    while True:
        print("1, Table Display\n2, Table Write\n0, Exit")
        sel = input("Input your selection:")
        sel = int(sel)
        if sel == 0:
            break
        elif sel == 1:
            ret = disp_power_table(ue)
            if ret is False:
                continue
            stdin_input("Any Key to Continue")
        elif sel == 2:
            while True:
                option = input(
                    "1, Write Power Count\n2, Write Power Calibraiton Values\n0, Exit\nInput your Selection:")
                option = int(option)
                if option == 0:
                    break
                elif option == 1:
                    pwr_cnt = input("Input the Power Count:")
                    ue.set_cali_cnt(pwr_cnt)
                elif option == 2:
                    pwr_cnt = ue.get_cali_cnt()
                    index_in = input("Input the Index(0~{0}):".format(pwr_cnt - 1))
                    power_in = stdin_input("Input the Power:")
                    power_in = float(power_in)
                    k0_in = stdin_input("Input the K0 Value:0x")
                    k0_in = int(k0_in, base=16)
                    datt_in = stdin_input("Input the Datt Value:")
                    datt_in = float(datt_in)
                    ue.set_cali_table(index_in, power_in, k0_in, datt_in)


def test_T1000():
    ue = RATB5()
    ue.set_ratb_ver(T1000)
    b_test = False
    while not b_test:
        ue.clear_serial_buf()
        sel_m = stdin_input(
            "1, DATT Config\n"
            "2, PLL Config\n"
            "3, GPIO Test\n"
            "4, Ant Select\n"
            "5, ADC Test\n"
            "6, EEPROM Test\n"
            "7, RSSI Test\n"
            "8, Time Config\n"
            "0, Exit\n"
            "Input your selection:")
        sel_m = int(sel_m)
        if sel_m == 1:
            while True:
                sel_n = int(stdin_input("1,DATT1\n"
                                        "2,DATT2\n"
                                        "3,DATT3\n"
                                        "0, Exit\n"
                                        "Input your selection:"))
                if sel_n == 0:
                    break
                datt_val = float(stdin_input("Input Att Value:"))
                if sel_n == 1:
                    ue.set_datt1(datt_val)
                elif sel_n == 2:
                    ue.set_datt2(datt_val)
                elif sel_n == 3:
                    ue.set_datt3(datt_val)
                print("DATT Config Success!")
        elif sel_m == 2:
            while True:
                sel_n = int(
                    stdin_input("1,Set Freq\n"
                                "2,Set Power Value\n"
                                "3,Set Power Onoff\n"
                                "0, Exit\n"
                                "Input your selection:"))
                if sel_n == 1:
                    freq_band = int(stdin_input("Input Freq Band 1=900Mhz, 0=800Mhz:"))
                    freq_point = int(stdin_input("Input Freq Point(0~19):"))
                    if (freq_band == 1 or freq_band == 0) and (0 <= freq_point <= 19):
                        band = PWR_FREQ_900 if freq_band == 1 else PWR_FREQ_800
                        ue.set_pwr_freq(band, freq_point)
                        print("Freq Set Success!")
                    else:
                        print("Input Value Error!")
                        break
                elif sel_n == 2:
                    power_value = int(stdin_input("Input power_value(-500~1800):"))
                    ue.set_pwr_level(power_value)
                    print("Set Power Value {0:.2f}".format(float(power_value) / 100))
                elif sel_n == 3:
                    onoff = int(stdin_input("Input Power Onoff selection, 1=ON, 0=OFF:"))
                    if onoff == 1:
                        ue.set_pwr_onoff(1)
                        print("Set Power On!")
                    else:
                        ue.set_pwr_onoff(0)
                        print("Set Power Off!")
                else:
                    break
        elif sel_m == 3:
            while True:
                sel_n = int(stdin_input("1,GPIO Read\n"
                                        "2,GPIO Set\n"
                                        "0, Exit\n"
                                        "Input your selection:"))
                if sel_n == 1:
                    value = ue.read_gpio()
                    print("GPIO Value Read:{0:08b}".format(value))
                elif sel_n == 2:
                    value = int(stdin_input("Input GPIO Set Value:0x"), 16)
                    ue.set_gpio(value)
                    print("GPIO Value Set to :{0:08b}".format(value))
                else:
                    break

        elif sel_m == 4:
            while True:
                sel_n = int(stdin_input("1,Switch ANT Port\n"
                                        "2,Switch Instrument\n"
                                        "0, Exit\n"
                                        "Input your selection:"))
                if sel_n == 1:
                    value = int(stdin_input("Input the ANT Number:"))
                    ue.send_msg(RATB_ANT_SEL, value)
                    print("ANT Port Switch to:{0}".format(value))
                elif sel_n == 2:
                    value = int(stdin_input("Input the Instrument ,1=SA,2=SG:"))
                    ue.send_msg(RATB_INS_SEL, value)
                    print("Instrument Switch to:{0}".format(value))
                else:
                    break
        elif sel_m == 5:
            while True:
                sel_n = int(stdin_input("1, Get Voltage\n"
                                        "2, Detect Power\n"
                                        "0, Exit\n"
                                        "Input your selection:"))
                if sel_n == 1:
                    ue.get_adc_voltage()
                elif sel_n == 2:
                    ue.detect_power()
                else:
                    break
        elif sel_m == 6:
            eeprom_test(ue)
        elif sel_m == 7:
            while True:
                sel_n = int(
                    stdin_input("1, Set Protocol\n"
                                "2, Set Code\n"
                                "3, Set Rate\n"
                                "4, Set Frame Count\n"
                                "5, Start Send Frame\n"
                                "0, Exit\n"
                                "Input your selection:"))
                if sel_n == 1:
                    sel = int(stdin_input("1, 6C\n2, HB\nInput Your Selection:"))
                    ue.set_protocol(sel)
                elif sel_n == 2:
                    sel = int(stdin_input("1, FM0\n2, MI2\nInput Your Selection:"))
                    ue.set_rssi_code(sel)
                elif sel_n == 3:
                    sel = int(stdin_input("Input the Rssi Rate:"))
                    ue.set_rssi_rate(sel)
                elif sel_n == 4:
                    sel = int(stdin_input("Input the Frame Count:"))
                    ue.set_frame_cnt(sel)
                elif sel_n == 5:
                    ue.rssi_send_en()
                else:
                    break
        elif sel_m == 8:
            ue.rtc_conf()
        else:
            break

    while b_test:
        sleep(5)
        print(gettime(2))
        print("rssi start")
        ue.set_rssi_rate(174)
        ue.set_rssi_code(2)
        ue.set_protocol(1)
        ue.set_frame_cnt(1000)
        ue.rssi_send_en()
        print("rssi end")
        print(gettime(2))


if __name__ == "__main__":
    test_T1000()
    # while True:
    #     sel_m = stdin_input("1, Signal Source Test\n2, EEPROM Test\n3, Power Table Opr\n0, Exit\nInput your selection:")
    #     sel_m = int(sel_m)
    #     if sel_m == 0:
    #         break
    #     elif sel_m == 1:
    #         signal_gen()
    #     elif sel_m == 2:
    #         eeprom_test()
    #     elif sel_m == 3:
    #         power_table_opr()
    #     elif sel_m == 4:
    #         test_T1000()
