import json, os, sys
from collections import OrderedDict
from json import JSONDecodeError

__all__ = "Config"

class Simple_json_config(OrderedDict):
    _data=OrderedDict()

    def __init__(self, autoSave=True, default={}, configFile = "config.json", *args, **kwargs):
        super(Simple_json_config, self).__init__(*args, **kwargs)
        self._data.autoSave = autoSave
        self._data.file = os.path.join(os.path.dirname(sys.argv[0]), configFile)
        self._data.default = default
        if not os.path.isfile(self._data.file):
            self.create_default()
        self.loadConfig()

    def __setattr__(self, key, value):
        print ("Setting 1",key,value)
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)
        if self._data.autoSave:
            self.saveConfig()

    def __setitem__(self, key, value):
        print ("Setting 2",key,value)
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)
        if self._data.autoSave:
            self.saveConfig()

    def __getattr__(self, item):
        try:
            return self.__getitem__(item)
        except KeyError:
            raise AttributeError(item)

    def create_default(self):
        with open(self._data.file, 'w') as outfile:
            json.dump(self._data.default, outfile, indent=2)

    def loadConfig(self):
        try:
            with open(self._data.file) as json_data:
                self.update(json.load(json_data, object_pairs_hook=OrderedDict))
        except JSONDecodeError:
            print("Invalid JSON, restoring default")
            self.create_default()

    def saveConfig(self):
        with open(self._data.file, 'w') as outfile:
            json.dump(self, outfile, indent=2)

if __name__ == '__main__':
    cfg = Simple_json_config(autoSave=True, default={'items':{}, 'rois':{}})
    cfg.noot="noot"
    cfg['aap']="mies"
    print ("res1:",cfg.noot)
    print ("res2:",cfg['aap'])
    print ("res3:",cfg.aap)
    print (cfg)
