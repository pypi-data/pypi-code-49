import struct
from . import RSAPlusAES

def generate_rsa_key_pair(key_pair=2048, out_dir='.'):
    RSAPlusAES.generate_keypair(key_pair, out_dir)
    return


def pack_aes_data(aes_key: bytes, msg: str, nonce: bytes = RSAPlusAES.generate_aes_key(12)):
    data, tag, nonce = RSAPlusAES.aes_encrypt(aes_key, msg, nonce)
    return struct.pack(">I", len(nonce)) + nonce + data + tag


def unpack_aes_data(aes_key: bytes, data: bytes):
    nonce_length = (struct.unpack(">I", data[0:4]))[0]
    nonce = data[4: nonce_length + 4]
    encrypted_data = data[(4 + nonce_length):(len(data) - 16)]
    tag = data[-16:len(data)]
    return RSAPlusAES.aes_decrypt(key=aes_key, data=encrypted_data, nonce=nonce, tag=tag)
