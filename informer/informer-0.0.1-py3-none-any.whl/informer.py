# -*- coding: utf-8 -*-
import socket
from informer.network import send_package, send_simple_package
from informer.utils import encode_img, encode_cmd
from informer import config

class Informer():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
    
    def send_vision(self, img, debug=False):
        data = encode_img(img)
        send_package(data, self.socket, config.ADDRESS, config.VISION_PORT, debug=debug)
    
    def send_cmd(self, v, w, c, debug=False):
        data = encode_cmd(v, w, c)
        send_simple_package(data, self.socket, config.ADDRESS, config.CMD_PORT, debug=debug)