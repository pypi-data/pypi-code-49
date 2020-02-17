#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains constant definitions for tpDccLib
"""

from __future__ import print_function, division, absolute_import

from tpDcc.libs.python import python

if python.is_python2():
    from aenum import Enum
else:
    from enum import Enum

# =================== PROJECTS
PROJECTS_NAME = 'project.json'
CODE_FOLDER = '__code__'
DATA_FOLDER = '__data__'
BACKUP_FOLDER = '__backup__'
VERSIONS_FOLDER = '__versions__'
MANIFEST_FILE = 'manifest.data'
DATA_FILE = 'data.json'


# =================== TOOLTIPS
DELETE_PROJECT_TOOLTIP = 'Delete selected project'
OPEN_PROJECT_IN_EXPLORER_TOOLTIP = 'Open Project Folder in Explorer'
SET_PROJECT_IMAGE_TOOLTIP = 'Set the Image used for the Project'


# =================== TYPES
class PointerTypes(Enum):
    Shape = 0
    Transform = 1
    Pointer = 2


class ObjectTypes(Enum):
    Generic = 0
    Sphere = 1
    Box = 2
    Cylinder = 3
    Capsule = 4
    Geometry = 5
    Model = 6
    PolyMesh = 7
    NurbsSurface = 8
    Curve = 9
    Light = 10
    Camera = 11
    Group = 12
    Null = 13
    Bone = 14
    Particle = 15
    Network = 16
    Circle = 17
    Biped = 18


class UnitSystem(Enum):
    Inches = 0
    Feet = 1
    Millimeters = 2
    Centimeters = 3
    Meters = 4
    Kilometers = 5
    Yards = 6
    Miles = 7


class MaterialAttributeTypes(Enum):
    Int = 0
    Float = 1
    String = 2
    Path = 3
    Color = 4
    Bool = 5


class MaterialTypes(Enum):
    Standard = 0
