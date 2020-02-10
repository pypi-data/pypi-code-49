from lhc.binf.align.alignment import Alignment


class SemiGlobalAlignment(Alignment):

    def __init__(self, s1: str, s2: str):
        super().__init__(s1, s2)
        if len(s1) < len(s2):
            for i in range(1, len(s1) + 1):
                self.set_entry(i - 1, -1, -i, Alignment.UP)
            for j in range(1, len(s2) + 1):
                self.set_entry(-1, j - 1, 0, Alignment.LEFT)
        else:
            for i in range(1, len(s1) + 1):
                self.set_entry(i - 1, -1, 0, Alignment.UP)
            for j in range(1, len(s2) + 1):
                self.set_entry(-1, j - 1, -j, Alignment.LEFT)

    def set_entry(self, i: int, j: int, score: int, pointer: int):
        if len(self.s1) < len(self.s2) and i == len(self.s1) - 1:
            if score > self.get_score():
                super().set_entry(i, j, score, pointer)
                self.max = [i, j]
            else:
                super().set_entry(i, j, score, Alignment.LEFT)
        elif len(self.s2) < len(self.s1) and j == len(self.s2) - 1:
            if score > self.get_score():
                super().set_entry(i, j, score, pointer)
                self.max = [i, j]
            else:
                super().set_entry(i, j, score, Alignment.UP)
        else:
            super().set_entry(i, j, score, pointer)
