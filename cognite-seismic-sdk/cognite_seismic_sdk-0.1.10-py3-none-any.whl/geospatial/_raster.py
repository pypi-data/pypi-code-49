# Copyright 2020 Cognite AS

import numpy as np

try:
    from collections.abc import Mapping  # noqa
    from collections.abc import MutableMapping  # noqa
except ImportError:
    from collections import Mapping  # noqa
    from collections import MutableMapping  # noqa


class Raster:  # (MutableMapping):
    def __init__(
        self,
        id: int = None,
        external_id: str = None,
        name: str = None,
        source: str = None,
        crs: str = None,
        metadata=None,
    ):
        self.id = id
        self.external_id = external_id
        self.name = name
        self.source = source
        self.crs = crs
        self.metadata = metadata
        self.double_vector = {}
        self.boolean_vector = {}
        self.text_vector = {}

    def add_double(self, name: str, vector):
        self.double_vector[name] = np.array(vector, dtype=np.double)

    def add_boolean(self, name: str, vector):
        self.boolean_vector[name] = np.array(vector, dtype=np.bool)

    def add_text(self, name: str, value: str):
        self.text_vector[name] = value

    def __getitem__(self, name: str):
        if name in self.double_vector:
            return self.double_vector[name]

        if name in self.boolean_vector:
            return self.boolean_vector[name]

        if name in self.text_vector:
            return self.text_vector[name]

        return None

    def get(self):
        active = self.__getitem__("Active")
        x = self.__getitem__("X")
        y = self.__getitem__("Y")
        z = self.__getitem__("Z")
        data = np.stack((x, y, z), axis=-1)
        return np.extract(active, data)

    def width(self):
        size = self.metadata["Grid_size"]
        if size is not None:
            dimensions = size.split("x")
            return int(dimensions[0].strip())

        return None

    def height(self):
        size = self.metadata["Grid_size"]
        if size is not None:
            dimensions = size.split("x")
            return int(dimensions[1].strip())

    def grid(self):
        width = self.width()
        height = self.height()
        active = self.__getitem__("Active")
        x = self.__getitem__("X")
        y = self.__getitem__("Y")
        z = self.__getitem__("Z")
        points = np.stack((x, y, z), axis=-1)
        size = min(len(active), len(points))
        active_indx = np.argwhere(active[:size] == True)
        data = np.ndarray(shape=(width, height, 3), dtype=np.double)
        for i in active_indx:
            r = int(i % height)
            c = int((i - r) / height)
            data[c, r] = points[i]

        return data
