import datetime
import collections

from .num_ops import bcd_to_int, make_word, hi_byte, lo_byte
from .merk_nzif_common import ProtocolException, NackException


PROFILE_RECORD_SZ = 8
MEM_LEN = 65536

MeterInfo = collections.namedtuple('MeterInfo', 'Address PulseToPhysicalUnitsFactor MemorySize MaxNbOfAddrToReadAtOnce')

CrProfileInfo = collections.namedtuple('CrProfileInfo', 'Address Overflow DateTime')


class NzifProfiles:
    def __init__(self, mi: MeterInfo):
        self.meter_info_ = mi
        
        self.LastReadAddress = -1       # if not yet read
        self.HasActiveHeader = False    # true => after last read header we didnt finish all its data-records
        
        # Defined if HasActiveHeader == True:
        self.HeaderDtmUtc = None                    # Date of the last header
        self.NbDataRecordsParsedSinceHeader = None 
        self.AggIvlMins = None


    def set_header(self, dtm_utc: datetime.datetime, agg_ivl: int):
        self.HasActiveHeader = True
        self.HeaderDtmUtc = dtm_utc
        self.NbDataRecordsParsedSinceHeader = 0
        self.AggIvlMins = agg_ivl

    def read_cr_profile_info(self, ctx, log) -> CrProfileInfo:
        # 2.4.3.5
        req = bytes((self.meter_info_.Address, 0x08, 0x04))
        
        ctx.send_rcv(req, 7, 'ReadCrProfileInfo', log)

        overflow = (ctx.data(0) & 0x80) > 0

        try:
            m = bcd_to_int(ctx.data(0) & 0x7f)
            h = bcd_to_int(ctx.data(1))
            D = bcd_to_int(ctx.data(2))
            M = bcd_to_int(ctx.data(3))
            Y = bcd_to_int(ctx.data(4)) + 2000
            
            dtm = datetime.datetime(Y, M, D, h, m)
        except ValueError as ex:
            log.warn(ex)
            raise ProtocolException(str(ex))

        cr_profile_addr = make_word(ctx.data(5), ctx.data(6))

        log.debug('Current profile: %s; Overflow: %s; Address: %s', dtm, overflow, cr_profile_addr)

        if (cr_profile_addr % 8) != 0:
            raise ProtocolException('Current profile address is not modulous to 8: {}'.format(cr_profile_addr))

        return CrProfileInfo(cr_profile_addr, overflow, dtm)

    # !NackException (subclass of ProtocolException)
    def read_once(self, ctx, start_addr: int, nb_recs: int, cr_profile_info: CrProfileInfo, log):
    
        log.debug('Read %s records from addr %s', nb_recs, start_addr)

        data_sz = nb_recs * PROFILE_RECORD_SZ

        # par 2.4.4
        req = bytes((self.meter_info_.Address, 0x06, 0x03, hi_byte(start_addr), lo_byte(start_addr), data_sz))
        
        try:
            ctx.send_rcv(req, data_sz, 'ReadProfileMemory', log)
        except NackException as ex:
            # 2.4.4.1
            # Если в конце физической памяти массива профиля отсутствует место для
            # записи целого часа (заголовка часа и часовых срезов мощности), то эта область 
            # памяти не используется, не очищается и может содержать любую информацию. Ее нельзя читать.
            # Заголовок следующего часа начинается с нулевого адреса и устанавливается признак переполнения массива профиля мощности.
            # По факту это значит, что попытка читать зону в конце часто оборачивается ответом NACK<1>
            if ex.nack_code == 1:
                # действительно мы в самом конце? попробуем считывать по 1 записи
                next_addr = start_addr + data_sz
                if next_addr < 65400:
                    return

                if nb_recs > 1:
                    log.debug('Reached end of memory, start reading by 1')
                    self.read_once(ctx, start_addr, 1, cr_profile_info, log)
                else:
                    log.debug('Reached end of memory, goto 0')
                    self.HasActiveHeader = False
                    self.LastReadAddress = MEM_LEN - PROFILE_RECORD_SZ
                    return
            else:
                raise

        self.LastReadAddress = start_addr + data_sz - PROFILE_RECORD_SZ

        for rec in range(nb_recs):
            offset = rec * PROFILE_RECORD_SZ
            rec_addr = start_addr + offset

            if not self.HasActiveHeader:
                try:
                    tpl = _parse_rec_header(ctx.data(), offset, log)
                except Exception as ex:
                    log.warn('Rec %s: header is invalid, skipping', rec_addr)
                    continue
                
                if not tpl:
                    # Поскольку мы начинаем наше чтение с произвольной записи (особенно при переполненном буфере), 
                    # то мы можем наткнуться на незаголовок. Просто пропускаем до следующего заголовка
                    log.debug('Rec %s: header not set, skipping', rec_addr)
                    continue
                
                aggIvl, dtmUTC = tpl

                nb_data_recs_after_hdr = 60 / aggIvl

                last_data_rec_addr_of_cr_hour = rec_addr + nb_data_recs_after_hdr * PROFILE_RECORD_SZ

                if last_data_rec_addr_of_cr_hour >= self.meter_info_.MemorySize:
                    # warn - потому что в этом случае не должно быть HEADER-записи
                    log.warn('Profile header doesnt fit into an hour')
                    self.HasActiveHeader = False
                    # чтобы на следующем цикле считать адрес 0
                    self.LastReadAddress = self.meter_info_.MemorySize - PROFILE_RECORD_SZ
                    return

                if rec_addr < cr_profile_info.Address and last_data_rec_addr_of_cr_hour >= cr_profile_info.Address:
                    # не умещается до текущего указателя
                    log.debug('Finished reading whole buffer')
                    self.HasActiveHeader = False
                    self.LastReadAddress = -1
                    return

                # LOG_DEBUG(lg, "Rec " << rec_addr << ": HEADER: " << dtmUTC << "(utc), ivl " << aggIvl << " min")
                self.set_header(dtmUTC, aggIvl)
                
            else:
                minutes_add = self.AggIvlMins * self.NbDataRecordsParsedSinceHeader

                self.NbDataRecordsParsedSinceHeader += 1

                pulse_pp, pulse_pn, pulse_qp, pulse_qn = _parse_data_rec(ctx.data(), offset)

                log.debug('Rec %s: PP=%s; PN=%s; QP=%s; QN=%s', rec_addr, pulse_pp, pulse_pn, pulse_qp, pulse_qn)

                if (minutes_add + self.AggIvlMins) >= 60:
                    log.debug('Finished hour')
                    self.HasActiveHeader = False


    # ProtocolException
    def read_profiles(self, ctx, max_read_requests, log):
        cr_profile = self.read_cr_profile_info(ctx, log)

        # page 150
        for _i in range(max_read_requests):
            # Check stop?
            
            frame = self.select_next_frame_(None if self.LastReadAddress == -1 else self.LastReadAddress, cr_profile, log)

            if not frame:
                # если lastReadAddr==-1, это значит, что мы ничего пока не читали и счетчик сейчас ведет только самый 1й профиль
                if self.LastReadAddress != -1:
                    log.info('Finished reading whole buffer')

                self.HasActiveHeader = False
                self.LastReadAddress = -1
                
                return
            
            next_addr, nb_recs = frame

            self.read_once(ctx, next_addr, nb_recs, cr_profile, log)

    # last_read_addr: None если чтений не было, иначе последний прочтенный адрес
    
    # None => no need to read
    # (next_addr, nb_recs)
    def select_next_frame_(self, last_read_addr: (int, None), cr_profile_info: CrProfileInfo, _log) -> bool:
        # 2.4.4.1
        MAX_NB_RECORDS_IN_REQUEST = self.meter_info_.MaxNbOfAddrToReadAtOnce // PROFILE_RECORD_SZ

        # Если признак =0, то массив профиля мощности не переполнен
        # и его первая запись (от момента инициализации массива) находится по физическому адресу
        # 0000h. Если признак =1, то массив срезов переполнен, и новые записи пишутся поверх самых
        # старых. При этом, первая запись (самая старая) находится по адресу указателя.
        if last_read_addr is None:  # новый цикл чтения
            if cr_profile_info.Overflow:
                # Поскольку есть вероятность, что за время, пока мы готовимся считать,
                # указатель перейдет на следующую запись, то мы читаем не самую старую, а с небольшим отступом
                next_addr = (cr_profile_info.Address + 5 * PROFILE_RECORD_SZ) % MEM_LEN

                if next_addr < cr_profile_info.Address:  # новый цикл чтения (переход через конец памяти)
                    nb_recs = MAX_NB_RECORDS_IN_REQUEST
                else:
                    absmax = (MEM_LEN - next_addr) // PROFILE_RECORD_SZ
                    nb_recs = min(MAX_NB_RECORDS_IN_REQUEST, absmax)
            else:
                next_addr = 0
                nb_recs = min(MAX_NB_RECORDS_IN_REQUEST, cr_profile_info.Address // PROFILE_RECORD_SZ)

                if nb_recs == 0:
                    return None
                    
            return (next_addr, nb_recs)
        else:
            # следующая запись за последней считанной
            next_addr = (last_read_addr + PROFILE_RECORD_SZ) % MEM_LEN

            # уперлись в текущий профиль
            if next_addr == cr_profile_info.Address:
                return None

            if next_addr < cr_profile_info.Address: 
                absmax = (cr_profile_info.Address - next_addr) // PROFILE_RECORD_SZ
            else:
                absmax = (MEM_LEN - next_addr) // PROFILE_RECORD_SZ

            return (next_addr, min(MAX_NB_RECORDS_IN_REQUEST, absmax))



# returns tuple (Address: int, Overflow: bool, DateTime: datetime)

# None -> это не header (ф-ция может использоваться для поиска хедера)
# (agg_ivl [minutes]: int, dtm: datetime)
# !ProtocolException  -  это хедер, но в нем ошибка (например, неверный BCD код или плохая дата)
def _parse_rec_header(d, offset: int, log) -> tuple:
    # По опыту у header-записей 8й байт равен FF или 0, но из документации
    # следует, что он вообще игнорируется,поэтому приходится полагаться только на CRC

    # check CRC
    _sum = d[offset+0] + d[offset+1] + d[offset+2] + d[offset+3] + d[offset+4] + d[offset+5]
    if d[offset+6] != (_sum & 0xff):
        # Это не ошибка, ведь функция может использоваться и для поиска заголовка
        return None

    try:
        h = bcd_to_int(d[offset+0])
        D = bcd_to_int(d[offset+1])
        M = bcd_to_int(d[offset+2])
        Y = bcd_to_int(d[offset+3])
        
        dtm_meter_tz = datetime.datetime(Y, M, D, h, 0)
    except ValueError as ex:
        log.warn(ex)
        #con_val.invalidate(Quality.QUALITY_NA)
        raise ProtocolException(str(ex))
    
    # !!! Meter TZ can be not a local time
    # *out_DtmUTC = SE::Platform::DateTime::localToUtc( &dtmMeterTZ );

    agg_ivl = d[offset+5]

    if agg_ivl == 0 or agg_ivl > 60 or (60 % agg_ivl) != 0:
        raise ProtocolException('Profile header contains invalid agg ivl {} (minutes)'.format(agg_ivl))

    return (agg_ivl, dtm_meter_tz)

# (pp|None, pn|None, qp|None, qn|None)
def _parse_data_rec(d, offset: int) -> tuple:
    # стр 101 [2.4.3.6.1] - сообщает о маскировании
    pp_good = (d[offset+0] & 0x80) == 0
    pn_good = (d[offset+2] & 0x80) == 0
    qp_good = (d[offset+4] & 0x80) == 0
    qn_good = (d[offset+6] & 0x80) == 0

    pp = make_word(d[offset + 0] & 0x7f, d[offset + 1]) if pp_good else None
    pn = make_word(d[offset + 2] & 0x7f, d[offset + 3]) if pn_good else None
    qp = make_word(d[offset + 4] & 0x7f, d[offset + 5]) if qp_good else None
    qn = make_word(d[offset + 6] & 0x7f, d[offset + 7]) if qn_good else None

    return (pp, pn, qp, qn)
