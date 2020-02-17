import struct

from volcano.general.stddef import Quality, ValueType
from volcano.general import stdsvcdef
from volcano.general.xml_reader import XmlReader, LoadException
from volcano.general import modbus

from . import time_tools


class MbFrame:
    def __init__(self, my_xml_node, proposed_aux_name, parent_dev, parent_log):
        p = XmlReader(my_xml_node)

        self.parent_dev_ = parent_dev
        self.aux_name_ = p.get_str('name', proposed_aux_name)
        self.log_ = parent_log.getChild(self.aux_name_)

    def aux_name(self):
        return self.aux_name_

    def log(self):
        return self.log_

    # def set_tag(self, tag_name_or_id: (int, str), value, quality: int) -> None:
    #    assert self.pipe_set_
    #    self.pipe_set_.set_tag(tag_name_or_id, value, quality)

    def device(self):
        return self.parent_dev_

    def empty(self):
        raise NotImplementedError()

    def read_write(self, ctx):
        raise NotImplementedError()

    def sync(self, services: dict):
        raise NotImplementedError()

    def on_channel_closed(self):
        raise NotImplementedError()


class MbFrameReg(MbFrame):
    def __init__(self, xml_node, proposed_aux_name, parent_dev, parent_log):

        super().__init__(xml_node, proposed_aux_name, parent_dev, parent_log)

        p = XmlReader(xml_node)

        self.fn_nb_ = p.get_int('fn', default=3, min_val=3, max_val=4)
        self.addr_ = None  # p.get_int('fn', default=-1, min=0, max=0xffff)
        self.nb_words_ = None

        read_period = p.get_time_secs('readPeriod', default=10.0, min_val=0.0, max_val=60.0)
        self.read_timeout_ = time_tools.Timeout(read_period, expired=True)

        self.ties_ = []
        self.load_ties_(xml_node)

        if not self.ties_:
            return

        # calc addr & size
        last_addr = None
        for t in self.ties_:
            if self.addr_ is None or self.addr_ > t.addr():
                self.addr_ = t.addr()

            tie_last_addr = t.addr() + t.size_words() - 1
            if last_addr is None or last_addr < tie_last_addr:
                last_addr = tie_last_addr

        assert last_addr > self.addr_

        self.nb_words_ = last_addr - self.addr_ + 1
        if self.nb_words_ > modbus.MAX_READ_WORDS_NB:
            raise LoadException('Frame size {} exceeds maximum allowed {}'.format(self.nb_words_, modbus.MAX_READ_WORDS_NB), xml_node)

    def empty(self):
        return len(self.ties_) == 0

    def sync(self, services: dict):
        assert isinstance(services, dict), services
        for t in self.ties_:
            t.sync(services)

    def load_ties_(self, xml_node):
        for node in xml_node:
            if node.tag != 'Link':
                raise LoadException('Unknown node name: {}'.format(node.tag), node)

            p = XmlReader(node)

            # tag_full_name = self.device().get_tag_full_name(p.get_str('name'))

            # TagInfo ti;
            # tie: MbFrameRegTie
            fmt_str = p.get_str('fmt')
            fmt = modbus.MB_FORMATS_DICT.get(fmt_str, None)
            if fmt:
                tie = MbFrameRegTieNum(p, fmt, self.device().branch(), self.log())
            else:
                if fmt_str == 'bool_sp':
                    pass  # tie = new MbWordFrameTie_Bool_SP( node, ti, &m_Address, log, &ok );
                elif fmt_str == 'bool_dp':
                    pass  # tie = new MbWordFrameTie_Bool_DP( node, ti, &m_Address, log, &ok );
                elif fmt_str == 'bool_cmp':
                    pass  # tie = new MbWordFrameTie_Bool_RegValueCompare( node, ti, &m_Address, log, &ok );
                else:
                    raise LoadException(node, 'Unknown format: "{}"'.format(fmt_str))

            assert tie
            # if ( tie->isWritable() )
            #    getDevice()->SubscribeTag( ti.id, this, ties_.size(), 0 );
            self.ties_.append(tie)

    def read_write(self, ctx):
        if not self.read_timeout_.is_expired():
            return

        log = self.log()

        log.debug('Read frame')

        try:
            data_bytes = ctx.read_words(self.device().slave_nb(), self.fn_nb_, self.addr_, self.nb_words_, self.aux_name(), log)
            assert isinstance(data_bytes, (bytes, bytearray)), data_bytes
            assert len(data_bytes) == self.nb_words_ * 2, data_bytes

            for tie in self.ties_:
                tie.on_read_complete(data_bytes, 2 * (tie.addr() - self.addr_))

        except (ConnectionError, TimeoutError, modbus.MbException, modbus.MbError) as e:
            log.warning(e)
            for tie in self.ties_:
                tie.invalidate(Quality.QUALITY_COMM)
        finally:
            self.read_timeout_.start()

    def on_channel_closed(self):
        for tie in self.ties_:
            tie.invalidate(Quality.QUALITY_COMM)


