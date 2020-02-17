from typing import Optional, List, Callable, Dict, Iterator
from nlp_jp_gears.utils import replace_by_dict


class AbstractZenHanConverter:
    def __init__(
        self,
        targets: Optional[List[str]] = None,
        excludes: Optional[List[str]] = None,
        symbol: bool = True,
        number: bool = True,
        alphabet: bool = True,
        *args,
        **kwargs,
    ):
        self._converter: Optional[Callable[..., str]] = None

    def __call__(self, text: str):
        raise NotImplementedError


class ZenToHanConverter(AbstractZenHanConverter):
    """
    convert Japanese "zenkaku" text into "hankaku" text
    Supports:
        ！＂＃＄％＆＇（）＊＋，－．／
        ：；＜＝＞？＠［＼］＾＿｀｛｜｝～
        ０１２３４５６７８９
        ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ
        ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ

    Args:
        targets: declaire target characters. if None (default), all support characters is converted.
        excludes: declaire characters to keep format.
        symbol: if True (default), symbol is converted.
        number: if True (default), number is converted.
        alphabet: if True (default), alphabet is converted.
    """

    def __init__(
        self,
        targets: Optional[List[str]] = None,
        excludes: Optional[List[str]] = None,
        symbol: bool = True,
        number: bool = True,
        alphabet: bool = True,
        *args,
        **kwargs,
    ):
        dic = get_zen_to_han_dic(targets, excludes, symbol, number, alphabet)
        # converts-attribute shows intrinsic all targets a instance make convert
        self.converts = "".join(dic)
        self._converter: Callable[[str], str] = replace_by_dict(dic)

    def __call__(self, text: str) -> str:
        """Convert Japanese "zenkaku" text of input text
        into "hankaku" text

        Args:
            text: input zenkaku text

        Returns:
            output hankaku text
        """
        return self._converter(text)


def get_zen_to_han_dic(
    targets: Optional[List[str]] = None,
    excludes: Optional[List[str]] = None,
    symbol: bool = True,
    number: bool = True,
    alphabet: bool = True,
) -> Dict[str, str]:
    """
    Convert Japanese "zenkaku" text into "hankaku" text
    Supports:
        ！＂＃＄％＆＇（）＊＋，－．／
        ：；＜＝＞？＠［＼］＾＿｀｛｜｝～
        ０１２３４５６７８９
        ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ
        ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ

    Args:
        targets: declaire target characters. if None (default), all support characters is converted.
        excludes: declaire characters to keep format.
        symbol: if True (default), symbol is converted.
        number: if True (default), number is converted.
        alphabet: if True (default), alphabet is converted.
    """
    tar = tuple(targets) if targets else {}
    exc = tuple(excludes) if excludes else {}
    dic = {chr(0xFF01 + i): chr(0x21 + i) for i in _range(symbol, number, alphabet)}
    if tar:
        dic = {key: val for key, val in dic.items() if key in tar}
    if exc:
        dic = {key: val for key, val in dic.items() if key not in exc}

    return dic


class HanToZenConverter(AbstractZenHanConverter):
    """
    Convert Japanese "hankaku" symbols into "zenkaku" symbols
    Supports:
        !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        0123456789
        ABCDEFGHIJKLMNOPQRSTUVWXYZ
        abcdefghijklmnopqrstuvwxyz

    Args:
        targets: declaire target characters. if None (default), all support characters is converted.
        excludes: declaire characters to keep format.
        symbol: if True (default), symbol is converted.
        number: if True (default), number is converted.
        alphabet: if True (default), alphabet is converted.
    """

    def __init__(
        self,
        targets: Optional[List[str]] = None,
        excludes: Optional[List[str]] = None,
        symbol: bool = True,
        number: bool = True,
        alphabet: bool = True,
        *args,
        **kwargs,
    ):
        dic = get_han_to_zen_dic(targets, excludes, symbol, number, alphabet)
        self.converts = "".join(dic)
        self._converter: Callable[[str], str] = replace_by_dict(dic)

    def __call__(self, text: str) -> str:
        """Convert Japanese "hankaku" text of input text
        into "zenkaku" text

        Args:
            text: input hankaku text

        Returns:
            output zenkaku text
        """
        return self._converter(text)


def get_han_to_zen_dic(
    targets: Optional[List[str]] = None,
    excludes: Optional[List[str]] = None,
    symbol: bool = True,
    number: bool = True,
    alphabet: bool = True,
) -> Dict[str, str]:
    """
    Convert Japanese "hankaku" symbols into "zenkaku" symbols
    Supports:
        !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        0123456789
        ABCDEFGHIJKLMNOPQRSTUVWXYZ
        abcdefghijklmnopqrstuvwxyz

    Args:
        targets: declaire target characters. if None (default), all support characters is converted.
        excludes: declaire characters to keep format.
        symbol: if True (default), symbol is converted.
        number: if True (default), number is converted.
        alphabet: if True (default), alphabet is converted.
    """
    tar = tuple(targets) if targets else {}
    exc = tuple(excludes) if excludes else {}
    dic = {chr(0x21 + i): chr(0xFF01 + i) for i in _range(symbol, number, alphabet)}
    if tar:
        dic = {key: val for key, val in dic.items() if key in tar}
    if exc:
        dic = {key: val for key, val in dic.items() if key not in exc}

    return dic


def _range(symbol: bool, number: bool, alphabet: bool) -> Iterator[int]:
    if symbol:
        for i in range(15):
            yield i
        for i in range(25, 32):
            yield i
        for i in range(58, 64):
            yield i
        for i in range(90, 94):
            yield i
    if number:
        for i in range(15, 25):
            yield i
    if alphabet:
        for i in range(32, 58):
            yield i
        for i in range(64, 90):
            yield i
