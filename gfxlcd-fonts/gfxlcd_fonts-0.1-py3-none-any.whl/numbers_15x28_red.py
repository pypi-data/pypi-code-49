"""Font for numbers"""
from .numbers import Numbers as Base


class Numbers(Base):
    """Digital font class"""
    def __init__(self):
        self.resource = self.get_resource("numbers_15x28_red.png")
        self.offsets = {
            0: 0,
            1: 17,
            2: 34,
            3: 51,
            4: 68,
            5: 85,
            6: 102,
            7: 119,
            8: 136,
            9: 153
        }
        self.loaded_resources = {}
        self.size = {'width': 16, 'height': 29}
        self.transparency = ((1, 1, 1), (0, 0, 0))
