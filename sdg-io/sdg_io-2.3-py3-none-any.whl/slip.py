class Slip:

    def __init__(self):
        self.buf = b''

    def code(self, msg):
        return b'\xC0' + msg.replace(b'\xDB', b'\xDB\xDD').replace(b'\xC0', b'\xDB\xDC') + b'\xC0'

    def encode(self, msg):
        self.buf += msg  # Новые данные соединяем с теми которые пришли раньше
        while self.buf:
            i = self.buf.find(b'\xC0')
            if i == -1:
                break
            msg = self.buf[:i]
            self.buf = self.buf[i + 1:]
            if msg:
                return msg.replace(b'\xDB\xDC', b'\xC0').replace(b'\xDB\xDD', b'\xDB')
            # если сообщение пустое (может быть если два 0xCO подряд), продолжаем поиск
        return b''

    def drop(self):
        self.buf = b''
