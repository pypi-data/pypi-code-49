import os

class Config:
    def __init__(self, args):
        self.args = args,
        self.host = args.host
        self.notepath = args.notepath
        self.assets_path = self._get_assets_path()

    def _get_assets_path(self):
        a = os.path.realpath(__file__)
        split = a.split("/")
        split.pop()
        joined = "/".join(split)
        return joined 
