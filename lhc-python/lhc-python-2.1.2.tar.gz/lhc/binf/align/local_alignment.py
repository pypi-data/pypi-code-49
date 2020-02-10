from lhc.binf.align.alignment import Alignment


class LocalAlignment(Alignment):

    def set_entry(self, i: int, j: int, score: int, pointer: int):
        super().set_entry(i, j, score, pointer)
        if score > self.get_score():
            self.stop = [i, j]
            self.max = [i, j]
