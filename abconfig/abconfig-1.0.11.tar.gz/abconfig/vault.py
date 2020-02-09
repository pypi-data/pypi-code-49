try:
    from hvac import Client as VaultClient
    from hvac.exceptions import VaultError
    from hvac.exceptions import Unauthorized as VaultUnauthorized
except ImportError:
    pass

try:
    import boto3
except ImportError:
    pass

from abconfig.common import Dict
from abconfig.env import OSEnviron

from abconfig.utils import Switch, Close, ignore_warnings


class VaultData(OSEnviron):
    _config_scheme = Dict(
        auth_type='token',
        data_type='json',
        addr=str,
        token=str,
        path=str,
        kv_version=2,
        header_value=str,
        role=str
    )

    def __init__(self, obj: Dict):
        self._required = obj.get('__vault_required__', True)
        self._config = (self._config_scheme + obj.get('__vault__')).bind(Close)
        try:
            self._cache = self._request()
        except VaultError as error:
            if self._required is True:
                raise VaultError(error)
            self._cache = {}

        if self._config['data_type'] == 'kv':
            super().__init__(obj + self.read(obj, obj.get('__prefix__')))
        elif self._config['data_type'] == 'json':
            super().__init__(obj + self._cache)
        else:
            raise ValueError(f'only supported "kv" or "json"')

    def env(self, prefix: str, k: str, v: any) -> tuple:
        key = k if k != '__vault__' else 'vault'
        if self.is_dict(v):
            return (key, self.read(v, self.concat(prefix,key)))
        else:
            return (key, self._cache.get(self.concat(prefix, key).upper(), None))

    def _request(self) -> Dict:
        if self._config['kv_version'] == 2:
            return Dict(self._auth.v2.read_secret_version(
                path=self._config['path']
            )['data']['data'])
        elif self._config['kv_version'] == 1:
            return Dict(self._auth.v1.read_secret(
                path=self._config['path']
            )['data'])
        else:
            return Dict()

    @property
    @ignore_warnings
    def _auth(self):
        client = VaultClient(url=self._config['addr'])
        auth = self._config['auth_type']
        token = self._config['token']

        if token and auth == 'token':
            client.token = token
        elif auth == 'aws_iam':
            session = boto3.Session()
            creds = session.get_credentials()
            kwargs = [
                self._config['header_value'],
                self._config['role']
            ]

            client.auth_aws_iam(
                creds.access_key,
                creds.secret_key,
                creds.token,
                **{
                    k:v for k,v in self._config.items()
                    if v and k in kwargs
                }
            )

        if client.is_authenticated() is False:
            raise VaultUnauthorized(f'auth_type: {auth}')

        return client.secrets.kv

    @staticmethod
    def enabled(obj: Dict):
        return Dict.is_dict(obj.get('__vault__'))


class Vault(metaclass=Switch):
    __target__ = VaultData
