# -*- coding: utf-8 -*-
import socket
import struct
import threading
from informer.network import send_package, send_simple_package
from informer.utils import encode_img, encode_cmd, encode_debug_message, to_json
from informer import config

class Informer():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
        
        server_address = ('', config.SYNC_RECEIVE_PORT)
        self.receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receive_socket.bind(server_address)
        # tell the operating system to add the socket to the multicast group on all interfaces.
        group = socket.inet_aton(config.ADDRESS)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self.receive_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        self.cloc_sync_thread = threading.Thread(
            target=self.cloc_sync, args=()
        )
        
        self.cnt = 0
        self.message_dick = {}
        # automaticly start cloc synchronization thread
        self.cloc_sync_thread.start()
    
    def send_vision(self, img, debug=False):
        data = encode_img(img)
        send_package(data, self.socket, config.ADDRESS, config.VISION_PORT, debug=debug)
    
    def send_cmd(self, v, w, c, debug=False):
        data = encode_cmd(v, w, c)
        send_simple_package(data, self.socket, config.ADDRESS, config.CMD_PORT, debug=debug)
        
    def draw_box(self, lt_x, lt_y, width, height, message='', color='red', **kwargs):
        data = to_json(dtype='box',
                       lt_x=lt_x, lt_y=lt_y, width=width, height=height,
                       message=message,
                       color=color)
        self.message_dick[str(self.cnt)] = data
        self.cnt += 1
        
    def draw_center_box(self, ct_x, ct_y, width, height, message='', color='red'):
        data = to_json(dtype='center_box',
                       ct_x=ct_x, ct_y=ct_y, width=width, height=height,
                       message=message,
                       color=color)
        self.message_dick[str(self.cnt)] = data
        self.cnt += 1
        
    def draw_line(self, s_x, s_y, e_x, e_y, color='red'):
        data = to_json(dtype='line',
                       s_x=s_x, s_y=s_y, e_x=e_x, e_y=e_y,
                       color=color)
        self.message_dick[str(self.cnt)] = data
        self.cnt += 1
        
    def clear(self):
        data = to_json(dtype='clear')
        self.message_dick[str(self.cnt)] = data
        self.cnt += 1
        
    def draw(self):
        data = encode_debug_message(self.message_dick)
        self.message_dick = {}
        self.cnt = 0
        send_simple_package(data, self.socket, config.ADDRESS, config.DEBUG_PORT)
        
    def cloc_sync(self):
        while True:
            data, addr = self.receive_socket.recvfrom(65535)
            new_data = bytes(str(int(data)-1), 'utf-8')
            send_package(new_data, self.socket, config.ADDRESS, config.SYNC_SEND_PORT)