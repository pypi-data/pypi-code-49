""" Module concerning some 3D vector manipulations in numpy

OST :Mercy in Darkness, by Two Steps From Hell

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np

SMALL = 1e-12


def renormalize(np_ar_vect):
    """ renormalize a numpy array of vectors,
    considering the last axis """
    result = (np_ar_vect
              / np.expand_dims(np.linalg.norm(np_ar_vect, axis=-1),
                               axis=-1))
    return result


def angle_btw_vects(np_ar_vect1, np_ar_vect2, convert_to_degree=False):
    """ compute the angle in deg btw two UNIT vectors """
    sdot = np.sum(renormalize(np_ar_vect1)
                  * renormalize(np_ar_vect2), axis=-1)

    # Clipping is needed when pscal.max() > 1 : 1.000000000002
    sdot = np.clip(sdot, -1.0, 1.0)
    angles = np.arcsin(sdot)
    if convert_to_degree:
        angles = np.rad2deg(angles)
    return angles


def yz_to_theta(np_ar_vect):
    """ return theta , a radians measure of ange in the yz plane,
    - range -pi/pi
    - 0 on the y+ axis (z=0, y>0)
    spanning -pi to pi
                   0pi=0deg
                  Y
                  ^
                  |
                  |
-0.5pi=-90deg     o------>Z   0.5pi=90deg

    """
    # return np.arctan2(np_ar_vect[:, 2],
    #                   np_ar_vect[:, 1])
    return np.arctan2(np.take(np_ar_vect, 2, axis=-1),
                      np.take(np_ar_vect, 1, axis=-1))


def rtheta2yz(rrr, theta):
    """ return yz fror rtheta ,
    theta in  radians measure of ange in the yz plane,
    - range -pi/pi
    - 0 on the y+ axis (z=0, y>0)
    spanning -pi to pi
 
::

                        0pi=0deg
                      Y
                      ^
                      |
                      |
    -0.5pi=-90deg     o------>Z   0.5pi=90deg

    """
    yyy = rrr * np.cos(theta)
    zzz = rrr * np.sin(theta)
    return yyy, zzz


def rotate_vect_around_x(np_ar_vect, angle_deg):
    """ rotate vector around axis x in degree """

    arr_r = np.hypot(np.take(np_ar_vect, 1, axis=-1),
                     np.take(np_ar_vect, 2, axis=-1))
    arr_theta = (yz_to_theta(np_ar_vect)
                 + np.deg2rad(angle_deg))

    result = np.stack((np.take(np_ar_vect, 0, axis=-1),
                       arr_r * np.cos(arr_theta),
                       arr_r * np.sin(arr_theta)),
                      axis=-1)

    return result

def dilate_vect_around_x(np_ar_vect, angle_deg_ini, angle_deg_targ=360):
    """ dilate vectors around axis x from a specified initial range angle
        to a target range angle.
    Parameters :
    ------------
    np_ar_vect : numpy array of dim (n,3)
    angle_deg_ini : tuple or float
    angle_deg_targ : tuple or float

    Returns :
    ---------
    numpy array of dim (n,3)
    """
    azimuth = yz_to_theta(np_ar_vect) * 180 / np.pi
    dilate_factor = angle_deg_targ / angle_deg_ini

    result = rotate_vect_around_x(np_ar_vect,
                                  azimuth * (dilate_factor - 1))
    return result

def mask_cloud(np_ar_xyz,
               axis,
               support):
    """ mask a cloud of n 3D points in in xyz
    axis among x,y,z,theta,r
    support a 2 value tuple : (0,3), (-12,float(inf))

    x and (0,3) reads as  0 <= x < 3 ( lower bound inclusive)
    z and (-12,float(inf)) reads as  -12 <= z
    theta in degree, cyl. coordinate around x axis
    - range -180,180
    - 0 on the y+ axis (z=0, y>0)
    """

    def true_between(np_arr, low, high):
        """ return a boolean array of the same shape,
        true if value are btw low and high"""
        return (np_arr >= low) * (np_arr < high)

    possible_axes = ["x", "y", "z", "theta", "r"]
    if axis not in possible_axes:
        raise IOError("axis " + axis + "not among possible axes "
                      + ";".join(possible_axes))

    if axis == "x":
        mask = true_between(
            np.take(np_ar_xyz, 0, axis=-1),
            support[0],
            support[1])
    if axis == "y":
        mask = true_between(
            np.take(np_ar_xyz, 1, axis=-1),
            support[0],
            support[1])
    if axis == "z":
        mask = true_between(
            np.take(np_ar_xyz, 2, axis=-1),
            support[0],
            support[1])
    if axis == "r":
        mask = true_between(
            np.hypot(np.take(np_ar_xyz, 1, axis=-1),
                     np.take(np_ar_xyz, 2, axis=-1)),
            support[0],
            support[1])
    if axis == "theta":
        mask = true_between(
            np.rad2deg(yz_to_theta(np_ar_xyz)),
            support[0],
            support[1])
    return mask
