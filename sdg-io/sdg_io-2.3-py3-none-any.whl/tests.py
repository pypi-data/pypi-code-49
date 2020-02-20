import unittest
from time import sleep
from sdg_io import SdgIO
from sdg_utils import rand_bytes, log_open


class TestProtocol(unittest.TestCase):
    print("Для выполнения теста нужно замкуть RX и TX порта (нуль-модем)")
    PORT = input("Ведите название порта 'нуль-модема' или нажмите Enter(по умочанию 'COM26'):")
    print(PORT)
    CNT = input("И кол-во циклов теста случайными пакетами или нажмите Enter(по умолчанию 1000):")
    if not PORT:
        PORT = 'COM26'
    try:
        CNT = int(CNT)
    except ValueError:
        CNT = 1000
    print(CNT)
    log = log_open()

    def test_random_msgs(self):
        self.log.info(""" Тест случайными данными. """)
        p = SdgIO(self.PORT, '115200_O_2', self.log)
        for i in range(self.CNT):
            msg = rand_bytes(mtu=256)
            p.write(msg)
            ack = p.read(timeout=.3)
            self.assertEqual(msg, ack)
        p.close()

    def test_drop(self):
        self.log.info(""" Тест функции Drop() """)
        p = SdgIO(self.PORT, '115200_O_2', self.log)
        msg = rand_bytes(mtu=256)
        p.write(msg)
        sleep(.1)
        ack = p.read(timeout=.1)
        self.assertEqual(ack, msg)
        p.write(msg)
        sleep(.1)
        p.drop()
        ack = p.read(timeout=.1)
        self.assertEqual(ack, b'')
        p.close()

    def test_multisend(self):
        self.log.info(""" Передача/прием сообщений пачками """)
        p = SdgIO(self.PORT, '115200_O_2', self.log)
        for _ in range(100):
            msgs = [rand_bytes(mtu=32) for _ in range(10)]
            for msg in msgs:
                p.write(msg)
            acks = []
            sleep(.1)
            for _ in range(len(msgs)):
                acks.append(p.read(timeout=0))
            self.assertEqual(msgs, acks)
        p.close()

    def test_fail_cfg_parametrs(self):
        self.log.info(""" Тест некорректной инициализации порта. """)
        with self.assertRaises(IOError):
            SdgIO(port='NoCOM5', portcfg='115200_O_2', log=self.log)
        with self.assertRaises(ValueError):
            SdgIO(port=self.PORT, portcfg='115200_X_2', log=self.log)
        with self.assertRaises(ValueError):
            SdgIO(port=self.PORT, portcfg='115200_O_5', log=self.log)
        with self.assertRaises(ValueError):
            SdgIO(port=self.PORT, portcfg='0_O_5', log=self.log)
        with self.assertRaises(ValueError):
            SdgIO(port=self.PORT, portcfg='OLOLO_O_5', log=self.log)
        with self.assertRaises(IndexError):
            SdgIO(port=self.PORT, portcfg='115200_O', log=self.log)
        with self.assertRaises(IndexError):
            SdgIO(port=self.PORT, portcfg='115200', log=self.log)
        # Обычно порты не поддерживают boudrate > 115200
        # pyserial генерирует SerialException конструктор Protocol-а его перехватывает
        # и генерирует исключение IOError, чтобы не плодить сущности
        # with self.assertRaises(IOError):
        #   SdgIO(port='COM1', portcfg='921600_O_1', log=self.log)


if __name__ == "__main__":
    unittest.main()
