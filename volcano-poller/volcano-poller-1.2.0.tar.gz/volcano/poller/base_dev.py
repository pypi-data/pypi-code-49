#!/usr/bin/python3
# encoding=utf-8

from volcano.general.xml_reader import XmlReader


class BaseDevice:
    def __init__(self, my_xml_node, proposed_aux_name, parent_log):
        p = XmlReader(my_xml_node)

        self.branch_ = p.get_str('branch')
        self.aux_name_ = p.get_str('name', proposed_aux_name)
        self.log_ = parent_log.getChild(self.aux_name_)
        self.go_offline_timeout_sec_ = p.get_time_secs('offlineTimeout', 5.0, min_val=0.0, max_val=600.0)

    def sync(self, services: dict):     # pylint: disable=no-self-use
        assert isinstance(services, dict), services

    def channel_closed_timeout(self):
        return self.go_offline_timeout_sec_

    def on_channel_closed(self):
        raise NotImplementedError()

    def branch(self, tag_name: str = None):
        return '{}.{}'.format(self.branch_, tag_name) if tag_name else self.branch_

    def aux_name(self):
        return self.aux_name_

    def log(self):
        return self.log_

    # не предполагает никаких exceptions
    # в случае проблем может просто закрыть канал
    def work(self, ctx) -> None:
        raise NotImplementedError()

    def get_tag_full_name(self, tag_short_name: str):
        # '@xxx' - global
        # 'xxx' - local
        if tag_short_name.startswith('@'):
            return tag_short_name[1:]
        else:
            return self.branch_ + '.' + tag_short_name
