from lhc.binf.align.alignment import Alignment


class GlobalAlignment(Alignment):

    def __init__(self, s1: str, s2: str):
        super().__init__(s1, s2)
        for i in range(1, len(s1) + 1):
            self.set_entry(i - 1, -1, -i, Alignment.UP)
        for j in range(1, len(s2) + 1):
            self.set_entry(-1, j - 1, -j, Alignment.LEFT)
