# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c)2018, 恒生电子股份有限公司
# All rights reserved.
#
# 文件名称：encrypt.py
# 摘    要：AES、DES加密
#
# 当前版本：V1.0.0
# 作    者：zhangyc24529
# 完成日期：2018-10-10
# 备    注：
###############################################################################
import sys
from binascii import b2a_hex, a2b_hex
from Crypto.Cipher import AES, DES


class AESEncrypt(object):
    def __init__(self, length=16):
        self._length = length

    def encrypt(self, data, key, iv):
        """
        使用AES对代码进行加密

        Args:
            data:  明文，需要注意的是：如果明文data的长度不是密钥长度的倍数【加密文本text必须为密钥长度的倍数！】，那就补足为密钥长度的倍数
            key :  密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.
            iv  ： 初始向量,长度必须为16Byte
        Returns:
            加密后的代码
        """
        if sys.version_info.minor > 5:
            cryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
        else:
            cryptor = AES.new(key.encode, AES.MODE_CBC, iv)
        data = data.encode("utf-8")
        count = len(data)
        add = self._length - (count % self._length)
        data = data + (b'\0' * add)
        context = cryptor.encrypt(data)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(context).decode("ASCII")

    def decrypt(self, data, key, iv):
        """
        对已经用AES加密的代码进行解密

        Args:
            data:  密文
            key :  密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.
            iv  ： 初始向量，必须与加密的初始向量相同
        Returns:
            解密后的代码
        """
        if sys.version_info.minor > 5:
            cryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
        else:
            cryptor = AES.new(key.encode, AES.MODE_CBC, iv)
        plain_text = cryptor.decrypt(a2b_hex(data))
        # 解密后，去掉补足的字段用strip() 去掉
        result_test = plain_text.rstrip(b'\0')
        return result_test.decode("utf-8")


class DESEncrypt(object):
    def __init__(self, length=32):
        self._length = length

    def encrypt(self, data, key, iv):
        """
        使用DES对代码进行加密

        Args:
            data:  明文，需要注意的是：如果明文data的长度不是密钥长度的倍数【加密文本text必须为密钥长度的倍数！】，那就补足为密钥长度的倍数
            key :  密钥key 长度必须为8Bytes 长度.
            iv  ： 初始向量,长度必须为8Byte
        Returns:
            加密后的代码
        """
        data = data.encode("utf-8")
        # if sys.version_info.minor > 5:
        #     cryptor = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv.encode('utf-8'))
        # else:
        #     cryptor = DES.new(key, DES.MODE_CBC, iv)
        cryptor = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv.encode('utf-8'))
        add = self._length - len(data) % self._length
        text = data + (b'\0' * add)
        # text = data + ('\0' * add)
        context = cryptor.encrypt(text)

        return b2a_hex(context)

    def decrypt(self, data, key, iv):
        """
        对已经用DES加密的代码进行解密

        Args:
            data: 密文
            key : 密钥key 长度必须为8Bytes 长度.
            iv  ：初始向量，必须与加密的初始向量相同
        Returns:
            解密后的代码
        """
        # if sys.version_info.minor > 5:
        #     cryptor = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv.encode('utf-8'))
        # else:
        #     cryptor = DES.new(key, DES.MODE_CBC, iv)
        cryptor = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv.encode('utf-8'))
        context = cryptor.decrypt(a2b_hex(data))
        result_test = str(context, encoding='utf-8')
        return result_test.strip('\0')
