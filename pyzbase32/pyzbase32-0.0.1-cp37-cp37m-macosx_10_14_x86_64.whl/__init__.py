from pyzbase32.ext import encode, decode

def decode_bytes(encoded):
  bits = len(encoded) * 5
  bits -= bits % 8
  return decode(encoded,bits)

def encode_bytes(data):
  return encode(data,len(data) * 8)
