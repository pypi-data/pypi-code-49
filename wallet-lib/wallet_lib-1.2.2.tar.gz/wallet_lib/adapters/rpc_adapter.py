from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from ..wallet_exceptions import WalletException
import logging
import os

from .wallet_adapter_base import WalletAdapterBase


class RPCAdapterException(WalletException):
    def __init__(self, reason):
        self.reason = reason
        super().__init__(reason, -801)


class RPCAdapterResponse:
    def __init__(self, result, error=None, code=None):
        self.result = result
        self.error = error
        self.code = code


class RPCAdapter(WalletAdapterBase):
    def __init__(self,
            rpc_user = os.getenv('RPC_USER'),
            rpc_password = os.getenv('RPC_PASSWORD'),
            rpc_host = os.environ.get('RPC_HOST', '127.0.0.1'),
            rpc_port = os.environ.get('RPC_PORT', '8332')):
        self.log = logging.getLogger('wallet_lib.rpcadapter')
        self.rpc_host = rpc_host
        self.rpc_port = rpc_port
        self.rpc_user = rpc_user
        self.rpc_password = rpc_password

    def run(self, command, *args):
        try:
            rpc_connection = AuthServiceProxy(
                "http://%s:%s@%s:%s" % (self.rpc_user, self.rpc_password, self.rpc_host, self.rpc_port))
            try:
                cmd_args = self._build_args(command, *args)
                response = rpc_connection.batch_(cmd_args)
            except JSONRPCException as e:
                return RPCAdapterResponse(None, e.message, e.code)
            return RPCAdapterResponse(response[0])
        except Exception:
            message = 'Failed to run {} command'.format(command)
            self.log.debug(message, exc_info=1)
            raise RPCAdapterException(message)

    def _build_args(self, command, *args):
        data = list(args)
        data.insert(0, command)
        return [data]
