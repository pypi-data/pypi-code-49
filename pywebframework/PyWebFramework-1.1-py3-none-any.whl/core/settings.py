# coding: utf-8


class Settings:
    ROOT = ''

    TAX_INIT_SAMPLE_ROOT = ''

    TEMPLATE_FILE_ROOT = ''

    def load_settings(self, mod):
        for setting in dir(mod):
            if not setting.isupper():
                continue
            setting_value = getattr(mod, setting)
            if setting in dir(self):
                setattr(self, setting, setting_value)


settings = Settings()
