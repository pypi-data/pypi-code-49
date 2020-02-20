"""
SDG UTILS.
"""


__version__ = '0.1'

import random
import datetime
from serial.tools.list_ports import comports

from .terminal import *
from .log import *


def rand_bytes(size=None, mtu=256):
    """
    Генерирует случайный пакет байт размера size.
    если size не задан, то размер случайный, но не более mtu.
    """
    if not size:
        assert(mtu > 0)
        size = random.randint(1, mtu)
    return bytes(random.randrange(255) for _ in range(size))


def dump_bytes(msg=b''):
    """
    Человеко читаемое представление пакета байт
    print(dump_msg(b'012345') > (6){30,31,32,33,34,35}
    """
    assert(type(msg) is bytes)
    return f"({len(msg)}){{{','.join(f'{i:02x}' for i in msg)}}}" if msg else ""


def dump_bits(bitsmask: int, shift=0) -> str:
    """
    Выводит строку с номерами установленных битов в числе 'bitsmask', через запятую.
    Например dump_bits(0x8080) --> '7,15'
    Параметр 'shift' позволяет начать отсчет битов с произвольного значения.
    Например dump_bits(0x8080, shift=1) --> '8,16'
    """
    # Таже фигня что и return ','.join(i for i in bits2nums(bitsmask)) только шустрее
    return ','.join([str(i + shift) for i in range(bitsmask.bit_length()) if bitsmask & 1 << i])


def bits2nums(bitsmask: int, shift=0) -> list:
    """
    Возвращает список с номерами установленных битов в числе 'bitsmask'.
    Например bits2nums(0x8080) --> [7, 15].
    Параметр 'shift' позволяет начать отсчет битов с произвольного значения.
    Например bits2nums(0x8080, shift=1) --> [8, 16]
    """
    return [i + shift for i in range(bitsmask.bit_length()) if bitsmask & 1 << i]


def nums2bits(*bits, shift=0):
    """
    Возвращает битовую маску с установленными битами из списка 'bits'
    Например nums2bits(7, 15) --> 0x8080.
    Параметр 'shift' позволяет сдвинуть биты на произвольное значение.
    Например nums2bits(8, 16, shift=-1) --> 0x8080.
    """
    bitmask = 0
    for b in bits:
        bitmask |= 1 << b + shift
    return bitmask


def get_comports(bluetooth_ports_filter=True):
    """ Возвращает список кортежей (порт, имя) доступных последовательных портов
    [ ('COM1', 'Последовательный порт 1), ('COM5','USB Serial Port'), ... ]
    по умолчанию с фильтрацией Bluetooth портов, тк они в системе присутствуют
    даже когда соединение с Bluetooth устройством не установлено
    и при попытке открыть такой порт происходит 'мертвая говядина'. """
    def it_bluetooth(portname):
        for bt_name in ["luetooth", "BT Port"]:
            if portname.find(bt_name) != -1:
                return True
        return False
    ports = []
    for port, portname, _ in comports():
        if sys.version_info < (3, 7):  # замена "невыводимых" символов на?
            portname = portname.encode(sys.stdout.encoding, errors='replace')
            portname = portname.decode(sys.stdout.encoding)
        if not bluetooth_ports_filter or not it_bluetooth(portname):
            ports.append((port, portname))
    return ports


def try_mkdir(path):
    """ Попытка создать каталог по пути path """
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def get_datetime() -> str:
    """ Возвращает строку с текущей датой временем в формате 2020.02.04_09.52.42050 """
    return datetime.datetime.today().strftime('%Y.%m.%d_%H.%M.%S%f')[:-3]
