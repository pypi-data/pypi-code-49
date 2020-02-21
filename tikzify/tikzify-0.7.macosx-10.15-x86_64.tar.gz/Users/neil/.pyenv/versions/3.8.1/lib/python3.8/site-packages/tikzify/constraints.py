import itertools as it
from collections.abc import Iterable
from numbers import Real

import numpy as np

__all__ = ['Constraints']


class Constraints:
    """
    This class transforms a set of constraints into two-dimensional positions
    that best satisfy those constraints.
    """

    def __init__(self, labels):
        self.labels = labels
        self.a = np.zeros((0, 2 * len(labels)))
        self.b = np.zeros((0,))

    # Properties --------------------------------------------------------------
    @property
    def num_labels(self):
        return len(self.labels)

    @property
    def num_constraints(self):
        return self.b.shape[0]

    # New methods -------------------------------------------------------------
    def add_constraint(self, a, b):
        self.a = np.vstack((self.a, a.reshape((1, 2 * self.num_labels))))
        self.b = np.hstack((self.b, b))

    def blank(self):
        return np.zeros((2 * self.num_labels,))

    def index(self, coord, label):
        return self.labels.index(label) + (
            self.num_labels if coord == 'y' else 0)

    def set_value(self, coord, c, value=0.0):
        a = self.blank()
        a[self.index(coord, c)] = 1.0
        self.add_constraint(a, value)

    def set_delta(self, coord, *args, delta=0.0):
        if len(args) <= 1:
            raise ValueError
        if isinstance(delta, Real):
            deltas = it.repeat(delta)
        else:
            deltas = delta
        for x, y, this_delta in zip(args, args[1:], deltas):
            a = self.blank()
            a[self.index(coord, x)] = 1.0
            a[self.index(coord, y)] = -1.0
            self.add_constraint(a, this_delta)

    def set_deltas(self, *args, delta=(0.0, 0.0)):
        if isinstance(delta, tuple):
            deltas = [delta for _ in range(len(args))]
        else:
            deltas = delta
        self.set_delta_x(*args, delta_x=[x for x, y in deltas])
        self.set_delta_y(*args, delta_y=[y for x, y in deltas])

    def set_x(self, c, x):
        self.set_value('x', c, x)

    def set_y(self, c, y):
        self.set_value('y', c, y)

    def set_delta_x(self, *args, delta_x=0.0):
        """
        Stack each of the args horizontally, spaced by delta_x, from left to
        right.
        """
        if isinstance(delta_x, Iterable):
            delta_x = reversed(delta_x)
        self.set_delta('x', *reversed(args), delta=delta_x)

    def set_delta_y(self, *args, delta_y=0.0):
        """
        Stack each of the args vertically, spaced by delta_y, from top to
        bottom.
        """
        self.set_delta('y', *args, delta=delta_y)

    def set_location(self, c, location):
        "Set c.x, c.y = location."
        if len(location) != 2:
            raise ValueError
        self.set_x(c, location[0])
        self.set_y(c, location[1])

    def set_between(self, coord, *items, ratios=None):
        """
        Space n items with spacing according to (n-1) ratios.
        E.g., ratios=[0, 1] puts item[1] at item[0]
        fraction = (d-c)/(d-c + (e-d)) => (d-c) = (e-c) * fraction
        """
        if ratios is None:
            ratios = [1] * (len(items) - 1)
        for c, d, e, r1, r2 in zip(items, items[1:], items[2:],
                                   ratios, ratios[1:]):
            fraction = r1 / (r1 + r2)
            a = self.blank()
            if c is not None:
                a[self.index(coord, c)] += fraction - 1.0
            if d is not None:
                a[self.index(coord, d)] += 1.0
            if e is not None:
                a[self.index(coord, e)] -= fraction
            self.add_constraint(a, 0.0)

    def set_x_between(self, *items, ratios=None):
        self.set_between('x', *items, ratios=ratios)

    def set_y_between(self, *items, ratios=None):
        self.set_between('y', *items, ratios=ratios)

    def set_deltas_equal(self, c, d, e, f):
        self.set_delta_x_equal(c, d, e, f)
        self.set_delta_y_equal(c, d, e, f)

    def set_delta_equal(self, coord, c, d, e, f):
        "Set c - d = e - f."
        a = self.blank()
        if c is not None:
            a[self.index(coord, c)] += 1.0
        if d is not None:
            a[self.index(coord, d)] -= 1.0
        if e is not None:
            a[self.index(coord, e)] -= 1.0
        if f is not None:
            a[self.index(coord, f)] += 1.0
        self.add_constraint(a, 0.0)

    def set_delta_x_equal(self, c, d, e, f):
        self.set_delta_equal('x', c, d, e, f)

    def set_delta_y_equal(self, c, d, e, f):
        self.set_delta_equal('y', c, d, e, f)

    def set_slope(self, slope, *args):
        assert len(args) >= 2
        for c, d in zip(args, args[1:]):
            a = self.blank()
            a[self.index('x', c)] += slope
            a[self.index('x', d)] -= slope
            a[self.index('y', c)] -= 1.0
            a[self.index('y', d)] += 1.0
            self.add_constraint(a, 0.0)

    def solve(self, decimals=6):
        solution, _, rank, _ = np.linalg.lstsq(self.a, self.b, rcond=None)
        # solution = np.linalg.solve(self.a, self.b)
        if rank != 2 * self.num_labels:
            raise Constraints.InsufficientConstraints(
                f"Only {rank} constraints provided for a problem that needs "
                + f"{2 * self.num_labels}")
        solution = np.around(solution, decimals=decimals)
        self.solution = np.where(np.signbit(solution) & (solution == 0.0),
                                 -solution,
                                 solution)

    def solved(self, c):
        return self.solution[[self.index('x', c), self.index('y', c)]]

    # Exceptions --------------------------------------------------------------
    class InsufficientConstraints(Exception):
        pass
