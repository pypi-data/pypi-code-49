import hashlib

import bech32
import ecdsa
from mnemonic import Mnemonic
from hdacpy.type import Wallet
import hdacpy.bip39_bip44_process as bip_to_mnemonic

PREFIX = "friday"
KEYWORD_PUB = "pub"


def generate_wallet() -> Wallet:
    m = Mnemonic("english")
    mnemonic = m.generate(strength=256)

    privkey, pubkey = bip_to_mnemonic.mnemonic_to_key(mnemonic)
    address = pubkey_to_address(pubkey)
    return {"private_key": privkey, "public_key": pubkey, "address": address, "mnemonic": mnemonic}


def privkey_to_pubkey(privkey: str) -> str:
    privkey_obj = ecdsa.SigningKey.from_string(bytes.fromhex(privkey), curve=ecdsa.SECP256k1)
    pubkey_obj = privkey_obj.get_verifying_key()
    return pubkey_obj.to_string("compressed").hex()


def pubkey_to_address(pubkey: str) -> str:
    pubkey_bytes = bytes.fromhex(pubkey)
    s = hashlib.new("sha256", pubkey_bytes).digest()
    r = hashlib.new("ripemd160", s).digest()
    return bech32.bech32_encode(PREFIX, bech32.convertbits(r, 8, 5))


def privkey_to_address(privkey: str) -> str:
    pubkey = privkey_to_pubkey(privkey)
    return pubkey_to_address(pubkey)


def mnemonic_to_privkey(mnemonic):
    privkey, _ = bip_to_mnemonic.mnemonic_to_key(mnemonic)
    return privkey


def mnemonic_to_pubkey(mnemonic):
    _, pubkey = bip_to_mnemonic.mnemonic_to_key(mnemonic)
    return pubkey


def mnemonic_to_address(mnemonic):
    _, pubkey = bip_to_mnemonic.mnemonic_to_key(mnemonic)
    return pubkey_to_address(pubkey)
