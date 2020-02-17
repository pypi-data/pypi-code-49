import collections
import datetime

from volcano.general import variant
from volcano.general.stddef import Quality
from volcano.general.xml_reader import XmlReader
from volcano.general.bin import word

from . import time_tools
from . import base_dev
from . import connected_values
from .merk_nzif_common import ProtocolException, NackException, BadDataException
from .nzif_defs import get_nzif_defs
from .num_ops import bcd_to_int, hi_byte, lo_byte
from .nzif_profiles import NzifProfiles, MeterInfo

NzifScaling = collections.namedtuple('NzifScaling', ('Ki', 'Ku', 'Ca', 'I_A', 'U_V', 'E_kwth', 'PQS_kwt', 'F_Hz', 'Cos'))


def _create_scaling(ki, ku, const_a, mtd) -> NzifScaling:
    i_a = 0.001 * 0.1 * float(ki) * float(mtd['ci'])  # 0.001 -перевод из мА в А
    u_v = 0.01 * float(ku)
    e_kwth = float(ki) * float(ku) / (2.0 * float(const_a))
    pqs_kwt = 0.001 * float(ku) * float(ki) * float(mtd['ks']) * 0.001  # 1ая 1/1000 - из формулы, 2ая 1/1000 - для перевода вт->кВт
    f_hz = 0.01
    cos = 0.01  # 2.4.3.23

    return NzifScaling(ki, ku, const_a, i_a, u_v, e_kwth, pqs_kwt, f_hz, cos)


def _get_uint32_ml(ba, offset):
    return (ba[offset + 0] << 24) | (ba[offset + 1] << 16) | (ba[offset + 2] << 8) | ba[offset + 3]


RWRI_SIGN_P = 'P'
RWRI_SIGN_Q = 'Q'
VAR_NAME_DATETIME = 'date_time'


