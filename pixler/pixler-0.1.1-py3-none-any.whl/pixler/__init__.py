import math
from typing import List

MapType = List[List[int]]


BRAILLE_BASE = 0x2800


class OutOfBoundsException(Exception):
    pass


class Pixler:
    char_map: MapType
    _width: int
    _height: int

    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
        width = math.ceil(width / 2)
        height = math.ceil(height / 4)

        self.char_map = [[0 for _ in range(width)] for _ in range(height)]

    @classmethod
    def from_pixels(cls, pixel_map: MapType) -> "Pixler":
        pixler = cls(width=len(pixel_map[0]), height=len(pixel_map))
        pixler.set_pixels(pixel_map)

        return pixler

    def set_pixels(self, pixel_map: MapType) -> None:
        for y, row in enumerate(pixel_map):
            for x, pixel in enumerate(row):
                self.set_pixel(x, y, bool(pixel))

    def set_pixel(self, x: int, y: int, pixel: bool = True) -> None:
        if x >= self._width or y >= self._height:
            raise OutOfBoundsException()

        char_x = math.floor(x / 2)
        char_y = math.floor(y / 4)
        if pixel:
            self.char_map[char_y][char_x] |= self.map_pixel(x, y)
        else:
            self.char_map[char_y][char_x] &= ~self.map_pixel(x, y)

    def get_frame(self) -> str:
        return "\n".join(
            "".join(chr(BRAILLE_BASE + c) for c in row) for row in self.char_map
        )

    @staticmethod
    def map_pixel(x: int, y: int) -> int:
        if y % 4 == 0:
            return 0x8 if x % 2 else 0x1
        if y % 4 == 1:
            return 0x10 if x % 2 else 0x2
        if y % 4 == 2:
            return 0x20 if x % 2 else 0x4
        return 0x80 if x % 2 else 0x40
