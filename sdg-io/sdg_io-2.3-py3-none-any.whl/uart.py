from serial import Serial, SerialException


class Uart(Serial):
    """
    Класс для работы с "Последовательным портом" наследник pySerial.
    """
    def __init__(self, port: str, portcfg='115200_O_2', timeout=0.02):
        """
        Констркутор класса для работы с "Последовательным портом"

        :param port: Последовательный порт.
        :param portcfg: Конфигурационная строка порта. 3 элемента разделенных
            нижним подчеркиванием '_'. Пример '115200_N_1': скорость = '115200';
            четность = 'N'-None, 'E'-Even, 'O'-Odd, 'M'-Mark, 'S'-Space;
            кол-во стоповых бит = '1' или '2';
        :param timeout: таймаут на чтение. Менее 20ms не работает из-за
            тормозов драйвера или ОС.

        При невозможности открыть 'port' генерируется IOError. При некорректной
        конфигурационной строке 'portcfg' - ValueError или IndexError.
        """
        s = portcfg.split('_')
        baudrate, parity, stopbits = int(s[0]), s[1].upper(), int(s[2])

        Serial.__init__(self,
                        port=port,
                        baudrate=baudrate,
                        parity=parity,
                        stopbits=stopbits,
                        timeout=timeout)

    def read(self, size=1):
        """
        Чтение данных. Функция блокируемая на 'timeout' заданный при
        инициализации или до поступления минимум 'size' байт.

        :param size: Минимальное кол-во ожидаемых байтов. По умолчанию size=1,
            т.е. функция блокируется до прихода хотя бы одного байта.
            На высоких скоростях обмена данные обычно валятся сразу пачками.
        :return: принятые данные, или b'' если данных по истечению 'timeout'
            не поступило.
        """
        return Serial.read(self, size=size) + Serial.read(self, size=Serial.inWaiting(self))

    def drop(self):
        """ Сброс буферов приема/передачи. """
        Serial.flushInput(self)
        Serial.flushOutput(self)
