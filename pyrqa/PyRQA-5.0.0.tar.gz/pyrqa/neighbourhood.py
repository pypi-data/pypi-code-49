#!/usr/bin/env python

"""
Neighbourhoods
"""

__author__ = "Tobias Rawald"
__copyright__ = "Copyright 2015, 2018, 2019, 2020 The PyRQA project"
__credits__ = ["Tobias Rawald",
               "Mike Sips"]
__license__ = "Apache-2.0"
__maintainer__ = "Tobias Rawald"
__email__ = "pyrqa@gmx.net"
__status__ = "Development"


class Neighbourhood(object):
    """
    Abstract neighbourhood.
    """

    def contains(self,
                 sample):
        """
        Check whether neighbourhood contains sample object.

        :param sample: Sample object, e.g. distance.
        """

        pass

    @property
    def condition(self):
        """
        Condition regarding sample object selection.

        :return: Scalar condition value or tuple of condition values.
        """

        pass


class FixedRadius(Neighbourhood):
    """
    Fixed radius neighbourhood.

    :ivar radius: Radius.
    """

    name = "fixed_radius"

    def __init__(self, radius=1.0):
        self.radius = radius

    def contains(self, distance):
        if distance < self.radius:
            return True

        return False

    @property
    def condition(self):
        return self.radius

    def __str__(self):
        return "%s (Radius: %.2f)" % (self.__class__.__name__,
                                      self.radius)


class RadiusCorridor(Neighbourhood):
    """
    Radius corridor neighbourhood.

    :ivar inner_radius: Inner radius.
    :ivar outer_radius: Outer radius.
    """

    name = "radius_corridor"

    def __init__(self,
                 inner_radius=0.1,
                 outer_radius=1.0):
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius

    def contains(self,
                 distance):
        if self.inner_radius < distance < self.outer_radius:
            return True

        return False

    @property
    def condition(self):
        return (self.inner_radius,
                self.outer_radius)

    def __str__(self):
        return "%s (Inner Radius: %.2f, Outer Radius: %.2f)" % (self.__class__.__name__,
                                                                self.inner_radius,
                                                                self.outer_radius)


class FAN(Neighbourhood):
    """
    Fixed amount of nearest neighbours neighbourhood.

    :ivar k: Number of nearest neighbours.
    :ivar indices: Indices of neighbours.
    :ivar distances: Distance of neighbours.
    """

    name = "fan"

    def __init__(self,
                 k=5):
        self.k = k
        self.indices = []
        self.distances = []

    def contains(self,
                 idx):
        if idx in self.indices:
            return True

        return False

    @property
    def condition(self):
        return self.k

    def __str__(self):
        return "%s (Amount of Nearest Neighbours (k): %d)" % (self.__class__.__name__,
                                                              self.k)
