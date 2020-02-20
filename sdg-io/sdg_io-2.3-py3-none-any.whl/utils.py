import sys
import random
import logging
from serial.tools.list_ports import comports


def dump_msg(msg=b''):
    """
    Человеко читаемое представление пакета байт
    print(dump_msg(b'012345') > (6){30,31,32,33,34,35}
    """
    assert(type(msg) is bytes)
    return f"({len(msg)}){{{','.join(f'{i:02x}' for i in msg)}}}" if msg else ""


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


def rand_bytes(size=None, mtu=256):
    """
    Генерирует случайный пакет байт размера size.
    если size не задан, то размер случайный, но не более mtu.
    """
    if not size:
        assert(mtu > 0)
        size = random.randint(1, mtu)
    return bytes(random.randrange(255) for _ in range(size))


def get_log(name=''):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    logging.addLevelName(logging.CRITICAL, "C")
    logging.addLevelName(logging.ERROR, "E")
    logging.addLevelName(logging.WARNING, "W")
    logging.addLevelName(logging.INFO, "|")
    logging.addLevelName(logging.DEBUG, "-")
    hndlr = logging.StreamHandler()
    hndlr.setFormatter(logging.Formatter('%(relativeCreated)04d %(name)-5s %(levelname)s %(message)s'))
    log.addHandler(hndlr)
    return log