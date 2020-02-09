__version__ = '1.0.11'

from abconfig.common import Dict

from abconfig.file import File
from abconfig.env import Environment
from abconfig.vault import Vault

from abconfig.utils import GetAttrs, Close
from abconfig.settings import Settings, HideSettings


class ABConfig(Dict, Settings):
    __pipeline__ = (File, Environment, Vault)

    def __init__(self, obj=None):
        super().__init__(
            GetAttrs(
                obj if obj else self,
                settings=self.__settings__
            )
            .do(*self.__pipeline__)
            .do(HideSettings, Close)
            .items()
        )
        self.__dict__.update(self)
