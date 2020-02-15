from binascii import a2b_hex, b2a_hex

from Crypto.Cipher import AES

AES_KEY = b'eea42cc6845811e99dcc005056895732'


def aes_encrypt(data, key=None):
    """
    AES加密
    :param data: 被加密数据
    :type data: str
    :param key: 密钥
    :type key: str / None / object can be str
    :return: 被加密字串
    :rtype: str
    """
    if key is None:
        key = AES_KEY
    else:
        key = aes_encrypt(str(key))
    cryptor = AES.new(key, AES.MODE_ECB)
    data = data.encode("utf-8")
    length = 16
    count = len(data)
    add = length - (count % length)
    data = data + (b'\0' * add)
    context = cryptor.encrypt(data)
    # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
    # 所以这里统一把加密后的字符串转化为16进制字符串
    return b2a_hex(context).decode("ASCII")


def aes_decrypt(data, key=None):
    """
    AES解密
    :param data: 加密数据
    :type data: str
    :param key: 密钥
    :type key: str / None / object can be str
    :return: 原文字串
    :rtype: str
    """
    if key is None:
        key = AES_KEY
    else:
        key = aes_encrypt(str(key))
    cryptor = AES.new(key, AES.MODE_ECB)
    plain_text = cryptor.decrypt(a2b_hex(data))
    # 解密后，去掉补足的字段用strip() 去掉
    result_test = plain_text.rstrip(b'\0')
    return result_test.decode("utf-8")
