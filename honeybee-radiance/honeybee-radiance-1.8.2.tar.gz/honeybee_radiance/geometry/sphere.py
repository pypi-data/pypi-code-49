"""Radiance Sphere.

http://radsite.lbl.gov/radiance/refer/ray.html#Sphere
"""
from .geometrybase import Geometry
import honeybee.typing as typing


class Sphere(Geometry):
    """Radiance Sphere.

    mod sphere id
    0
    0
    4 xcent ycent zcent radius
    """
    __slots__ = ('_center_pt', '_radius')

    def __init__(self, name, center_pt=None, radius=10, modifier=None,
                 dependencies=None):
        """Radiance Sphere.

        Attributes:
            name: Geometry name as a string. Do not use white space or special
                character.
            center_pt: Sphere center point as (x, y, z) (Default: (0, 0 ,0)).
            radius: Sphere radius as a number (Default: 10).
            modifier: Geometry modifier (Default: "void").
            dependencies: A list of primitives that this primitive depends on. This
                argument is only useful for defining advanced primitives where the
                primitive is defined based on other primitives. (Default: [])

        Usage:

            .. code-block:: python

            sphere = Sphere("test_sphere", (0, 0, 10), 10)
            print(sphere)
        """
        Geometry.__init__(self, name, modifier=modifier, dependencies=dependencies)
        self.center_pt = center_pt or (0, 0, 0)
        self.radius = radius if radius is not None else 10

        self._update_values()

    def _update_values(self):
        """update value dictionaries."""
        self._values[2] = \
            [self.center_pt[0], self.center_pt[1], self.center_pt[2], self.radius]

    @property
    def center_pt(self):
        """Sphere center point as (x, y, z) (Default: (0, 0 ,0))."""
        return self._center_pt
    
    @center_pt.setter
    def center_pt(self, value):
        self._center_pt = tuple(float(v) for v in value)
        assert len(self._center_pt) == 3, \
            'Radiance Sphere center point must have 3 values for (x, y, z).'

    @property
    def radius(self):
        """Sphere radius as a number (Default: 10)."""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = typing.float_positive(value)

    @classmethod
    def from_primitive_dict(cls, primitive_dict):
        """Initialize a Sphere from a primitive dict.

        Args:
            data: A dictionary in the format below.

            .. code-block:: python

            {
                "modifier": "", // primitive modifier (Default: "void")
                "type": "sphere", // primitive type
                "name": "", // primitive name
                "values": [] // values,
                "dependencies": []
            }
        """
        assert 'type' in primitive_dict, 'Input dictionary is missing "type".'
        if primitive_dict['type'] != cls.__name__.lower():
            raise ValueError(
                'Type must be %s not %s.' % (cls.__name__.lower(), primitive_dict['type'])
            )

        modifier, dependencies = cls.filter_dict_input(primitive_dict)
        values = primitive_dict['values'][2]

        cls_ = cls(
            name=primitive_dict['name'],
            center_pt=values[0:3],
            radius=values[3],
            modifier=modifier,
            dependencies=dependencies
        )
        # this might look redundant but it is NOT. see glass for explanation.
        cls_.values = primitive_dict['values']
        return cls_

    @classmethod
    def from_dict(cls, data):
        """Initialize a Sphere from a dictionary.

        Args:
            data: A dictionary in the format below.

            .. code-block:: python

            {
                "type": "sphere", // Geometry type
                "modifier": {} or "void",
                "name": "", // Geometry Name
                "center_pt": {"x": float, "y": float, "z": float},
                "radius": float,
                "dependencies": []
            }
        """
        assert 'type' in data, 'Input dictionary is missing "type".'
        if data['type'] != cls.__name__.lower():
            raise ValueError(
                'Type must be %s not %s.' % (cls.__name__.lower(),
                    data['type'])
            )
        modifier, dependencies = cls.filter_dict_input(data)

        return cls(name=data["name"],
                   center_pt=(data["center_pt"]),
                   radius=data["radius"],
                   modifier=modifier,
                   dependencies=dependencies)

    def to_dict(self):
        """Translate this object to a dictionary."""
        return {
            "modifier": self.modifier.to_dict(),
            "type": self.__class__.__name__.lower(),
            "name": self.name,
            "center_pt": self.center_pt,
            "radius": self.radius,
            'dependencies': [dp.to_dict() for dp in self.dependencies]
        }
