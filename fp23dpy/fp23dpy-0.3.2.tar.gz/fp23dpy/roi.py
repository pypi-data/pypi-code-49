"""
Module for manipulating rectangle of interest stuff
"""
import numpy as np

class Roi:
    """
    Class for manipulating rectangle of interest stuff
    """
    def __init__(self, l=None):
        if not l is None and not len(l) == 6:
            raise AttributeError("Wrong length of list in constructor")
        self.roi = l

    def full(shape):
        [h, w] = shape
        return Roi([0, h, 0, w, h, w])

    def find_from_mask(mask):
        [h, w] = mask.shape
        r, c = np.where(~mask)
        edge = 10
        minr = max(0, np.min(r) - edge)
        minc = max(0, np.min(c) - edge)
        maxr = min(mask.shape[0], np.max(r) + edge)
        maxc = min(mask.shape[1], np.max(c) + edge)
        return Roi([minr, maxr, minc, maxc, h, w])

    def apply(self, image):
        if self.empty():
            return image
        roi = self.roi
        if len(image.shape) == 2:
            image = image[roi[0]:roi[1], roi[2]:roi[3]]
        else:
            image = image[:, roi[0]:roi[1], roi[2]:roi[3]]
        return image

    def unapply(self, image):
        roi = self.roi
        if self.empty():
            return image

        if len(image.shape) == 2:
            full_image = np.ma.zeros(roi[4:])
            full_image.mask = True
            full_image[roi[0]:roi[1], roi[2]:roi[3]] = image
        else:
            full_shape = [image.shape[0],] + self.full_shape()
            full_image = np.ma.zeros(full_shape)
            full_image.mask = True
            full_image[:, roi[0]:roi[1], roi[2]:roi[3]] = image
        return full_image

    def apply_to_points(self, points):
        """Each row in the points array is point and the columns are x and y"""
        if self.empty():
            return points
        points = np.array(points)
        points[:, 0] -= self.roi[2]
        points[:, 1] -= self.roi[0]
        return points


    def rebase(self, full_roi):
        if self.empty() or full_roi.empty():
            return
        full_roi = full_roi.roi
        new_roi = self.roi.copy()
        new_roi[0] -= full_roi[0]
        new_roi[1] -= full_roi[0]
        new_roi[2] -= full_roi[2]
        new_roi[3] -= full_roi[2]
        new_roi[4] = full_roi[1] - full_roi[0]
        new_roi[5] = full_roi[3] - full_roi[2]
        self.roi = new_roi

    def maximize(self, roi2):
        roi1 = self.roi
        roi2 = roi2.roi
        if roi1 is None and roi2 is None:
            roi = None
        elif roi1 is None:
            roi = roi2
        elif roi2 is None:
            roi = roi1
        else:
            roi = [min(roi1[0], roi2[0]),
                   max(roi1[1], roi2[1]),
                   min(roi1[2], roi2[2]),
                   max(roi1[3], roi2[3]),
                   max(roi1[4], roi2[4]),
                   max(roi1[5], roi2[5])]
        self.roi = roi
        
    def empty(self):
        return self.roi is None

    def full_shape(self):
        if self.empty():
            return None
        else:
            return self.roi[4:]

    def copy(self):
        if self.empty():
            return Roi()
        else:
            return Roi(self.roi.copy())

    def _assert_not_empty(self):
        if self.empty():
            raise AssertionError("Roi must not be empty for this operation")

    def __str__(self):
        return "Roi: " + self.roi.__str__()

    def write(self, path):
        np.savetxt(path, self.roi, fmt='%d')
