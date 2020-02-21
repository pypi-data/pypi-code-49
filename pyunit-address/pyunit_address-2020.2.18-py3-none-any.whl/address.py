#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/2/18 15:23
# @Author: Jtyoui@qq.com
import zipfile
import os
import pickle
import re


class Address:

    def __init__(self, max_address=5, is_max_address=False):
        """初始化

        :param max_address: 最长地址个数
        :param is_max_address: 满足最长地址
        """

        # 加载精准匹配的词库，共40万
        self.address_data = self._unzip()
        self.length_all = len(self.address_data)

        # 加载模糊匹配的词库
        self.vague = [w.strip() for w in open(os.path.dirname(__file__) + os.sep + 'CAT.txt', encoding='UTF-8')]
        self.length_vague = len(self.vague)

        self.is_max_address = is_max_address
        self.max_address = max_address

    def set_vague_text(self, text):
        """重新加载模糊匹配的文本数据

        数据格式： ['地址1','地址2',....] 并且排序。默认是：sorted()
        """
        self.vague = text

    @staticmethod
    def _unzip():
        """解压地址数据包"""
        name = 'address'
        f = zipfile.ZipFile(os.path.dirname(__file__) + os.sep + name + '.zip')
        fp = f.read(name)
        return pickle.loads(fp)

    @staticmethod
    def _bisect_right(a, x, lo, hi):
        """二分法算法"""
        while lo < hi:
            mid = (lo + hi) // 2
            mid_value = a[mid]
            if x < mid_value:
                hi = mid
            elif x == mid_value:
                return lo, mid_value
            else:
                lo = mid + 1
        return lo

    def _vague(self, values):
        """模糊匹配"""
        value = self._bisect_right(self.vague, values, 0, self.length_vague)
        if isinstance(value, tuple):
            return value[1]
        return None

    def find_address(self, data: str) -> list:
        """查找地址"""
        data = re.sub(r"[!#$%&'()*+,-./:：，。？！；‘’、《》;<=>?@[\]^_`{|}~\s]", '', data)
        i, ls, length = 0, [], len(data)
        while i + 1 < length:
            width = self.max_address if length - i > self.max_address else (length - i)  # 补差位数
            for j in range(2, width + 1):
                n = data[i:i + j]
                value = self._bisect_right(self.address_data, n, 0, self.length_all)
                if isinstance(value, tuple):
                    flag = value[1]  # 精准匹配
                else:
                    v = self._vague(n)  # 进行模糊匹配
                    flag = v if v else None
                if flag:
                    index = data.find(flag, i)
                    i = index + len(flag)  # 跳过选择后的地址
                    ls.append(flag)
                    break
            else:
                i += 1
        if self.is_max_address:
            max_address = []
            match = re.sub('|'.join(ls), lambda x: '*' * len(x.group()), data)
            for addr in re.finditer(r'[*]+', match):
                max_address.append(data[addr.start():addr.end()])
            return max_address
        return ls
