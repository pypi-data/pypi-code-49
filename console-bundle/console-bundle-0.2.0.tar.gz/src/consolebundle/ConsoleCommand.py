from argparse import Namespace, ArgumentParser
from typing import Optional

class ConsoleCommand:

    def configure(self, argumentParser: ArgumentParser):
        pass

    def getCommand(self) -> str:
        raise Exception('Command name must be defined: {}'.format(self.__class__))

    def getDescription(self) -> Optional[str]:
        return None

    def run(self, inputArgs: Namespace):
        raise Exception('Command main method run() must be defined')
