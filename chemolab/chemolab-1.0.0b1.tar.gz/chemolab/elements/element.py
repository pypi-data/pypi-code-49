import xml.etree.ElementTree as et
from pathlib import Path

class Element():
    """Creates an instance of an element"""
    def __init__(self, element_data):
        path = str(Path(__file__).parent)+'\\'+str(element_data)
        root = et.parse(path).getroot()
        self.NAME = root.find('chemolab-element').get('nam')
        self.SYMBOL = root.find('chemolab-element').get('sym')
        self.ATOMIC_NUMBER = root.find('chemolab-element').get('atn')
        self.ATOMIC_MASS = root.find('chemolab-element').get('atm')
        self.NATURE = root.find('chemolab-element').get('ntr')
        self.STATE = root.find('chemolab-element').get('stt')
        self.ELECTRONEGATIVITY = root.find('chemolab-element').get('eneg')
        self.OXIDATION_STATES = root.find('chemolab-element').get('oxi')
        self.IONIC_NAME = root.find('chemolab-element').get('ion')
        self.ELECTRONIC_CONFIG = root.find('chemolab-element').get('ecfg')

    def get_info(self):
        """Returns the entire info of the element"""
        return 'Name : '+self.NAME+'\nSymbol : '+self.SYMBOL+'\nAtomic Number : '+self.ATOMIC_NUMBER+'\nAtomic Mass : '+self.ATOMIC_MASS+'\nElectronegativity : '+self.ELECTRONEGATIVITY+'\nOxidation State : '+self.OXIDATION_STATES+'\nElectronic Configuration : '+self.ELECTRONIC_CONFIG+'\nNature : '+self.NATURE+'\nState : '+self.STATE+'\nIon Name : '+self.IONIC_NAME