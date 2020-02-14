import base64
import hashlib
import random
import string
import time

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


def sign(_private_key, sign_str):
    key = RSA.importKey(_private_key)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(SHA256.new(sign_str.encode("utf8")))
    return base64.b64encode(signature).decode('utf-8')


def verify_sign(_public_key, content, signature):
    rsa_key = RSA.importKey(_public_key)
    signer = PKCS1_v1_5.new(rsa_key)
    h = SHA256.new(content.encode('utf-8'))
    if signer.verify(h, base64.b64decode(signature)):
        return True
    return False


def get_b64md5(source=''):
    m = hashlib.md5()
    m.update(source.encode('utf8'))
    m_str = m.hexdigest()
    base_str = base64.b64encode(bytearray.fromhex(m_str))
    return base_str.decode('utf8')


def get_million_timestamp():
    t = time.time()
    return int(round(t * 1000))


def generate_random_str():
    random_length = random.randint(30, 32)
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(random_length)]
    random_str = ''.join(str_list)
    return random_str
