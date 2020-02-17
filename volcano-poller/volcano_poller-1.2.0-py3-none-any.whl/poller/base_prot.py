#!/usr/bin/python3

import traceback

from volcano.general.xml_reader import XmlReader

from . import time_tools
from . import tools


class BaseProtocol:
    def __init__(self, my_xml_node, comm_channel, io_ctx, proposed_name, parent_log):
        p = XmlReader(my_xml_node)

        self.comm_channel_ = comm_channel
        self.aux_name_ = p.get_str('name', proposed_name)
        self.log_ = parent_log.getChild(self.aux_name_)
        self.devices_ = []

        # run_once context:
        self.last_dev_idx_ = None
        self.is_online_ = None
        self.io_ctx_ = io_ctx
        self.offline_timer_ = time_tools.Timer()  # сколько времени уже канал закрыт
        self.offline_notified_devs_ = None  # для кого уже было вызвано .on_channel_closed(). set of aux_name (в рамках 1 канала они уникальны)
        self.open_channel_timeout_ = time_tools.Timeout(5.0, expired=True)

    def sync(self, services: dict):
        assert isinstance(services, dict), dict
        for dev in self.devices():
            dev.sync(services)

    def aux_name(self):
        return self.aux_name_

    def empty(self):
        return len(self.devices_) == 0

    def log(self):
        return self.log_

    def devices(self):
        return self.devices_

    def add_device(self, device):
        self.devices_.append(device)

    def find_device(self, aux_name):
        return tools.search(self.devices_, lambda x: x.aux_name() == aux_name)

    def run_once_safe(self, _reactor) -> None:
        log = self.log()
        channel = self.comm_channel_

        try:
            if channel.is_open():
                assert not self.empty()

                self.last_dev_idx_ = 0 if self.last_dev_idx_ is None else (self.last_dev_idx_ + 1) % len(self.devices_)

                dev = self.devices_[self.last_dev_idx_]

                dev.work(self.io_ctx_)
            else:
                # is_online_ is None    => first iteration
                # is_online_ == True    => channel crashed on last iter
                # is_online_ == False   => channel is closed and we know that already
                if self.is_online_ is None or self.is_online_:
                    just_crashed = self.is_online_
                    self.is_online_ = False

                    if just_crashed:
                        log.warning('Channel became offline')
                        self.open_channel_timeout_.start()  # на 1м цикле не надо ждать таймаут для попытки открыть канал

                    self.offline_timer_.set_now()
                    self.offline_notified_devs_ = set()

                if self.open_channel_timeout_.is_expired():
                    if channel.open(5.0, log):
                        self.is_online_ = True
                        self.last_dev_idx_ = None
                        log.info('Connection established')
                    else:
                        self.open_channel_timeout_.start()

                if not self.is_online_:  # канал мог открыться только что
                    for dev in self.devices_:
                        if dev.aux_name() not in self.offline_notified_devs_ and self.offline_timer_.secs() >= dev.channel_closed_timeout():
                            dev.on_channel_closed()
                            self.offline_notified_devs_.add(dev.aux_name())

        except Exception as e:  # exceptions in threads are not visible by default
            log.error(e)
            traceback.print_exc()

        finally:
            _reactor.callInThread(self.run_once_safe, _reactor)

    def safe_close(self) -> None:
        self.log().info('Protocol released')
        self.comm_channel_.safe_close()
