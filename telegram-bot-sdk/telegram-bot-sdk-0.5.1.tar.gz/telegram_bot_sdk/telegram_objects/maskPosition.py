class MaskPosition:
    """This class represents the position on faces, where a mask should be placed by default

    :param point: The part of th face relative to which the mask should be placed. One of "forehead", "eyes, "mouth" \
    or "chin"
    :type point: str
    :param x_shift: Shift by X-axis measured in widths of the mask scaled to the face size, from left to right
    :type x_shift: float
    :param y_shift: Sift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom
    :type y_shift: float
    :param scale: Mask scaling coefficient
    :type scale: float
    """
    def __init__(self, *, point=None, x_shift=None, y_shift=None, scale=None):
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale
