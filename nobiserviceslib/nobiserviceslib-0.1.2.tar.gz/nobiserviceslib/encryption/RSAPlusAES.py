from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
import base64


def main():
    while True:
        msg = input('->')
        if msg == 'rsa_enc':
            public_key = key_file_to_string(input("enter public key name\n"))
            data = input("enter data\n")
            encrypted_data = rsa_encrypt(public_key, data)
            private_key = key_file_to_string("private.pem")
            msg = rsa_decrypt(private_key, encrypted_data).decode('utf-8')
            print(msg)

        elif msg == 'rsa_dec':
            continue
        elif msg == 'file to str':
            key_file_to_string(input("enter file name\n"))
        elif msg == 'aes_enc':
            key = generate_aes_key(int(input("enter key size\n")))
            data, tag, nonce = aes_encrypt(key, input("enter your message\n"), generate_aes_key(12))
            aes_decrypt(key=key, data=data, tag=tag, nonce=nonce)
        elif msg == 'gen_key_pair':
            generate_keypair(int(input("Enter key length\n")))
        elif msg == 'q':
            break


def generate_keypair(key_len: int = 2048, out_dir='.'):
    key = RSA.generate(key_len)
    private_key = key.export_key()
    with open("%s/private.pem" % out_dir, 'wb') as f:
        f.write(private_key)

    public_key = key.publickey().export_key()
    with open("%s/public.pem" % out_dir, 'wb') as f:
        f.write(public_key)


def key_file_to_string(file_name: str):
    try:
        with open(file_name) as f:
            string = f.read()
            print(string)
            return string
    except FileNotFoundError:
        print("File Not Found")
        return


def rsa_encrypt(key_str: str, data):
    try:
        public_key = RSA.import_key(key_str)
        cipher_rsa = PKCS1_OAEP.new(public_key)
        if data == type(str):
            msg = cipher_rsa.encrypt(base64.b64encode(data.encode('utf-8')))
        else:
            msg = cipher_rsa.encrypt(base64.b64encode(data))
        return msg
    except TypeError:
        print("something error")
        set1 = set()
        set1.add(1)
        return None


def rsa_decrypt(key_str: str, data: bytes):
    try:
        private_key = RSA.import_key(key_str)
        cipher_rsa = PKCS1_OAEP.new(private_key)
        decrypted_data = cipher_rsa.decrypt(data)
        msg = base64.b64decode(decrypted_data)
        print(msg)
        return msg
    except TypeError:
        return
    except ValueError:
        return


def generate_aes_key(key_length: int):
    return get_random_bytes(key_length)


def aes_encrypt(key: bytes, data: str, nonce: bytes):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    nonce = cipher.nonce
    data, tag = cipher.encrypt_and_digest(data.encode('utf-8'))

    return data, tag, nonce


def aes_decrypt(key: bytes, data: bytes, tag: bytes, nonce: bytes):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    msg = cipher.decrypt(data)
    try:
        cipher.verify(tag)
        return msg
    except ValueError:
        return


if __name__ == '__main__':
    main()
