#!/usr/bin/python3

from volcano.general.xml_reader import XmlReader, get_node_location, load_xml_file_le, LoadException
from volcano.general import variant

from . import base_dev
from . import tools
from . import mb_frame
from . import connected_values


class MbDevice(base_dev.BaseDevice):

    def __init__(self, my_xml_node, proposed_aux_name, parent_log):
        super().__init__(my_xml_node, proposed_aux_name, parent_log)

        p = XmlReader(my_xml_node)

        self.slave_nb_ = p.get_int('slaveNb', min_val=0, max_val=0xff)
        self.frames_ = []
        self.last_processed_frame_idx_ = -1

        template_name = p.get_str('template')
        template_xml = load_xml_file_le(template_name)

        self.load_frames_(template_xml.getroot())

        self.is_online_ = connected_values.ConnectedValue(self.branch('online'), variant.BoolValue(), True)

    def slave_nb(self):
        return self.slave_nb_

    def empty(self):
        return len(self.frames_) == 0

    def sync(self, services: dict):
        assert isinstance(services, dict), services
        super().sync(services)
        self.is_online_.sync(services)
        for f in self.frames_:
            f.sync(services)

    def _find_frame_by_aux_name(self, frame_aux_name):
        return tools.search(self.frames_, lambda x: x.aux_name() == frame_aux_name)

    def load_frames_(self, xml_node):
        log = self.log()

        for node in xml_node:
            frame = None
            proposed_aux_name = tools.unique_name('frame_', lambda x: not self._find_frame_by_aux_name(x))
            if node.tag == 'Registers':
                frame = mb_frame.MbFrameReg(node, proposed_aux_name, self, log)
            elif node.tag == 'Bits':
                pass
            # elif node.tag == 'Cmd':
            #    frame = MbCmdFrame( node )
            # elif node.tag == 'Opg':
            #    frame = MbFrameReadOpg( node )
            # elif node.tag == 'RegBlock'
            #    frame = MbFrameRawWriteRegs( node, this, &ok )
            else:
                raise LoadException(
                    'Unknown frame type "{}". Use "Registers, Bits, Cmd, Opg, RegBlock"'.format(node.tag), node)

            assert frame
            if frame.empty():
                log.warning('{}: Frame is empty and will be removed'.format(get_node_location(node)))
            else:
                self.frames_.append(frame)

    def on_channel_closed(self):
        self.log().debug('Channel closed and device going offline')
        self.is_online_.set(False)
        for f in self.frames_:
            f.on_channel_closed()

    def work(self, ctx):
        assert not self.empty()

        for i in range(len(self.frames_)):  # to prevent endless loop when none of frames is expired; pylint: disable=unused-variable
            self.last_processed_frame_idx_ += 1
            if self.last_processed_frame_idx_ >= len(self.frames_):
                self.last_processed_frame_idx_ = 0

            frame = self.frames_[self.last_processed_frame_idx_]
            if frame.read_write(ctx):
                return

        # log.debug ('No frames to read now')
