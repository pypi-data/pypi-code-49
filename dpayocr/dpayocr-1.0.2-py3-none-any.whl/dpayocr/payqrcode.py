import re
from io import BytesIO
from pathlib import Path
from typing import NamedTuple, Tuple, Union

import pytesseract
import pyzbar.pyzbar as pyzbar
from PIL import Image

re_price_for_alipay = re.compile(r"¥([.0-9]+)")
re_price_for_weipay = re.compile(r"([.0-9]+)")


class PayQrCode(NamedTuple):
    """支付二维码信息

    Attributes
    ----------
    pay_type : int
        支付类型。1 为支付宝， 2 为微信，-1 未识别出来
    price : float
        金额
    url : str
        支付链接
    """

    pay_type: int
    price: float
    url: str


def parse_pay_qr_code_type_and_url(im) -> Tuple[int, str]:
    """解析支付二维码类型和链接

    Parameters
    ----------
    im : PIL.Image
        二维码图像

    Returns
    -------
    pay_type : int
        支付类型。1 为支付宝， 2 为微信，-1 未识别出来
    url : str
        链接
    """
    pay_type = -1
    url = ""

    decodeds = pyzbar.decode(im)
    if not decodeds:
        raise ValueError("no decoded")

    decoded = decodeds[0]
    url = decoded.data.decode()
    if url.startswith("https://qr.alipay.com"):
        pay_type = 1
    elif url.startswith("wxp://"):
        pay_type = 2

    return pay_type, url


def parse_pay_qr_code_price(im, pay_type: int = 1) -> float:
    """解析支付二维码金额

    Parameters
    ----------
    im : PIL.Image
        二维码图像
    pay_type : int
        支付类型

    Returns
    -------
    float
        金额。未识别出来返回 -1.0
    """
    price = -1.0
    if pay_type == 1:
        custom_oem_psm_config = "--oem 1 --psm 6"
        re_pattern = re_price_for_alipay
    elif pay_type == 2:
        custom_oem_psm_config = "--oem 1 --psm 11"
        re_pattern = re_price_for_weipay
    else:
        raise ValueError("pay type invaild")

    text = pytesseract.image_to_string(im, lang="eng", config=custom_oem_psm_config)
    match = re_pattern.search(text)
    if match:
        price = float(match.group(1))

    return price


def parse_pay_qr_code(fp: Union[str, Path, BytesIO]) -> PayQrCode:
    """解析支付二维码

    Parameters
    ----------
    fp : (str, bytesio)
        文件名或者二进制IO

    Returns
    -------
    PayQrCode
        支付二维码的信息
    """
    im = Image.open(fp)
    pay_type, url = parse_pay_qr_code_type_and_url(im)
    price = parse_pay_qr_code_price(im, pay_type)

    return PayQrCode(pay_type, price, url)


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="the file name want to parse.")
    args = parser.parse_args()

    print(parse_pay_qr_code(args.filename))


if __name__ == "__main__":
    main()
