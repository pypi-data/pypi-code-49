# -*- coding: utf-8 -*-
# @CreateTime : 2020/2/11
# @Author     : Liu Gang
# @File       : zllrp_func.py
# @Software   : PyCharm

import threading
import time
import logging
import socket
from logging import NullHandler
from queue import Queue, Empty
from ZLLRP.zllrp_prot_lib import ZLLRP
from ZLLRP.compat import iterkeys, conv_bytes_str
from copy import deepcopy

logging.getLogger("ZllrpMsg").addHandler(NullHandler())

class TcpClient(object):
    def __init__(self, ip, port):
        self.dev_ip = ip
        self.dev_port = port
        self.dev_addr = (self.dev_ip, int(self.dev_port))
        self.dev_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建TCP客户端套接字
        self.dev_socket.settimeout(0.1)

    def open(self):
        try:
            self.dev_socket.connect(self.dev_addr)  # 连接设备
        except socket.timeout:
            print("Timeout, Recreate socket")
            del self.dev_socket
            self.dev_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.dev_socket.settimeout(0.1)
            return False
        except Exception as exp:
            print("TCP Exception:{0}".format(exp))
            return False

        return True

    def recv_data(self):
        recv_data = self.dev_socket.recv(1024)  # 接收设备发送的数据
        print("RX:" + conv_bytes_str(recv_data))

        return recv_data

    def send_data(self, send_data):
        print("TX:" + conv_bytes_str(send_data))

        send_len = self.dev_socket.send(send_data)  # 发送数据给设备
        return send_len

    def close(self):
        self.dev_socket.close()  # 关闭TCP客户端套接字


"""
struct fmt:
format  ctype   size
Q       u_int64  8
B       u_int8   1
H       u_int16  2
I       u_int32  4
"""


