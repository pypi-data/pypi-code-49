from abconfig.common import Dict
from abconfig.utils import GetAttrs


class Settings:
    __hidesettings__ = True
    __hidesettings_exclude__ = []
    __file__ = False
    __file_required__ = False
    __env__ = True
    __prefix__ = None
    __vault__ = False
    __vault_required__ = True
    __settings__ = (
        '__hidesettings__',
        '__hidesettings_exclude__',
        '__file__',
        '__file_required__',
        '__env__',
        '__prefix__',
        '__vault__',
        '__vault_required__'
    )


class HideSettings(Dict):
    def __init__(self, obj: Dict):
        super().__init__(self.remove_settings(obj))

    def remove_settings(self, obj: Dict) -> [tuple]:
        result = []
        exclude = obj.get('__hidesettings_exclude__', [])
        if obj.get('__hidesettings__', True) is True:
            for k,v in dict(obj).items():
                if not k in Settings.__settings__ or k in exclude:
                    result.append((k,v))
        return result