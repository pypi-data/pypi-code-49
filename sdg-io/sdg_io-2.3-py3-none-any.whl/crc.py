import crcmod


class Crc:
    def __init__(self):
        self.crc16_func = crcmod.mkCrcFun(0x11021, initCrc=0xffff, xorOut=0x0)

    def code(self, msg):
        crc = self.crc16_func(msg)
        msg += crc.to_bytes(2, byteorder='little')
        return msg

    def encode(self, msg):
        if msg:
            if self.crc16_func(msg) == 0:
                return msg[:-2]
        return b''

    def drop(self):
        pass
