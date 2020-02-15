#!/usr/bin/env python
# coding=utf-8

_first_letter = {
    "b": "b", "c": "c", "d": "d", "f": "f", "g": "g", "h": "h", "i": "ch", "j": "j", "k": "k", "l": "l",
    "m": "m", "n": "n", "p": "p", "q": "q", "r": "r", "s": "s", "t": "t", "u": "sh", "v": "zh", "w": "w",
    "x": "x", "y": "y", "z": "z"
}
_second_letter = {
    "a": "a", "b": "in", "c": "ao", "d": "ai", "e": "e", "f": "en", "g": "eng", "h": "ang",
    "i": "i", "j": "an", "k": ["ing", "uai"], "l": ["iang", "uang"], "m": "ian", "n": "iao",
    "o": ["o", "uo"], "p": "ie", "q": "iu", "r": "uan", "s": ["iong", "ong"], "t": ["ue", "ve"],
    "u": "u", "v": ["ui", "v"], "w": "ei", "x": ["ia", "ua"], "y": "un", "z": "ou"
}
_other_letter = {
    "aa": "a", "ah": "ang", "ai": "ai", "an": "an", "ao": "ao", "ee": "e",
    "eg": "eng", "ei": "ei", "en": "en", "er": "er", "oo": "o", "ou": "ou"
}
_valid_words = [
    "jia", "qia", "xia", "gua", "kua", "hua", "zhua", "chua", "shua", "guai", "kuai", "huai",
    "zhuai", "chuai", "shuai", "bing", "ping", "ming", "ding", "ting", "ning", "ling", "jing", "qing",
    "xing", "ying", "guang", "kuang", "huang", "zhuang", "chuang", "shuang", "diang", "niang", "liang",
    "jiang", "qiang", "xiang", "bo", "po", "mo", "fo", "lo", "wo", "duo", "tuo", "nuo", "luo", "guo", "kuo",
    "huo", "zhuo", "chuo", "shuo", "ruo", "zuo", "cuo", "suo", "jiong", "qiong", "xiong", "dong", "tong",
    "nong", "long", "gong", "kong", "hong", "zhong", "chong", "rong", "zong", "cong", "song", "yong",
    "jue", "que", "xue", "yue", "nve", "lve", "dui", "tui", "gui", "kui", "hui", "zhui", "chui", "shui", "rui",
    "zui", "cui", "sui", "nv", "lv"
]


def believe():
    print('我信仰帅副!')


def translate(text, add_blank=True):
    _result = ""
    _i = 0
    _len = len(text)
    while _i < _len:
        if _i == _len - 1:
            _result += text[_i]
            break
        _t = text[_i] + text[_i + 1]
        _blank = ' ' if _i + 2 < _len and text[_i + 2] != ' ' and add_blank else ''
        if _t in _other_letter:
            _result += (_other_letter[_t] + _blank)
            _i += 1
        elif text[_i] in _first_letter and text[_i + 1] in _second_letter:
            if isinstance(_second_letter[text[_i + 1]], list):
                _w1 = _first_letter[text[_i]] + _second_letter[text[_i + 1]][0]
                _w2 = _first_letter[text[_i]] + _second_letter[text[_i + 1]][1]
                if _w1 in _valid_words:
                    _result += (_w1 + _blank)
                elif _w2 in _valid_words:
                    _result += (_w2 + _blank)
            else:
                _result += _first_letter[text[_i]] + _second_letter[text[_i + 1]] + _blank
            _i += 1
        else:
            _result += text[_i]
        _i += 1
    return _result


def version():
    return "0.6.0"


fjyi = translate

bjbf = version

xbyh = believe
