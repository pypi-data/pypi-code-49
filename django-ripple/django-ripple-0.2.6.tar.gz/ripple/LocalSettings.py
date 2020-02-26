LOCAL_SETTINGS = {}


class Settings:
    SETTINGS = LOCAL_SETTINGS

    @staticmethod
    def get(name, default=None):
        if name in Settings.SETTINGS.keys():
            return Settings.SETTINGS[name]
        if default is not None:
            return default
        raise Exception(('Setting %s not found. Add %s to config/LOCAL_SETTINGS.py') % (name, name))
