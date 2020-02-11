#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import string
import hashlib

CHINESE_PUNCTUATION = u'，。！￥？——；“”：《》（）'
ENGLISH_PUNCTUATION = string.punctuation


def is_chinese_punctuation(char):
    return char in CHINESE_PUNCTUATION


def remove_chinese_punctuation(s):
    ret = u''
    for c in s:
        if not is_chinese_punctuation(c):
            ret += c
    return ret


def is_english_punctuation(char):
    return char in ENGLISH_PUNCTUATION


def remove_english_punctuation(s):
    ret = u''
    for c in s:
        if not is_english_punctuation(c):
            ret += c
    return ret


def is_pure_english(s):
    yes = True
    for e in s:
        if ord(e) > 127:
            yes = False
            break
    if yes:
        return True
    else:
        return False


def english_words(s):
    return ''.join([e for e in s if ord(e) <= 127]).strip()


def common_suffix(s1, s2):
    """
    get common suffix of two string
    @param s1: first string
    @param s2: second string
    @return: the common suffix

    """
    min_len = min(len(s1), len(s2))
    if min_len == 0:
        return ''
    for i in range(-1, -min_len - 1, -1):
        if s1[i] != s2[i]:
            break
    if i == -1:
        return ''
    elif i == -min_len:
        return s1[i:]
    else:
        return s1[i + 1:]


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def test():
    def print_list(lst):
        for e in lst:
            print(e.encode('utf-8'))


def DBC2SBC(data):
    '''
    全角转半角
    '''
    res = ""
    for uchar in data:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
            if not (0x0021 <= inside_code and inside_code <= 0x7e):
                res += uchar
                continue
        res += chr(inside_code)
    return res


def symbol_cn2en(data):
    '''
    中文标点转英文标点
    '''
    if not data:
        return data
    d = {
        '。': '.',
        '｡': '.',
        '〝': '"',
        '〞': '"',
        "‛": "'",
        '“': '"',
        '”': '"',
        "‘": "'",
        "’": "'",
        '～': '~',
        '—': '-',
        '＄': '$',
        '￥': '$',
        '【': '[',
        '】': ']',
        '》': '>',
        '《': '<'
    }
    table = ''.maketrans(d)
    norm = data.translate(table)
    return norm


def reverse_roman(data):
    '''
    将罗马数字转到键盘可输入的字符
    '''
    if not data:
        return data
    d = {
        'Ⅰ': 'I',
        'Ⅱ': 'II',
        'Ⅲ': 'III',
        'Ⅳ': 'IV',
        'Ⅴ': 'V',
        'Ⅵ': 'VI',
        'Ⅶ': 'VII',
        'Ⅷ': 'VIII',
        'Ⅸ': 'IX',
        'Ⅹ': 'X',
        'Ⅺ': 'XI',
        'Ⅻ': 'XII',
        'ⅰ':'i',
        'ⅱ':'ii',
        'ⅲ':'iii',
        'ⅳ':'iv',
        'ⅴ':'v',
        'ⅵ':'vi',
        'ⅶ':'vii',
        'ⅷ':'viii',
        'ⅸ':'ix',
        'ⅹ':'x',
        'ⅺ':'xi',
        'ⅻ':'xii'
    }
    table = ''.maketrans(d)
    norm = data.translate(table)
    return norm


def del_meaningless_char(data):
    '''
    删除无意义字符
    '''
    if not data:
        return data
    data = data.replace('^?', '').replace('\x7f', '')
    return data


def standard_string_format(
        data,
        ds=1,
        no_roman=1,
        en_punc=1,
        no_space=1,
        no_abnormal=1,
        upper=0,
        lower=0,
):
    '''
    按照参数指定的样式格式化字符串
    data:输入的字符串
    ds:是否要全角转半角，1表示是，0表示否
    no_roman：是否把罗马数字字符转成字母，1表示是，0表示否
    en_punc：是否把中文标点转英文标点，1表示是，0表示否
    no_space：是否删除空字符，1表示是，0表示否
    no_abnormal：是否删除异常字符，1表示是，0表示否
    upper：是否把字符串转成大写，1表示是，0表示否
    lower：是否把字符串转成小写，1表示是，0表示否
    '''
    if not data:
        return data
    if no_space:
        data = re.sub('\s', '', data)
    if upper:
        data = data.upper()
    if lower:
        data = data.lower()
    if ds:
       data = DBC2SBC(data)
    if en_punc:
        data = symbol_cn2en(data)
    if no_roman:
        data = reverse_roman(data)
    if no_abnormal:
        data = del_meaningless_char(data)
    return data


if __name__ == '__main__':
    test()
