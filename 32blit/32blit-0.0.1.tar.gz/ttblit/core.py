class AssetBuilder():
    def __init__(self, parser):
        self.parser = parser.add_parser(self.command, help=self.help)

    def run(self, args):
        raise NotImplementedError