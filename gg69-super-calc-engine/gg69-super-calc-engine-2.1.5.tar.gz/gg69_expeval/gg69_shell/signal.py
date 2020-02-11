"""Crutch"""


class Signal(Exception):
    """Signal for testing shell"""
    name: str
    description: str

    def __init__(self, nm, desc):
        self.name = nm
        self.description = desc

    def __repr__(self):
        return f"{self.name} signal: {self.description}"
