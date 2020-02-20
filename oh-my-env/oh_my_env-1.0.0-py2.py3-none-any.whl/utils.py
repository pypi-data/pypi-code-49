# coding=utf8
# coding=utf8

import six
from base64 import b64decode, b64encode
from M2Crypto.EVP import Cipher

AES_KEY = "BA2453031F6917AD572D8083FB8AE110"
AES_IV = "32CE750A8231386BAC138ECD7D336C0F"

_ENC=1
_DEC=0

def build_cipher(key, iv, op=_ENC):
    return Cipher(alg='aes_128_cbc', key=key, iv=iv, op=op)

def _encryptor(key, iv=None):
    # Decode the key and iv
    key = b64decode(key)
    if iv is None:
        iv = '\0' * 16
    else:
        iv = b64decode(iv)
   
    # Return the encryption function
    def _encrypt(data, debug=False):
        if debug:
            return data
        data = six.ensure_binary(data)
        cipher = build_cipher(key, iv, _ENC)
        v = cipher.update(data)
        v = v + cipher.final()
        del cipher
        v = b64encode(v)
        return six.ensure_str(v)
    return _encrypt



def _decryptor(key, iv=None):
    # Decode the key and iv
    key = b64decode(key)
    if iv is None:
        iv = '\0' * 16
    else:
        iv = b64decode(iv)

    def _decrypt(data, debug=False):
        if debug:
            return data
        data = b64decode(data)
        cipher = build_cipher(key, iv, _DEC)
        v = cipher.update(data)
        v = v + cipher.final()
        del cipher
        return six.ensure_str(v)
    return _decrypt

def decrypt(v):
    try:
        return _decryptor(AES_KEY, iv=AES_IV)(v)
    except TypeError:
        return v

def encrypt(v):
    return _encryptor(AES_KEY, iv=AES_IV)(v)


if __name__ == "__main__":
    print(encrypt('hello'))
