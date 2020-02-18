import rawpy
from imageSegmentAnalyzer import image


def load(file, name=None):
    img =rawpy.imread(file)
    if not name:
        name =file

    return image(image=img, name=name)