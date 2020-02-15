import hashlib, binascii, os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generateKey(private_key="private_key.pem", public_key="public_key.pem"):
    generated_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    generated_public_key = generated_private_key.public_key()
    pem_private_key = generated_private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption())
    pem_public_key = generated_public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
    with open(private_key, 'wb') as f:
        f.write(pem_private_key)
    with open(public_key, 'wb') as f:
        f.write(pem_public_key)

def getPrivateKey(private_key="private_key.pem"):
    with open(private_key, "rb") as key_file:
        return serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())

def getPublicKey(public_key="public_key.pem"):
    with open(public_key, "rb") as key_file:
        return serialization.load_pem_public_key(key_file.read(), backend=default_backend())

def encrypt(public_key, text):
    return public_key.encrypt(text.encode('ascii'), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

def decrypt(private_key, text):
    return private_key.decrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)).decode("utf-8")

def hashText(text):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', text.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verifyHash(hash, text):
    salt = hash[:64]
    hash = hash[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', text.encode('utf-8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == hash
