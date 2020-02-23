"""Font for numbers"""
from .numbers import Numbers as Base


class Numbers(Base):
    """Digital font class"""
    def __init__(self):
        self.resource = self.get_resource("numbers_24x42.jpg")
        self.offsets = {
            0: 0,
            1: 24,
            2: 48,
            3: 72,
            4: 96,
            5: 120,
            6: 144,
            7: 168,
            8: 192,
            9: 216
        }
        self.loaded_resources = {}
        self.size = {'width': 24, 'height': 42}
        self.transparency = ((1, 1, 1), (9, 9, 9))
