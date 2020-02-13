import hashlib

from Crypto import Random
from Crypto.Cipher import AES


class AESCipher:
    _IV = "ab3rgkb28fki561l"

    @classmethod
    def encrypt(cls, _data, _key):
        aes = AES.new(_key, AES.MODE_CBC, cls._IV)
        return aes.encrypt(cls._pad(_data))

    @classmethod
    def decrypt(cls, _encrypted_data, _key):
        aes = AES.new(_key, AES.MODE_CBC, cls._IV)
        return aes.decrypt(_encrypted_data)

    @classmethod
    def _pad(cls, _data):
        return _data + b"\0" * (AES.block_size - len(_data) % AES.block_size)
