from envconfig import param
from envconfig import EnvConfig


class AppConfig(EnvConfig):

    FOO = param.Str(required=True)


class App:
    def __init__(self, config):
        self.config = config


env = AppConfig()
print(env.FOO)

app = App(env)
