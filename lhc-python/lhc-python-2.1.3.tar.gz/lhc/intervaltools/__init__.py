from lhc.interval import Interval

def full_difference(this: Interval, that: Interval):
    intervals = []
    left, right = this.difference(that)
