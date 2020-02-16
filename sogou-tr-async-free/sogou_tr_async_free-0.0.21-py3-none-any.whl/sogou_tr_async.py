'''
sogou_tr_async
'''

from typing import Optional, Union, Tuple, Callable, Any

from urllib import parse
import hashlib

import httpx
# from jmespath import search  # type: ignore
from fuzzywuzzy import fuzz, process  # type: ignore

from loguru import logger

from freemt_utils import httpx_get, make_url
from .get_snuid import SNUID

URL0 = 'https://fanyi.sogou.com'
URL = "https://fanyi.sogou.com/reventondc/translateV2"

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'  # NOQA
HEADERS = {
    "origin": URL0,
    "User-Agent": UA,
    'Referer': URL0,
    # 'Pragma': 'no-cache',
    'Cookie': 'SNUID=%s' % SNUID,
}

SECCODE = '8511813095152'  # V 20190929

SOGOUTR_CODES = [
    'auto', 'ar', 'et', 'bg', 'pl', 'ko', 'bs-Latn', 'fa', 'mww', 'da', 'de',
    'ru', 'fr', 'fi', 'tlh-Qaak', 'tlh', 'hr', 'otq', 'ca', 'cs', 'ro', 'lv',
    'ht', 'lt', 'nl', 'ms', 'mt', 'pt', 'ja', 'sl', 'th', 'tr', 'sr-Latn',
    'sr-Cyrl', 'sk', 'sw', 'af', 'no', 'en', 'es', 'uk', 'ur', 'el', 'hu',
    'cy', 'yua', 'he', 'zh-CHS', 'it', 'hi', 'id', 'zh-CHT', 'vi', 'sv', 'yue',
    'fj', 'fil', 'sm', 'to', 'ty', 'mg', 'bn'
]
ERROR_DICT = {
    '1001': 'Translate API: Unsupported language type',
    '1002': 'Translate API: Text too long',
    '1003': 'Translate API: Invalid PID',
    '1004': 'Translate API: Trial PID limit reached',
    '1005': 'Translate API: PID traffic too high',
    '1006': 'Translate API: Insufficient balance',
    '1007': 'Translate API: Random number does not exist',
    '1008': 'Translate API: Signature does not exist',
    '1009': 'Translate API: The signature is incorrect',
    '10010': 'Translate API: Text does not exist',
    '1050': 'Translate API: Internal server error',
}


def with_func_attrs(**attrs: Any) -> Callable:
    ''' with_func_attrs '''
    def with_attrs(fct: Callable) -> Callable:
        for key, val in attrs.items():
            setattr(fct, key, val)
        return fct
    return with_attrs


@with_func_attrs(resp='')
async def sogou_tr_async(  # pylint: disable=too-many-arguments
        text: str,
        from_lang: str = 'auto',
        to_lang: str = 'zh',
        fuzzy: bool = True,
        proxy: Optional[str] = None,
        debug: bool = False,
) -> Union[str, Tuple[str, Optional[str]]]:
    ''' sogou_tr_async '''

    try:
        text = text.strip()
    except Exception as exc:  # pragma: no cover
        logger.error(exc)
        sogou_tr_async.text = str(exc)
        text = ''
    if not text:
        sogou_tr_async.text = 'nothing to do'
        return ''

    from_lang = from_lang.lower()
    to_lang = to_lang.lower()

    if from_lang == 'auto' and to_lang == 'auto':
        to_lang = 'zh'

    if from_lang in ['zh', 'chinese']:
        from_lang = 'zh-CHS'
    if to_lang in ['zh', 'chinese']:
        to_lang = 'zh-CHS'

    if fuzzy:
        if from_lang not in SOGOUTR_CODES:
            from_lang = process.extractOne(from_lang, SOGOUTR_CODES, scorer=fuzz.UWRatio)[0]  # NOQA
        if to_lang not in SOGOUTR_CODES:
            to_lang = process.extractOne(to_lang, SOGOUTR_CODES, scorer=fuzz.UWRatio)[0]  # NOQA

    if from_lang == to_lang:
        sogou_tr_async.text = 'nothing to do'
        return text

    str_ = from_lang + to_lang + text + SECCODE
    md5 = hashlib.md5(str_.encode('utf-8'))
    sign = md5.hexdigest()

    proxy = make_url(proxy)
    data = {
        'from': from_lang,
        'to': to_lang,
        'text': text,
        'client': 'pc',
        'fr': 'browser_pc',
        'pid': 'sogou-dict-vr',
        'dict': 'true',
        'word_group': 'true',
        'second_query': 'true',
        'uuid': 'dc1058e6-7eff-4c5e-84c3-3137f4dceb26',
        'needQc': '1',
        's': sign
    }

    _ = f'{URL}?{parse.urlencode(data)}'
    try:
        resp = await httpx_get(
            _,
            headers=HEADERS,
            proxy=proxy,
        )

        resp.raise_for_status()
    except Exception as exc:
        logger.error(exc)
        req = httpx.models.Request('GET', URL)
        resp = httpx.Response(
            status_code=499,
            request=req,
            content=str(exc).encode(),
        )

    sogou_tr_async.resp = resp

    try:
        # pip install jmespath problem in linux?
        # res = search('data.translate.dit', resp.json())
        res = resp.json().get('data').get('translate').get('dit')
    except Exception as exc:
        logger.error(exc)
        raise

    if debug:
        return res, proxy

    return res
