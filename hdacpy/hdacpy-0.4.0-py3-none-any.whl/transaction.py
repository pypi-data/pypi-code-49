import base64
import hashlib
import json
from typing import Any, Dict, List

import ecdsa
import requests

from hdacpy.exceptions import BadRequestException, EmptyMsgException
from hdacpy.type import SyncMode
from hdacpy.wallet import privkey_to_address, privkey_to_pubkey, pubkey_to_address


class Transaction:
    """A Hdac transaction."""

    def __init__(
        self,
        *,
        host: str,
        privkey: str,
        gas_price: int = 0,
        memo: str = "",
        chain_id: str = "friday-devnet",
        sync_mode: SyncMode = "sync",
    ) -> None:
        self._host = host
        self._privkey = privkey
        self._account_num = 0
        self._sequence = 0
        self._gas_price = gas_price
        self._memo = memo
        self._chain_id = chain_id
        self._sync_mode = sync_mode
        self._msgs: List[dict] = []

    def _get(self, url: str, params: dict) -> requests.Response:
        resp = requests.get(url, params=params)
        return resp

    def _post_json(self, url: str, json_param: dict) -> requests.Response:
        resp = requests.post(url, json=json_param)
        return resp

    def _put_json(self, url: str, json_param: dict) -> requests.Response:
        resp = requests.put(url, json=json_param)
        return resp

    def _get_account_info(self, address):
        url = "/".join([self._host, "auth/accounts", address])
        res = self._get(url, None)
        if res.status_code != 200:
            raise BadRequestException

        resp = res.json()
        self._account_num = int(resp["result"]["value"]["account_number"])
        self._sequence = int(resp["result"]["value"]["sequence"])

    def _get_pushable_tx(self) -> str:
        pubkey = privkey_to_pubkey(self._privkey)
        base64_pubkey = base64.b64encode(bytes.fromhex(pubkey)).decode("utf-8")
        pushable_tx = {
            "tx": {
                "msg": self._msgs,
                "fee": {"gas": str(self._gas_price), "amount": [],},
                "memo": self._memo,
                "signatures": [
                    {
                        "signature": self._sign(),
                        "pub_key": {"type": "tendermint/PubKeySecp256k1", "value": base64_pubkey},
                        "account_number": str(self._account_num),
                        "sequence": str(self._sequence),
                    }
                ],
            },
            "mode": self._sync_mode,
        }
        return pushable_tx

    def _sign(self) -> str:
        message_str = json.dumps(self._get_sign_message(), separators=(",", ":"), sort_keys=True)
        message_bytes = message_str.encode("utf-8")

        privkey = ecdsa.SigningKey.from_string(bytes.fromhex(self._privkey), curve=ecdsa.SECP256k1)
        signature_compact = privkey.sign_deterministic(
            message_bytes, hashfunc=hashlib.sha256, sigencode=ecdsa.util.sigencode_string_canonize
        )

        signature_base64_str = base64.b64encode(signature_compact).decode("utf-8")
        return signature_base64_str

    def _get_sign_message(self) -> Dict[str, Any]:
        return {
            "chain_id": self._chain_id,
            "account_number": str(self._account_num),
            "fee": {"gas": str(self._gas_price), "amount": [],},
            "memo": self._memo,
            "sequence": str(self._sequence),
            "msgs": self._msgs,
        }

    def balance(self, address: str, blockHash: str = None):
        url = "/".join([self._host, "hdac/balance"])
        resp = self._get(url, params={"address": address, "block": blockHash})
        return resp

    def transfer(
        self,
        token_contract_address: str,
        recipient_address: str,
        amount: int,
        gas_price: int,
        fee: int,
        memo: str = "",
    ) -> None:
        sender_pubkey = privkey_to_pubkey(self._privkey)
        sender_address = pubkey_to_address(sender_pubkey)

        self._gas_price = gas_price
        self._memo = memo
        self._get_account_info(sender_address)

        url = "/".join([self._host, "hdac/transfer"])
        params = {
            "base_req": {
                "chain_id": self._chain_id,
                "memo": memo,
                "gas": str(gas_price),
                "from": sender_address,
            },
            "fee": str(fee),
            "token_contract_address": sender_address,
            "recipient_address_or_nickname": recipient_address,
            "amount": str(amount),
        }
        resp = self._post_json(url, json_param=params)
        if resp.status_code != 200:
            raise BadRequestException

        value = resp.json().get("value")
        msgs = value.get("msg")
        if len(msgs) == 0:
            raise EmptyMsgException

        self._msgs.extend(msgs)

    def bond(
        self, token_contract_address: str, amount: int, gas_price: int, fee: int, memo: str = ""
    ):
        pubkey = privkey_to_pubkey(self._privkey)
        address = pubkey_to_address(pubkey)

        self._gas_price = gas_price
        self._memo = memo
        self._get_account_info(address)

        url = "/".join([self._host, "hdac/bond"])
        params = {
            "base_req": {
                "chain_id": self._chain_id,
                "memo": memo,
                "gas": str(gas_price),
                "from": address,
            },
            "token_contract_address": token_contract_address,
            "fee": str(fee),
            "amount": str(amount),
        }
        resp = self._post_json(url, json_param=params)
        if resp.status_code != 200:
            raise BadRequestException

        value = resp.json().get("value")
        msgs = value.get("msg")
        if len(msgs) == 0:
            raise EmptyMsgException

        self._msgs.extend(msgs)

    def unbond(
        self, token_contract_address: str, amount: int, gas_price: int, fee: int, memo: str = ""
    ):
        pubkey = privkey_to_pubkey(self._privkey)
        address = pubkey_to_address(pubkey)

        self._gas_price = gas_price
        self._memo = memo
        self._get_account_info(address)

        url = "/".join([self._host, "hdac/unbond"])
        params = {
            "base_req":{
                "chain_id": self._chain_id,
                "memo": memo,
                "gas": str(gas_price),
                "from": address,
            },
            "token_contract_address": token_contract_address,
            "fee": str(fee),
            "amount": str(amount),
        }
        resp = self._post_json(url, json_param=params)
        if resp.status_code != 200:
            raise BadRequestException

        value = resp.json().get("value")
        msgs = value.get("msg")
        if len(msgs) == 0:
            raise EmptyMsgException

        self._msgs.extend(msgs)

    def set_nick(self, name: str, gas_price: int, memo: str = ""):
        pubkey = privkey_to_pubkey(self._privkey)
        address = pubkey_to_address(pubkey)

        self._gas_price = gas_price
        self._memo = memo
        self._get_account_info(address)

        url = "/".join([self._host, "nickname/new"])
        params = {
            "base_req": {
                "chain_id": self._chain_id,
                "gas": str(gas_price),
                "memo": memo,
                "from": address,
            },
            "nickname": name,
        }
        resp = self._post_json(url, json_param=params)
        if resp.status_code != 200:
            raise BadRequestException

        value = resp.json().get("value")
        msgs = value.get("msg")
        if len(msgs) == 0:
            raise EmptyMsgException

        self._msgs.extend(msgs)

    def changekey(self, name: str, newaddr: str, gas_price: int, memo: str = ""):
        oldpubkey = privkey_to_pubkey(self._privkey)
        oldaddr = pubkey_to_address(oldpubkey)

        self._gas_price = gas_price
        self._memo = memo
        self._get_account_info(oldaddr)

        url = "/".join([self._host, "nickname/change"])
        params = {
            "base_req":{
                "chain_id": self._chain_id,
                "gas": str(gas_price),
                "memo": memo,
                "from": oldaddr,
            },
            "name": name,
            "new_address": newaddr,
        }
        resp = self._put_json(url, json_param=params)
        if resp.status_code != 200:
            raise BadRequestException

        value = resp.json().get("value")
        msgs = value.get("msg")
        if len(msgs) == 0:
            raise EmptyMsgException

        self._msgs.extend(msgs)

    def create_validator(
        self,
        validator_address: str,
        cons_pub_key: str,
        moniker: str,
        identity: str,
        website: str,
        details: str,
        gas_price: int,
        memo: str = "",
    ):
        pubkey = privkey_to_pubkey(self._privkey)
        address = pubkey_to_address(pubkey)

        self._gas_price = gas_price
        self._memo = memo
        self._get_account_info(address)

        url = "/".join([self._host, "hdac/validators"])
        params = {
            "base_req":{
                "chain_id": self._chain_id,
                "memo": memo,
                "gas": str(gas_price),
                "from": validator_address,
            },
            "cons_pub_key": cons_pub_key,
            "description": {
                "moniker": moniker,
                "identity": identity,
                "website": website,
                "details": details,
            },
        }
        resp = self._post_json(url, json_param=params)
        if resp.status_code != 200:
            raise BadRequestException

        value = resp.json().get("value")
        msgs = value.get("msg")
        if len(msgs) == 0:
            raise EmptyMsgException

        self._msgs.extend(msgs)

    def edit_validator(
        self,
        validator_address: str,
        moniker: str,
        identity: str,
        website: str,
        details: str,
        gas_price: int,
        memo: str = "",
    ):
        pubkey = privkey_to_pubkey(self._privkey)
        address = pubkey_to_address(pubkey)

        self._gas_price = gas_price
        self._memo = memo
        self._get_account_info(address)

        url = "/".join([self._host, "hdac/validators"])
        params = {
            "base_req":{
                "chain_id": self._chain_id,
                "memo": memo,
                "gas": str(gas_price),
                "from": validator_address,
            },
            "description": {
                "moniker": moniker,
                "identity": identity,
                "website": website,
                "details": details,
            },
        }
        resp = self._put_json(url, json_param=params)
        if resp.status_code != 200:
            raise BadRequestException

        value = resp.json().get("value")
        msgs = value.get("msg")
        if len(msgs) == 0:
            raise EmptyMsgException

        self._msgs.extend(msgs)

    def send_tx(self):
        tx = self._get_pushable_tx()
        url = "/".join([self._host, "txs"])
        resp = self._post_json(url, json_param=tx)
        return resp