class MbFrameRegTie:
    def sync(self, services: dict):
        raise NotImplementedError()

    def on_read_complete(self, data_bytes: bytearray, my_offset: int):
        raise NotImplementedError()

    def invalidate(self, quality: int):
        raise NotImplementedError()


class MbFrameRegTieNum(MbFrameRegTie, stdsvcdef.IFindTagHandler):
    # mb_fmt: see vctools.modbus_formats
    def __init__(self, p: XmlReader, mb_fmt: tuple, branch: str, log):
        assert isinstance(p, XmlReader), p
        assert isinstance(mb_fmt, tuple), mb_fmt
        assert isinstance(branch, str), branch

        fmt_id, fmt_size_words, fmt_min_n, fmt_max_n, fmt_struct_format, *r = mb_fmt    # pylint: disable=unused-variable

        self.fmt_size_words_ = fmt_size_words
        self.fmt_map_string_ = fmt_struct_format
        self.tag_short_name_ = p.get_str('name')
        self.tag_full_name_ = branch + '.' + self.tag_short_name_
        self.abs_addr_ = p.get_int('addr', min_val=0, max_val=(0xffff - fmt_size_words + 1))

        self.log_ = log
        # self.pipe_set_: services_defs.ISetValueService = None
        self.pipe_set_ = None

        self.value_ = None
        self.quality_ = Quality.QUALITY_NOT_INIT

    def addr(self):
        return self.abs_addr_

    def size_words(self):
        return self.fmt_size_words_

    def sync(self, services: dict):
        assert isinstance(services, dict), services

        assert 'set' in services, services
        assert isinstance(services['set'], stdsvcdef.ISetValueService)
        self.pipe_set_ = services['set']

        assert 'find' in services, services
        assert isinstance(services['find'], stdsvcdef.IFindTagService)
        services['find'].find_tag(self.tag_full_name_, self)

    def on_find_tag_ok(self, tag_id: int, tag_name: str, vt: str, user_data):
        if ValueType(vt) in (ValueType.VT_INT, ValueType.VT_FLOAT):
            # pipe.subscribe(tag_name, self)
            self.pipe_set_.set_tag(tag_name, self.value_, self.quality_)
        else:
            raise Warning('Cant link tag {} [{}]. Only support int,float'.format(tag_name, vt))

    def on_find_tag_err(self, tag_name_or_id: (int, str), user_data):
        raise Warning('Cant link tag {}: tag not found'.format(self.tag_full_name_))

    def on_read_complete(self, data_bytes: bytearray, my_offset: int):
        value, = struct.unpack_from(self.fmt_map_string_, data_bytes, my_offset)

        if self.value_ != value or self.quality_ != 0:
            self.value_ = value
            self.quality_ = 0
            self.log_.debug('Tie updated {}={}[{}]'.format(self.tag_full_name_, self.value_, self.quality_))
            self.pipe_set_.set_tag(self.tag_full_name_, self.value_)

    def invalidate(self, quality: int):
        if self.value_ is not None or self.quality_ != quality:
            self.value_ = None
            self.quality_ = quality
            self.log_.debug('Tie invalidated {}={}[{}]'.format(self.tag_full_name_, self.value_, self.quality_))
            self.pipe_set_.set_tag(self.tag_full_name_, None, self.quality_)