class NzifDevice(base_dev.BaseDevice):

    def __init__(self, my_xml_node, proposed_aux_name, parent_log):
        super().__init__(my_xml_node, proposed_aux_name, parent_log)
        
        log = self.log()

        p = XmlReader(my_xml_node)

        self.addr_ = p.get_int('slaveNb', min_val=0, max_val=0xff)
        
        self.time_sync_delta_sec_ = p.get_int('timeSyncDeltaSec', min_val=0, max_val=600, default=30)
        self.last_sync_date_ = None     # последняя синхронизация. Объект Date()
        if self.time_sync_delta_sec_ == 0:
            log.info('Time sync disabled. Use timeSyncDeltaSec="XX" argument for Device to enable.')

        # device type
        self.type_def_ = p.get_dic('type', get_nzif_defs(log))

        # password
        pwd_str = p.get_str('pwd', '000000')
        if len(pwd_str) != 6:
            raise Exception('{}: password "{}" is invalid: should be 6 characters long'.format(p.location(), pwd_str))
        self.password_ = bytes([ord(x) for x in pwd_str])

        self.scaling_ = None

        # timeouts
        self.timeout_general_ = time_tools.Timeout(p.get_time_secs('readPeriod', 5.0, min_val=0.0, max_val=600.0), expired=True)

        # profiles
        enable_profiles = p.get_bool('profiles', default=False)
        if enable_profiles:
            mi = MeterInfo(Address=self.addr_, PulseToPhysicalUnitsFactor=1.0, MemorySize=0x10000, MaxNbOfAddrToReadAtOnce=16)
            self.profiles_ = NzifProfiles(mi)
            log.info('Profiles reading ON')
        else:
            self.profiles_ = None
            log.info('Profiles reading OFF')

        # Create values
        self.msr_1ph_ = self.type_def_['msr-1ph']
        self.msr_3ph_ = self.type_def_['msr-3ph']
        self.msr_energy_ = self.type_def_['energy']

        self.val_online_ = connected_values.ConnectedValue(self.branch('online'), variant.BoolValue(), True)

        self.values_ = {}

        for name in ('TypeCode', 'ConstA', 'Ki', 'Ku', 'Status'):
            self.values_[name] = connected_values.ConnectedValue(self.branch(name), variant.IntValue(), False)

        for x in self.msr_1ph_:
            name = x['tag']
            self.values_[name] = connected_values.ConnectedValue(self.branch(name), variant.FloatValue(), False)

        for x in self.msr_3ph_:
            nX, n1, n2, n3 = x['tags']
            for name in (nX, n1, n2, n3):
                if name:  # nX can be None
                    self.values_[name] = connected_values.ConnectedValue(self.branch(name), variant.FloatValue(), False)

        for x in self.msr_energy_:
            n1, n2, n3, n4 = x['tags']
            for name in (n1, n2, n3, n4):
                self.values_[name] = connected_values.ConnectedValue(self.branch(name), variant.FloatValue(), False)

        self.values_[VAR_NAME_DATETIME] = connected_values.ConnectedValue(self.branch(VAR_NAME_DATETIME), variant.StrValue(), is_obligatory=False)


    def sync(self, services: dict):
        assert isinstance(services, dict), services
        super().sync(services)

        self.val_online_.sync(services)
        for k, v in self.values_.items():   # pylint: disable=unused-variable
            v.sync(services)

    def on_channel_closed(self):
        self.log().debug('Channel closed and device going offline')
        self.set_offline()

    def set_offline(self):
        self.val_online_.set(False)
        self.scaling_ = None
        for k, v in self.values_.items():   # pylint: disable=unused-variable
            v.invalidate(Quality.QUALITY_COMM)

    def work(self, ctx):
        log = self.log()

        if not self.timeout_general_.is_expired():
            return

        # Этот блок должен быть ДО открытия канала, потому что часть параметров (например, typeCode) считываются в критическом блоке
        # (1й try/except) и они должны быть отмечены как read уже в нем.
        for name, con_val in self.values_.items():  # pylint: disable=unused-variable
            con_val.mark_unread()

        try:
            self.open_channel(ctx)

            const_a = self.read_type_info(ctx)

            if self.scaling_ is None:
                ki, ku = self.read_ki_ku(ctx)
                self.scaling_ = _create_scaling(ki, ku, const_a, self.type_def_)

            self.read_status(ctx)

        except (ConnectionError, TimeoutError, ProtocolException) as e:
            log.warning(e)
            self.set_offline()
            self.timeout_general_.start()
            return

        self.val_online_.set(True)

        try:  # finally -> restart timeout
            for x in self.msr_3ph_:
                nX, n1, n2, n3 = x['tags']
                f = x['f']
                p1, p2, p3 = x['rwri']
                comment = 'Read {} {} {}'.format(n1, n2, n3)
                try:
                    self.read_3phase(ctx, getattr(self.scaling_, f), p1, p2, p3, comment, (nX, n1, n2, n3))
                except (ConnectionError, TimeoutError, ProtocolException) as e:
                    log.warning('Error reading {}: {}'.format(comment, e))
                    if not ctx.is_open():
                        raise

            for x in self.msr_1ph_:
                n = x['tag']
                f = x['f']
                p1, p2, p3 = x['rwri']

                comment = 'Read {}'.format(n)
                try:
                    self.read_1phase(ctx, getattr(self.scaling_, f), p1, p2, p3, comment, n)
                except (ConnectionError, TimeoutError, ProtocolException) as e:
                    log.warning('Error reading {}: {}'.format(comment, e))
                    if not ctx.is_open():
                        raise

            for x in self.msr_energy_:
                n1, n2, n3, n4 = x['tags']
                arr = x['arr']
                comment = 'Read energy {} {} {} {}'.format(n1, n2, n3, n4)
                try:
                    self.read_energy(ctx, arr, comment, (n1, n2, n3, n4))
                except (ConnectionError, TimeoutError, ProtocolException) as e:
                    log.warning('Error reading {}: {}'.format(comment, e))
                    if not ctx.is_open():
                        raise
            # timesync
            try:
                self.time_sync(ctx)
            except (ConnectionError, TimeoutError, ProtocolException) as ex:
                log.warning('Error during time sync: {}'.format(ex))
                if not ctx.is_open():
                    raise

            # profiles
            try:
                if self.profiles_:
                    self.profiles_.read_profiles(ctx, 2, log)
            except (ConnectionError, TimeoutError, ProtocolException) as ex:
                log.warning('Error during reading profiles: {}'.format(ex))
                if not ctx.is_open():
                    raise

        except (ConnectionError, TimeoutError, ProtocolException) as e:
            # Here we get errors only from Ph1, Ph3, En reads when ctx is not recoverable.
            # Isonline remains True
            # log.warn already called
            for name, con_val in self.values_.items():
                if not con_val.is_read():
                    con_val.invalidate(Quality.QUALITY_COMM)
        finally:
            self.timeout_general_.start()

    def open_channel(self, ctx):
        log = self.log_

        req = bytes([self.addr_, 0x01]) + self.password_

        try:
            ctx.send_rcv(req, None, 'Open channel', self.log())
        except NackException as e:
            if e.nack_code == 3:
                log.warning('Nack 3 in open channel often caused by invalid password. Current password: {}'.format(self.password_))
            raise

    # rval: ConstA / raise
    def read_type_info(self, ctx):
        log = self.log()
        # 2.4.3.24
        # Исполнение, константа А
        # Команда предназначена для чтения варианта исполнения счетчика, установленного на
        # заводе-изготовителе. Команда введена в счетчики СЭТ-4ТМ.02 начиная с V14.ХХ.ХХ.
        req = bytes([self.addr_, 0x08, 0x12])

        ctx.send_rcv(req, 3, 'Read type info', self.log())  # * is ok

        const_a_code = ctx.data(1) & 0x0f
        const_a_map = {
            0: 5000,
            1: 25000,
            2: 1250,
            3: 6250,
            4: 500,
            5: 250,
            6: 6400
        }
        const_a = const_a_map.get(const_a_code, None)
        if const_a is None:
            raise BadDataException('{}: Unknown const A code: {}'.format('Read type info', const_a_code))

        type_code = (ctx.data(2) & 0xf0) >> 4
        if self.type_def_['type_code'] != type_code:
            raise BadDataException(
                'Type code mismatch. Expected {}, got {}'.format(self.type_def_['type_code'], type_code))

        log.debug("TypeCode=%s, ConstA=%s", type_code, const_a)

        self.values_['TypeCode'].set(type_code)
        self.values_['ConstA'].set(const_a)

        return const_a

    # rval: ki,ku / raise
    def read_ki_ku(self, ctx):
        # Ki Ku  - 2.4.3.3
        log = self.log()

        req = bytes((self.addr_, 0x08, 0x02))

        ctx.send_rcv(req, 10, 'Read KiKu', self.log())

        ku = word(ctx.data(0), ctx.data(1))
        ki = word(ctx.data(2), ctx.data(3))

        log.debug('Ki=%s, Ku=%s', ki, ku)

        self.values_['Ki'].set(ki)
        self.values_['Ku'].set(ku)

        return ki, ku

    def read_status(self, ctx) -> None:
        # 2.4.3.14
        log = self.log()

        req = bytes((self.addr_, 0x08, 0x0a))
        nb_bytes_expected = self.type_def_['st_bytes']

        ctx.send_rcv(req, nb_bytes_expected, 'Read status', self.log())

        d = ctx.data()
        status = 0
        for i in range(nb_bytes_expected):
            status += d[i] << (8 * i)

        log.debug('Status={:02x}'.format(status))

        self.values_['Status'].set(status)

    # при групповом чтении измерений возвращает элемент
    # item:
    #	0 = сумма фаз
    #	1-3 = по указанной фазе
    # rval: (value, sign_p, sign_q)
    @staticmethod
    def get_group_read_item(data, item):
        # 2.4.3.23
        # В ответ на запрос счетчик возвращает слово из трех байт в двоичном коде. Два старших
        # бита старшего байта указывают положение вектора полной мощности и должны маскироваться
        # для получения модуля значения параметра. В счетчиках СЭТ-4ТМ.02,03М, ПСЧ-3,4ТМ.05М
        # при чтении мощности потерь старшие биты указывают положение вектора полной мощности потерь.
        hi_b = data[item * 3 + 0]
        hi_b_data = hi_b & 0x3f
        hi_b_p_sgn = hi_b & 0x80
        hi_b_q_sgn = hi_b & 0x40

        value = (hi_b_data << 16) | (data[item * 3 + 1] << 8) | data[item * 3 + 2]
        sign_p = 1 if hi_b_p_sgn == 0 else -1
        sign_q = 1 if hi_b_q_sgn == 0 else -1

        return value, sign_p, sign_q

    def time_sync(self, ctx):
        # 2.4.1.1.1
        log = self.log_
        comment = 'Read time'
        con_val = self.values_[VAR_NAME_DATETIME]

        req = bytes([self.addr_, 0x04, 0x00])

        try:
            ctx.send_rcv(req, 8, comment, log)
        except NackException:
            con_val.invalidate(Quality.QUALITY_NA)
            raise
            
        # Замер системного времени надо сделать максимально близко к чтению времени из счетчика
        sys_time = datetime.datetime.now()

        try:
            ss = bcd_to_int(ctx.data(0))        # !ValueError
            mm = bcd_to_int(ctx.data(1))
            hh = bcd_to_int(ctx.data(2))
            D = bcd_to_int(ctx.data(4))
            M = bcd_to_int(ctx.data(5))
            Y = bcd_to_int(ctx.data(6)) + 2000
            
            dtm = datetime.datetime(Y, M, D, hh, mm, ss)        # !ValueError
        except ValueError as ex:
            log.warn(ex)
            con_val.invalidate(Quality.QUALITY_NA)
            raise ProtocolException(str(ex))
        
        con_val.set(str(dtm))

        # compare 
        delta = sys_time - dtm
        delta_secs = int(delta.total_seconds())

        log.debug('Datetime: Meter=%s, System=%s, Delta=%s sec', dtm, sys_time, delta_secs)

        if self.time_sync_delta_sec_ == 0 or self.time_sync_delta_sec_ > abs(delta_secs):
            log.debug('Time sync disabled for device')
            return
        
        log.debug('Time sync needed: Delta is %s sec [Max allowed = %s sec]', abs(delta_secs), self.time_sync_delta_sec_)
        
        if self.last_sync_date_ is not None and self.last_sync_date_ == datetime.date.today():
            log.debug('Time sync already done today')
            return
            
        if delta_secs > 120:
            secs_to_add = 120
        elif delta_secs < -120: 
            secs_to_add = -120
        else:
            secs_to_add = delta_secs
            
            
        # Ограничением выполнения команды является требование коррекции времени без перехода
        # в следующий или предыдущий час. Если, тем не менее, запрашивается коррекция времени
        # с переходом в следующий или предыдущий час, то счетчик возвращает в байте состояния обмена
        # код 01h (недопустимая команда или параметр).
        # Поскольку коррекция идет макс на 120 сек (2 мин), то проверим минуты
        new_time = dtm + datetime.timedelta(seconds=secs_to_add)
        if dtm.hour != new_time.hour:
            log.debug('Time sync now would result in hour change. Postponing')
            return
            
        # Тут могут быть отрицательные значения, но для нас это неважно: int32 для отрицательных
        # значений будет FF FF FF XY, а i16 FF XY, то есть отбрасывание старших
        # байтов валидно.
        req = bytes([self.addr_, 0x03, 0x0b, hi_byte(secs_to_add), lo_byte(secs_to_add)])
        comment = 'Adjust time'
            
        try:
            ctx.send_rcv(req, None, comment, log)
        except NackException as ex:
            # con_val.invalidate(Quality.QUALITY_NA) Это была запись, нет нужды инвалидировать текущее время
            # Часы уже корректировались, запомним это. Такой вариант бывает, если Ридер запустить повторно, ведь я пока не сохраняю в БД даты последней коррекции
            if ex.nack_code == 0x04:
                log.warn('Time sync failed with nack code 4 (already synced today)')
                return
            # Как было описано выше, этот код означает, что была попытка перевести часы в другой час. Хотя у меня и есть
            # защита от этого, но кто знает.
            elif ex.nack_code == 0x01:
                log.warn('Time sync failed with nack code 1 (attempt to change an hour). Just repeat later.')
                return
            else:
                raise
            
        log.info('Time successfully synced')
        self.last_sync_date_ = datetime.date.today()
        

    @staticmethod
    def msr_code_rwri(mode, param, phase):
        return (mode << 4) | (param << 2) | phase

    def read_3phase(self, ctx, scaling_f, rwri_p1, rwri_p2, rwri_sign, comment, targets_tuple):
        # 2.4.3.28
        log = self.log_

        req = bytes([self.addr_, 0x08, 0x16, NzifDevice.msr_code_rwri(rwri_p1, rwri_p2, 0)])

        try:
            ctx.send_rcv(req, 12, comment, log)
        except NackException as e:
            q = Quality.QUALITY_NA_TEMP if e.nack_code == 0x07 else Quality.QUALITY_NA
            for n in targets_tuple:
                if n:
                    self.values_[n].invalidate(q)
            raise

        sum_raw = 0.0
        if targets_tuple[0] is not None:
            sum_raw, sign_p, sign_q = NzifDevice.get_group_read_item(ctx.data(), 0)
            if rwri_sign == RWRI_SIGN_P: sum_raw = sum_raw * sign_p
            if rwri_sign == RWRI_SIGN_Q: sum_raw = sum_raw * sign_q

        ph1_raw, sign_p, sign_q = NzifDevice.get_group_read_item(ctx.data(), 1)
        if rwri_sign == RWRI_SIGN_P: ph1_raw = ph1_raw * sign_p
        if rwri_sign == RWRI_SIGN_Q: ph1_raw = ph1_raw * sign_q

        ph2_raw, sign_p, sign_q = NzifDevice.get_group_read_item(ctx.data(), 2)
        if rwri_sign == RWRI_SIGN_P: ph2_raw = ph2_raw * sign_p
        if rwri_sign == RWRI_SIGN_Q: ph2_raw = ph2_raw * sign_q

        ph3_raw, sign_p, sign_q = NzifDevice.get_group_read_item(ctx.data(), 3)
        if rwri_sign == RWRI_SIGN_P: ph3_raw = ph3_raw * sign_p
        if rwri_sign == RWRI_SIGN_Q: ph3_raw = ph3_raw * sign_q

        sum_physical = sum_raw * scaling_f
        ph1_physical = ph1_raw * scaling_f
        ph2_physical = ph2_raw * scaling_f
        ph3_physical = ph3_raw * scaling_f

        log.debug('%s: sum_raw=%s, ph1_raw=%s, ph2_raw=%s, ph3_raw=%s, sum=%s, ph1=%s, ph2=%s, ph3=%s',
                  comment, sum_raw, ph1_raw, ph2_raw, ph3_raw, sum_physical, ph1_physical, ph2_physical, ph3_physical)

        if targets_tuple[0] is not None:
            self.values_[targets_tuple[0]].set(sum_physical)
        self.values_[targets_tuple[1]].set(ph1_physical)
        self.values_[targets_tuple[2]].set(ph2_physical)
        self.values_[targets_tuple[3]].set(ph3_physical)

    def read_1phase(self, ctx, scaling_f, rwri_p1, rwri_p2, rwri_p3, comment, target):
        # 2.4.3.28
        log = self.log_

        req = bytes((self.addr_, 0x08, 0x11, NzifDevice.msr_code_rwri(rwri_p1, rwri_p2, rwri_p3)))

        try:
            ctx.send_rcv(req, 3, comment, log)
        except NackException as e:
            q = Quality.QUALITY_NA_TEMP if e.nack_code == 0x07 else Quality.QUALITY_NA
            self.values_[target].invalidate(q)
            raise

        val_raw, sign_p, sign_q = NzifDevice.get_group_read_item(ctx.data(), 0) # pylint: disable=unused-variable
        val_phys = val_raw * scaling_f

        log.debug('%s: raw=%s, phys=%s', comment, val_raw, val_phys)

        self.values_[target].set(val_phys)

    def read_energy(self, ctx, array_nb, comment, tags_tuple):
        log = self.log_

        assert self.scaling_ is not None

        month_nb = 0
        tariff_nb = 0

        req = bytes([self.addr_, 0x05, (array_nb << 4) | month_nb, tariff_nb])

        try:
            ctx.send_rcv(req, 16, comment, log)
        except NackException as e:
            q = Quality.QUALITY_NA_TEMP if e.nack_code == 0x07 else Quality.QUALITY_NA
            for n in tags_tuple:
                self.values_[n].invalidate(q)
            raise

        f = self.scaling_.E_kwth
        eap = _get_uint32_ml(ctx.data(), 0) * f
        ean = _get_uint32_ml(ctx.data(), 4) * f
        erp = _get_uint32_ml(ctx.data(), 8) * f
        ern = _get_uint32_ml(ctx.data(), 12) * f

        log.debug("Eap=%s, Ean=%s, Erp=%s, Ern=%s", eap, ean, erp, ern)

        self.values_[tags_tuple[0]].set(eap)
        self.values_[tags_tuple[1]].set(ean)
        self.values_[tags_tuple[2]].set(erp)
        self.values_[tags_tuple[3]].set(ern)
