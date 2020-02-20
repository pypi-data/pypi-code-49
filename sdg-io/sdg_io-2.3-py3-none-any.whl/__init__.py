"""
СКБ-шный стек протоколов обмена через "последовательный порт"
* Передача: `-> CRC16 -> SLIP -> UART`.
* Прием:    `<- CRC16 <- SLIP <- UART`.

`CRC16` -> канальный уровень, контроль целостности пакетов (на библиотеке crcmod).
`SLIP` -> канальный уровень, для деление потока на пакеты (https://tools.ietf.org/html/rfc1055).
`UART` -> физический уровень (на библиотеке pyserial).

Для контроля целостности пакета используется контрольная сумма `CRC-16`, рассчитываемая
по алгоритму `CRC-16 CCITT REVERSED` (полином – `0x1021`, начальное значение – `0хFFFF`).
`CRC` рассчитывается по данным до их преобразования в пакет, передается после данных младшим байтом вперед.
Байты `CRC` входят в состав пакета, т.е. подлежат перекодировке по `SLIP`.

Информационные сообщения между устройствами пересылаются в виде пакетов кодированных `SLIP`-ом:
признаком конца пакета является байт со значением `0хC0`.
байт данных со значением `0хC0` заменяется последовательностью байт `0хDB 0хDC`;
байт данных со значением `0хDB` заменяется последовательностью байт `0хDB 0хDD`.
Для повышения помехоустоичивости обмена применяется `0хС0` перед пакетом.

Структура пакета - `0хС0, data bytes..., crc16L, crc16H, 0хС0`.

Пример использования:
-------------
```python
from sdg_io import SdgIO, rand_bytes
p = SdgIO('COM1', '115200_O_2')
p.write(rand_bytes(mtu=256)) # — send msg —
print(p.read(timeout=.3)) # — recive msg —
```
"""


from time import time
from sdg_utils import dump_bytes, log_starttime
from .crc import Crc
from .slip import Slip
from .uart import Uart, SerialException

__version__ = '2.3'


class SdgIO:
    """
    Интерфейс ввода/вывода для обмена через стек протоколов СКБ.
    """
    def __init__(self,
                 port='COM1',
                 portcfg='115200_O_2',
                 log=None,
                 dump=None,
                 uart_timeout=0.02):
        """
        Конструктор интерфейса ввода/вывода стека протоколов СКБ.

        :param port: Последовательный порт.
        :param portcfg: Конфигурационная строка порта. 3 элемента разделенных
            нижним подчеркиванием '_'. Пример '115200_N_1': скорость = '115200';
            четность = 'N'-None, 'E'-Even, 'O'-Odd, 'M'-Mark, 'S'-Space;
            кол-во стоповых бит = '1' или '2';
        :param log: Logger object или None если логер не нужен.
        :param dump: путь к файлу для дампа обмена или None если дамп не нужен.
        :param uart_timeout: таймаут Uart.read() можно установить только при инициализации
            Uart-a, сделал 20мс, меньше не работает из-за тормозов драйвера или ОС.
            Слишком большой таймаут не хорошо, тк функция SdgIO.read(timeout) работает
            повехр Uart.read() с дискретностью 'uart_timeout'. Например при вызове
            SdgIO.read(timeout=.05) будет 3 вызова Uart.read() с блокировкой по ~.02

        При невозможности открыть 'port' генерируется IOError. При некорректной
        конфигурационной строке 'portcfg' - ValueError или IndexError.
        """
        self.log = log
        try:
            self.uart = Uart(port, portcfg, timeout=uart_timeout)
        except SerialException as e:
            if self.log:
                self.log.error(u"Ошибка открытия %s." % port)
            raise IOError('SdgIO open err > %s' % e)
        self.crc = Crc()
        self.slip = Slip()
        self.dump = None
        if self.log:
            self.log.info("SdgIO open")
        if dump:
            self.dump = open(dump, 'w')
            self.tstart = log_starttime()  # для синхронизации логов и дампа

    def close(self):
        """ Закрыть интерфейс"""
        if self.dump:
            self.dump.close()
        self.uart.close()
        if self.log:
            self.log.info("SdgIO closed")

    def read(self, timeout=0.05) -> bytes:
        """
        Прием и декодирование сообщений через стек CRC16 <- SLIP <- UART.
        При невозможности прочитать порт Uart, генерирует IOError.

        :param timeout: Таймаут приема пакета, по умолчанию 50мс.
               работает не совсем точно см. описание конструктора.
        :return: принятый пакет или  b'' по истечению timeout-а.
        """
        readstart = time()
        while True:
            msg = self.slip.encode(b'')
            # Если в слипе пусто, читаем из уарта
            if not msg:
                try:  # ф-я блокируемая (default=~20мс задается при инициализации Uarta)
                    msg = self.uart.read()
                except SerialException as e:
                    raise IOError("SdgIO read err > %s" % e)
                if msg:
                    if self.log:
                        self.log.debug('u< %s' % dump_bytes(msg))
                    if self.dump:
                        self.dump.write("%d<%s\n" % (self._dumptime(), dump_bytes(msg)))
                    msg = self.slip.encode(msg)
                # Таймаут чтения
                elif time() - readstart > timeout:
                    if self.log:
                        self.log.debug("u< timeout %.3f" % (time() - readstart))
                    break
            if msg:
                if self.log:
                    self.log.debug('s< %s' % dump_bytes(msg))
                msg = self.crc.encode(msg)
                if self.log:
                    self.log.debug('c< %s' % dump_bytes(msg))
                if msg:
                    break
        if msg:
            if self.log:
                self.log.info('<- %s' % dump_bytes(msg))
            if self.dump:
                self.dump.flush()
        return msg

    def write(self, msg: bytes) -> None:
        """
        Кодирование и передача сообщений через стек CRC16 -> SLIP -> UART.
        При невозможности передать в порт Uart, генерирует IOError.

        :param msg: передаваемое сообщение.
        """
        assert (type(msg) is bytes)
        if msg:
            if self.log:
                self.log.info('>- %s' % dump_bytes(msg))
                self.log.debug('c> %s' % dump_bytes(msg))
            msg = self.crc.code(msg)
            if self.log:
                self.log.debug('s> %s' % dump_bytes(msg))
            msg = self.slip.code(msg)
            try:
                self.uart.write(msg)
            except SerialException as e:
                raise IOError("SdgIO write err > %s" % e)
            if self.log:
                self.log.debug('u> %s' % dump_bytes(msg))
            if self.dump:
                self.dump.write("%d>%s\n" % (self._dumptime(), dump_bytes(msg)))
                self.dump.flush()

    def drop(self):
        """ Чистка всех буферов стека протоколов """
        self.crc.drop()
        self.slip.drop()
        try:
            self.uart.drop()
        except SerialException as e:
            raise IOError("SdgIO dpor err > %s" % e)

    def _dumptime(self):
        return (time() - self.tstart) * 1000
