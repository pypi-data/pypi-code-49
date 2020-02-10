import hashlib
import logging
import os

from cryptography.fernet import Fernet

__all__ = ['encrypt', 'decrypt', 'SecretManage', 'get_file_md5', 'local_secret_path',
           'set_secret_path']
local_secret_path = '~/.secret'


def set_secret_path(path):
    global local_secret_path
    local_secret_path = path


def get_file_md5(path, chunk=1024 * 4):
    m = hashlib.md5()
    with open(path, 'rb') as f:
        while True:
            data = f.read(chunk)
            if not data:
                break
            m.update(data)

    return m.hexdigest()


class SecretManage(object):
    def __init__(self, key, value=None, path='default', secret_dir=None, save=True):
        self.key = key
        secret_dir = secret_dir or local_secret_path

        secret_dir = secret_dir.replace("~", os.environ['HOME'])
        self.secret_path = '{}/{}/.{}'.format(secret_dir, path, key)
        self.value = value

        if save:
            self.write()

        if self.value is None:
            self.read()

    def read(self):
        """
        从文件读取
        """
        if self.value is not None:
            return self.value
        try:
            if os.path.exists(self.secret_path):
                self.value = open(self.secret_path).read()
                print("read from local {}".format(self.secret_path))
        except Exception as e:
            print("read error ,init {}".format(e))
        return self.value

    def write(self):
        """
        写入到文件
        """
        if self.value is None:
            return
        try:
            secret_dir = os.path.dirname(self.secret_path)
            if not os.path.exists(secret_dir):
                os.makedirs(secret_dir)
            with open(self.secret_path, 'w')as f:
                f.write(self.value)
                print("write to local {}".format(self.secret_path))
        except Exception as e:
            print('error {}'.format(e))

    def delete_key(self):
        """
        删除
        """
        if os.path.exists(self.secret_path):
            os.remove(self.secret_path)


logger = logging.getLogger('tool')


def get_fernet(cipher_key=None):
    """
    从本地拿取加密的key
    :param cipher_key:传入的key
    :return:
    """
    if cipher_key:
        secert = SecretManage(key='cipher_key', value=str(cipher_key, encoding="utf-8"))
    else:
        secert = SecretManage(key='cipher_key')

    secert_r = secert.read()
    if secert_r is not None:
        cipher_key = bytes(secert_r, encoding="utf8")
    else:
        cipher_key = Fernet.generate_key()
        SecretManage(key='cipher_key', value=str(cipher_key, encoding="utf-8"))
    return Fernet(cipher_key)


def encrypt(text, cipher_key=None):
    cipher = get_fernet(cipher_key)
    encrypted_text = cipher.encrypt(text.encode())

    return encrypted_text


def decrypt(encrypted_text, cipher_key=None):
    cipher = get_fernet(cipher_key)
    decrypted_text = cipher.decrypt(encrypted_text)

    return decrypted_text.decode()


def test():
    text = 'My super secret message'
    print(encrypt(text))
    print(encrypt(text))
    print(decrypt(encrypt(text)))
