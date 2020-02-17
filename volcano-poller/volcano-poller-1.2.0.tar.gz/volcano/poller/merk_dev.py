from volcano.general import variant
from volcano.general.stddef import Quality
from volcano.general.xml_reader import XmlReader

from . import time_tools
from . import base_dev
from . import merk_defs
from . import connected_values
from .merk_nzif_common import ProtocolException

MEASURES_ENERGY = (
    ('Eap', 'Ean', 'Erp', 'Ern', 0x00),
)

'''
    Поддерживаемые форматы запросов (см. раздел 2.3.14 руководства Инкотекс):
    
    format:
        power_14    2.3.14.1, чтение мощностей запросом с кодом 14
        
        uicos_14    2.3.14.2, чтение токов, напряжений и углов запросом с кодом 14
'''

MERK230_TYPE_DEF = {
    'msr-pqs': [
        {'tags': ['P', 'P1', 'P2', 'P3'], 'f': 0.01, 'bwri': [0, 0, 0], 'pq_sign': 'P'},
        {'tags': ['Q', 'Q1', 'Q2', 'Q3'], 'f': 0.01, 'bwri': [0, 1, 0], 'pq_sign': 'Q'},
        {'tags': ['S', 'S1', 'S2', 'S3'], 'f': 0.01, 'bwri': [0, 2, 0], 'pq_sign': None}
    ],
    'msr-uicos': [
        {'tags': ['Ia', 'Ib', 'Ic'], 'f': 0.001, 'bwri': [2, None, None]},
        {'tags': ['Ua', 'Ub', 'Uc'], 'f': 0.01, 'bwri': [1, None, None]},
        {'tags': ['CosAB', 'CosAC', 'CosBC'], 'f': 0.001, 'bwri': [5, None, None]}
    ]
}

FREQ_TAG_NAME = 'F'
STATUS_TAG_NAME = 'status'


