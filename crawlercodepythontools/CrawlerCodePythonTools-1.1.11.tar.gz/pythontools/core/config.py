from pythontools.core import tools
import os

cfg = None

class Config(object):

    def __init__(self, path="", default_config={}):
        self.path = path
        self.default_config = default_config
        if "%APPDATA%" in self.path:
            self.path = self.path.replace("%APPDATA%", str(os.getenv("APPDATA")))
        if not tools.existDirectory(self.path):
            try:
                tools.createDirectory(self.path)
            except:
                pass
        self.reloadConfig()

    def reloadConfig(self):
        if not tools.existFile(self.path + "config.json"):
            tools.createFile(self.path + "config.json")
            tools.saveJson(self.path + "config.json", self.default_config)
        self.config = tools.loadJson(self.path + "config.json")
        global cfg
        cfg = self

    def getConfig(self):
        return self.config

    def saveConfig(self):
        tools.saveJson(self.path + "config.json", self.config)

def setConfig(config):
    global cfg
    cfg = config

def getConfig():
    global cfg
    return cfg