class ZllrpMsg(TcpClient):
    def __init__(self, dev_ip, dev_port):
        # logging.basicConfig(level=logging.INFO,
        #                     format='%(asctime)s - %(name)s - line:%(lineno)d - %(levelname)s - %(message)s',
        #                     stream=sys.stdout)
        self.logger = logging.getLogger("ZllrpMsg")
        super(ZllrpMsg, self).__init__(dev_ip, dev_port)

        self.zllrp = ZLLRP()
        self.b_exit = False
        self.lock = threading.Lock()
        self.msg_queue = Queue()
        self.b_msg_queue = Queue()
        self.tag_queue = Queue()
        self.current_dev_info = dict()
        self.msg_id = 0x55

        self.thr_msg_recv = threading.Thread(target=self.msg_receive)
        self.thr_msg_proc = threading.Thread(target=self.msg_process)

    def serialize(self, msgdict):
        # name = msgdict.keys()[0]
        name = next(iterkeys(msgdict))
        send_data = self.zllrp.zllrp_msg_encode(self.current_dev_info["DeviceSN"],
                                                self.current_dev_info["Ver"],
                                                name,
                                                self.msg_id,
                                                msgdict[name])
        return send_data

    def deserialize(self, msgbytes):
        ret = self.zllrp.zllrp_msg_decode(msgbytes)
        if ret is False:
            return False

        ret_msg_dict, body = ret
        if len(body) != 0:
            self.logger.debug("RX_In_DeSer:" + conv_bytes_str(body))
            self.msg_queue.put(body)

        # name = ret_msg_dict.keys()[0]
        name = next(iterkeys(ret_msg_dict))
        self.current_dev_info['DeviceSN'] = ret_msg_dict[name]['DeviceSN']
        self.current_dev_info['Ver'] = ret_msg_dict[name]['Ver']
        self.current_dev_info['ID'] = ret_msg_dict[name]['ID']
        # self.logger.debug(ret_msg_dict)
        return ret_msg_dict

    def connect(self, time_out=120):
        try:
            re_times = time_out / 5
            while re_times > 0:
                ret = self.open()
                if ret is False:
                    self.logger.debug("Open TCP error,retry!")
                    re_times -= 1
                    time.sleep(5)
                else:
                    break
            else:
                self.logger.error("Connect Fail!")
                return False

            self.thr_msg_recv.start()
            self.thr_msg_proc.start()
            ret = self.zllrp_msg()
        except socket.error as err:
            self.logger.debug("TCP Open Error:{0}".format(err))
            self.b_exit = True
        else:
            # msg_name = ret.keys()[0]
            msg_name = next(iterkeys(ret))
            if msg_name == "DeviceEventNotification":
                self.logger.debug("Connect Success!")
                return True

            return False

    def disconnect(self):
        self.b_exit = True
        self.logger.debug("start exit!")
        while self.thr_msg_proc.isAlive():
            pass
        self.logger.debug("thr proc exit!")

        while self.thr_msg_recv.isAlive():
            pass
        self.logger.debug("thr recv exit!")

        self.close()

    def send_data(self, send_data):
        self.logger.debug("TX:" + conv_bytes_str(send_data))
        self.lock.acquire()
        try:
            send_len = self.dev_socket.send(send_data)  # 发送数据给设备
        finally:
            self.lock.release()

        return send_len

    def recv_data(self):
        self.lock.acquire()
        try:
            recv_data = self.dev_socket.recv(1024)  # 接收设备发送的数据
        finally:
            self.lock.release()

        self.logger.debug("RX:" + conv_bytes_str(recv_data))

        return recv_data

    def parse_msg(self, msg_encode):
        msg_dict = self.deserialize(msg_encode)

        if msg_dict is False:
            self.logger.error("Deserialze Fail!")
            return False
        else:
            return msg_dict

    def msg_receive(self):
        while not self.b_exit:
            try:
                msg = self.recv_data()
            except socket.timeout:
                pass
            except socket.error as err:
                self.logger.error("Socekt Err:{0}".format(err))
            else:
                self.msg_queue.put(msg)
            finally:
                time.sleep(0.1)

    def msg_process(self):
        while not self.b_exit:
            if self.msg_queue.empty():
                time.sleep(0.1)
                pass
            else:
                msg = self.msg_queue.get()
                msg_decode = self.parse_msg(msg)
                self.msg_handle(msg_decode)

    def msg_handle(self, msg):
        # msg_name = msg.keys()[0]
        msg_name = next(iterkeys(msg))
        if msg_name == "Keepalive":
            self.keep_alive_ack()

        elif msg_name == "DeviceEventNotification":
            if 'ConnectionAttemptEvent' in msg[msg_name]:
                self.b_msg_queue.put(msg)
            else:
                self.logger.debug(msg)
        elif msg_name == 'TagSelectAccessReport':
            self.tag_queue.put(msg[msg_name])
        else:
            self.b_msg_queue.put(msg)

    def zllrp_msg(self, msg_dict=None, timeout=5):
        if msg_dict is not None:
            ret_bytes = self.serialize(msg_dict)
            self.msg_id += 1
            self.send_data(ret_bytes)
        try:
            msg_receive = self.b_msg_queue.get(timeout=timeout)
        except Empty:
            self.logger.error("Message Receive Empty!")
            return False
        self.logger.debug(msg_receive)
        return msg_receive

    def keep_alive_ack(self):
        ret_msg_dict = {
            "KeepaliveAck": {}
        }
        ret_bytes = self.serialize(ret_msg_dict)
        self.send_data(ret_bytes)
        return True

    def get_version(self, ver_type):
        """

        @param ver_type: 0, BOOT; 1, Sys; 2, Sec
        @return:version str or False
        """
        ver_map = ["BOOT", "SYS", "SEC"]
        msg_content = {
            "VerType": ver_type
        }
        msg_dict = {
            "GetVersion": msg_content
        }
        msg_receive = self.zllrp_msg(msg_dict)
        if msg_receive is False:
            return False

        if msg_receive["GetVersionAck"]['Status']["StatusCode"] != 0:
            self.logger.error("GetVersionAck Error!")
            return False
        else:
            ver_ret = msg_receive["GetVersionAck"]['VersionInfo']
            ret_dict = {ver_map[ver_type]: {}}
            for ver_dict in ver_ret:
                ver_data = ver_dict["VersionData"]
                if ver_type == 2:
                    ver_str = "V{0:1d}.{1:02d}.{2:02d}".format(ver_data[-2] >> 4,
                                                               ((ver_data[-2] << 4) & 0xf0) | (ver_data[-1] >> 4),
                                                               ver_data[-1] & 0x0f)
                elif ver_type == 0 or ver_type == 1:
                    ver_str = "V{0:1d}.{1:02d}.{2:02d}".format(ver_data[0], ver_data[1], ver_data[2])

                else:
                    return False

                if ver_dict["UsedOrSpare"] == 1:
                    ver_tag = "Master"
                else:
                    ver_tag = "Slave"

                ret_dict[ver_map[ver_type]][ver_tag] = ver_str

            return ret_dict

    def diagnostic_vswr(self):
        msg_content = {
            "DiagnosticTestItem": [{"DiagnosticTestID": 2}]
        }
        msg_dict = {
            "DiagnosticTest": msg_content
        }
        msg_receive = self.zllrp_msg(msg_dict)
        # print(msg_receive)
        if msg_receive["DiagnosticTestAck"]['Status']["StatusCode"] != 0:
            self.logger.error("DiagnosticTestAck Error!")
            return False
        else:
            vswr_info_list = msg_receive["DiagnosticTestAck"]['DiagnosticTestResultItem']
            if type(vswr_info_list) != list:
                vswr_info_list = [vswr_info_list]

            ret_dict = {"AntCount": 0, "VSWRList": [0, 0, 0, 0]}
            for vswr_info in vswr_info_list:
                vswr_value = vswr_info["DiagnosticTestResultAntennaVSWR"]["AntennaVSWR"] / 100.0
                vswr_index = vswr_info["DiagnosticTestResultAntennaVSWR"]["AntennaID"] - 1
                ret_dict["VSWRList"][vswr_index] = vswr_value
                ret_dict["AntCount"] += 1

            return ret_dict

    def get_dev_config(self, req_data, ant_id):
        msg_content = {
            'RequestedData': req_data,
            'AntennaID': ant_id
        }
        msg_dict = {
            'GetDeviceConfig': msg_content
        }
        msg_receive = self.zllrp_msg(msg_dict)
        if msg_receive["GetDeviceConfigAck"]['Status']["StatusCode"] != 0:
            self.logger.error("GetDeviceConfigAck Error!")
            return False
        else:
            self.logger.debug("GetDeviceConfigAck Success!")

            # Device Name
            if req_data == 1:
                dev_name = msg_receive["GetDeviceConfigAck"]["Identification"]["DeviceName"]
                return dev_name

            # DeviceEventNotificationSpec
            elif req_data == 2:
                event_noti_state = msg_receive["GetDeviceConfigAck"]["DeviceEventNotificationSpec"]
                return event_noti_state

            # CommunicationConfiguration
            elif req_data == 3:
                comm_conf = msg_receive["GetDeviceConfigAck"]["CommunicationConfiguration"]
                return comm_conf

            # AlarmConfiguration
            elif req_data == 4:
                alm_conf = msg_receive["GetDeviceConfigAck"]["AlarmConfiguration"]
                return alm_conf

            # AntennaProperties
            elif req_data == 5:
                ant_prop = msg_receive["GetDeviceConfigAck"]["AntennaProperties"]
                return ant_prop

            # AntennaConfiguration
            elif req_data == 6:
                ant_conf = msg_receive["GetDeviceConfigAck"]["AntennaConfiguration"]
                return ant_conf

            # ModuleDepth
            elif req_data == 7:
                mod_depth = msg_receive["GetDeviceConfigAck"]["ModuleDepth"]
                return mod_depth

            # SelectReportSpec
            elif req_data == 8:
                sel_spec = msg_receive["GetDeviceConfigAck"]["SelectReportSpec"]
                return sel_spec

            # AccessReportSpec
            elif req_data == 9:
                acc_spec = msg_receive["GetDeviceConfigAck"]["AccessReportSpec"]
                return acc_spec

            # LocationConfiguration
            elif req_data == 10:
                loc_conf = msg_receive["GetDeviceConfigAck"]["LocationConfiguration"]
                return loc_conf

            # Sec SN
            elif req_data == 11:
                sn = msg_receive["GetDeviceConfigAck"]["SecurityModuleConfiguration"]["GenaralConfigData"][
                    "SecurityModuleSN"][
                    "SerialNumber"]

                sn_str = "{0:c}{1:c}{2:02d}{3:03d}{4:05d}".format(sn[0], sn[1], sn[2],
                                                                  sn[3] << 8 | sn[4],
                                                                  sn[5] << 16 | sn[6] << 8 | sn[7])
                return sn_str

    def set_dev_config(self, config_dict):
        content_dict = config_dict
        content_dict["ResetToFactoryDefault"] = 0
        content_dict["Reserved"] = 0
        msg_dict = {
            'SetDeviceConfig': content_dict
        }
        msg_receive = self.zllrp_msg(msg_dict)
        if msg_receive["SetDeviceConfigAck"]['Status']["StatusCode"] != 0:
            self.logger.error("SetDeviceConfigAck Error!")
            return False
        else:
            self.logger.debug("SetDeviceConfigAck Success!")
            return True

    def set_ant_config(self, ant_num, power_index=None, freq_indexes=None, for_rate_index=None, rev_rate_index=None,
                       for_mod_index=None, rev_encoding_index=None):
        current_config = self.get_dev_config(6, 0)
        revise_config = list()

        for config in current_config:
            config_dict = deepcopy(config)
            if ant_num == 0 or dict(config)["AntennaID"] == ant_num:
                if power_index is not None:
                    config_dict["TransmitPowerIndex"] = power_index

                if freq_indexes is not None:
                    config_dict["FrequencyIndexes"] = freq_indexes

                if for_rate_index is not None:
                    config_dict["ForDataRateIndex"] = for_rate_index

                if rev_rate_index is not None:
                    config_dict["RevDataRateIndex"] = rev_rate_index

                if for_mod_index is not None:
                    config_dict["ForModulationIndex"] = for_mod_index

                if rev_encoding_index is not None:
                    config_dict["RevDataEncodingIndex"] = rev_encoding_index

            revise_config.append(config_dict)

        config_dict = {
            "AntennaConfiguration": revise_config
        }

        return self.set_dev_config(config_dict)

    def query_sec_sn(self):
        return self.get_dev_config(11, 0)

    def add_select_spec(self, select_spec_id):
        msg_content = {
            "SelectSpec": {
                'SelectSpecID': select_spec_id,
                'Priority': 0,
                'CurrentState': 0,
                'Persistence': 0,
                'Reserved': 0,
                'SelectSpecStartTrigger': {
                    'SelectSpecStartTriggerType': 0
                },
                'SelectSpecStopTrigger': {
                    'SelectSpecStopTriggerType': 0,
                    'DurationValue': 0
                },
                'AntennaSpec': {
                    'AntennaIDs': [1],
                    'AntennaSpecStopTrigger': {
                        'AntennaSpecStopTriggerType': 3,
                        'DurationValue': 0,
                        'TagObservationTrigger': {
                            'TriggerType': 2,
                            'NumberOfTags': 0,
                            'NumberOfAttempts': 1,
                            'TValue': 0,
                            'Timeout': 0
                        }
                    },
                    'RfSpec': {
                        'RfSpecID': select_spec_id,
                        'ProtocolID': 0,
                        'SelectType': 1,
                        'MemoryBank': {
                            'MemoryBankID': 0,
                            'ReadType': 0,
                            'Pointer': 4,
                            'Count': 10,
                            'BankType': 2
                        }
                    }
                },
                'SelectReportSpec': {
                    'SelectReportTrigger': 2,
                    'NValue': 1,
                    'EnableSelectSpecID': 1,
                    'EnableSpecIndex': 1,
                    'EnableRfSpecID': 1,
                    'EnableAntennaID': 1,
                    'EnablePeakRSSI': 1,
                    'EnableFirstSeenTimestamp': 1,
                    'EnableLastSeenTimestamp': 1,
                    'EnableTagSeenCount': 1,
                    'EnableAccessSpecID': 1,
                    'Reserved': 64
                }
            }
        }
        msg_dict = {
            "AddSelectSpec": msg_content
        }
        msg_receive = self.zllrp_msg(msg_dict)
        if msg_receive["AddSelectSpecAck"]['Status']["StatusCode"] != 0:
            self.logger.error("AddSelectSpecAck Error!")
            self.logger.error("Error:{0}".format(msg_receive["AddSelectSpecAck"]['Status']["ErrorDescription"]))
            return False
        else:
            self.logger.debug("AddSelectSpecAck Success!")
            return True

    def del_select_spec(self, select_spec_id):
        msg_content = {
            'SelectSpecID': select_spec_id
        }
        msg_dict = {
            'DeleteSelectSpec': msg_content
        }
        msg_receive = self.zllrp_msg(msg_dict)
        if msg_receive["DeleteSelectSpecAck"]['Status']["StatusCode"] != 0:
            self.logger.error("DeleteSelectSpecAck Error!")
            self.logger.error("Error:{0}".format(msg_receive["DeleteSelectSpecAck"]['Status']["ErrorDescription"]))
            return False
        else:
            self.logger.debug("DeleteSelectSpecAck Success!")
            return True

    def enable_select_spec(self, select_spec_id):
        msg_content = {
            'SelectSpecID': select_spec_id
        }
        msg_dict = {
            'EnableSelectSpec': msg_content
        }
        msg_receive = self.zllrp_msg(msg_dict)
        if msg_receive["EnableSelectSpecAck"]['Status']["StatusCode"] != 0:
            self.logger.error("EnableSelectSpecAck Error!")
            self.logger.error("Error:{0}".format(msg_receive["EnableSelectSpecAck"]['Status']["ErrorDescription"]))
            return False
        else:
            self.logger.debug("EnableSelectSpecAck Success!")
            return True

    def start_select_spec(self, select_spec_id):
        msg_content = {
            'SelectSpecID': select_spec_id
        }
        msg_dict = {
            'StartSelectSpec': msg_content
        }
        msg_receive = self.zllrp_msg(msg_dict)
        if msg_receive["StartSelectSpecAck"]['Status']["StatusCode"] != 0:
            self.logger.error("StartSelectSpecAck Error!")
            self.logger.error("Error:{0}".format(msg_receive["StartSelectSpecAck"]['Status']["ErrorDescription"]))
            return False
        else:
            self.logger.debug("StartSelectSpecAck Success!")
            return True

    def stop_select_spec(self, select_spec_id):
        msg_content = {
            'SelectSpecID': select_spec_id
        }
        msg_dict = {
            'StopSelectSpec': msg_content
        }
        msg_receive = self.zllrp_msg(msg_dict)
        if msg_receive["StopSelectSpecAck"]['Status']["StatusCode"] != 0:
            self.logger.error("StopSelectSpecAck Error!")
            self.logger.error("Error:{0}".format(msg_receive["StopSelectSpecAck"]['Status']["ErrorDescription"]))
            return False
        else:
            self.logger.debug("StopSelectSpecAck Success!")
            return True

    def tag_invent_read(self, spec_id):
        self.del_select_spec(spec_id)
        self.add_select_spec(spec_id)
        self.enable_select_spec(spec_id)
        self.start_select_spec(spec_id)
        time.sleep(1)

        tag_list = list()
        while self.tag_queue.empty() is False:
            msg = self.tag_queue.get()
            tag_list.append(msg["TagReportData"][0])

        ret_dict = dict()
        ret_dict["tag_count"] = len(tag_list)
        ret_dict["tag_tid"] = list()
        ret_dict["tag_data"] = list()
        ret_dict["tag_rssi"] = list()
        for cnt in range(ret_dict["tag_count"]):
            # print(tag_list[cnt])
            tag_data = str()
            tag_tid = str()
            tag_rssi = tag_list[cnt]["PeakRSSI"]["PeakRSSI"]
            for d in tag_list[cnt]["TID"]:
                tag_tid += "{0:02X}".format(d)

            # car license number
            fpdh = tag_list[cnt]["CustomizedSelectSpecResult"]["ReadDataInfo"]["FPDH"]["FPDHData"]
            tag_data += "{0}{1} ".format(self.zllrp.fpdh_list[fpdh[0] - 1], chr(ord('A') + fpdh[1]))
            hphmxh = tag_list[cnt]["CustomizedSelectSpecResult"]["ReadDataInfo"]["HPHMXH"]["HPHMXHData"]
            for d in hphmxh:
                if d > 25:
                    d_char = chr(ord('0') + d - 26)
                else:
                    d_char = chr(ord('A') + d)
                tag_data += d_char

            ret_dict["tag_tid"].append(tag_tid)
            ret_dict["tag_rssi"].append(tag_rssi)
            ret_dict["tag_data"].append(tag_data)

        self.stop_select_spec(spec_id)
        self.del_select_spec(spec_id)
        return ret_dict


if __name__ == '__main__':
    dev_conn = ZllrpMsg("10.86.20.50", 5084)
    if dev_conn.connect() is False:
        exit(1)

    dev_conn.logger.info(dev_conn.get_version(0))
    # dev_conn.logger.info(dev_conn.get_version(1))
    # dev_conn.logger.info(dev_conn.get_version(2))
    # dev_conn.logger.info(dev_conn.diagnostic_vswr())
    # dev_conn.logger.info(dev_conn.query_sec_sn())
    tag_info = dev_conn.tag_invent_read(0x17)
    for cnt in range(tag_info["tag_count"]):
        dev_conn.logger.info(
            "{0}, {1}, {2}".format(tag_info["tag_tid"][cnt], tag_info["tag_data"][cnt], tag_info["tag_rssi"][cnt]))
    # dev_conn.set_ant_config(0, 0)
    time.sleep(5)
    dev_conn.disconnect()
