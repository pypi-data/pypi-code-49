# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 15:37
# @Author  : liugang
# @Email   : liugang0814@126.com
# @File    : zllrp_dummy_test.py
# @Software: PyCharm
from ZLLRP.compat import PY3

DeviceEventNotification_bstr = "30 31 FF FF FF FF FF FF 01 01 2E 00 00 00 12 00 00 00 00 " \
                               "01 2D 00 08 00 05 9D CF 33 01 26 DE 01 32 00 02 00 00"
GetVersionAck_Boot_bstr = "30 31 FF FF FF FF FF FF 01 02 BD 00 00 00 24 00 00 00 37 01 2C 00 06 00 00 00 00 00 00 " \
                          "02 BC 00 09 00 04 01 14 01 00 B0 00 00 02 BC 00 09 00 04 01 14 01 00 20 00 00"
GetVersionAck_Sys_bstr = "30 31 FF FF FF FF FF FF 01 02 BD 00 00 00 24 00 00 00 38 01 2C 00 06 00 00 00 00 00 00 " \
                         "02 BC 00 09 00 04 01 14 03 00 B0 00 00 02 BC 00 09 00 04 01 14 03 00 00 00 00"
GetVersionAck_Sec_bstr = "30 31 FF FF FF FF FF FF 01 02 BD 00 00 00 19 00 00 00 39 01 2C 00 06 00 00 00 00 00 00 " \
                         "02 BC 00 0B 00 06 00 10 00 03 00 63 B0 00 00"
DiagnosticTestAck_bstr = "30 31 FF FF FF FF FF FF 01 02 E5 00 00 00 4E 00 00 00 3A 01 2C 00 06 00 00 00 00 00 00 " \
                         "02 E5 00 0D 00 02 00 00 00 00 02 E7 00 03 01 00 78 02 E5 00 0D 00 02 00 00 00 00 " \
                         "02 E7 00 03 02 00 CB 02 E5 00 0D 00 02 00 00 00 00 02 E7 00 03 03 00 CE " \
                         "02 E5 00 0D 00 02 00 00 00 00 02 E7 00 03 04 00 CC"
GetDeviceConfigAck_Ident_bstr = "30 31 FF FF FF FF FF FF 01 02 95 00 00 00 19 00 00 00 3B " \
                                "01 2C 00 06 00 00 00 00 00 00 02 99 00 0B 00 09 7A 6C 69 74 73 36 37 33 30"
GetDeviceConfigAck_Event_bstr = "30 31 FF FF FF FF FF FF 01 02 95 00 00 00 2A 00 00 00 3C " \
                                "01 2C 00 06 00 00 00 00 00 00 02 94 00 1C 02 95 00 03 00 00 00 " \
                                "02 95 00 03 00 01 80 02 95 00 03 00 02 00 02 95 00 03 00 03 00"
GetDeviceConfigAck_Sec_bstr = "30 31 FF FF FF FF FF FF 01 02 95 00 00 00 35 00 00 00 3D " \
                              "01 2C 00 06 00 00 00 00 00 00 02 AC 00 27 02 AD 00 23 " \
                              "02 AE 00 08 00 00 01 C4 C0 B0 09 3A 02 AF 00 0A 00 08 52 41 02 00 03 00 05 02 " \
                              "02 B0 00 05 00 00 00 0F A0"

GetDeviceConfigAck_Comm_bstr = "30 31 FF FF FF FF FF FF 01 02 95 00 00 00 A9 00 00 00 3D " \
                               "01 2C 00 06 00 00 00 00 00 00 02 9C 00 9B 02 9D 00 16 00 " \
                               "02 9E 00 05 01 00 00 0B B8 02 9F 00 08 01 00 02 A2 00 02 13 DC " \
                               "02 9D 00 16 00 02 9E 00 05 01 00 00 0B B8 02 9F 00 08 01 00 02 A2 00 02 17 C4 " \
                               "02 9D 00 11 02 02 9E 00 05 00 00 00 0B B8 02 A3 00 03 01 00 00 " \
                               "02 A5 00 12 00 C0 A8 FF FB FF FF FF F8 C0 A8 FF F9 00 00 00 00 00 " \
                               "02 A8 00 02 01 03 02 A7 00 32 00 00 00 03 02 A1 00 13 00 00 04 C0 " \
                               "A8 00 02 57 47 44 47 54 49 5A 2D 30 33 37 36 02 A1 00 13 00 00 04 C0 A8 " \
                               "00 01 AA AA AA AA AA AA AA AA AA AA AA AA"

GetDeviceConfigAck_Alm_bstr = "30 31 FF FF FF FF FF FF 01 02 95 00 00 00 15 00 00 00 3E " \
                              "01 2C 00 06 00 00 00 00 00 00 02 9A 00 07 FF 02 9B 00 02 5F D8"

GetDeviceConfigAck_AntProp_bstr = "30 31 FF FF FF FF FF FF 01 02 95 00 00 00 2A 00 00 00 3F " \
                                  "01 2C 00 06 00 00 00 00 00 00 02 96 00 04 80 01 00 00 " \
                                  "02 96 00 04 00 02 00 00 02 96 00 04 00 03 00 00 02 96 00 04 00 04 00 00"

GetDeviceConfigAck_AntConf_bstr = "30 31 FF FF FF FF FF FF 01 02 95 00 00 00 56 00 00 00 40 " \
                                  "01 2C 00 06 00 00 00 00 00 00 " \
                                  "02 97 00 0F 01 00 00 00 01 00 0A 00 00 00 01 00 01 00 00 " \
                                  "02 97 00 0F 02 00 00 00 01 00 0A 00 01 00 05 00 01 00 01 " \
                                  "02 97 00 0F 03 00 00 00 01 00 0A 00 01 00 05 00 01 00 01 " \
                                  "02 97 00 0F 04 00 00 00 01 00 0A 00 01 00 05 00 01 00 01"


def bstr_to_bytes(bstr):
    bstr_list = bstr.split(" ")

    if PY3:
        ret_str = bytes(map(lambda x: int(x, base=16), bstr_list))
    else:
        ret_str = ""
        for bs in bstr_list:
            ret_str += chr(int(bs, base=16))
    return ret_str


if __name__ == '__main__':
    print(bstr_to_bytes(GetDeviceConfigAck_Sec_bstr))
