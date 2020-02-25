# coding=utf-8
from __future__ import absolute_import, print_function

import cv2
import imageio

from suanpan import asyncio, path
from suanpan.utils import convert


def read(file, *args, **kwargs):
    img = cv2.imread(file, *args, **kwargs)  # pylint: disable-msg=e1101
    if img is None:
        raise Exception(f"Image read failed: {file}")
    return img


def _save(file, image):
    path.safeMkdirsForFile(file)
    success = cv2.imwrite(file, image)  # pylint: disable-msg=e1101
    if not success:
        path.remove(file)
        raise Exception(f"Image save failed: {file}")
    return file


def _saveflat(file, data):
    image = convert.flatAsImage(data)
    return _save(file, image)


def _savegif(file, data):
    image3D = convert.to3D(data)
    path.safeMkdirsForFile(file)
    imageio.mimsave(file, image3D)
    return file


def save(file, data, flag=None):
    mapping = {None: _save, "flat": _saveflat, "animated": _savegif}
    func = mapping.get(flag)
    if not func:
        raise Exception(f"Unknow flag: {flag}")
    return func(file, data)


def saves(filepathPrefix, images):
    counts = len(images)
    n = len(str(counts))
    iterable = (
        (f"{filepathPrefix}_{str(index).zfill(n)}.png", image)
        for index, image in enumerate(images)
    )
    asyncio.starmap(_save, iterable, thread=True)
    return filepathPrefix


def saveall(filepathPrefix, data):
    image3D = convert.to3D(data)
    layers = len(image3D)
    n = len(str(layers))
    results = [
        asyncio.run(
            _save,
            args=(f"{filepathPrefix}_{str(index).zfill(n)}.png", image),
            thread=True,
        )
        for index, image in enumerate(image3D)
    ]
    results.append(
        asyncio.run(_saveflat, args=(f"{filepathPrefix}.png", image3D), thread=True)
    )
    results.append(
        asyncio.run(_savegif, args=(f"{filepathPrefix}.gif", image3D), thread=True)
    )
    asyncio.wait(results)
    return filepathPrefix


def resize(data, size):
    return cv2.resize(data, size)  # pylint: disable-msg=e1101


# if __name__ == "__main__":
#     import numpy as np
#     from suanpan.utils import image

#     data = np.empty((32, 32, 32, 3), dtype=np.uint8)
#     image.saveall("tmp/test", data)
