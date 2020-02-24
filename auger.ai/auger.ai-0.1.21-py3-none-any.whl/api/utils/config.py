import os
import logging

from auger.api.utils.config_yaml import ConfigYaml

log = logging.getLogger("auger")


class Config(object):

    def __init__(self):
        super(Config, self).__init__()
        self.parts = {}
        self.load()

    def get(self, path, default=None):
        if len(self.parts.keys()) == 0:
            return default
        if 'config' in self.parts.keys():
            default = self.parts['config'].get(path, default)
        return self.parts['auger'].get(path, default)

    def set(self, part_name, path, value):
        if (part_name == 'config' and self.ismultipart()):
            self.parts['config'].set(path, value)
        else:
            self.parts['auger'].set(path, value)

    def write(self, part_name):
        if (part_name == 'config' and self.ismultipart()):
            self.parts['config'].write()
        else:
            self.parts['auger'].write()

    def load(self, path = None):
        if path is None:
            path = os.getcwd()
        for cfgname in ['config', 'auger']:
            filename = os.path.abspath(os.path.join(path, '%s.yaml' % cfgname))
            if os.path.isfile(filename):
                self.parts[cfgname] = self._load(filename)
        return self

    def ismultipart(self):
        return(len(self.parts.keys()) > 1)

    def _load(self, name):
        part = ConfigYaml()
        if os.path.isfile(name):
            part.load_from_file(name)
        return part
