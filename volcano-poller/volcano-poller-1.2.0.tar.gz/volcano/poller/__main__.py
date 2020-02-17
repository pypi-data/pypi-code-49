#!/usr/bin/python3

import argparse
import sys
import logging

from twisted.internet import reactor

from volcano.general.log import configure_arg_parser_for_log, configure_logger
from volcano.general import stdsvc
from volcano.general.stddef import VOLCANO_DEFAULT_TCP_PORT
from volcano.general.xml_reader import XmlReader, LoadException, load_xml_file_le, get_node_location

from volcano.twistedclient.twisted_factory import VolcanoTwistedFactory
from volcano.twistedclient.twisted_client_mt import VolcanoTwistedClientMT

from .channel_tcp import TcpChannel
from .channel_serial import SerialChannel
from . import merk_prot
from . import nzif_prot
from . import mb_prot
from . import tools
from . import build_cfg


def configure_my_args(parser):
    parser.add_argument('--core_host', help='Volcano core host', default='localhost')
    parser.add_argument('--core_port', help='Volcano core port', default=VOLCANO_DEFAULT_TCP_PORT, type=int)
    parser.add_argument('--core_connect_attempts', type=int)
    parser.add_argument('--core_reconnect_pause', type=int)

    parser.add_argument('-n', '--name', help='Instance name', default='poller')
    parser.add_argument('-f', '--file', help='Config file', default='poller.xml')
    parser.add_argument('-b', '--build', help='Build config', type=str, default='')


def load(env, log):
    cfg = load_xml_file_le(env.file)

    protocols_map = {}
    for node in cfg.getroot():
        p = XmlReader(node)

        if node.tag == 'Channel':
            # media
            media_type = node.attrib['channelType']
            if media_type == 'tcp':
                channel = TcpChannel(node)
            elif media_type == 'serial':
                channel = SerialChannel(node)
            else:
                raise LoadException('Unknown channel type: "{}"'.format(media_type), node)

            # protocol
            proposed_aux_name = tools.unique_name('protocol_', lambda x: x not in protocols_map)

            protocol_name = p.get_str('protocol', allowed=('merk', 'nzif', 'modbus'))
            if protocol_name == 'merk':
                protocol = merk_prot.MerkProtocol(node, channel, proposed_aux_name, log)
            elif protocol_name == 'nzif':
                protocol = nzif_prot.NzifProtocol(node, channel, proposed_aux_name, log)
            else:
                protocol = mb_prot.MbProtocol(node, channel, proposed_aux_name, log)

            if not protocol.empty():
                protocols_map[protocol.aux_name()] = protocol
            else:
                log.warning('Protocol {} is empty and will be removed'.format(get_node_location(node)))
        else:
            raise LoadException('Unknown node name: "{}"'.format(node.tag), node)

    log.info('Loaded {} channels'.format(len(protocols_map)))

    t_max = reactor.getThreadPool().max     # pylint: disable=no-member
    if len(protocols_map) > t_max:
        log.warning(
            'Number of channels ({}) exceeds default thread pool size({}). Threading will be inefficient (some channels will wait for another to finish). Try splitting task into several processes.'.format(
                len(protocols_map), t_max))

    return protocols_map


class VolcanoClient(VolcanoTwistedClientMT):    # pylint: disable=abstract-method
    protocols_map = None

    def __init__(self, env):
        super().__init__(logging.getLogger(env.name))
        self.env = env
        self.services_ = None

    def connectionMade(self):
        assert self.protocols_map

        super().connectionMade()

        self.log.info('Connected to core')

        self.services_ = {
            'hs': stdsvc.HandshakeService(stdsvc.PipeMarker(self, 'hs')),
            'echo': stdsvc.SingleThreadEchoService(stdsvc.PipeMarker(self, 'echo')),
            'set': stdsvc.MultiThreadSetValueService(stdsvc.PipeMarker(self, 'set')),
            'find': stdsvc.SingleThreadFindTagService(stdsvc.PipeMarker(self, 'find')),
        }
        self.services_['hs'].salute(self.env.name)

        for proto in self.protocols_map.values():
            proto.sync(self.services_)
        self.services_['echo'].echo(self.on_sync_complete)

    def on_sync_complete(self):
        for proto in self.protocols_map.values():
            reactor.callInThread(proto.run_once_safe, reactor)  # pylint: disable=no-member

    def on_msg_rcvd_mt(self, msg: dict) -> None:
        assert 'ch' in msg, msg

        ch_name = msg['ch']
        assert ch_name in self.services_, (ch_name, self.services_)

        self.services_[ch_name].push_single_message(msg)  # error should raise


def main() -> int:
    try:
        # Args
        arg_parser = argparse.ArgumentParser()
        configure_my_args(arg_parser)
        configure_arg_parser_for_log(arg_parser)  # let logger add his arguments for later configure_logger() call
        env = arg_parser.parse_args()

        # Logging
        configure_logger(env)
        log = logging.getLogger(env.name)
        protocols_map = None

        try:
            if env.build:
                build_cfg.enable_build()
                load(env, log)
                build_cfg.flush_build()
                return 0
            else:
                protocols_map = load(env, log)

            factory = VolcanoTwistedFactory()
            factory.log = log
            factory.client = VolcanoClient(env)
            factory.client.protocols_map = protocols_map

            if env.core_connect_attempts is not None:
                factory.nb_attempts = env.core_connect_attempts

            if env.core_reconnect_pause is not None:
                factory.reconnect_pause = env.core_reconnect_pause

            log.info('Connect to core at %s:%s', env.core_host, env.core_port)
            reactor.connectTCP(env.core_host, env.core_port, factory)   # pylint: disable=no-member
            reactor.run()   # pylint: disable=no-member

            return 0

        except (Warning, LoadException) as e:
            log.error(e)
            return 1

        finally:
            # я не использую factory.stopFactory(), потому что она вызывается при каждой неудачной попытке подключения к ядру
            if protocols_map:
                for proto in protocols_map.values():
                    proto.safe_close()
    finally:
        logging.shutdown()


if __name__ == '__main__':
    sys.exit(main())
