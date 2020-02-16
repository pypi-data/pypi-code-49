'''
fetch SNIUID
'''

# import requests
# from itertools import dropwhile

import httpx
from loguru import logger

URL = 'https://fanyi.sogou.com/'


def get_snuid() -> str:
    ''' get SNUID
    # return next(dropwhile(lambda elm: elm[0] != 'SNUID', requests.get('https://fanyi.sogou.com/').cookies.iteritems()))[1]

    cookies_items:
    [('IPLOC', 'CN8100'),
    ('SNUID', '284BF439E6E37B4232219E03E68DFC67'),
    ('SUID', 'CEAD12DFB52EA00A000000005E48A2B5'),
    ('ABTEST', '7|1581818549|v17')]
    '''
    try:
        # cookies_items = requests.get(URL).cookies.iteritems()
        cookies_items = httpx.get(URL).cookies.items()
    except Exception as exc:
        logger.error(exc)
        cookies_items = [('SNUID', '')]

    _ = dict(cookies_items).get('SNUID')

    if isinstance(_, str):
        return _
    return ''


SNUID = get_snuid()
