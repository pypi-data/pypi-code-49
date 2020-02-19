from typing import Iterator
from lhc.interval import Interval


def difference(these: Iterator[Interval], those: Iterator[Interval]):
    try:
        that = next(those)
        for this in these:
            while that.stop < this.start:
                that = next(those)

            if this.overlaps(that):
                left, right = this.difference(that)
    except StopIteration:
        pass

    for this in these:
        yield this
