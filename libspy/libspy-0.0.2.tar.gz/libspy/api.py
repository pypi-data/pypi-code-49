# Copyright (c) 2017-2020, Carl Cheung
# All rights reserved.


import logging
import os
import sys
import time
from multiprocessing import Process
from threading import Thread

from shadowsocks import asyncdns, tcprelay, udprelay, eventloop


class SSClient:
    def __init__(self, server, server_port, local_address, local_port, password, method, timeout=300, verbose=False):
        logging.basicConfig(level=logging.INFO,
                            format='%(levelname)-s: %(message)s')
        self.config = {'server': server,
                       'server_port': server_port,
                       'local_port': local_port,
                       'password': password if isinstance(password, bytes) else password.encode(),
                       'timeout': timeout,
                       'method': method,
                       'port_password': None,
                       'fast_open': False,
                       'workers': 1,
                       'pid-file': '/var/run/shadowsocks.pid' if 'nt' not in os.name else './shadowsocks.pid',
                       'log-file': '/var/log/shadowsocks.log' if 'nt' not in os.name else './shadowsocks.log',
                       'verbose': verbose,
                       'local_address': local_address,
                       'one_time_auth': False,
                       'prefer_ipv6': False}

        self._is_stopped = False
        self._is_started = False
        self.server_started = False
        self._server_process = Process(target=self._start_ss)
        self._server_process_ppid = self._server_process.pid

    def _start_ss(self):
        logging.info("starting local at %s:%d" % (self.config['local_address'], self.config['local_port']))
        print("starting local at %s:%d" % (self.config['local_address'], self.config['local_port']))
        dns_resolver = asyncdns.DNSResolver()
        tcp_server = tcprelay.TCPRelay(self.config, dns_resolver, True)
        udp_server = udprelay.UDPRelay(self.config, dns_resolver, True)
        loop = eventloop.EventLoop()
        dns_resolver.add_to_loop(loop)
        tcp_server.add_to_loop(loop)
        udp_server.add_to_loop(loop)

        loop.run()

    def start_forever(self):
        self._is_started = True
        self.daemon()

    def daemon(self):
        while True:
            try:
                time.sleep(3)

                if self._is_started and not self.server_started:
                    self.server_started = True
                    self._server_process.start()

                if self._is_stopped:
                    self._server_process.terminate()
                    logging.info('user exit')
                    sys.exit()

            except KeyboardInterrupt:
                self._is_stopped = True

    def stop(self):
        self._is_stopped = True


if __name__ == '__main__':
    ssc = SSClient('127.0.0.1', 12345, '127.0.0.1', 1080, '123456', 'rc4-md5')

    Thread(target=ssc.start_forever).start()
    time.sleep(5)
    ssc.stop()
