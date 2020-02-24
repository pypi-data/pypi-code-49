from .interfaceCharacterization import InterfaceCharacterization
from time import sleep


class Characterization(InterfaceCharacterization):
    def compute(self, theDevice):
        sleep(10e-9)