class MerkDevice(base_dev.BaseDevice):

    def __init__(self, my_xml_node, proposed_aux_name, parent_log):
        super().__init__(my_xml_node, proposed_aux_name, parent_log)

        p = XmlReader(my_xml_node)

        self.addr_ = p.get_int('slaveNb', min_val=0, max_val=0xff)

        # device type
        self.type_def_ = p.get_dic('type', merk_defs.g_merk_type_defs)

        # password
        pwd_str = p.get_str('pwd', '000000')
        if len(pwd_str) == 6:
            self.password_ = bytes([ord(x) for x in pwd_str])
        else:
            pwd_tokens = pwd_str.split(',')
            if len(pwd_tokens) != 6:
                raise Exception('{}: password "{}" is invalid: should be 6 ascii characters (111111) or 6 comma-separated codes (0x1,0x1,0x1,0x1,0x1,0x1)'.format(p.location(), pwd_str))
            
            try:
                self.password_ = bytes([int(tok, 16 if tok.startswith('0x') else 10) for tok in pwd_tokens])
            except:
                raise Exception('{}: password "{}" is invalid: should be 6 ascii characters (111111) or 6 comma-separated codes (0x1,0x1,0x1,0x1,0x1,0x1)'.format(p.location(), pwd_str))

        self.log().debug('Password parsed as {}'.format(self.password_))

        # timeouts
        self.timeout_general_ = time_tools.Timeout(p.get_time_secs('readPeriod', 5.0, min_val=0.0, max_val=600.0), expired=True)

        # Create values
        self.val_online_ = connected_values.ConnectedValue(self.branch('online'), variant.BoolValue(), True)
        self.values_ = {}
        for n1, n2, n3, n4, *r in MEASURES_ENERGY:      # pylint: disable=unused-variable
            for name in (n1, n2, n3, n4):
                self.values_[name] = connected_values.ConnectedValue(self.branch(name), variant.FloatValue(), is_obligatory=False)

        self.msr_pqs_ = MERK230_TYPE_DEF['msr-pqs']
        for x in self.msr_pqs_:
            nX, n1, n2, n3 = x['tags']
            for name in (nX, n1, n2, n3):
                if name:  # nX can be None
                    self.values_[name] = connected_values.ConnectedValue(self.branch(name), variant.FloatValue(), is_obligatory=False)

        self.msr_uicos_ = MERK230_TYPE_DEF['msr-uicos']
        for x in self.msr_uicos_:
            n1, n2, n3 = x['tags']
            for name in (n1, n2, n3):
                self.values_[name] = connected_values.ConnectedValue(self.branch(name), variant.FloatValue(), is_obligatory=False)
        
        self.values_[FREQ_TAG_NAME] = connected_values.ConnectedValue(self.branch(FREQ_TAG_NAME), variant.FloatValue(), is_obligatory=False)
        self.values_[STATUS_TAG_NAME] = connected_values.ConnectedValue(self.branch(STATUS_TAG_NAME), variant.IntValue(), is_obligatory=False)
                

    def sync(self, services: dict):
        assert isinstance(services, dict), services
        super().sync(services)
        self.val_online_.sync(services)
        for k, v in self.values_.items():       # pylint: disable=unused-variable
            v.sync(services)

    def on_channel_closed(self):
        self.log().debug('Channel closed and device going offline')
        self.set_offline()

    def set_offline(self):
        self.val_online_.set(False)
        # self.scaling_ = None
        for k, v in self.values_.items():       # pylint: disable=unused-variable
            v.invalidate(Quality.QUALITY_COMM)

    def work(self, ctx):
        log = self.log()

        if not self.timeout_general_.is_expired():
            return

        try:
            self.open_channel(ctx)
        except (ConnectionError, TimeoutError, ProtocolException) as e:
            log.warning(e)
            self.set_offline()
            self.timeout_general_.start()
            return

        self.val_online_.set(True)
        for name, con_val in self.values_.items():  # pylint: disable=unused-variable
            con_val.mark_unread()

        try:
            comment = 'Read status'
            try:
                self.read_status(ctx, comment)
            except (ConnectionError, TimeoutError, ProtocolException) as ex:
                log.warning('Error reading {}: {}'.format(comment, ex))
                if not ctx.is_open():
                    raise
        
            for n1, n2, n3, n4, arr in MEASURES_ENERGY:
                try:
                    self.read_energy(ctx, arr, 'Read energy {} {} {} {}'.format(n1, n2, n3, n4), (n1, n2, n3, n4))
                except (ConnectionError, TimeoutError, ProtocolException) as e:
                    if ctx.is_open():
                        log.warning(e)
                    else:
                        raise

            def calc_bwri(arr) -> int:
                p1, p2, p3 = arr
                res = p1 << 4
                if p2 is not None:
                    res |= p2 << 2
                if p3 is not None:
                    res |= p3
                return res
            

            for x in self.msr_pqs_:
                nX, n1, n2, n3 = x['tags']
                factor = x['f']
                bwri = calc_bwri(x['bwri'])
                pq_sign = x['pq_sign']

                comment = 'Read {} {} {}'.format(n1, n2, n3)
                try:
                    self.read_pqs(ctx, bwri, factor, comment, (nX, n1, n2, n3), pq_sign)
                except (ConnectionError, TimeoutError, ProtocolException) as e:
                    log.warning('Error reading {}: {}'.format(comment, e))
                    if not ctx.is_open():
                        raise

            for x in self.msr_uicos_:
                n1, n2, n3 = x['tags']
                factor = x['f']
                bwri = calc_bwri(x['bwri'])

                comment = 'Read {} {} {}'.format(n1, n2, n3)
                try:
                    self.read_uicos(ctx, bwri, factor, comment, (n1, n2, n3))
                except (ConnectionError, TimeoutError, ProtocolException) as e:
                    log.warning('Error reading {}: {}'.format(comment, e))
                    if not ctx.is_open():
                        raise

            comment = 'Read freq'
            try:
                self.read_freq(ctx, comment)
            except (ConnectionError, TimeoutError, ProtocolException) as ex:
                log.warning('Error reading {}: {}'.format(comment, ex))
                if not ctx.is_open():
                    raise

        except (ConnectionError, TimeoutError, ProtocolException) as e:
            log.warning(e)

        finally:
            for name, con_val in self.values_.items():
                if not con_val.is_read():
                    con_val.invalidate(Quality.QUALITY_COMM)
            self.timeout_general_.start()

    def open_channel(self, ctx):
        # access level
        req = bytes([self.addr_, 0x01, 0x01]) + self.password_

        ctx.send_rcv(req, None, 'Open channel', self.log())

    @staticmethod
    # None => энергия маскирована (не поддерживается)
    # rval: вт*ч
    def parse_energy_4_bytes(d: (bytes, bytearray), off: int) -> (int, None):
        assert isinstance(d, (bytes, bytearray)), d
        assert isinstance(off, int), off
        assert off + 4 <= len(d), (d, off)

        b0 = d[off + 0]
        b1 = d[off + 1]
        b2 = d[off + 2]
        b3 = d[off + 3]

        if b0 == 0xff and b1 == 0xff and b2 == 0xff and b3 == 0xff:
            return None

        return b2 | (b3 << 8) | (b0 << 16) | (b1 << 24)

    def read_energy(self, ctx, array_nb, comment, tpl):
        log = self.log()

        month_nb = 0
        tariff_nb = 0  # 0 - сумма тарифов

        req = bytes([self.addr_, 0x05, (array_nb << 4) | month_nb, tariff_nb])

        ctx.send_rcv(req, 16, comment, log)

        eap_wth = MerkDevice.parse_energy_4_bytes(ctx.data(), 0)
        ean_wth = MerkDevice.parse_energy_4_bytes(ctx.data(), 4)
        erp_wth = MerkDevice.parse_energy_4_bytes(ctx.data(), 8)
        ern_wth = MerkDevice.parse_energy_4_bytes(ctx.data(), 12)

        eap_kwth = 0.0 if eap_wth is None else eap_wth / 1000.0
        ean_kwth = 0.0 if ean_wth is None else ean_wth / 1000.0
        erp_kwth = 0.0 if erp_wth is None else erp_wth / 1000.0
        ern_kwth = 0.0 if ern_wth is None else ern_wth / 1000.0

        log.debug('Eap={} Ean={} Erp={} Ern={} [kwth]'.format(eap_kwth, ean_kwth, erp_kwth, ern_kwth))

        eap_name, ean_name, erp_name, ern_name = tpl

        self.values_[eap_name].set(eap_kwth)
        self.values_[ean_name].set(ean_kwth)
        self.values_[erp_name].set(erp_kwth)
        self.values_[ern_name].set(ern_kwth)

    # bwri - код чтения
    # factor - коэффициент (в Меркурии все измерения масштабируются статическим коэффициентом)
    # tpl - имена переменных, куда записать значения
    # pq_sign - 'P', 'Q', None
    def read_pqs(self, ctx, bwri, factor, comment, tpl, pq_sign):

        assert 0 <= bwri <= 0xff, bwri
        assert isinstance(tpl, tuple) and len(tpl) == 4, tpl
        assert pq_sign == 'P' or pq_sign == 'Q' or pq_sign is None, pq_sign

        def extract_pqs(d, off) -> int:
            b2 = d[off + 0]
            b1 = d[off + 1]
            b4 = d[off + 2]
            b3 = d[off + 3]

            b1_data = b1 & 0x3F     # маскируем старшие 2 разряда
            
            # старший разряд - направление P (0 = прямое, 1 = обратное)
            p_sign = 1 if (b1 & 0x80) == 0 else -1
            
            # 2й слева разряд - направление Q (0 = прямое, 1 = обратное)
            q_sign = 1 if (b1 & 0x40) == 0 else -1

            val = b4 | (b3 << 8) | (b2 << 16) | (b1_data << 24)
            
            if pq_sign == 'P':
                return val * p_sign

            if pq_sign == 'Q':
                return val * q_sign
            
            return val


        log = self.log()

        # 2.3.14.1
        req = bytes([self.addr_, 0x08, 0x14, bwri])
        ctx.send_rcv(req, 16, comment, log)

        sum_raw = extract_pqs(ctx.data(), 0)
        ph1_raw = extract_pqs(ctx.data(), 4)
        ph2_raw = extract_pqs(ctx.data(), 8)
        ph3_raw = extract_pqs(ctx.data(), 12)

        sum_phys = sum_raw * factor
        ph1_phys = ph1_raw * factor
        ph2_phys = ph2_raw * factor
        ph3_phys = ph3_raw * factor

        log.debug('%s: sum_raw=%s, ph1_raw=%s, ph2_raw=%s, ph3_raw=%s, sum=%s, ph1=%s, ph2=%s, ph3=%s',
                  comment, sum_raw, ph1_raw, ph2_raw, ph3_raw, sum_phys, ph1_phys, ph2_phys, ph3_phys)

        sum_name, ph1_name, ph2_name, ph3_name = tpl

        self.values_[sum_name].set(sum_phys)
        self.values_[ph1_name].set(ph1_phys)
        self.values_[ph2_name].set(ph2_phys)
        self.values_[ph3_name].set(ph3_phys)
        
    def read_uicos(self, ctx, bwri, factor, comment, tpl):

        assert 0 <= bwri <= 0xff, bwri
        assert isinstance(tpl, tuple) and len(tpl) == 3, tpl

        def extract_uicos(d, off) -> int:
            b1 = d[off + 0]
            b3 = d[off + 1]
            b2 = d[off + 2]

            return b3 | (b2 << 8) | (b1 << 16)


        log = self.log()

        # 2.3.14.2
        req = bytes([self.addr_, 0x08, 0x14, bwri])
        ctx.send_rcv(req, 9, comment, log)

        ph1_raw = extract_uicos(ctx.data(), 0)
        ph2_raw = extract_uicos(ctx.data(), 3)
        ph3_raw = extract_uicos(ctx.data(), 6)

        ph1_phys = ph1_raw * factor
        ph2_phys = ph2_raw * factor
        ph3_phys = ph3_raw * factor

        log.debug('%s: ph1_raw=%s, ph2_raw=%s, ph3_raw=%s, ph1=%s, ph2=%s, ph3=%s',
                  comment, ph1_raw, ph2_raw, ph3_raw, ph1_phys, ph2_phys, ph3_phys)

        ph1_name, ph2_name, ph3_name = tpl

        self.values_[ph1_name].set(ph1_phys)
        self.values_[ph2_name].set(ph2_phys)
        self.values_[ph3_name].set(ph3_phys)
        
    def read_freq(self, ctx, comment):

        log = self.log()

        # 2.3.14.4
        req = bytes([self.addr_, 0x08, 0x14, 0x40])
        ctx.send_rcv(req, 3, comment, log)

        d = ctx.data()
        b1 = d[0]
        b3 = d[1]
        b2 = d[2]

        freq_raw = b3 | (b2 << 8) | (b1 << 16)
        freq_phys = freq_raw * 0.01

        log.debug('%s: raw=%s, phys=%s', comment, freq_raw, freq_phys)

        self.values_[FREQ_TAG_NAME].set(freq_phys)
        
    def read_status(self, ctx, comment):

        log = self.log()

        # 2.3.10
        req = bytes([self.addr_, 0x08, 0x0a])
        ctx.send_rcv(req, 6, comment, log)

        d = ctx.data()
        
        big_val = (d[0] << 40) | (d[1] << 32) | (d[2] << 24) | (d[3] << 16) | (d[4] << 8) | d[5]
        
        log.debug('%s: status=%s', comment, big_val)

        self.values_[STATUS_TAG_NAME].set(big_val)
