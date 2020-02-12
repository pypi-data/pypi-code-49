r'''
https://github.com/ssut/py-googletrans/blob/master/googletrans/gtoken.py

tkk = '426151.3141811846'

playground\google-fanyi\crud-boy
sign_based_on_googletrans_acquirer.py

from googletrans.gtoken import TokenAcquirer
TOKENAC = TokenAcquirer()

def google_sign(text):
    return TOKENAC.do(text)

def get_tkk():
    global tkk
    if not tkk:
        res = requests.get('https://translate.google.cn/', proxies=proxy).text
        tkk = re.search(r"tkk:'(\d+\.\d+)", res).group(1)
    return tkk
---
httpx
def get_tkk(proxies=None):
    """ get_tkk """
    with httpx.Client(proxies=proxies) as client:
        try:
            # res = requests.get('https://translate.google.cn/', proxies=proxy).text
            res = client.get('https://translate.google.cn/').text
            tkk = re.search(r"tkk:'(\d+\.\d+)", res).group(1)
        except Exception as exc:
            logger.error('Unable to fetch tkk, fall back to None')
            tkk = None
    return tkk

'''
import math
import re
import httpx

from loguru import logger

TKK = '436443.3778881810'
GTK = ''


def rshift(val, n):
    """python port for '>>>'(right shift with padding)
    """
    return (val % 0x100000000) >> n


def _xr(a, b):
    size_b = len(b)
    c = 0
    while c < size_b - 2:
        d = b[c + 2]
        d = ord(d[0]) - 87 if 'a' <= d else int(d)
        d = rshift(a, d) if '+' == b[c + 1] else a << d
        a = a + d & 4294967295 if '+' == b[c] else a ^ d

        c += 3
    return a


def get_tkk(proxies=None):
    """ get_tkk """
    with httpx.Client(proxies=proxies) as client:
        try:
            # res = requests.get('https://translate.google.cn/', proxies=proxy).text
            res = client.get('https://translate.google.cn/').text
            tkk = re.search(r"tkk:'(\d+\.\d+)", res).group(1)
        except Exception as exc:  # tested with monkeypatch re.search
            logger.error('%s, unable to fetch tkk, fall back to None' % exc)
            tkk = None
    return tkk


def google_sign(text, tkk=None):
    '''
    google_sign

    set tkk to a value to aoid fetching tkk for reach requests
    e.g.,
    tkk = get_tkk()
    google_sign(text1, tkk=tkk)
    google_sign(text2, tkk=tkk)

    '436443.3778881810'
    '''
    if tkk is None:
        try:
            tkk = get_tkk()
        except Exception as exc:  # pragma: nocover
            logger.error('%s, unable to fetch tkk, set to None' % exc)
            tkk = None
    if tkk is None:  # pragma: nocover
        tkk = TKK

    a = []
    # Convert text to ints
    for i in text:
        val = ord(i)
        if val < 0x10000:  # 65536 test with chr
            a += [val]
        else:
            # Python doesn't natively use Unicode surrogates, so account for those
            a += [
                math.floor((val - 0x10000) / 0x400 + 0xD800),
                math.floor((val - 0x10000) % 0x400 + 0xDC00),
            ]

    b = tkk if tkk != '0' else ''
    d = b.split('.')
    b = int(d[0]) if len(d) > 1 else 0

    # assume e means char code array
    e = []
    g = 0
    size = len(text)
    while g < size:
        l = a[g]
        # just append if l is less than 128(ascii: DEL)
        if l < 128:  # äöü
            e.append(l)
        # append calculated value if l is less than 2048
        else:  # non-ascii
            if l < 2048:
                e.append(l >> 6 | 192)
            else:
                # append calculated value if l matches special condition
                if (l & 64512) == 55296 and g + 1 < size and a[g + 1] & 64512 == 56320:  # pragma: no cover
                    g += 1
                    l = (
                        65536 + ((l & 1023) << 10) + (a[g] & 1023)
                    )  # This bracket is important
                    e.append(l >> 18 | 240)
                    e.append(l >> 12 & 63 | 128)
                else:
                    e.append(l >> 12 | 224)
                e.append(l >> 6 & 63 | 128)
            e.append(l & 63 | 128)
        g += 1
    a = b
    for i, value in enumerate(e):
        a += value
        a = _xr(a, '+-a^+6')
    a = _xr(a, '+-3^+b+-f')
    a ^= int(d[1]) if len(d) > 1 else 0
    if a < 0:  # pragma: nocover
        a = (a & 2147483647) + 2147483648
    a %= 1000000  # int(1E6)

    return '{}.{}'.format(a, a ^ b)


def test_sanity():  # pragma: no cover
    ''' test sanity '''
    assert google_sign('test') == '476257.126138'
