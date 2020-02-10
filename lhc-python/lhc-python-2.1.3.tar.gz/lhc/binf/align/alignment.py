import numpy


class Alignment:
    END = 0
    DIAG = 1
    LEFT = 2
    UP = 3

    def __init__(self, s1: str, s2: str):
        self.s1 = s1
        self.s2 = s2

        self.scores = numpy.zeros((len(s1) + 1, len(s2) + 1), numpy.int32)
        self.pointers = numpy.zeros((len(s1) + 1, len(s2) + 1), numpy.int32)
        self.stop = [len(s1) - 1, len(s2) - 1]
        self.max = [len(s1) - 1, len(s2) - 1]

    def __str__(self) -> str:
        si = self.s1
        sj = self.s2
        i, j = self.stop

        a = []
        ai = []
        aj = []

        pointer = self.pointers[i, j]
        while pointer != Alignment.END:
            if pointer == Alignment.LEFT:
                ai.append('-')
                aj.append(sj[j])
                a.append(' ')
                j -= 1
            elif pointer == Alignment.UP:
                ai.append(si[i])
                aj.append('-')
                a.append(' ')
                i -= 1
            elif pointer == Alignment.DIAG:
                ai.append(si[i])
                aj.append(sj[j])
                a.append('|' if si[i] == sj[j] else '.')
                i -= 1
                j -= 1
            pointer = self.pointers[i, j]

        return ''.join(reversed(ai)) + '\n' + ''.join(reversed(a)) + '\n' + ''.join(reversed(aj))

    def get_entry(self, i: int, j: int):
        return self.scores[i, j], self.pointers[i, j]

    def set_entry(self, i: int, j: int, score: int, pointer: int):
        self.scores[i, j] = score
        self.pointers[i, j] = pointer

    def get_score(self) -> int:
        return self.scores[self.max[0], self.max[1]]
