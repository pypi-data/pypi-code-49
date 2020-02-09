# [rights]  Copyright 2020 brianddk at github https://github.com/brianddk
# [license] Apache 2.0 License https://www.apache.org/licenses/LICENSE-2.0
# [repo]    https://github.com/brianddk/pypaperwallet
# [btc]     BTC-b32: bc1qwc2203uym96u0nmq04pcgqfs9ldqz9l3mz8fpj
# [tipjar]  https://gist.github.com/brianddk/3ec16fbf1d008ea290b0

from binascii import hexlify, unhexlify
from io import BytesIO
from base64 import encodebytes
from .template import bitaddress, style, margins
from .ensure_cairolib import *         # <== searches for libcairo-2.dll
from weasyprint import HTML, CSS       # github/Kozea/WeasyPrint
from qrcode import QRCode              # github/lincolnloop/python-qrcode
from mnemonic import Mnemonic          # github/trezor/python-mnemonic
from pycoin.symbols.btc import network as btc  # github/richardkiss/pycoin

def write_pdf(html, pdf):
    css_style = CSS(string=style())
    css_margins = CSS(string=margins())
    HTML(string=html).write_pdf(target=pdf, stylesheets=[css_margins, css_style])


def render_qr(data, marker, html):
    qr = QRCode(box_size=5, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = BytesIO()
    img.save(buf)
    tag = 'data:image/png;base64,' + encodebytes(buf.getvalue()).decode()
    return html.replace(marker, tag)


def read_html(filename):
    with open(filename, "r") as file:
        html = file.read()
    return html


def thunk_lbl(src, target, html):
    return html.replace(target, src)
    

def mk_wallet(filename):
    mnemo = Mnemonic("english")
    # code = "all all all all all all all all all all all all"
    
    code = mnemo.generate()
    seed = mnemo.to_seed(code)
    root = btc.keys.bip32_seed(seed)
    xpub = root.hwif(as_private=False)
    xprv = root.hwif(as_private=True)

    legacy_key = root.subkey_for_path('44H/0H/0H/0/0')
    legacy_address = legacy_key.address()
    legacy_wif = legacy_key.wif()

    p2s_key = root.subkey_for_path('49H/0H/0H/0/0')
    p2s_hash = p2s_key.hash160(is_compressed=True)
    p2s_script = btc.contract.for_p2pkh_wit(p2s_hash)
    p2s_address = btc.address.for_p2s(p2s_script)
    p2s_wif = p2s_key.wif()

    segwit_key = root.subkey_for_path('84H/0H/0H/0/0')
    segwit_hash = segwit_key.hash160(is_compressed=True)
    segwit_address = btc.address.for_p2pkh_wit(segwit_hash)
    segwit_wif = segwit_key.wif()

    print("bip39 mnemonic seed:", code)
    print("bip39 master seed:", hexlify(seed).decode())
    print("root xpub:", xpub)
    print("root xprv:", xprv)
    print("m/44'/0'/0'/0/0 legacy pub/priv:", legacy_address, legacy_wif)
    print("m/49'/0'/0'/0/0 p2sh-wit pub/priv:", p2s_address, p2s_wif)
    print("m/84'/0'/0'/0/0 segwit pub/priv:", segwit_address, segwit_wif)

    html = bitaddress()

    html = render_qr(code, 'seed.png', html)
    html = render_qr(legacy_address, 'pub.png', html)
    html = render_qr(legacy_wif, 'priv.png', html)

    html = thunk_lbl(" ".join(code.split()[0:6]), '__BIP39_SEED_1OF2__', html)
    html = thunk_lbl(" ".join(code.split()[6:12]), '__BIP39_SEED_2OF2__', html)
    html = thunk_lbl(legacy_address, '__BTC__ADDRESS__', html)
    html = thunk_lbl(legacy_wif, '__BTC__WIF__', html)
   
    write_pdf(html, filename)

