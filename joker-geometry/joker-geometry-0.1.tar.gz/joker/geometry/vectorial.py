#!/usr/bin/env python3
# coding: utf-8

import numpy as np
from joker.geometry.utils import represent


class BaseVector(object):
    __slots__ = ['coordinates']

    def __init__(self, obj):
        if isinstance(obj, BaseVector):
            self.coordinates = obj.coordinates
            return
        self.coordinates = np.array(obj)
        self.coordinates.shape = -1

    @property
    def nonzero(self):
        return np.any(self.coordinates)

    @property
    def dim(self):
        return self.coordinates.ndim

    def __eq__(self, other):
        return np.array_equal(self.coordinates, other.coordinates)

    def __repr__(self):
        return represent(self, list(self.coordinates))

    def __sub__(self, other):
        if isinstance(other, BaseVector):
            return self.__class__(self.coordinates - other.coordinates)
        raise TypeError('unsupported operation')


class Vector(BaseVector):
    __slots__ = []
    # __slots__ = ['coordinates']

    @property
    def length(self):
        return np.linalg.norm(self.coordinates)

    def __add__(self, other):
        if isinstance(other, Vector):
            return self.__class__(self.coordinates + other.coordinates)
        raise TypeError('unsupported operation')

    def __mul__(self, other):
        if np.isscalar(other):
            return self.__class__(self.coordinates * other)
        # TODO: consider if it should be Vector (not BaseVector)
        if isinstance(other, BaseVector):
            return np.dot(self.coordinates, other.coordinates)
        raise TypeError('unsupported operation')

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if np.isscalar(other):
            return self.__class__(self.coordinates / other)
        raise TypeError('unsupported operation')

    @property
    def perpendicular(self):
        n = len(self.coordinates)
        rcoordinates = np.zeros(n)
        for i in range(n):
            if self.coordinates[i]:
                j = (i + 1) % n
                rcoordinates[j] = -self.coordinates[i]
                rcoordinates[i] = self.coordinates[j]
                break
        return self.__class__(rcoordinates)

    def collinear(self, other):
        mat = np.vstack([self.coordinates, other.coordinates])
        return 1 == np.linalg.matrix_rank(mat)


class Point(BaseVector):
    __slots__ = []
    # __slots__ = ['coordinates']

    def __sub__(self, other):
        return Vector(BaseVector.__sub__(self, other))

    def __or__(self, other):
        if isinstance(other, Point):
            return Line(self, self - other)
        raise TypeError('unsupported operation')


class Line(object):
    __slots__ = ['position', 'direction']

    def __init__(self, position: Point, direction: Vector):
        if not direction.nonzero:
            raise ValueError('direction vector of length 0')
        if position.dim != direction.dim:
            raise ValueError('direction vector of wrong dimension')
        self.position = position
        self.direction = direction

    def __repr__(self):
        return represent(self, self.position, self.direction)

    def __contains__(self, point: BaseVector):
        return point == self.position or \
               self.direction.collinear(point - self.position)

    @property
    def dim(self):
        return self.position.dim

    def collinear(self, other):
        return self.direction.collinear(other.direction)

    def distance_to_point(self, point):
        vector = self.position - point
        c = vector.length
        a = self.direction * vector / self.direction.length
        return np.sqrt(c ** 2. - a ** 2.)

    def distance_to_line(self, line):
        if self.dim != line.dim:
            return ValueError('lines of different dimensions')
        if self.dim not in {2, 3}:
            return NotImplementedError('only 2d and 3d line-line dist')

