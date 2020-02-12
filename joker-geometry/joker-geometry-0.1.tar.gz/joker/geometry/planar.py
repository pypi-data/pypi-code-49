#!/usr/bin/env python3
# coding: utf-8

import numpy as np

from joker.geometry import utils
from joker.geometry import vectorial

_array = utils.array


class BaseVector2D(vectorial.BaseVector):
    __slots__ = []
    # __slots__ = ['coordinates']

    def __init__(self, *args):
        if not args:
            obj = np.zeros(2)
        elif len(args) == 1:
            obj = args[0]
        elif len(args) == 2:
            obj = args
        else:
            raise TypeError('too many arguments')
        vectorial.BaseVector.__init__(self, obj)

    def __repr__(self):
        return utils.represent(self, *self.coordinates)

    @property
    def x(self):
        return self.coordinates[0]

    @property
    def y(self):
        return self.coordinates[1]

    def angle(self, ref=0, degree=False):
        ratio = 180. / np.pi if degree else 1.
        ref /= ratio
        rv = np.arctan2(self.y, self.x) - ref
        rv %= np.pi * 2
        return rv * ratio


class Vector2D(BaseVector2D, vectorial.Vector):
    __slots__ = []


class Point2D(BaseVector2D, vectorial.Point):
    __slots__ = []

    def __or__(self, other):
        if isinstance(other, Point2D):
            return Line2D(self, self - other)
        raise TypeError('unsupported operation')

    def __sub__(self, other):
        return Vector2D(vectorial.BaseVector.__sub__(self, other))


class Line2D(vectorial.Line):
    __slots__ = ['position', 'direction']

    @property
    def normal(self):
        return self.direction.perpendicular

    @property
    def slope(self):
        if self.direction.x == 0:
            return float('inf')
        return self.direction.y / self.direction.x

    def __and__(self, other):
        return self.intersect(other)

    def intersect(self, other):
        if not isinstance(other, Line2D):
            raise TypeError('operation not supported')
        if self.collinear(other):
            return self if self.position in other else None

        npmat = np.array([[self.normal * self.position],
                          [other.normal * other.position]])
        nmat = np.array([[self.normal.x, self.normal.y],
                         [other.normal.x, other.normal.y]])
        prod = np.matmul(np.linalg.inv(nmat), npmat).reshape([-1])
        return Point2D(prod)

    def distance(self, point: Point2D):
        nvec = self.normal
        nvec /= nvec.length
        return nvec * (point - self.position)
