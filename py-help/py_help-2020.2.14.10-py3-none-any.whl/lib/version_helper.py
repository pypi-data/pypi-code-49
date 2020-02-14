# -*- coding: utf-8 -*-

import re
from .CommonLogger import debug, info, warn, error


def confirm_num(elem):
    return elem.isdigit()


MIX_DIGIT_STR_MATCH = r'^(\d+)(\D*)'


class VersionHelper:

    @classmethod
    def cmp(cls, v1, v2):
        """比较两个版本(1.1.1)的大小，需要按.分割后比较各个部分的大小
        :param v1 对比的第一个字符串
        :param v2 对比的第二个字符串
        :return 0 如果v1与v2相等
        """
        if v1 == v2:
            return 0
        a_list = v1.split('.')
        b_list = v2.split('.')
        len_a_list = len(a_list)
        len_b_list = len(b_list)
        str_length = len_b_list if len_a_list > len_b_list else len_a_list
        for i in range(str_length):
            temp1 = a_list[i]
            temp2 = b_list[i]
            if confirm_num(temp1) and confirm_num(temp2):
                ret = int(temp1) - int(temp2)
                if ret == 0:
                    continue
                return 1 if ret > 0 else -1
            else:
                temp1_list = temp1.split()
                temp2_list = temp2.split()
                temp_length = len(temp2_list) if len(temp1_list) > len(temp2_list) else len(temp1_list)
                for j in range(temp_length):
                    t1 = temp1_list[j]
                    t2 = temp2_list[j]

                    # 纯数字比较
                    if confirm_num(t1) and confirm_num(t2):
                        ret2 = int(t1) - int(t2)
                        if ret2 == 0:
                            continue
                        return 1 if ret2 > 0 else -1

                    # 数字开头混字母比较
                    elif re.match(MIX_DIGIT_STR_MATCH, t1) or re.match(MIX_DIGIT_STR_MATCH, t2):
                        t1_match = re.match(MIX_DIGIT_STR_MATCH, t1)
                        t2_match = re.match(MIX_DIGIT_STR_MATCH, t2)
                        t1_digit = int(t1_match.group(1))
                        t2_digit = int(t2_match.group(1))
                        ret2 = t1_digit - t2_digit
                        if ret2 == 0:
                            if t1_match.group(2) == t2_match.group(2):
                                continue
                            else:
                                return 1 if t1_match.group(2) > t2_match.group(2) else -1
                        return 1 if ret2 > 0 else -1
                    # 纯字母比较
                    elif (not confirm_num(t1)) and (not confirm_num(t2)):
                        if t1 == t2:
                            continue
                        return 1 if t1 > t2 else -1

                    # 数字字母混合比较 默认数字小于字母
                    else:
                        return -1 if confirm_num(t1) else 1

        # 长度不等的话,看是不是都是0,如果是的话,就判断相等,否则长的就是最大的
        len_diff = len_a_list - len_b_list
        if len_diff != 0:
            if len_diff > 0:
                diff_list = a_list[str_length:]
            else:
                diff_list = b_list[str_length:]
            for one_item in diff_list:
                if confirm_num(one_item):
                    if int(one_item) == 0:
                        continue
                    else:
                        return 1 if len_diff > 0 else -1
                else:
                    return 1 if len_diff > 0 else -1

        debug("版本对比出现相等 {} <=> {}".format(v1, v2))
        return 0

    @classmethod
    def max(cls, a, b):
        """比较两个版本(1.1.1)的大小，需要按.分割后比较各个部分的大小
        :param a 对比的第一个字符串
        :param b 对比的第二个字符串
        """
        ret = cls.cmp(a, b)
        if ret >= 0:
            return a
        else:
            return b

    @classmethod
    def min(cls, a, b):
        """比较两个版本(1.1.1)的大小，需要按.分割后比较各个部分的大小
        :param a 对比的第一个字符串
        :param b 对比的第二个字符串
        """
        ret = cls.cmp(a, b)
        if ret >= 0:
            return b
        else:
            return a
