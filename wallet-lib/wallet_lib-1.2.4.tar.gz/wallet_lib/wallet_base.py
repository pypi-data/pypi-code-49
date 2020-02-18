import simplejson as json

from simplejson.errors import JSONDecodeError
from abc import ABCMeta, abstractmethod
from .adapters import WalletAdapterBase
from .wallet_exceptions import WalletException
from .zmq_notifier import ZMQNotifier

class WalletBase(metaclass=ABCMeta):

    def load_json(self, val: str, raw: bool):
        invalid_type = type(val) in [dict, list, float]
        if raw: return val
        elif invalid_type: return val
        else:
            try: return json.loads(val)
            except JSONDecodeError: return val

    @abstractmethod
    def __init__(self, *args): pass

    @abstractmethod
    def create_address(self, *args): pass

    @abstractmethod
    def get_balance(self, *args): pass

    @abstractmethod
    def get_transaction(self, *args): pass

    @abstractmethod
    def get_transactions(self, *args): pass

    @abstractmethod
    def send(self, *args): pass

    @abstractmethod
    def get_transactions_since(self, *args): pass

    @abstractmethod
    def run(self, *args): pass

    def get_zmq_notifier(self, **kwargs):
        return ZMQNotifier(**kwargs)
