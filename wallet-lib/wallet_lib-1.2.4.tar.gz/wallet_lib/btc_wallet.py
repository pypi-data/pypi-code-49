from .adapters.wallet_adapter_base import WalletAdapterBase
from .wallet_exceptions import WalletException, WalletInputException
from .wallet_base import WalletBase

class BTCWallet(WalletBase):

    TICKER_SYMBOL = "BTC"

    _GET_BALANCE_COMMAND = 'getbalance'
    _GET_TRANSACTION_COMMAND = 'gettransaction'
    _LIST_TRANSACTIONS_COMMAND = 'listtransactions'
    _LIST_SINCE_BLOCK_COMMAND = 'listsinceblock'
    _GET_NEW_ADDRESS_COMMAND = 'getnewaddress'
    _SEND_TO_ADDRESS_COMMAND = 'sendtoaddress'

    def __init__(self, adapter: WalletAdapterBase):
        self.adapter = adapter

    def create_address(self, label=None, raw=True):
        label_str = label or ''
        res = self.adapter.run(self._GET_NEW_ADDRESS_COMMAND, label_str)
        if res.error: raise WalletException(res.error, res.code)
        return self.load_json(res.result, raw)

    def get_balance(self, raw=True):
        res = self.adapter.run(self._GET_BALANCE_COMMAND)
        if res.error: raise WalletException(res.error, res.code)
        return self.load_json(res.result, raw)

    def get_transaction(self, tx_id, raw=True):
        res = self.adapter.run(self._GET_TRANSACTION_COMMAND, tx_id)
        if res.error: raise WalletException(res.error, res.code)
        return self.load_json(res.result, raw)

    def get_transactions(self, label: str = None, count: int = 25, offset: int = 0, raw=False):
        label_str = label or ''
        res = self.adapter.run(
            self._LIST_TRANSACTIONS_COMMAND, label_str, count, offset)
        if res.error: raise WalletException(res.error, res.code)
        return self.load_json(res.result, raw)

    def send(self, address:str, amount:int, raw=True):
        if address is None:
            raise WalletInputException('Address is invalid')
        if amount <= 0:
            raise WalletInputException('Amount should be greater than 0')
        res = self.adapter.run(self._SEND_TO_ADDRESS_COMMAND, address, str(amount))
        if res.error: raise WalletException(res.error, res.code)
        return self.load_json(res.result, raw)

    def get_transactions_since(self, block_hash, raw=True):
        res = self.adapter.run(
            self._LIST_SINCE_BLOCK_COMMAND, block_hash)
        if res.error: raise WalletException(res.error, res.code)
        return self.load_json(res.result, raw)

    def run(self, command, *args, **kwargs):
        res = self.adapter.run(command, *args)
        if res.error: raise WalletException(res.error, res.code)
        return self.load_json(res.result, kwargs.get('raw', True))
