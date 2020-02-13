# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#  HEBI Core python API - Copyright 2018 HEBI Robotics
#  See https://hebi.us/softwarelicense for license details
#
# ------------------------------------------------------------------------------


import ctypes as _ctypes
import numpy as np
from ._internal import math_utils as _math_utils
from ._internal.trajectory import Trajectory as _Trajectory
from ._internal.ffi import ctypes_func_defs as api

from ._internal.ffi.ctypes_utils import byref, pointer_offset, to_double_ptr, cast_to_double_ptr, NULLPTR


def _check_dims_2d(arr, name, waypoints, joints):
  shape = arr.shape
  shape_expected = (joints, waypoints)
  if shape != shape_expected:
    raise ValueError("Invalid dimensionality of {} matrix (expected {}, got {})".format(name, shape_expected, shape))


def create_trajectory(time, position, velocity=None, acceleration=None):
  """
  Creates a smooth trajectory through a set of waypoints (position
  velocity and accelerations defined at particular times). This trajectory
  wrapper object can create multi-dimensional trajectories (i.e., multiple
  joints moving together using the same time reference).

  Deprecation notice: It is deprecated to pass a `str` in as a parameter
  for any of the waypoint dimensions or time.
  This functionality will be removed in a future release.

  :param time: A vector of desired times at which to reach each
               waypoint; this must be defined
               (and not ``None`` or ``nan`` for any element).
  :type time:  list, numpy.ndarray

  :param position: A matrix of waypoint joint positions (in SI units). The
                   number of rows should be equal to the number of joints,
                   and the number of columns equal to the number of waypoints. 
                   Any elements that are ``None`` or ``nan`` will be considered
                   free parameters when solving for a trajectory.
                   Values of ``+/-inf`` are not allowed.
  :type position:  str, list, numpy.ndarray, ctypes.Array
  
  :param velocity: An optional matrix of velocity constraints at the
                   corresponding waypoints; should either be ``None``
                   or matching the size of the positions matrix.
                   Any elements that are ``None`` or ``nan`` will be considered
                   free parameters when solving for a trajectory.
                   Values of ``+/-inf`` are not allowed.
  :type velocity:  NoneType, str, list, numpy.ndarray, ctypes.Array
  
  :param acceleration: An optional matrix of acceleration constraints at
                       the corresponding waypoints; should either be ``None``
                       or matching the size of the positions matrix.
                       Any elements that are ``None`` or ``nan`` will be considered
                       free parameters when solving for a trajectory.
                       Values of ``+/-inf`` are not allowed.
  :type acceleration:  NoneType, str, list, numpy.ndarray, ctypes.Array
  
  :return: The trajectory. This will never be ``None``.
  :rtype: Trajectory

  :raises ValueError: If dimensionality or size of any
                      input parameters are invalid.
  :raises RuntimeError: If trajectory could not be created.
  """
  if time is None:
    raise ValueError("time cannot be None")
  if position is None:
    raise ValueError("position cannot be None")

  # FIXME: Do not use `np.matrix`. However, the logic is painful because `matrix` uses row vectors,
  # and this causes the dimensionality below to be erroneous if refactored naively to use `np.ndarray`.

  time = np.asarray(time, np.float64)
  position = np.asmatrix(position, np.float64)
  joints = position.shape[0]
  waypoints = position.shape[1]

  pointer_stride = waypoints * 8
  shape_checker = lambda arr, name: _check_dims_2d(arr, name, waypoints, joints)

  if time.size != waypoints:
    raise ValueError('length of time vector must be equal to number of waypoints (time:{} != waypoints:{})'.format(time.size, waypoints))

  if not _math_utils.is_finite(time):
    raise ValueError('time vector must have all finite values')

  if velocity is not None:
    velocity = np.asmatrix(velocity, np.float64)
    shape_checker(velocity, 'velocity')
    velocity_c = to_double_ptr(velocity.ravel())
    get_vel_offset = lambda i: pointer_offset(velocity_c, i * pointer_stride)
  else:
    velocity_c = cast_to_double_ptr(NULLPTR)
    get_vel_offset = lambda i: velocity_c

  if acceleration is not None:
    acceleration = np.asmatrix(acceleration, np.float64)
    shape_checker(acceleration, 'acceleration')
    acceleration_c = to_double_ptr(acceleration.ravel())
    get_acc_offset = lambda i: pointer_offset(acceleration_c, i * pointer_stride)
  else:
    acceleration_c = cast_to_double_ptr(NULLPTR)
    get_acc_offset = lambda i: acceleration_c

  time_c = to_double_ptr(time)
  position_c = to_double_ptr(position.ravel())
  trajectories = [None] * joints

  for i in range(0, joints):
    pos_offset = pointer_offset(position_c, i * pointer_stride)
    vel_offset = get_vel_offset(i)
    acc_offset = get_acc_offset(i)
    c_trajectory = api.hebiTrajectoryCreateUnconstrainedQp(waypoints, pos_offset, vel_offset, acc_offset, time_c)

    if not c_trajectory:
      raise RuntimeError('Could not create trajectory')
    trajectories[i] = c_trajectory

  return _Trajectory(trajectories, time.copy(), waypoints)
