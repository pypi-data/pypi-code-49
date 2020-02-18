from . import BCHWallet, BTCWallet, DASHWallet, ZECWallet
from .wallet_exceptions import WalletException, WalletIsNotSupportedException
from .adapters.wallet_adapter_base import WalletAdapterBase
from .adapters.rpc_adapter import RPCAdapter


class WalletFactory:

    _SUPPORTED_WALLETS = {
        'BCH': BCHWallet,
        'BTC': BTCWallet,
        'DASH': DASHWallet,
        'ZEC': ZECWallet
    }

    def get(self, ticker_symbol, adapter: WalletAdapterBase = RPCAdapter()):
        ''' Returns a wallet instance based on 'ticker_symbol' that you can use to work with your local wallet. '''
        if ticker_symbol in WalletFactory._SUPPORTED_WALLETS:
            wallet = WalletFactory._SUPPORTED_WALLETS[ticker_symbol]
            return wallet(adapter)
        raise WalletIsNotSupportedException(ticker_symbol)

    def get_all_wallets(self):
        return list(WalletFactory._SUPPORTED_WALLETS.keys())