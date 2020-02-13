import numpy as np
import ctypes

from .wrappers import UnmanagedObject, UnmanagedSharedObject
from . import _marshalling
from ._marshalling import GroupNumberedFloatFieldContainer, MutableGroupNumberedFloatFieldContainer, GroupMessageIoFieldBankContainer, MutableGroupMessageIoFieldBankContainer, GroupMessageIoFieldContainer, MutableGroupMessageIoFieldContainer, GroupMessageLEDFieldContainer, MutableGroupMessageLEDFieldContainer
from . import ctypes_func_defs as api
from . import ctypes_defs
from . import enums
from hebi._internal.type_utils import create_string_buffer_compat as create_str


_command_metadata = ctypes_defs.HebiCommandMetadata()
_feedback_metadata = ctypes_defs.HebiFeedbackMetadata()
_info_metadata = ctypes_defs.HebiInfoMetadata()
api.hebiCommandGetMetadata(ctypes.byref(_command_metadata))
api.hebiFeedbackGetMetadata(ctypes.byref(_feedback_metadata))
api.hebiInfoGetMetadata(ctypes.byref(_info_metadata))


class Command(UnmanagedObject):
  """
  Used to represent a Command object.
  Do not instantiate directly - use only through a GroupCommand instance.
  """

  __slots__ = ["_ref"]

  def __init__(self, internal, ref):
    """
    This is invoked internally. Do not use directly.
    """
    super(Command, self).__init__(internal)
    self._ref = ref

  @property
  def velocity(self):
    """
    Velocity of the module output (post-spring).
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocity)

  @velocity.setter
  def velocity(self, value):
    """
    Setter for velocity
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocity, value)

  @property
  def effort(self):
    """
    Effort at the module output; units vary (e.g., N * m for rotational joints and N for linear stages).
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffort)

  @effort.setter
  def effort(self, value):
    """
    Setter for effort
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffort, value)

  @property
  def position_kp(self):
    """
    Proportional PID gain for position
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatPositionKp)

  @position_kp.setter
  def position_kp(self, value):
    """
    Setter for position_kp
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatPositionKp, value)

  @property
  def position_ki(self):
    """
    Integral PID gain for position
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatPositionKi)

  @position_ki.setter
  def position_ki(self, value):
    """
    Setter for position_ki
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatPositionKi, value)

  @property
  def position_kd(self):
    """
    Derivative PID gain for position
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatPositionKd)

  @position_kd.setter
  def position_kd(self, value):
    """
    Setter for position_kd
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatPositionKd, value)

  @property
  def position_feed_forward(self):
    """
    Feed forward term for position (this term is multiplied by the target and added to the output).
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatPositionFeedForward)

  @position_feed_forward.setter
  def position_feed_forward(self, value):
    """
    Setter for position_feed_forward
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatPositionFeedForward, value)

  @property
  def position_dead_zone(self):
    """
    Error values within +/- this value from zero are treated as zero (in terms of computed proportional output, input to numerical derivative, and accumulated integral error).
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatPositionDeadZone)

  @position_dead_zone.setter
  def position_dead_zone(self, value):
    """
    Setter for position_dead_zone
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatPositionDeadZone, value)

  @property
  def position_i_clamp(self):
    """
    Maximum allowed value for the output of the integral component of the PID loop; the integrated error is not allowed to exceed value that will generate this number.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatPositionIClamp)

  @position_i_clamp.setter
  def position_i_clamp(self, value):
    """
    Setter for position_i_clamp
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatPositionIClamp, value)

  @property
  def position_punch(self):
    """
    Constant offset to the position PID output outside of the deadzone; it is added when the error is positive and subtracted when it is negative.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatPositionPunch)

  @position_punch.setter
  def position_punch(self, value):
    """
    Setter for position_punch
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatPositionPunch, value)

  @property
  def position_min_target(self):
    """
    Minimum allowed value for input to the PID controller
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatPositionMinTarget)

  @position_min_target.setter
  def position_min_target(self, value):
    """
    Setter for position_min_target
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatPositionMinTarget, value)

  @property
  def position_max_target(self):
    """
    Maximum allowed value for input to the PID controller
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatPositionMaxTarget)

  @position_max_target.setter
  def position_max_target(self, value):
    """
    Setter for position_max_target
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatPositionMaxTarget, value)

  @property
  def position_target_lowpass(self):
    """
    A simple lowpass filter applied to the target set point; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatPositionTargetLowpass)

  @position_target_lowpass.setter
  def position_target_lowpass(self, value):
    """
    Setter for position_target_lowpass
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatPositionTargetLowpass, value)

  @property
  def position_min_output(self):
    """
    Output from the PID controller is limited to a minimum of this value.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatPositionMinOutput)

  @position_min_output.setter
  def position_min_output(self, value):
    """
    Setter for position_min_output
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatPositionMinOutput, value)

  @property
  def position_max_output(self):
    """
    Output from the PID controller is limited to a maximum of this value.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatPositionMaxOutput)

  @position_max_output.setter
  def position_max_output(self, value):
    """
    Setter for position_max_output
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatPositionMaxOutput, value)

  @property
  def position_output_lowpass(self):
    """
    A simple lowpass filter applied to the controller output; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatPositionOutputLowpass)

  @position_output_lowpass.setter
  def position_output_lowpass(self, value):
    """
    Setter for position_output_lowpass
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatPositionOutputLowpass, value)

  @property
  def velocity_kp(self):
    """
    Proportional PID gain for velocity
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocityKp)

  @velocity_kp.setter
  def velocity_kp(self, value):
    """
    Setter for velocity_kp
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocityKp, value)

  @property
  def velocity_ki(self):
    """
    Integral PID gain for velocity
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocityKi)

  @velocity_ki.setter
  def velocity_ki(self, value):
    """
    Setter for velocity_ki
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocityKi, value)

  @property
  def velocity_kd(self):
    """
    Derivative PID gain for velocity
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocityKd)

  @velocity_kd.setter
  def velocity_kd(self, value):
    """
    Setter for velocity_kd
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocityKd, value)

  @property
  def velocity_feed_forward(self):
    """
    Feed forward term for velocity (this term is multiplied by the target and added to the output).
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocityFeedForward)

  @velocity_feed_forward.setter
  def velocity_feed_forward(self, value):
    """
    Setter for velocity_feed_forward
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocityFeedForward, value)

  @property
  def velocity_dead_zone(self):
    """
    Error values within +/- this value from zero are treated as zero (in terms of computed proportional output, input to numerical derivative, and accumulated integral error).
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocityDeadZone)

  @velocity_dead_zone.setter
  def velocity_dead_zone(self, value):
    """
    Setter for velocity_dead_zone
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocityDeadZone, value)

  @property
  def velocity_i_clamp(self):
    """
    Maximum allowed value for the output of the integral component of the PID loop; the integrated error is not allowed to exceed value that will generate this number.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocityIClamp)

  @velocity_i_clamp.setter
  def velocity_i_clamp(self, value):
    """
    Setter for velocity_i_clamp
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocityIClamp, value)

  @property
  def velocity_punch(self):
    """
    Constant offset to the velocity PID output outside of the deadzone; it is added when the error is positive and subtracted when it is negative.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocityPunch)

  @velocity_punch.setter
  def velocity_punch(self, value):
    """
    Setter for velocity_punch
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocityPunch, value)

  @property
  def velocity_min_target(self):
    """
    Minimum allowed value for input to the PID controller
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocityMinTarget)

  @velocity_min_target.setter
  def velocity_min_target(self, value):
    """
    Setter for velocity_min_target
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocityMinTarget, value)

  @property
  def velocity_max_target(self):
    """
    Maximum allowed value for input to the PID controller
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocityMaxTarget)

  @velocity_max_target.setter
  def velocity_max_target(self, value):
    """
    Setter for velocity_max_target
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocityMaxTarget, value)

  @property
  def velocity_target_lowpass(self):
    """
    A simple lowpass filter applied to the target set point; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocityTargetLowpass)

  @velocity_target_lowpass.setter
  def velocity_target_lowpass(self, value):
    """
    Setter for velocity_target_lowpass
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocityTargetLowpass, value)

  @property
  def velocity_min_output(self):
    """
    Output from the PID controller is limited to a minimum of this value.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocityMinOutput)

  @velocity_min_output.setter
  def velocity_min_output(self, value):
    """
    Setter for velocity_min_output
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocityMinOutput, value)

  @property
  def velocity_max_output(self):
    """
    Output from the PID controller is limited to a maximum of this value.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocityMaxOutput)

  @velocity_max_output.setter
  def velocity_max_output(self, value):
    """
    Setter for velocity_max_output
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocityMaxOutput, value)

  @property
  def velocity_output_lowpass(self):
    """
    A simple lowpass filter applied to the controller output; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocityOutputLowpass)

  @velocity_output_lowpass.setter
  def velocity_output_lowpass(self, value):
    """
    Setter for velocity_output_lowpass
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocityOutputLowpass, value)

  @property
  def effort_kp(self):
    """
    Proportional PID gain for effort
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffortKp)

  @effort_kp.setter
  def effort_kp(self, value):
    """
    Setter for effort_kp
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffortKp, value)

  @property
  def effort_ki(self):
    """
    Integral PID gain for effort
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffortKi)

  @effort_ki.setter
  def effort_ki(self, value):
    """
    Setter for effort_ki
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffortKi, value)

  @property
  def effort_kd(self):
    """
    Derivative PID gain for effort
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffortKd)

  @effort_kd.setter
  def effort_kd(self, value):
    """
    Setter for effort_kd
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffortKd, value)

  @property
  def effort_feed_forward(self):
    """
    Feed forward term for effort (this term is multiplied by the target and added to the output).
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffortFeedForward)

  @effort_feed_forward.setter
  def effort_feed_forward(self, value):
    """
    Setter for effort_feed_forward
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffortFeedForward, value)

  @property
  def effort_dead_zone(self):
    """
    Error values within +/- this value from zero are treated as zero (in terms of computed proportional output, input to numerical derivative, and accumulated integral error).
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffortDeadZone)

  @effort_dead_zone.setter
  def effort_dead_zone(self, value):
    """
    Setter for effort_dead_zone
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffortDeadZone, value)

  @property
  def effort_i_clamp(self):
    """
    Maximum allowed value for the output of the integral component of the PID loop; the integrated error is not allowed to exceed value that will generate this number.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffortIClamp)

  @effort_i_clamp.setter
  def effort_i_clamp(self, value):
    """
    Setter for effort_i_clamp
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffortIClamp, value)

  @property
  def effort_punch(self):
    """
    Constant offset to the effort PID output outside of the deadzone; it is added when the error is positive and subtracted when it is negative.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffortPunch)

  @effort_punch.setter
  def effort_punch(self, value):
    """
    Setter for effort_punch
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffortPunch, value)

  @property
  def effort_min_target(self):
    """
    Minimum allowed value for input to the PID controller
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffortMinTarget)

  @effort_min_target.setter
  def effort_min_target(self, value):
    """
    Setter for effort_min_target
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffortMinTarget, value)

  @property
  def effort_max_target(self):
    """
    Maximum allowed value for input to the PID controller
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffortMaxTarget)

  @effort_max_target.setter
  def effort_max_target(self, value):
    """
    Setter for effort_max_target
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffortMaxTarget, value)

  @property
  def effort_target_lowpass(self):
    """
    A simple lowpass filter applied to the target set point; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffortTargetLowpass)

  @effort_target_lowpass.setter
  def effort_target_lowpass(self, value):
    """
    Setter for effort_target_lowpass
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffortTargetLowpass, value)

  @property
  def effort_min_output(self):
    """
    Output from the PID controller is limited to a minimum of this value.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffortMinOutput)

  @effort_min_output.setter
  def effort_min_output(self, value):
    """
    Setter for effort_min_output
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffortMinOutput, value)

  @property
  def effort_max_output(self):
    """
    Output from the PID controller is limited to a maximum of this value.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffortMaxOutput)

  @effort_max_output.setter
  def effort_max_output(self, value):
    """
    Setter for effort_max_output
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffortMaxOutput, value)

  @property
  def effort_output_lowpass(self):
    """
    A simple lowpass filter applied to the controller output; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffortOutputLowpass)

  @effort_output_lowpass.setter
  def effort_output_lowpass(self, value):
    """
    Setter for effort_output_lowpass
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffortOutputLowpass, value)

  @property
  def spring_constant(self):
    """
    The spring constant of the module.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatSpringConstant)

  @spring_constant.setter
  def spring_constant(self, value):
    """
    Setter for spring_constant
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatSpringConstant, value)

  @property
  def reference_position(self):
    """
    Set the internal encoder reference offset so that the current position matches the given reference command
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatReferencePosition)

  @reference_position.setter
  def reference_position(self, value):
    """
    Setter for reference_position
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatReferencePosition, value)

  @property
  def reference_effort(self):
    """
    Set the internal effort reference offset so that the current effort matches the given reference command
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatReferenceEffort)

  @reference_effort.setter
  def reference_effort(self, value):
    """
    Setter for reference_effort
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatReferenceEffort, value)

  @property
  def velocity_limit_min(self):
    """
    The firmware safety limit for the minimum allowed velocity.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocityLimitMin)

  @velocity_limit_min.setter
  def velocity_limit_min(self, value):
    """
    Setter for velocity_limit_min
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocityLimitMin, value)

  @property
  def velocity_limit_max(self):
    """
    The firmware safety limit for the maximum allowed velocity.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatVelocityLimitMax)

  @velocity_limit_max.setter
  def velocity_limit_max(self, value):
    """
    Setter for velocity_limit_max
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatVelocityLimitMax, value)

  @property
  def effort_limit_min(self):
    """
    The firmware safety limit for the minimum allowed effort.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffortLimitMin)

  @effort_limit_min.setter
  def effort_limit_min(self, value):
    """
    Setter for effort_limit_min
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffortLimitMin, value)

  @property
  def effort_limit_max(self):
    """
    The firmware safety limit for the maximum allowed effort.
    """
    return _marshalling.get_command_float(self._ref, enums.CommandFloatEffortLimitMax)

  @effort_limit_max.setter
  def effort_limit_max(self, value):
    """
    Setter for effort_limit_max
    """
    _marshalling.set_command_float(self._ref, enums.CommandFloatEffortLimitMax, value)

  @property
  def position(self):
    """
    Position of the module output (post-spring).
    """
    return _marshalling.get_command_highresangle(self._ref, enums.CommandHighResAnglePosition)

  @position.setter
  def position(self, value):
    """
    Setter for position
    """
    _marshalling.set_command_highresangle(self._ref, enums.CommandHighResAnglePosition, value)

  @property
  def position_limit_min(self):
    """
    The firmware safety limit for the minimum allowed position.
    """
    return _marshalling.get_command_highresangle(self._ref, enums.CommandHighResAnglePositionLimitMin)

  @position_limit_min.setter
  def position_limit_min(self, value):
    """
    Setter for position_limit_min
    """
    _marshalling.set_command_highresangle(self._ref, enums.CommandHighResAnglePositionLimitMin, value)

  @property
  def position_limit_max(self):
    """
    The firmware safety limit for the maximum allowed position.
    """
    return _marshalling.get_command_highresangle(self._ref, enums.CommandHighResAnglePositionLimitMax)

  @position_limit_max.setter
  def position_limit_max(self, value):
    """
    Setter for position_limit_max
    """
    _marshalling.set_command_highresangle(self._ref, enums.CommandHighResAnglePositionLimitMax, value)

  @property
  def position_d_on_error(self):
    """
    Controls whether the Kd term uses the "derivative of error" or "derivative of measurement." When the setpoints have step inputs or are noisy, setting this to @c false can eliminate corresponding spikes or noise in the output.
    """
    return _marshalling.get_command_bool(self._ref, enums.CommandBoolPositionDOnError)

  @position_d_on_error.setter
  def position_d_on_error(self, value):
    """
    Setter for position_d_on_error
    """
    _marshalling.set_command_bool(self._ref, enums.CommandBoolPositionDOnError, value)

  @property
  def velocity_d_on_error(self):
    """
    Controls whether the Kd term uses the "derivative of error" or "derivative of measurement." When the setpoints have step inputs or are noisy, setting this to @c false can eliminate corresponding spikes or noise in the output.
    """
    return _marshalling.get_command_bool(self._ref, enums.CommandBoolVelocityDOnError)

  @velocity_d_on_error.setter
  def velocity_d_on_error(self, value):
    """
    Setter for velocity_d_on_error
    """
    _marshalling.set_command_bool(self._ref, enums.CommandBoolVelocityDOnError, value)

  @property
  def effort_d_on_error(self):
    """
    Controls whether the Kd term uses the "derivative of error" or "derivative of measurement." When the setpoints have step inputs or are noisy, setting this to @c false can eliminate corresponding spikes or noise in the output.
    """
    return _marshalling.get_command_bool(self._ref, enums.CommandBoolEffortDOnError)

  @effort_d_on_error.setter
  def effort_d_on_error(self, value):
    """
    Setter for effort_d_on_error
    """
    _marshalling.set_command_bool(self._ref, enums.CommandBoolEffortDOnError, value)

  @property
  def accel_includes_gravity(self):
    """
    Whether to include acceleration due to gravity in acceleration feedback.
    """
    return _marshalling.get_command_bool(self._ref, enums.CommandBoolAccelIncludesGravity)

  @accel_includes_gravity.setter
  def accel_includes_gravity(self, value):
    """
    Setter for accel_includes_gravity
    """
    _marshalling.set_command_bool(self._ref, enums.CommandBoolAccelIncludesGravity, value)

  @property
  def save_current_settings(self):
    """
    Indicates if the module should save the current values of all of its settings.
    """
    return _marshalling.get_command_flag(self._ref, enums.CommandFlagSaveCurrentSettings)

  @save_current_settings.setter
  def save_current_settings(self, value):
    """
    Setter for save_current_settings
    """
    _marshalling.set_command_flag(self._ref, enums.CommandFlagSaveCurrentSettings, value)

  @property
  def reset(self):
    """
    Restart the module.
    """
    return _marshalling.get_command_flag(self._ref, enums.CommandFlagReset)

  @reset.setter
  def reset(self, value):
    """
    Setter for reset
    """
    _marshalling.set_command_flag(self._ref, enums.CommandFlagReset, value)

  @property
  def boot(self):
    """
    Boot the module from bootloader into application.
    """
    return _marshalling.get_command_flag(self._ref, enums.CommandFlagBoot)

  @boot.setter
  def boot(self, value):
    """
    Setter for boot
    """
    _marshalling.set_command_flag(self._ref, enums.CommandFlagBoot, value)

  @property
  def stop_boot(self):
    """
    Stop the module from automatically booting into application.
    """
    return _marshalling.get_command_flag(self._ref, enums.CommandFlagStopBoot)

  @stop_boot.setter
  def stop_boot(self, value):
    """
    Setter for stop_boot
    """
    _marshalling.set_command_flag(self._ref, enums.CommandFlagStopBoot, value)

  @property
  def clear_log(self):
    """
    Clears the log message on the module.
    """
    return _marshalling.get_command_flag(self._ref, enums.CommandFlagClearLog)

  @clear_log.setter
  def clear_log(self, value):
    """
    Setter for clear_log
    """
    _marshalling.set_command_flag(self._ref, enums.CommandFlagClearLog, value)

  @property
  def control_strategy(self):
    """
    How the position, velocity, and effort PID loops are connected in order to control motor PWM.
    """
    return _marshalling.get_command_enum(self._ref, enums.CommandEnumControlStrategy)

  @control_strategy.setter
  def control_strategy(self, value):
    """
    Setter for control_strategy

    Note that the following (case sensitive) strings can also be used:
      * "Off"
      * "DirectPWM"
      * "Strategy2"
      * "Strategy3"
      * "Strategy4"
    """
    value = GroupCommand._map_enum_strings_if_needed(value, GroupCommandBase._enum_control_strategy_str_mappings)
    _marshalling.set_command_enum(self._ref, enums.CommandEnumControlStrategy, value)

  @property
  def mstop_strategy(self):
    """
    The motion stop strategy for the actuator
    """
    return _marshalling.get_command_enum(self._ref, enums.CommandEnumMstopStrategy)

  @mstop_strategy.setter
  def mstop_strategy(self, value):
    """
    Setter for mstop_strategy

    Note that the following (case sensitive) strings can also be used:
      * "Disabled"
      * "MotorOff"
      * "HoldPosition"
    """
    value = GroupCommand._map_enum_strings_if_needed(value, GroupCommandBase._enum_mstop_strategy_str_mappings)
    _marshalling.set_command_enum(self._ref, enums.CommandEnumMstopStrategy, value)

  @property
  def min_position_limit_strategy(self):
    """
    The position limit strategy (at the minimum position) for the actuator
    """
    return _marshalling.get_command_enum(self._ref, enums.CommandEnumMinPositionLimitStrategy)

  @min_position_limit_strategy.setter
  def min_position_limit_strategy(self, value):
    """
    Setter for min_position_limit_strategy

    Note that the following (case sensitive) strings can also be used:
      * "HoldPosition"
      * "DampedSpring"
      * "MotorOff"
      * "Disabled"
    """
    value = GroupCommand._map_enum_strings_if_needed(value, GroupCommandBase._enum_min_position_limit_strategy_str_mappings)
    _marshalling.set_command_enum(self._ref, enums.CommandEnumMinPositionLimitStrategy, value)

  @property
  def max_position_limit_strategy(self):
    """
    The position limit strategy (at the maximum position) for the actuator
    """
    return _marshalling.get_command_enum(self._ref, enums.CommandEnumMaxPositionLimitStrategy)

  @max_position_limit_strategy.setter
  def max_position_limit_strategy(self, value):
    """
    Setter for max_position_limit_strategy

    Note that the following (case sensitive) strings can also be used:
      * "HoldPosition"
      * "DampedSpring"
      * "MotorOff"
      * "Disabled"
    """
    value = GroupCommand._map_enum_strings_if_needed(value, GroupCommandBase._enum_max_position_limit_strategy_str_mappings)
    _marshalling.set_command_enum(self._ref, enums.CommandEnumMaxPositionLimitStrategy, value)

  @property
  def name(self):
    """
    The name for this module. The string must be null-terminated and less than 21 characters.
    """
    return _marshalling.get_command_string(self, enums.CommandStringName)

  @name.setter
  def name(self, value):
    """
    Setter for name
    """
    _marshalling.set_command_string(self, enums.CommandStringName, value)

  @property
  def family(self):
    """
    The family for this module. The string must be null-terminated and less than 21 characters.
    """
    return _marshalling.get_command_string(self, enums.CommandStringFamily)

  @family.setter
  def family(self, value):
    """
    Setter for family
    """
    _marshalling.set_command_string(self, enums.CommandStringFamily, value)

  @property
  def append_log(self):
    """
    Appends to the current log message on the module.
    """
    return _marshalling.get_command_string(self, enums.CommandStringAppendLog)

  @append_log.setter
  def append_log(self, value):
    """
    Setter for append_log
    """
    _marshalling.set_command_string(self, enums.CommandStringAppendLog, value)


class Feedback(UnmanagedObject):
  """
  Used to represent a Feedback object.
  Do not instantiate directly - use only through a GroupFeedback instance.
  """

  __slots__ = ["_ref"]

  def __init__(self, internal, ref):
    """
    This is invoked internally. Do not use directly.
    """
    super(Feedback, self).__init__(internal)
    self._ref = ref

  @property
  def board_temperature(self):
    """
    Ambient temperature inside the module (measured at the IMU chip)
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatBoardTemperature)

  @property
  def processor_temperature(self):
    """
    Temperature of the processor chip.
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatProcessorTemperature)

  @property
  def voltage(self):
    """
    Bus voltage at which the module is running.
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatVoltage)

  @property
  def velocity(self):
    """
    Velocity of the module output (post-spring).
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatVelocity)

  @property
  def effort(self):
    """
    Effort at the module output; units vary (e.g., N * m for rotational joints and N for linear stages).
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatEffort)

  @property
  def velocity_command(self):
    """
    Commanded velocity of the module output (post-spring)
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatVelocityCommand)

  @property
  def effort_command(self):
    """
    Commanded effort at the module output; units vary (e.g., N * m for rotational joints and N for linear stages).
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatEffortCommand)

  @property
  def deflection(self):
    """
    Difference between the pre-spring and post-spring output position.
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatDeflection)

  @property
  def deflection_velocity(self):
    """
    Velocity of the difference between the pre-spring and post-spring output position.
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatDeflectionVelocity)

  @property
  def motor_velocity(self):
    """
    The velocity of the motor shaft.
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatMotorVelocity)

  @property
  def motor_current(self):
    """
    Current supplied to the motor.
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatMotorCurrent)

  @property
  def motor_sensor_temperature(self):
    """
    The temperature from a sensor near the motor housing.
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatMotorSensorTemperature)

  @property
  def motor_winding_current(self):
    """
    The estimated current in the motor windings.
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatMotorWindingCurrent)

  @property
  def motor_winding_temperature(self):
    """
    The estimated temperature of the motor windings.
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatMotorWindingTemperature)

  @property
  def motor_housing_temperature(self):
    """
    The estimated temperature of the motor housing.
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatMotorHousingTemperature)

  @property
  def battery_level(self):
    """
    Charge level of the device's battery (in percent).
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatBatteryLevel)

  @property
  def pwm_command(self):
    """
    Commanded PWM signal sent to the motor; final output of PID controllers.
    """
    return _marshalling.get_feedback_float(self._ref, enums.FeedbackFloatPwmCommand)

  @property
  def position(self):
    """
    Position of the module output (post-spring).
    """
    return _marshalling.get_feedback_highresangle(self._ref, enums.FeedbackHighResAnglePosition)

  @property
  def position_command(self):
    """
    Commanded position of the module output (post-spring).
    """
    return _marshalling.get_feedback_highresangle(self._ref, enums.FeedbackHighResAnglePositionCommand)

  @property
  def motor_position(self):
    """
    The position of an actuator's internal motor before the gear reduction.
    """
    return _marshalling.get_feedback_highresangle(self._ref, enums.FeedbackHighResAngleMotorPosition)

  @property
  def sequence_number(self):
    """
    Sequence number going to module (local)
    """
    return _marshalling.get_feedback_uint64(self._ref, enums.FeedbackUInt64SequenceNumber)

  @property
  def receive_time(self):
    """
    Timestamp of when message was received from module (local)
    """
    return _marshalling.get_feedback_uint64(self._ref, enums.FeedbackUInt64ReceiveTime)

  @property
  def transmit_time(self):
    """
    Timestamp of when message was transmitted to module (local)
    """
    return _marshalling.get_feedback_uint64(self._ref, enums.FeedbackUInt64TransmitTime)

  @property
  def hardware_receive_time(self):
    """
    Timestamp of when message was received by module (remote)
    """
    return _marshalling.get_feedback_uint64(self._ref, enums.FeedbackUInt64HardwareReceiveTime)

  @property
  def hardware_transmit_time(self):
    """
    Timestamp of when message was transmitted from module (remote)
    """
    return _marshalling.get_feedback_uint64(self._ref, enums.FeedbackUInt64HardwareTransmitTime)

  @property
  def sender_id(self):
    """
    Unique ID of the module transmitting this feedback
    """
    return _marshalling.get_feedback_uint64(self._ref, enums.FeedbackUInt64SenderId)

  @property
  def accelerometer(self):
    """
    Accelerometer data
    """
    return _marshalling.get_feedback_vector3f(self._ref, enums.FeedbackVector3fAccelerometer)

  @property
  def gyro(self):
    """
    Gyro data
    """
    return _marshalling.get_feedback_vector3f(self._ref, enums.FeedbackVector3fGyro)

  @property
  def ar_position(self):
    """
    A device's position in the world as calculated from an augmented reality framework
    """
    return _marshalling.get_feedback_vector3f(self._ref, enums.FeedbackVector3fArPosition)

  @property
  def orientation(self):
    """
    A filtered estimate of the orientation of the module.
    """
    return _marshalling.get_feedback_quaternionf(self._ref, enums.FeedbackQuaternionfOrientation)

  @property
  def ar_orientation(self):
    """
    A device's orientation in the world as calculated from an augmented reality framework
    """
    return _marshalling.get_feedback_quaternionf(self._ref, enums.FeedbackQuaternionfArOrientation)

  @property
  def temperature_state(self):
    """
    Describes how the temperature inside the module is limiting the output of the motor
    """
    return _marshalling.get_feedback_enum(self._ref, enums.FeedbackEnumTemperatureState)

  @property
  def mstop_state(self):
    """
    Current status of the MStop
    """
    return _marshalling.get_feedback_enum(self._ref, enums.FeedbackEnumMstopState)

  @property
  def position_limit_state(self):
    """
    Software-controlled bounds on the allowable position of the module; user settable
    """
    return _marshalling.get_feedback_enum(self._ref, enums.FeedbackEnumPositionLimitState)

  @property
  def velocity_limit_state(self):
    """
    Software-controlled bounds on the allowable velocity of the module
    """
    return _marshalling.get_feedback_enum(self._ref, enums.FeedbackEnumVelocityLimitState)

  @property
  def effort_limit_state(self):
    """
    Software-controlled bounds on the allowable effort of the module
    """
    return _marshalling.get_feedback_enum(self._ref, enums.FeedbackEnumEffortLimitState)

  @property
  def command_lifetime_state(self):
    """
    The state of the command lifetime safety controller, with respect to the current group
    """
    return _marshalling.get_feedback_enum(self._ref, enums.FeedbackEnumCommandLifetimeState)

  @property
  def ar_quality(self):
    """
    The status of the augmented reality tracking, if using an AR enabled device. See HebiArQuality for values.
    """
    return _marshalling.get_feedback_enum(self._ref, enums.FeedbackEnumArQuality)


class Info(UnmanagedObject):
  """
  Used to represent a Info object.
  Do not instantiate directly - use only through a GroupInfo instance.
  """

  __slots__ = ["_ref"]

  def __init__(self, internal, ref):
    """
    This is invoked internally. Do not use directly.
    """
    super(Info, self).__init__(internal)
    self._ref = ref

  @property
  def position_kp(self):
    """
    Proportional PID gain for position
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatPositionKp)

  @property
  def position_ki(self):
    """
    Integral PID gain for position
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatPositionKi)

  @property
  def position_kd(self):
    """
    Derivative PID gain for position
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatPositionKd)

  @property
  def position_feed_forward(self):
    """
    Feed forward term for position (this term is multiplied by the target and added to the output).
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatPositionFeedForward)

  @property
  def position_dead_zone(self):
    """
    Error values within +/- this value from zero are treated as zero (in terms of computed proportional output, input to numerical derivative, and accumulated integral error).
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatPositionDeadZone)

  @property
  def position_i_clamp(self):
    """
    Maximum allowed value for the output of the integral component of the PID loop; the integrated error is not allowed to exceed value that will generate this number.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatPositionIClamp)

  @property
  def position_punch(self):
    """
    Constant offset to the position PID output outside of the deadzone; it is added when the error is positive and subtracted when it is negative.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatPositionPunch)

  @property
  def position_min_target(self):
    """
    Minimum allowed value for input to the PID controller
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatPositionMinTarget)

  @property
  def position_max_target(self):
    """
    Maximum allowed value for input to the PID controller
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatPositionMaxTarget)

  @property
  def position_target_lowpass(self):
    """
    A simple lowpass filter applied to the target set point; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatPositionTargetLowpass)

  @property
  def position_min_output(self):
    """
    Output from the PID controller is limited to a minimum of this value.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatPositionMinOutput)

  @property
  def position_max_output(self):
    """
    Output from the PID controller is limited to a maximum of this value.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatPositionMaxOutput)

  @property
  def position_output_lowpass(self):
    """
    A simple lowpass filter applied to the controller output; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatPositionOutputLowpass)

  @property
  def velocity_kp(self):
    """
    Proportional PID gain for velocity
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatVelocityKp)

  @property
  def velocity_ki(self):
    """
    Integral PID gain for velocity
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatVelocityKi)

  @property
  def velocity_kd(self):
    """
    Derivative PID gain for velocity
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatVelocityKd)

  @property
  def velocity_feed_forward(self):
    """
    Feed forward term for velocity (this term is multiplied by the target and added to the output).
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatVelocityFeedForward)

  @property
  def velocity_dead_zone(self):
    """
    Error values within +/- this value from zero are treated as zero (in terms of computed proportional output, input to numerical derivative, and accumulated integral error).
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatVelocityDeadZone)

  @property
  def velocity_i_clamp(self):
    """
    Maximum allowed value for the output of the integral component of the PID loop; the integrated error is not allowed to exceed value that will generate this number.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatVelocityIClamp)

  @property
  def velocity_punch(self):
    """
    Constant offset to the velocity PID output outside of the deadzone; it is added when the error is positive and subtracted when it is negative.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatVelocityPunch)

  @property
  def velocity_min_target(self):
    """
    Minimum allowed value for input to the PID controller
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatVelocityMinTarget)

  @property
  def velocity_max_target(self):
    """
    Maximum allowed value for input to the PID controller
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatVelocityMaxTarget)

  @property
  def velocity_target_lowpass(self):
    """
    A simple lowpass filter applied to the target set point; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatVelocityTargetLowpass)

  @property
  def velocity_min_output(self):
    """
    Output from the PID controller is limited to a minimum of this value.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatVelocityMinOutput)

  @property
  def velocity_max_output(self):
    """
    Output from the PID controller is limited to a maximum of this value.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatVelocityMaxOutput)

  @property
  def velocity_output_lowpass(self):
    """
    A simple lowpass filter applied to the controller output; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatVelocityOutputLowpass)

  @property
  def effort_kp(self):
    """
    Proportional PID gain for effort
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatEffortKp)

  @property
  def effort_ki(self):
    """
    Integral PID gain for effort
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatEffortKi)

  @property
  def effort_kd(self):
    """
    Derivative PID gain for effort
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatEffortKd)

  @property
  def effort_feed_forward(self):
    """
    Feed forward term for effort (this term is multiplied by the target and added to the output).
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatEffortFeedForward)

  @property
  def effort_dead_zone(self):
    """
    Error values within +/- this value from zero are treated as zero (in terms of computed proportional output, input to numerical derivative, and accumulated integral error).
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatEffortDeadZone)

  @property
  def effort_i_clamp(self):
    """
    Maximum allowed value for the output of the integral component of the PID loop; the integrated error is not allowed to exceed value that will generate this number.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatEffortIClamp)

  @property
  def effort_punch(self):
    """
    Constant offset to the effort PID output outside of the deadzone; it is added when the error is positive and subtracted when it is negative.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatEffortPunch)

  @property
  def effort_min_target(self):
    """
    Minimum allowed value for input to the PID controller
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatEffortMinTarget)

  @property
  def effort_max_target(self):
    """
    Maximum allowed value for input to the PID controller
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatEffortMaxTarget)

  @property
  def effort_target_lowpass(self):
    """
    A simple lowpass filter applied to the target set point; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatEffortTargetLowpass)

  @property
  def effort_min_output(self):
    """
    Output from the PID controller is limited to a minimum of this value.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatEffortMinOutput)

  @property
  def effort_max_output(self):
    """
    Output from the PID controller is limited to a maximum of this value.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatEffortMaxOutput)

  @property
  def effort_output_lowpass(self):
    """
    A simple lowpass filter applied to the controller output; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatEffortOutputLowpass)

  @property
  def spring_constant(self):
    """
    The spring constant of the module.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatSpringConstant)

  @property
  def velocity_limit_min(self):
    """
    The firmware safety limit for the minimum allowed velocity.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatVelocityLimitMin)

  @property
  def velocity_limit_max(self):
    """
    The firmware safety limit for the maximum allowed velocity.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatVelocityLimitMax)

  @property
  def effort_limit_min(self):
    """
    The firmware safety limit for the minimum allowed effort.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatEffortLimitMin)

  @property
  def effort_limit_max(self):
    """
    The firmware safety limit for the maximum allowed effort.
    """
    return _marshalling.get_info_float(self._ref, enums.InfoFloatEffortLimitMax)

  @property
  def position_limit_min(self):
    """
    The firmware safety limit for the minimum allowed position.
    """
    return _marshalling.get_info_highresangle(self._ref, enums.InfoHighResAnglePositionLimitMin)

  @property
  def position_limit_max(self):
    """
    The firmware safety limit for the maximum allowed position.
    """
    return _marshalling.get_info_highresangle(self._ref, enums.InfoHighResAnglePositionLimitMax)

  @property
  def position_d_on_error(self):
    """
    Controls whether the Kd term uses the "derivative of error" or "derivative of measurement." When the setpoints have step inputs or are noisy, setting this to @c false can eliminate corresponding spikes or noise in the output.
    """
    return _marshalling.get_info_bool(self._ref, enums.InfoBoolPositionDOnError)

  @property
  def velocity_d_on_error(self):
    """
    Controls whether the Kd term uses the "derivative of error" or "derivative of measurement." When the setpoints have step inputs or are noisy, setting this to @c false can eliminate corresponding spikes or noise in the output.
    """
    return _marshalling.get_info_bool(self._ref, enums.InfoBoolVelocityDOnError)

  @property
  def effort_d_on_error(self):
    """
    Controls whether the Kd term uses the "derivative of error" or "derivative of measurement." When the setpoints have step inputs or are noisy, setting this to @c false can eliminate corresponding spikes or noise in the output.
    """
    return _marshalling.get_info_bool(self._ref, enums.InfoBoolEffortDOnError)

  @property
  def accel_includes_gravity(self):
    """
    Whether to include acceleration due to gravity in acceleration feedback.
    """
    return _marshalling.get_info_bool(self._ref, enums.InfoBoolAccelIncludesGravity)

  @property
  def save_current_settings(self):
    """
    Indicates if the module should save the current values of all of its settings.
    """
    return _marshalling.get_info_flag(self._ref, enums.InfoFlagSaveCurrentSettings)

  @property
  def control_strategy(self):
    """
    How the position, velocity, and effort PID loops are connected in order to control motor PWM.
    """
    return _marshalling.get_info_enum(self._ref, enums.InfoEnumControlStrategy)

  @property
  def calibration_state(self):
    """
    The calibration state of the module
    """
    return _marshalling.get_info_enum(self._ref, enums.InfoEnumCalibrationState)

  @property
  def mstop_strategy(self):
    """
    The motion stop strategy for the actuator
    """
    return _marshalling.get_info_enum(self._ref, enums.InfoEnumMstopStrategy)

  @property
  def min_position_limit_strategy(self):
    """
    The position limit strategy (at the minimum position) for the actuator
    """
    return _marshalling.get_info_enum(self._ref, enums.InfoEnumMinPositionLimitStrategy)

  @property
  def max_position_limit_strategy(self):
    """
    The position limit strategy (at the maximum position) for the actuator
    """
    return _marshalling.get_info_enum(self._ref, enums.InfoEnumMaxPositionLimitStrategy)

  @property
  def name(self):
    """
    The name for this module. The string must be null-terminated and less than 21 characters.
    """
    return _marshalling.get_info_string(self, enums.InfoStringName)

  @property
  def family(self):
    """
    The family for this module. The string must be null-terminated and less than 21 characters.
    """
    return _marshalling.get_info_string(self, enums.InfoStringFamily)

  @property
  def serial(self):
    """
    Gets the serial number for this module (e.g., X5-0001).
    """
    return _marshalling.get_info_string(self, enums.InfoStringSerial)


class GroupCommandBase(UnmanagedSharedObject):
  """
  Base class for command. Do not use directly.
  """

  __slots__ = ['_command_refs', '_number_of_modules', '__weakref__', '_io', '_debug', '_led']

  def _initialize(self, number_of_modules):
    self._number_of_modules = number_of_modules
    from hebi._internal.ffi.ctypes_defs import HebiCommandRef
    self._command_refs = (HebiCommandRef * number_of_modules)()

    from hebi._internal.ffi._marshalling import create_io_int_group_getter, create_io_float_group_getter, create_io_group_has
    getter_int = create_io_int_group_getter(self._command_refs, api.hwCommandGetIoPinInt)
    getter_float = create_io_float_group_getter(self._command_refs, api.hwCommandGetIoPinFloat)
    has_int = create_io_group_has(self._command_refs, api.hwCommandHasIoPinInt)
    has_float = create_io_group_has(self._command_refs, api.hwCommandHasIoPinFloat)
    from hebi._internal.ffi._marshalling import create_io_int_group_setter, create_io_float_group_setter
    setter_int = create_io_int_group_setter(self._command_refs, api.hwCommandSetIoPinInt)
    setter_float = create_io_float_group_setter(self._command_refs, api.hwCommandSetIoPinFloat)
    self._io = MutableGroupMessageIoFieldContainer(self, getter_int, getter_float, has_int, has_float, setter_int, setter_float, enums.CommandIoBankField)
    from hebi._internal.ffi._marshalling import create_numbered_float_group_getter, create_numbered_float_group_has, create_numbered_float_group_setter
    getter = create_numbered_float_group_getter(self._command_refs, enums.CommandNumberedFloatDebug, api.hwCommandGetNumberedFloat)
    has = create_numbered_float_group_has(self._command_refs, enums.CommandNumberedFloatDebug, api.hwCommandHasField, _command_metadata)
    setter = create_numbered_float_group_setter(self._command_refs, enums.CommandNumberedFloatDebug, api.hwCommandSetNumberedFloat)
    self._debug = MutableGroupNumberedFloatFieldContainer(self, enums.CommandNumberedFloatDebug, getter, has, setter)
    from hebi._internal.ffi._marshalling import create_led_group_getter, create_led_group_setter
    getter = create_led_group_getter(self._command_refs, enums.CommandLedLed, api.hwCommandGetLed)
    setter = create_led_group_setter(self._command_refs, enums.CommandLedLed, api.hwCommandSetLed)
    self._led = MutableGroupMessageLEDFieldContainer(self, getter, setter, enums.CommandLedLed)

  def __init__(self, internal=None, on_delete=None, existing=None, isdummy=False):
    super(GroupCommandBase, self).__init__(internal, on_delete, existing, isdummy)

  @property
  def refs(self):
    return (ctypes_defs.HebiCommandRef * self._number_of_modules)(*self._command_refs)

  @property
  def size(self):
    """
    The number of modules in this group message.
    """
    return self._number_of_modules

  @property
  def velocity(self):
    """
    Velocity of the module output (post-spring).
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocity)

  @velocity.setter
  def velocity(self, value):
    """
    Setter for velocity
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocity, value)

  @property
  def effort(self):
    """
    Effort at the module output; units vary (e.g., N * m for rotational joints and N for linear stages).
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffort)

  @effort.setter
  def effort(self, value):
    """
    Setter for effort
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffort, value)

  @property
  def position_kp(self):
    """
    Proportional PID gain for position
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatPositionKp)

  @position_kp.setter
  def position_kp(self, value):
    """
    Setter for position_kp
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatPositionKp, value)

  @property
  def position_ki(self):
    """
    Integral PID gain for position
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatPositionKi)

  @position_ki.setter
  def position_ki(self, value):
    """
    Setter for position_ki
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatPositionKi, value)

  @property
  def position_kd(self):
    """
    Derivative PID gain for position
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatPositionKd)

  @position_kd.setter
  def position_kd(self, value):
    """
    Setter for position_kd
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatPositionKd, value)

  @property
  def position_feed_forward(self):
    """
    Feed forward term for position (this term is multiplied by the target and added to the output).
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatPositionFeedForward)

  @position_feed_forward.setter
  def position_feed_forward(self, value):
    """
    Setter for position_feed_forward
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatPositionFeedForward, value)

  @property
  def position_dead_zone(self):
    """
    Error values within +/- this value from zero are treated as zero (in terms of computed proportional output, input to numerical derivative, and accumulated integral error).
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatPositionDeadZone)

  @position_dead_zone.setter
  def position_dead_zone(self, value):
    """
    Setter for position_dead_zone
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatPositionDeadZone, value)

  @property
  def position_i_clamp(self):
    """
    Maximum allowed value for the output of the integral component of the PID loop; the integrated error is not allowed to exceed value that will generate this number.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatPositionIClamp)

  @position_i_clamp.setter
  def position_i_clamp(self, value):
    """
    Setter for position_i_clamp
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatPositionIClamp, value)

  @property
  def position_punch(self):
    """
    Constant offset to the position PID output outside of the deadzone; it is added when the error is positive and subtracted when it is negative.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatPositionPunch)

  @position_punch.setter
  def position_punch(self, value):
    """
    Setter for position_punch
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatPositionPunch, value)

  @property
  def position_min_target(self):
    """
    Minimum allowed value for input to the PID controller
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatPositionMinTarget)

  @position_min_target.setter
  def position_min_target(self, value):
    """
    Setter for position_min_target
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatPositionMinTarget, value)

  @property
  def position_max_target(self):
    """
    Maximum allowed value for input to the PID controller
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatPositionMaxTarget)

  @position_max_target.setter
  def position_max_target(self, value):
    """
    Setter for position_max_target
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatPositionMaxTarget, value)

  @property
  def position_target_lowpass(self):
    """
    A simple lowpass filter applied to the target set point; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatPositionTargetLowpass)

  @position_target_lowpass.setter
  def position_target_lowpass(self, value):
    """
    Setter for position_target_lowpass
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatPositionTargetLowpass, value)

  @property
  def position_min_output(self):
    """
    Output from the PID controller is limited to a minimum of this value.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatPositionMinOutput)

  @position_min_output.setter
  def position_min_output(self, value):
    """
    Setter for position_min_output
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatPositionMinOutput, value)

  @property
  def position_max_output(self):
    """
    Output from the PID controller is limited to a maximum of this value.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatPositionMaxOutput)

  @position_max_output.setter
  def position_max_output(self, value):
    """
    Setter for position_max_output
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatPositionMaxOutput, value)

  @property
  def position_output_lowpass(self):
    """
    A simple lowpass filter applied to the controller output; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatPositionOutputLowpass)

  @position_output_lowpass.setter
  def position_output_lowpass(self, value):
    """
    Setter for position_output_lowpass
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatPositionOutputLowpass, value)

  @property
  def velocity_kp(self):
    """
    Proportional PID gain for velocity
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocityKp)

  @velocity_kp.setter
  def velocity_kp(self, value):
    """
    Setter for velocity_kp
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocityKp, value)

  @property
  def velocity_ki(self):
    """
    Integral PID gain for velocity
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocityKi)

  @velocity_ki.setter
  def velocity_ki(self, value):
    """
    Setter for velocity_ki
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocityKi, value)

  @property
  def velocity_kd(self):
    """
    Derivative PID gain for velocity
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocityKd)

  @velocity_kd.setter
  def velocity_kd(self, value):
    """
    Setter for velocity_kd
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocityKd, value)

  @property
  def velocity_feed_forward(self):
    """
    Feed forward term for velocity (this term is multiplied by the target and added to the output).
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocityFeedForward)

  @velocity_feed_forward.setter
  def velocity_feed_forward(self, value):
    """
    Setter for velocity_feed_forward
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocityFeedForward, value)

  @property
  def velocity_dead_zone(self):
    """
    Error values within +/- this value from zero are treated as zero (in terms of computed proportional output, input to numerical derivative, and accumulated integral error).
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocityDeadZone)

  @velocity_dead_zone.setter
  def velocity_dead_zone(self, value):
    """
    Setter for velocity_dead_zone
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocityDeadZone, value)

  @property
  def velocity_i_clamp(self):
    """
    Maximum allowed value for the output of the integral component of the PID loop; the integrated error is not allowed to exceed value that will generate this number.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocityIClamp)

  @velocity_i_clamp.setter
  def velocity_i_clamp(self, value):
    """
    Setter for velocity_i_clamp
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocityIClamp, value)

  @property
  def velocity_punch(self):
    """
    Constant offset to the velocity PID output outside of the deadzone; it is added when the error is positive and subtracted when it is negative.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocityPunch)

  @velocity_punch.setter
  def velocity_punch(self, value):
    """
    Setter for velocity_punch
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocityPunch, value)

  @property
  def velocity_min_target(self):
    """
    Minimum allowed value for input to the PID controller
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocityMinTarget)

  @velocity_min_target.setter
  def velocity_min_target(self, value):
    """
    Setter for velocity_min_target
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocityMinTarget, value)

  @property
  def velocity_max_target(self):
    """
    Maximum allowed value for input to the PID controller
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocityMaxTarget)

  @velocity_max_target.setter
  def velocity_max_target(self, value):
    """
    Setter for velocity_max_target
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocityMaxTarget, value)

  @property
  def velocity_target_lowpass(self):
    """
    A simple lowpass filter applied to the target set point; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocityTargetLowpass)

  @velocity_target_lowpass.setter
  def velocity_target_lowpass(self, value):
    """
    Setter for velocity_target_lowpass
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocityTargetLowpass, value)

  @property
  def velocity_min_output(self):
    """
    Output from the PID controller is limited to a minimum of this value.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocityMinOutput)

  @velocity_min_output.setter
  def velocity_min_output(self, value):
    """
    Setter for velocity_min_output
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocityMinOutput, value)

  @property
  def velocity_max_output(self):
    """
    Output from the PID controller is limited to a maximum of this value.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocityMaxOutput)

  @velocity_max_output.setter
  def velocity_max_output(self, value):
    """
    Setter for velocity_max_output
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocityMaxOutput, value)

  @property
  def velocity_output_lowpass(self):
    """
    A simple lowpass filter applied to the controller output; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocityOutputLowpass)

  @velocity_output_lowpass.setter
  def velocity_output_lowpass(self, value):
    """
    Setter for velocity_output_lowpass
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocityOutputLowpass, value)

  @property
  def effort_kp(self):
    """
    Proportional PID gain for effort
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffortKp)

  @effort_kp.setter
  def effort_kp(self, value):
    """
    Setter for effort_kp
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffortKp, value)

  @property
  def effort_ki(self):
    """
    Integral PID gain for effort
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffortKi)

  @effort_ki.setter
  def effort_ki(self, value):
    """
    Setter for effort_ki
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffortKi, value)

  @property
  def effort_kd(self):
    """
    Derivative PID gain for effort
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffortKd)

  @effort_kd.setter
  def effort_kd(self, value):
    """
    Setter for effort_kd
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffortKd, value)

  @property
  def effort_feed_forward(self):
    """
    Feed forward term for effort (this term is multiplied by the target and added to the output).
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffortFeedForward)

  @effort_feed_forward.setter
  def effort_feed_forward(self, value):
    """
    Setter for effort_feed_forward
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffortFeedForward, value)

  @property
  def effort_dead_zone(self):
    """
    Error values within +/- this value from zero are treated as zero (in terms of computed proportional output, input to numerical derivative, and accumulated integral error).
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffortDeadZone)

  @effort_dead_zone.setter
  def effort_dead_zone(self, value):
    """
    Setter for effort_dead_zone
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffortDeadZone, value)

  @property
  def effort_i_clamp(self):
    """
    Maximum allowed value for the output of the integral component of the PID loop; the integrated error is not allowed to exceed value that will generate this number.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffortIClamp)

  @effort_i_clamp.setter
  def effort_i_clamp(self, value):
    """
    Setter for effort_i_clamp
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffortIClamp, value)

  @property
  def effort_punch(self):
    """
    Constant offset to the effort PID output outside of the deadzone; it is added when the error is positive and subtracted when it is negative.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffortPunch)

  @effort_punch.setter
  def effort_punch(self, value):
    """
    Setter for effort_punch
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffortPunch, value)

  @property
  def effort_min_target(self):
    """
    Minimum allowed value for input to the PID controller
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffortMinTarget)

  @effort_min_target.setter
  def effort_min_target(self, value):
    """
    Setter for effort_min_target
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffortMinTarget, value)

  @property
  def effort_max_target(self):
    """
    Maximum allowed value for input to the PID controller
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffortMaxTarget)

  @effort_max_target.setter
  def effort_max_target(self, value):
    """
    Setter for effort_max_target
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffortMaxTarget, value)

  @property
  def effort_target_lowpass(self):
    """
    A simple lowpass filter applied to the target set point; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffortTargetLowpass)

  @effort_target_lowpass.setter
  def effort_target_lowpass(self, value):
    """
    Setter for effort_target_lowpass
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffortTargetLowpass, value)

  @property
  def effort_min_output(self):
    """
    Output from the PID controller is limited to a minimum of this value.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffortMinOutput)

  @effort_min_output.setter
  def effort_min_output(self, value):
    """
    Setter for effort_min_output
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffortMinOutput, value)

  @property
  def effort_max_output(self):
    """
    Output from the PID controller is limited to a maximum of this value.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffortMaxOutput)

  @effort_max_output.setter
  def effort_max_output(self, value):
    """
    Setter for effort_max_output
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffortMaxOutput, value)

  @property
  def effort_output_lowpass(self):
    """
    A simple lowpass filter applied to the controller output; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffortOutputLowpass)

  @effort_output_lowpass.setter
  def effort_output_lowpass(self, value):
    """
    Setter for effort_output_lowpass
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffortOutputLowpass, value)

  @property
  def spring_constant(self):
    """
    The spring constant of the module.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatSpringConstant)

  @spring_constant.setter
  def spring_constant(self, value):
    """
    Setter for spring_constant
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatSpringConstant, value)

  @property
  def reference_position(self):
    """
    Set the internal encoder reference offset so that the current position matches the given reference command
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatReferencePosition)

  @reference_position.setter
  def reference_position(self, value):
    """
    Setter for reference_position
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatReferencePosition, value)

  @property
  def reference_effort(self):
    """
    Set the internal effort reference offset so that the current effort matches the given reference command
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatReferenceEffort)

  @reference_effort.setter
  def reference_effort(self, value):
    """
    Setter for reference_effort
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatReferenceEffort, value)

  @property
  def velocity_limit_min(self):
    """
    The firmware safety limit for the minimum allowed velocity.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocityLimitMin)

  @velocity_limit_min.setter
  def velocity_limit_min(self, value):
    """
    Setter for velocity_limit_min
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocityLimitMin, value)

  @property
  def velocity_limit_max(self):
    """
    The firmware safety limit for the maximum allowed velocity.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatVelocityLimitMax)

  @velocity_limit_max.setter
  def velocity_limit_max(self, value):
    """
    Setter for velocity_limit_max
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatVelocityLimitMax, value)

  @property
  def effort_limit_min(self):
    """
    The firmware safety limit for the minimum allowed effort.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffortLimitMin)

  @effort_limit_min.setter
  def effort_limit_min(self, value):
    """
    Setter for effort_limit_min
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffortLimitMin, value)

  @property
  def effort_limit_max(self):
    """
    The firmware safety limit for the maximum allowed effort.
    """
    return _marshalling.get_group_command_float(self._command_refs, enums.CommandFloatEffortLimitMax)

  @effort_limit_max.setter
  def effort_limit_max(self, value):
    """
    Setter for effort_limit_max
    """
    _marshalling.set_group_command_float(self._command_refs, enums.CommandFloatEffortLimitMax, value)

  @property
  def position(self):
    """
    Position of the module output (post-spring).
    """
    return _marshalling.get_group_command_highresangle(self._command_refs, enums.CommandHighResAnglePosition)

  @position.setter
  def position(self, value):
    """
    Setter for position
    """
    _marshalling.set_group_command_highresangle(self._command_refs, enums.CommandHighResAnglePosition, value)

  @property
  def position_limit_min(self):
    """
    The firmware safety limit for the minimum allowed position.
    """
    return _marshalling.get_group_command_highresangle(self._command_refs, enums.CommandHighResAnglePositionLimitMin)

  @position_limit_min.setter
  def position_limit_min(self, value):
    """
    Setter for position_limit_min
    """
    _marshalling.set_group_command_highresangle(self._command_refs, enums.CommandHighResAnglePositionLimitMin, value)

  @property
  def position_limit_max(self):
    """
    The firmware safety limit for the maximum allowed position.
    """
    return _marshalling.get_group_command_highresangle(self._command_refs, enums.CommandHighResAnglePositionLimitMax)

  @position_limit_max.setter
  def position_limit_max(self, value):
    """
    Setter for position_limit_max
    """
    _marshalling.set_group_command_highresangle(self._command_refs, enums.CommandHighResAnglePositionLimitMax, value)

  @property
  def debug(self):
    """
    Values for internal debug functions (channel 1-9 available).
    """
    return self._debug

  @property
  def position_d_on_error(self):
    """
    Controls whether the Kd term uses the "derivative of error" or "derivative of measurement." When the setpoints have step inputs or are noisy, setting this to @c false can eliminate corresponding spikes or noise in the output.
    """
    return _marshalling.get_group_command_bool(self._command_refs, enums.CommandBoolPositionDOnError)

  @position_d_on_error.setter
  def position_d_on_error(self, value):
    """
    Setter for position_d_on_error
    """
    _marshalling.set_group_command_bool(self._command_refs, enums.CommandBoolPositionDOnError, value)

  @property
  def velocity_d_on_error(self):
    """
    Controls whether the Kd term uses the "derivative of error" or "derivative of measurement." When the setpoints have step inputs or are noisy, setting this to @c false can eliminate corresponding spikes or noise in the output.
    """
    return _marshalling.get_group_command_bool(self._command_refs, enums.CommandBoolVelocityDOnError)

  @velocity_d_on_error.setter
  def velocity_d_on_error(self, value):
    """
    Setter for velocity_d_on_error
    """
    _marshalling.set_group_command_bool(self._command_refs, enums.CommandBoolVelocityDOnError, value)

  @property
  def effort_d_on_error(self):
    """
    Controls whether the Kd term uses the "derivative of error" or "derivative of measurement." When the setpoints have step inputs or are noisy, setting this to @c false can eliminate corresponding spikes or noise in the output.
    """
    return _marshalling.get_group_command_bool(self._command_refs, enums.CommandBoolEffortDOnError)

  @effort_d_on_error.setter
  def effort_d_on_error(self, value):
    """
    Setter for effort_d_on_error
    """
    _marshalling.set_group_command_bool(self._command_refs, enums.CommandBoolEffortDOnError, value)

  @property
  def accel_includes_gravity(self):
    """
    Whether to include acceleration due to gravity in acceleration feedback.
    """
    return _marshalling.get_group_command_bool(self._command_refs, enums.CommandBoolAccelIncludesGravity)

  @accel_includes_gravity.setter
  def accel_includes_gravity(self, value):
    """
    Setter for accel_includes_gravity
    """
    _marshalling.set_group_command_bool(self._command_refs, enums.CommandBoolAccelIncludesGravity, value)

  @property
  def name(self):
    """
    The name for this module. The string must be null-terminated and less than 21 characters.
    """
    return _marshalling.get_group_command_string(self, enums.CommandStringName, [None] * self._number_of_modules)

  @name.setter
  def name(self, value):
    """
    Setter for name
    """
    _marshalling.set_group_command_string(self, enums.CommandStringName, value)

  @property
  def family(self):
    """
    The family for this module. The string must be null-terminated and less than 21 characters.
    """
    return _marshalling.get_group_command_string(self, enums.CommandStringFamily, [None] * self._number_of_modules)

  @family.setter
  def family(self, value):
    """
    Setter for family
    """
    _marshalling.set_group_command_string(self, enums.CommandStringFamily, value)

  @property
  def append_log(self):
    """
    Appends to the current log message on the module.
    """
    return _marshalling.get_group_command_string(self, enums.CommandStringAppendLog, [None] * self._number_of_modules)

  @append_log.setter
  def append_log(self, value):
    """
    Setter for append_log
    """
    _marshalling.set_group_command_string(self, enums.CommandStringAppendLog, value)

  @property
  def save_current_settings(self):
    """
    Indicates if the module should save the current values of all of its settings.
    """
    return _marshalling.get_group_command_flag(self._command_refs, enums.CommandFlagSaveCurrentSettings)

  @save_current_settings.setter
  def save_current_settings(self, value):
    """
    Setter for save_current_settings
    """
    _marshalling.set_group_command_flag(self._command_refs, enums.CommandFlagSaveCurrentSettings, value)

  @property
  def reset(self):
    """
    Restart the module.
    """
    return _marshalling.get_group_command_flag(self._command_refs, enums.CommandFlagReset)

  @reset.setter
  def reset(self, value):
    """
    Setter for reset
    """
    _marshalling.set_group_command_flag(self._command_refs, enums.CommandFlagReset, value)

  @property
  def boot(self):
    """
    Boot the module from bootloader into application.
    """
    return _marshalling.get_group_command_flag(self._command_refs, enums.CommandFlagBoot)

  @boot.setter
  def boot(self, value):
    """
    Setter for boot
    """
    _marshalling.set_group_command_flag(self._command_refs, enums.CommandFlagBoot, value)

  @property
  def stop_boot(self):
    """
    Stop the module from automatically booting into application.
    """
    return _marshalling.get_group_command_flag(self._command_refs, enums.CommandFlagStopBoot)

  @stop_boot.setter
  def stop_boot(self, value):
    """
    Setter for stop_boot
    """
    _marshalling.set_group_command_flag(self._command_refs, enums.CommandFlagStopBoot, value)

  @property
  def clear_log(self):
    """
    Clears the log message on the module.
    """
    return _marshalling.get_group_command_flag(self._command_refs, enums.CommandFlagClearLog)

  @clear_log.setter
  def clear_log(self, value):
    """
    Setter for clear_log
    """
    _marshalling.set_group_command_flag(self._command_refs, enums.CommandFlagClearLog, value)

  @property
  def control_strategy(self):
    """
    How the position, velocity, and effort PID loops are connected in order to control motor PWM.
    """
    return _marshalling.get_group_command_enum(self._command_refs, enums.CommandEnumControlStrategy)

  @control_strategy.setter
  def control_strategy(self, value):
    """
    Setter for control_strategy

    Note that the following (case sensitive) strings can also be used:
      * "Off"
      * "DirectPWM"
      * "Strategy2"
      * "Strategy3"
      * "Strategy4"
    """
    value = GroupCommand._map_enum_strings_if_needed(value, GroupCommand._enum_control_strategy_str_mappings)
    _marshalling.set_group_command_enum(self._command_refs, enums.CommandEnumControlStrategy, value)

  @property
  def mstop_strategy(self):
    """
    The motion stop strategy for the actuator
    """
    return _marshalling.get_group_command_enum(self._command_refs, enums.CommandEnumMstopStrategy)

  @mstop_strategy.setter
  def mstop_strategy(self, value):
    """
    Setter for mstop_strategy

    Note that the following (case sensitive) strings can also be used:
      * "Disabled"
      * "MotorOff"
      * "HoldPosition"
    """
    value = GroupCommand._map_enum_strings_if_needed(value, GroupCommand._enum_mstop_strategy_str_mappings)
    _marshalling.set_group_command_enum(self._command_refs, enums.CommandEnumMstopStrategy, value)

  @property
  def min_position_limit_strategy(self):
    """
    The position limit strategy (at the minimum position) for the actuator
    """
    return _marshalling.get_group_command_enum(self._command_refs, enums.CommandEnumMinPositionLimitStrategy)

  @min_position_limit_strategy.setter
  def min_position_limit_strategy(self, value):
    """
    Setter for min_position_limit_strategy

    Note that the following (case sensitive) strings can also be used:
      * "HoldPosition"
      * "DampedSpring"
      * "MotorOff"
      * "Disabled"
    """
    value = GroupCommand._map_enum_strings_if_needed(value, GroupCommand._enum_min_position_limit_strategy_str_mappings)
    _marshalling.set_group_command_enum(self._command_refs, enums.CommandEnumMinPositionLimitStrategy, value)

  @property
  def max_position_limit_strategy(self):
    """
    The position limit strategy (at the maximum position) for the actuator
    """
    return _marshalling.get_group_command_enum(self._command_refs, enums.CommandEnumMaxPositionLimitStrategy)

  @max_position_limit_strategy.setter
  def max_position_limit_strategy(self, value):
    """
    Setter for max_position_limit_strategy

    Note that the following (case sensitive) strings can also be used:
      * "HoldPosition"
      * "DampedSpring"
      * "MotorOff"
      * "Disabled"
    """
    value = GroupCommand._map_enum_strings_if_needed(value, GroupCommand._enum_max_position_limit_strategy_str_mappings)
    _marshalling.set_group_command_enum(self._command_refs, enums.CommandEnumMaxPositionLimitStrategy, value)

  @property
  def io(self):
    """
    Command objects have various fields that can be set; when sent to the
    module, these fields control internal properties and setpoints.
    """
    return self._io

  @property
  def led(self):
    """
    The module's LED.
    
    You can retrieve or set the LED color through this interface. The underlying object has a field ``color``
    which can be set using an integer or string. For example::
    
      cmd.led.color = 'red'
      cmd.led.color = 0xFF0000
    
    The available string colors are
    
      * red
      * green
      * blue
      * black
      * white
      * cyan
      * magenta
      * yellow
      * transparent
    """
    return self._led

  @staticmethod
  def _map_enum_entry(value, mapping):
    if value in mapping:
      value = mapping[value]
    else:
      raise ValueError("{0} is not a valid value for enum.\nValid values: {1}".format(value, mapping.keys()))
    return value

  @staticmethod
  def _map_enum_strings_if_needed(value, mapping):
    if isinstance(value, str):
      value = GroupCommand._map_enum_entry(value, mapping)
    elif hasattr(value, '__len__'):
      for i in range(len(value)):
        value[i] = GroupCommand._map_enum_entry(value[i], mapping)
    return value

  _enum_control_strategy_str_mappings = {
    "Off" : 0,
    "DirectPWM" : 1,
    "Strategy2" : 2,
    "Strategy3" : 3,
    "Strategy4" : 4,
  }
  _enum_mstop_strategy_str_mappings = {
    "Disabled" : 0,
    "MotorOff" : 1,
    "HoldPosition" : 2,
  }
  _enum_min_position_limit_strategy_str_mappings = {
    "HoldPosition" : 0,
    "DampedSpring" : 1,
    "MotorOff" : 2,
    "Disabled" : 3,
  }
  _enum_max_position_limit_strategy_str_mappings = {
    "HoldPosition" : 0,
    "DampedSpring" : 1,
    "MotorOff" : 2,
    "Disabled" : 3,
  }


class GroupCommand(GroupCommandBase):
  """
  Command objects have various fields that can be set; when sent to the
  module, these fields control internal properties and setpoints.
  """

  __slots__ = ['_commands']

  def _initialize(self, number_of_modules):
    super(GroupCommand, self)._initialize(number_of_modules)

    self._commands = [None] * self._number_of_modules
    from hebi._internal.ffi.ctypes_func_defs import hebiCommandGetReference as get_ref
    for i in range(self._number_of_modules):
      ref = self._command_refs[i]
      mod = Command(api.hebiGroupCommandGetModuleCommand(self, i), ref)
      self._commands[i] = mod
      get_ref(mod, ctypes.byref(ref))


  def __init__(self, number_of_modules, shared=None):
    if shared:
      if not (isinstance(shared, GroupCommand)):
        raise TypeError('Parameter shared must be a GroupCommand')
      elif number_of_modules != shared.size:
        raise ValueError('Requested number of modules does not match shared parameter')
      super(GroupCommand, self).__init__(existing=shared)
    else:
      super(GroupCommand, self).__init__(internal=api.hebiGroupCommandCreate(number_of_modules), on_delete=api.hebiGroupCommandRelease)
    self._initialize(number_of_modules)

  def __getitem__(self, key):
    return self._commands[key]

  def clear(self):
    """
    Clears all of the fields
    """
    api.hebiGroupCommandClear(self)

  def create_view(self, mask):
    """
    Creates a view into this instance with the indices as specified.

    Note that the created view will hold a strong reference to this object.
    This means that this object will not be destroyed until the created view
    is also destroyed.

    :rtype: GroupCommandView
    """
    return GroupCommandView(self, [int(entry) for entry in mask])

  def copy_from(self, src):
    """
    Copies all fields from the provided message. All fields in the current message are cleared before copied from `src`.
    """
    if self._number_of_modules != src._number_of_modules:
      raise ValueError("Number of modules must be equal")
    elif not isinstance(src, GroupCommand):
      raise TypeError("Input must be a GroupCommand instance")
    return api.hebiGroupCommandCopy(self, src) == enums.StatusSuccess

  def read_gains(self, file):
    """
    Import the gains from a file into this object.

    :raises: IOError if the file could not be opened for reading
    """
    from os.path import isfile
    if not isfile(file):
      raise IOError('{0} is not a file'.format(file))

    res = api.hebiGroupCommandReadGains(self, create_str(file))
    if res != enums.StatusSuccess:
      from hebi._internal.errors import HEBI_Exception
      raise HEBI_Exception(res, 'hebiGroupCommandReadGains failed')

  def write_gains(self, file):
    """
    Export the gains from this object into a file, creating it if necessary.
    """
    res = api.hebiGroupCommandWriteGains(self, create_str(file))
    if res != enums.StatusSuccess:
      from hebi._internal.errors import HEBI_Exception
      raise HEBI_Exception(res, 'hebiGroupCommandWriteGains failed')

  def read_safety_params(self, file):
    """
    Import the safety params from a file into this object.

    :raises: IOError if the file could not be opened for reading
    """
    from os.path import isfile
    if not isfile(file):
      raise IOError('{0} is not a file'.format(file))

    res = api.hebiGroupCommandReadSafetyParameters(self, create_str(file))
    if res != enums.StatusSuccess:
      from hebi._internal.errors import HEBI_Exception
      raise HEBI_Exception(res, 'hebiGroupCommandReadSafetyParameters failed')

  def write_safety_params(self, file):
    """
    Export the safety params from this object into a file, creating it if necessary.
    """
    res = api.hebiGroupCommandWriteSafetyParameters(self, create_str(file))
    if res != enums.StatusSuccess:
      from hebi._internal.errors import HEBI_Exception
      raise HEBI_Exception(res, 'hebiGroupCommandWriteSafetyParameters failed')

  @property
  def modules(self):
    return self._commands[:]


class GroupCommandView(GroupCommandBase):
  """
  A view into a GroupCommand instance.
  This is meant to be used to read and write into a subset of the GroupCommand.
  """

  __slots__ = ['_indices', '_modules']

  def __repr__(self):
    return 'GroupCommandView(mask: {0})'.format(self._indices)

  def _initialize(self, number_of_modules, msg, indices):
    super(GroupCommandView, self)._initialize(number_of_modules)

    for i, entry in enumerate(indices):
      self._command_refs[i] = msg._command_refs[entry]

  def __init__(self, msg, indices):
    super(GroupCommandView, self).__init__(existing=msg)
    num_indices = len(indices)
    num_modules = msg.size

    for entry in indices:
      if not entry < num_modules or entry < 0:
        raise ValueError("input indices is out of range (expected (0 <= x < {})".format(num_modules))

    all_modules = msg.modules
    self._modules = [all_modules[index] for index in indices]
    self._indices = indices
    self._initialize(num_indices, msg, indices)

  @property
  def modules(self):
    return self._modules[:]

  @property
  def _as_parameter_(self):
    raise TypeError("Attempted to use a GroupCommandView to a ctypes function. Did you mean to use a GroupCommand object instead?")


class GroupFeedbackBase(UnmanagedSharedObject):
  """
  Base class for feedback. Do not use directly.
  """

  __slots__ = ['_feedback_refs', '_number_of_modules', '__weakref__', '_io', '_debug', '_led']

  def _initialize(self, number_of_modules):
    self._number_of_modules = number_of_modules
    from hebi._internal.ffi.ctypes_defs import HebiFeedbackRef
    self._feedback_refs = (HebiFeedbackRef * number_of_modules)()

    from hebi._internal.ffi._marshalling import create_io_int_group_getter, create_io_float_group_getter, create_io_group_has
    getter_int = create_io_int_group_getter(self._feedback_refs, api.hwFeedbackGetIoPinInt)
    getter_float = create_io_float_group_getter(self._feedback_refs, api.hwFeedbackGetIoPinFloat)
    has_int = create_io_group_has(self._feedback_refs, api.hwFeedbackHasIoPinInt)
    has_float = create_io_group_has(self._feedback_refs, api.hwFeedbackHasIoPinFloat)
    self._io = GroupMessageIoFieldContainer(self, getter_int, getter_float, has_int, has_float, enums.FeedbackIoBankField)
    from hebi._internal.ffi._marshalling import create_numbered_float_group_getter, create_numbered_float_group_has
    getter = create_numbered_float_group_getter(self._feedback_refs, enums.FeedbackNumberedFloatDebug, api.hwFeedbackGetNumberedFloat)
    has = create_numbered_float_group_has(self._feedback_refs, enums.FeedbackNumberedFloatDebug, api.hwFeedbackHasField, _feedback_metadata)
    self._debug = GroupNumberedFloatFieldContainer(self, enums.FeedbackNumberedFloatDebug, getter, has)
    from hebi._internal.ffi._marshalling import create_led_group_getter
    getter = create_led_group_getter(self._feedback_refs, enums.FeedbackLedLed, api.hwFeedbackGetLed)
    self._led = GroupMessageLEDFieldContainer(self, getter, enums.FeedbackLedLed)

  def __init__(self, internal=None, on_delete=None, existing=None, isdummy=False):
    super(GroupFeedbackBase, self).__init__(internal, on_delete, existing, isdummy)

  @property
  def refs(self):
    return (ctypes_defs.HebiFeedbackRef * self._number_of_modules)(*self._feedback_refs)

  @property
  def size(self):
    """
    The number of modules in this group message.
    """
    return self._number_of_modules

  @property
  def board_temperature(self):
    """
    Ambient temperature inside the module (measured at the IMU chip)
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatBoardTemperature)

  @property
  def processor_temperature(self):
    """
    Temperature of the processor chip.
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatProcessorTemperature)

  @property
  def voltage(self):
    """
    Bus voltage at which the module is running.
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatVoltage)

  @property
  def velocity(self):
    """
    Velocity of the module output (post-spring).
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatVelocity)

  @property
  def effort(self):
    """
    Effort at the module output; units vary (e.g., N * m for rotational joints and N for linear stages).
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatEffort)

  @property
  def velocity_command(self):
    """
    Commanded velocity of the module output (post-spring)
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatVelocityCommand)

  @property
  def effort_command(self):
    """
    Commanded effort at the module output; units vary (e.g., N * m for rotational joints and N for linear stages).
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatEffortCommand)

  @property
  def deflection(self):
    """
    Difference between the pre-spring and post-spring output position.
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatDeflection)

  @property
  def deflection_velocity(self):
    """
    Velocity of the difference between the pre-spring and post-spring output position.
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatDeflectionVelocity)

  @property
  def motor_velocity(self):
    """
    The velocity of the motor shaft.
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatMotorVelocity)

  @property
  def motor_current(self):
    """
    Current supplied to the motor.
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatMotorCurrent)

  @property
  def motor_sensor_temperature(self):
    """
    The temperature from a sensor near the motor housing.
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatMotorSensorTemperature)

  @property
  def motor_winding_current(self):
    """
    The estimated current in the motor windings.
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatMotorWindingCurrent)

  @property
  def motor_winding_temperature(self):
    """
    The estimated temperature of the motor windings.
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatMotorWindingTemperature)

  @property
  def motor_housing_temperature(self):
    """
    The estimated temperature of the motor housing.
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatMotorHousingTemperature)

  @property
  def battery_level(self):
    """
    Charge level of the device's battery (in percent).
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatBatteryLevel)

  @property
  def pwm_command(self):
    """
    Commanded PWM signal sent to the motor; final output of PID controllers.
    """
    return _marshalling.get_group_feedback_float(self._feedback_refs, enums.FeedbackFloatPwmCommand)

  @property
  def position(self):
    """
    Position of the module output (post-spring).
    """
    return _marshalling.get_group_feedback_highresangle(self._feedback_refs, enums.FeedbackHighResAnglePosition)

  @property
  def position_command(self):
    """
    Commanded position of the module output (post-spring).
    """
    return _marshalling.get_group_feedback_highresangle(self._feedback_refs, enums.FeedbackHighResAnglePositionCommand)

  @property
  def motor_position(self):
    """
    The position of an actuator's internal motor before the gear reduction.
    """
    return _marshalling.get_group_feedback_highresangle(self._feedback_refs, enums.FeedbackHighResAngleMotorPosition)

  @property
  def debug(self):
    """
    Values for internal debug functions (channel 1-9 available).
    """
    return self._debug

  @property
  def sequence_number(self):
    """
    Sequence number going to module (local)
    """
    return _marshalling.get_group_feedback_uint64(self._feedback_refs, enums.FeedbackUInt64SequenceNumber)

  @property
  def receive_time(self):
    """
    Timestamp of when message was received from module (local) in seconds
    """
    return _marshalling.get_group_feedback_uint64(self._feedback_refs, enums.FeedbackUInt64ReceiveTime)*1e-6

  @property
  def receive_time_us(self):
    """
    Timestamp of when message was received from module (local) in microseconds
    """
    return _marshalling.get_group_feedback_uint64(self._feedback_refs, enums.FeedbackUInt64ReceiveTime)

  @property
  def transmit_time(self):
    """
    Timestamp of when message was transmitted to module (local) in seconds
    """
    return _marshalling.get_group_feedback_uint64(self._feedback_refs, enums.FeedbackUInt64TransmitTime)*1e-6

  @property
  def transmit_time_us(self):
    """
    Timestamp of when message was transmitted to module (local) in microseconds
    """
    return _marshalling.get_group_feedback_uint64(self._feedback_refs, enums.FeedbackUInt64TransmitTime)

  @property
  def hardware_receive_time(self):
    """
    Timestamp of when message was received by module (remote) in seconds
    """
    return _marshalling.get_group_feedback_uint64(self._feedback_refs, enums.FeedbackUInt64HardwareReceiveTime)*1e-6

  @property
  def hardware_receive_time_us(self):
    """
    Timestamp of when message was received by module (remote) in microseconds
    """
    return _marshalling.get_group_feedback_uint64(self._feedback_refs, enums.FeedbackUInt64HardwareReceiveTime)

  @property
  def hardware_transmit_time(self):
    """
    Timestamp of when message was transmitted from module (remote) in seconds
    """
    return _marshalling.get_group_feedback_uint64(self._feedback_refs, enums.FeedbackUInt64HardwareTransmitTime)*1e-6

  @property
  def hardware_transmit_time_us(self):
    """
    Timestamp of when message was transmitted from module (remote) in microseconds
    """
    return _marshalling.get_group_feedback_uint64(self._feedback_refs, enums.FeedbackUInt64HardwareTransmitTime)

  @property
  def sender_id(self):
    """
    Unique ID of the module transmitting this feedback
    """
    return _marshalling.get_group_feedback_uint64(self._feedback_refs, enums.FeedbackUInt64SenderId)

  @property
  def accelerometer(self):
    """
    Accelerometer data
    """
    return _marshalling.get_group_feedback_vector3f(self._feedback_refs, enums.FeedbackVector3fAccelerometer)

  @property
  def gyro(self):
    """
    Gyro data
    """
    return _marshalling.get_group_feedback_vector3f(self._feedback_refs, enums.FeedbackVector3fGyro)

  @property
  def ar_position(self):
    """
    A device's position in the world as calculated from an augmented reality framework
    """
    return _marshalling.get_group_feedback_vector3f(self._feedback_refs, enums.FeedbackVector3fArPosition)

  @property
  def orientation(self):
    """
    A filtered estimate of the orientation of the module.
    """
    return _marshalling.get_group_feedback_quaternionf(self._feedback_refs, enums.FeedbackQuaternionfOrientation)

  @property
  def ar_orientation(self):
    """
    A device's orientation in the world as calculated from an augmented reality framework
    """
    return _marshalling.get_group_feedback_quaternionf(self._feedback_refs, enums.FeedbackQuaternionfArOrientation)

  @property
  def temperature_state(self):
    """
    Describes how the temperature inside the module is limiting the output of the motor
    """
    return _marshalling.get_group_feedback_enum(self._feedback_refs, enums.FeedbackEnumTemperatureState)

  @property
  def mstop_state(self):
    """
    Current status of the MStop
    """
    return _marshalling.get_group_feedback_enum(self._feedback_refs, enums.FeedbackEnumMstopState)

  @property
  def position_limit_state(self):
    """
    Software-controlled bounds on the allowable position of the module; user settable
    """
    return _marshalling.get_group_feedback_enum(self._feedback_refs, enums.FeedbackEnumPositionLimitState)

  @property
  def velocity_limit_state(self):
    """
    Software-controlled bounds on the allowable velocity of the module
    """
    return _marshalling.get_group_feedback_enum(self._feedback_refs, enums.FeedbackEnumVelocityLimitState)

  @property
  def effort_limit_state(self):
    """
    Software-controlled bounds on the allowable effort of the module
    """
    return _marshalling.get_group_feedback_enum(self._feedback_refs, enums.FeedbackEnumEffortLimitState)

  @property
  def command_lifetime_state(self):
    """
    The state of the command lifetime safety controller, with respect to the current group
    """
    return _marshalling.get_group_feedback_enum(self._feedback_refs, enums.FeedbackEnumCommandLifetimeState)

  @property
  def ar_quality(self):
    """
    The status of the augmented reality tracking, if using an AR enabled device. See HebiArQuality for values.
    """
    return _marshalling.get_group_feedback_enum(self._feedback_refs, enums.FeedbackEnumArQuality)

  @property
  def io(self):
    """
    Feedback objects have various fields representing feedback from modules;
    which fields are populated depends on the module type and various other settings.
    """
    return self._io

  @property
  def led(self):
    """
    Interface to the IO pins of the module.
    
    This field exposes a read-only view of all banks - ``a``, ``b``, ``c``, ``d``, ``e``, ``f`` - which
    all have one or more pins. Each pin has ``int`` and ``float`` values. The two values are not the same
    view into a piece of data and thus can both be set to different values.
    
    Examples::
    
      a2 = fbk.io.a.get_int(2)
      e4 = fbk.io.e.get_float(4)
    
    """
    return self._led



class GroupFeedback(GroupFeedbackBase):
  """
  Feedback objects have various fields representing feedback from modules;
  which fields are populated depends on the module type and various other settings.
  """

  __slots__ = ['_feedbacks']

  def _initialize(self, number_of_modules):
    super(GroupFeedback, self)._initialize(number_of_modules)

    self._feedbacks = [None] * self._number_of_modules
    from hebi._internal.ffi.ctypes_func_defs import hebiFeedbackGetReference as get_ref
    for i in range(self._number_of_modules):
      ref = self._feedback_refs[i]
      mod = Feedback(api.hebiGroupFeedbackGetModuleFeedback(self, i), ref)
      self._feedbacks[i] = mod
      get_ref(mod, ctypes.byref(ref))


  def __init__(self, number_of_modules, shared=None):
    if shared:
      if not (isinstance(shared, GroupFeedback)):
        raise TypeError('Parameter shared must be a GroupFeedback')
      elif number_of_modules != shared.size:
        raise ValueError('Requested number of modules does not match shared parameter')
      super(GroupFeedback, self).__init__(existing=shared)
    else:
      super(GroupFeedback, self).__init__(internal=api.hebiGroupFeedbackCreate(number_of_modules), on_delete=api.hebiGroupFeedbackRelease)
    self._initialize(number_of_modules)

  def __getitem__(self, key):
    return self._feedbacks[key]

  def clear(self):
    """
    Clears all of the fields
    """
    api.hebiGroupFeedbackClear(self)

  def create_view(self, mask):
    """
    Creates a view into this instance with the indices as specified.

    Note that the created view will hold a strong reference to this object.
    This means that this object will not be destroyed until the created view
    is also destroyed.

    :rtype: GroupFeedbackView
    """
    return GroupFeedbackView(self, [int(entry) for entry in mask])

  def copy_from(self, src):
    """
    Copies all fields from the provided message. All fields in the current message are cleared before copied from `src`.
    """
    if self._number_of_modules != src._number_of_modules:
      raise ValueError("Number of modules must be equal")
    elif not isinstance(src, GroupFeedback):
      raise TypeError("Input must be a GroupFeedback instance")
    return api.hebiGroupFeedbackCopy(self, src) == enums.StatusSuccess

  def get_position(self, array):
    """
    Convenience method to get positions into an existing array.
    The input must be a numpy object with dtype compatible with ``numpy.float64``.

    :param array: a numpy array or matrix with size matching the
                  number of modules in this group message
    :type array:  numpy.ndarray
    """
    if array.size != self._number_of_modules:
      raise ValueError('Input array must be the size of the group feedback')
    _marshalling.get_group_feedback_highresangle_into(self._feedback_refs, enums.FeedbackHighResAnglePosition, array)

  def get_position_command(self, array):
    """
    Convenience method to get position commands into an existing array.
    The input must be a numpy object with dtype compatible with ``numpy.float64``.

    :param array: a numpy array or matrix with size matching the
                  number of modules in this group message
    :type array:  numpy.ndarray
    """
    if array.size != self._number_of_modules:
      raise ValueError('Input array must be the size of the group feedback')
    _marshalling.get_group_feedback_highresangle_into(self._feedback_refs, enums.FeedbackHighResAnglePositionCommand, array)

  def get_velocity(self, array):
    """
    Convenience method to get velocities into an existing array.
    The input must be a numpy object with dtype compatible with ``numpy.float32``.

    :param array: a numpy array or matrix with size matching the
                  number of modules in this group message
    :type array:  numpy.ndarray
    """
    if array.size != self._number_of_modules:
      raise ValueError('Input array must be the size of the group feedback')
    _marshalling.get_group_feedback_float_into(self._feedback_refs, enums.FeedbackFloatVelocity, array)

  def get_velocity_command(self, array):
    """
    Convenience method to get velocity commands into an existing array.
    The input must be a numpy object with dtype compatible with ``numpy.float32``.

    :param array: a numpy array or matrix with size matching the
                  number of modules in this group message
    :type array:  numpy.ndarray
    """
    if array.size != self._number_of_modules:
      raise ValueError('Input array must be the size of the group feedback')
    _marshalling.get_group_feedback_float_into(self._feedback_refs, enums.FeedbackFloatVelocityCommand, array)

  def get_effort(self, array):
    """
    Convenience method to get efforts into an existing array.
    The input must be a numpy object with dtype compatible with ``numpy.float32``.

    :param array: a numpy array or matrix with size matching the
                  number of modules in this group message
    :type array:  numpy.ndarray
    """
    if array.size != self._number_of_modules:
      raise ValueError('Input array must be the size of the group feedback')
    _marshalling.get_group_feedback_float_into(self._feedback_refs, enums.FeedbackFloatEffort, array)

  def get_effort_command(self, array):
    """
    Convenience method to get effort commands into an existing array.
    The input must be a numpy object with dtype compatible with ``numpy.float32``.

    :param array: a numpy array or matrix with size matching the
                  number of modules in this group message
    :type array:  numpy.ndarray
    """
    if array.size != self._number_of_modules:
      raise ValueError('Input array must be the size of the group feedback')
    _marshalling.get_group_feedback_float_into(self._feedback_refs, enums.FeedbackFloatEffortCommand, array)

  @property
  def modules(self):
    return self._feedbacks[:]


class GroupFeedbackView(GroupFeedbackBase):
  """
  A view into a GroupFeedback instance.
  This is meant to be used to read into a subset of the GroupFeedback.
  """

  __slots__ = ['_indices', '_modules']

  def __repr__(self):
    return 'GroupFeedbackView(mask: {0})'.format(self._indices)

  def _initialize(self, number_of_modules, msg, indices):
    super(GroupFeedbackView, self)._initialize(number_of_modules)

    for i, entry in enumerate(indices):
      self._feedback_refs[i] = msg._feedback_refs[entry]

  def __init__(self, msg, indices):
    super(GroupFeedbackView, self).__init__(existing=msg)
    num_indices = len(indices)
    num_modules = msg.size

    for entry in indices:
      if not entry < num_modules or entry < 0:
        raise ValueError("input indices is out of range (expected (0 <= x < {})".format(num_modules))

    all_modules = msg.modules
    self._modules = [all_modules[index] for index in indices]
    self._indices = indices
    self._initialize(num_indices, msg, indices)

  @property
  def modules(self):
    return self._modules[:]

  @property
  def _as_parameter_(self):
    raise TypeError("Attempted to use a GroupFeedbackView to a ctypes function. Did you mean to use a GroupFeedback object instead?")


class GroupInfoBase(UnmanagedSharedObject):
  """
  Base class for info. Do not use directly.
  """

  __slots__ = ['_info_refs', '_number_of_modules', '__weakref__', '_led']

  def _initialize(self, number_of_modules):
    self._number_of_modules = number_of_modules
    from hebi._internal.ffi.ctypes_defs import HebiInfoRef
    self._info_refs = (HebiInfoRef * number_of_modules)()
    from hebi._internal.ffi._marshalling import create_led_group_getter
    getter = create_led_group_getter(self._info_refs, enums.InfoLedLed, api.hwInfoGetLed)
    self._led = GroupMessageLEDFieldContainer(self, getter, enums.InfoLedLed)

  def __init__(self, internal=None, on_delete=None, existing=None, isdummy=False):
    super(GroupInfoBase, self).__init__(internal, on_delete, existing, isdummy)

  @property
  def refs(self):
    return (ctypes_defs.HebiInfoRef * self._number_of_modules)(*self._info_refs)

  @property
  def size(self):
    """
    The number of modules in this group message.
    """
    return self._number_of_modules

  @property
  def position_kp(self):
    """
    Proportional PID gain for position
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatPositionKp)

  @property
  def position_ki(self):
    """
    Integral PID gain for position
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatPositionKi)

  @property
  def position_kd(self):
    """
    Derivative PID gain for position
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatPositionKd)

  @property
  def position_feed_forward(self):
    """
    Feed forward term for position (this term is multiplied by the target and added to the output).
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatPositionFeedForward)

  @property
  def position_dead_zone(self):
    """
    Error values within +/- this value from zero are treated as zero (in terms of computed proportional output, input to numerical derivative, and accumulated integral error).
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatPositionDeadZone)

  @property
  def position_i_clamp(self):
    """
    Maximum allowed value for the output of the integral component of the PID loop; the integrated error is not allowed to exceed value that will generate this number.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatPositionIClamp)

  @property
  def position_punch(self):
    """
    Constant offset to the position PID output outside of the deadzone; it is added when the error is positive and subtracted when it is negative.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatPositionPunch)

  @property
  def position_min_target(self):
    """
    Minimum allowed value for input to the PID controller
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatPositionMinTarget)

  @property
  def position_max_target(self):
    """
    Maximum allowed value for input to the PID controller
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatPositionMaxTarget)

  @property
  def position_target_lowpass(self):
    """
    A simple lowpass filter applied to the target set point; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatPositionTargetLowpass)

  @property
  def position_min_output(self):
    """
    Output from the PID controller is limited to a minimum of this value.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatPositionMinOutput)

  @property
  def position_max_output(self):
    """
    Output from the PID controller is limited to a maximum of this value.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatPositionMaxOutput)

  @property
  def position_output_lowpass(self):
    """
    A simple lowpass filter applied to the controller output; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatPositionOutputLowpass)

  @property
  def velocity_kp(self):
    """
    Proportional PID gain for velocity
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatVelocityKp)

  @property
  def velocity_ki(self):
    """
    Integral PID gain for velocity
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatVelocityKi)

  @property
  def velocity_kd(self):
    """
    Derivative PID gain for velocity
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatVelocityKd)

  @property
  def velocity_feed_forward(self):
    """
    Feed forward term for velocity (this term is multiplied by the target and added to the output).
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatVelocityFeedForward)

  @property
  def velocity_dead_zone(self):
    """
    Error values within +/- this value from zero are treated as zero (in terms of computed proportional output, input to numerical derivative, and accumulated integral error).
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatVelocityDeadZone)

  @property
  def velocity_i_clamp(self):
    """
    Maximum allowed value for the output of the integral component of the PID loop; the integrated error is not allowed to exceed value that will generate this number.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatVelocityIClamp)

  @property
  def velocity_punch(self):
    """
    Constant offset to the velocity PID output outside of the deadzone; it is added when the error is positive and subtracted when it is negative.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatVelocityPunch)

  @property
  def velocity_min_target(self):
    """
    Minimum allowed value for input to the PID controller
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatVelocityMinTarget)

  @property
  def velocity_max_target(self):
    """
    Maximum allowed value for input to the PID controller
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatVelocityMaxTarget)

  @property
  def velocity_target_lowpass(self):
    """
    A simple lowpass filter applied to the target set point; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatVelocityTargetLowpass)

  @property
  def velocity_min_output(self):
    """
    Output from the PID controller is limited to a minimum of this value.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatVelocityMinOutput)

  @property
  def velocity_max_output(self):
    """
    Output from the PID controller is limited to a maximum of this value.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatVelocityMaxOutput)

  @property
  def velocity_output_lowpass(self):
    """
    A simple lowpass filter applied to the controller output; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatVelocityOutputLowpass)

  @property
  def effort_kp(self):
    """
    Proportional PID gain for effort
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatEffortKp)

  @property
  def effort_ki(self):
    """
    Integral PID gain for effort
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatEffortKi)

  @property
  def effort_kd(self):
    """
    Derivative PID gain for effort
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatEffortKd)

  @property
  def effort_feed_forward(self):
    """
    Feed forward term for effort (this term is multiplied by the target and added to the output).
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatEffortFeedForward)

  @property
  def effort_dead_zone(self):
    """
    Error values within +/- this value from zero are treated as zero (in terms of computed proportional output, input to numerical derivative, and accumulated integral error).
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatEffortDeadZone)

  @property
  def effort_i_clamp(self):
    """
    Maximum allowed value for the output of the integral component of the PID loop; the integrated error is not allowed to exceed value that will generate this number.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatEffortIClamp)

  @property
  def effort_punch(self):
    """
    Constant offset to the effort PID output outside of the deadzone; it is added when the error is positive and subtracted when it is negative.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatEffortPunch)

  @property
  def effort_min_target(self):
    """
    Minimum allowed value for input to the PID controller
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatEffortMinTarget)

  @property
  def effort_max_target(self):
    """
    Maximum allowed value for input to the PID controller
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatEffortMaxTarget)

  @property
  def effort_target_lowpass(self):
    """
    A simple lowpass filter applied to the target set point; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatEffortTargetLowpass)

  @property
  def effort_min_output(self):
    """
    Output from the PID controller is limited to a minimum of this value.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatEffortMinOutput)

  @property
  def effort_max_output(self):
    """
    Output from the PID controller is limited to a maximum of this value.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatEffortMaxOutput)

  @property
  def effort_output_lowpass(self):
    """
    A simple lowpass filter applied to the controller output; needs to be between 0 and 1. At each timestep: x_t = x_t * a + x_{t-1} * (1 - a).
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatEffortOutputLowpass)

  @property
  def spring_constant(self):
    """
    The spring constant of the module.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatSpringConstant)

  @property
  def velocity_limit_min(self):
    """
    The firmware safety limit for the minimum allowed velocity.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatVelocityLimitMin)

  @property
  def velocity_limit_max(self):
    """
    The firmware safety limit for the maximum allowed velocity.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatVelocityLimitMax)

  @property
  def effort_limit_min(self):
    """
    The firmware safety limit for the minimum allowed effort.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatEffortLimitMin)

  @property
  def effort_limit_max(self):
    """
    The firmware safety limit for the maximum allowed effort.
    """
    return _marshalling.get_group_info_float(self._info_refs, enums.InfoFloatEffortLimitMax)

  @property
  def position_limit_min(self):
    """
    The firmware safety limit for the minimum allowed position.
    """
    return _marshalling.get_group_info_highresangle(self._info_refs, enums.InfoHighResAnglePositionLimitMin)

  @property
  def position_limit_max(self):
    """
    The firmware safety limit for the maximum allowed position.
    """
    return _marshalling.get_group_info_highresangle(self._info_refs, enums.InfoHighResAnglePositionLimitMax)

  @property
  def position_d_on_error(self):
    """
    Controls whether the Kd term uses the "derivative of error" or "derivative of measurement." When the setpoints have step inputs or are noisy, setting this to @c false can eliminate corresponding spikes or noise in the output.
    """
    return _marshalling.get_group_info_bool(self._info_refs, enums.InfoBoolPositionDOnError)

  @property
  def velocity_d_on_error(self):
    """
    Controls whether the Kd term uses the "derivative of error" or "derivative of measurement." When the setpoints have step inputs or are noisy, setting this to @c false can eliminate corresponding spikes or noise in the output.
    """
    return _marshalling.get_group_info_bool(self._info_refs, enums.InfoBoolVelocityDOnError)

  @property
  def effort_d_on_error(self):
    """
    Controls whether the Kd term uses the "derivative of error" or "derivative of measurement." When the setpoints have step inputs or are noisy, setting this to @c false can eliminate corresponding spikes or noise in the output.
    """
    return _marshalling.get_group_info_bool(self._info_refs, enums.InfoBoolEffortDOnError)

  @property
  def accel_includes_gravity(self):
    """
    Whether to include acceleration due to gravity in acceleration feedback.
    """
    return _marshalling.get_group_info_bool(self._info_refs, enums.InfoBoolAccelIncludesGravity)

  @property
  def name(self):
    """
    The name for this module. The string must be null-terminated and less than 21 characters.
    """
    return _marshalling.get_group_info_string(self, enums.InfoStringName, [None] * self._number_of_modules)

  @property
  def family(self):
    """
    The family for this module. The string must be null-terminated and less than 21 characters.
    """
    return _marshalling.get_group_info_string(self, enums.InfoStringFamily, [None] * self._number_of_modules)

  @property
  def serial(self):
    """
    Gets the serial number for this module (e.g., X5-0001).
    """
    return _marshalling.get_group_info_string(self, enums.InfoStringSerial, [None] * self._number_of_modules)

  @property
  def save_current_settings(self):
    """
    Indicates if the module should save the current values of all of its settings.
    """
    return _marshalling.get_group_info_flag(self._info_refs, enums.InfoFlagSaveCurrentSettings)

  @property
  def control_strategy(self):
    """
    How the position, velocity, and effort PID loops are connected in order to control motor PWM.
    """
    return _marshalling.get_group_info_enum(self._info_refs, enums.InfoEnumControlStrategy)

  @property
  def calibration_state(self):
    """
    The calibration state of the module
    """
    return _marshalling.get_group_info_enum(self._info_refs, enums.InfoEnumCalibrationState)

  @property
  def mstop_strategy(self):
    """
    The motion stop strategy for the actuator
    """
    return _marshalling.get_group_info_enum(self._info_refs, enums.InfoEnumMstopStrategy)

  @property
  def min_position_limit_strategy(self):
    """
    The position limit strategy (at the minimum position) for the actuator
    """
    return _marshalling.get_group_info_enum(self._info_refs, enums.InfoEnumMinPositionLimitStrategy)

  @property
  def max_position_limit_strategy(self):
    """
    The position limit strategy (at the maximum position) for the actuator
    """
    return _marshalling.get_group_info_enum(self._info_refs, enums.InfoEnumMaxPositionLimitStrategy)

  @property
  def led(self):
    """
    The module's LED.
    """
    return self._led



class GroupInfo(GroupInfoBase):
  """
  Info objects have various fields representing the module state;
  which fields are populated depends on the module type and various other settings.
  """

  __slots__ = ['_infos']

  def _initialize(self, number_of_modules):
    super(GroupInfo, self)._initialize(number_of_modules)

    self._infos = [None] * self._number_of_modules
    from hebi._internal.ffi.ctypes_func_defs import hebiInfoGetReference as get_ref
    for i in range(self._number_of_modules):
      ref = self._info_refs[i]
      mod = Info(api.hebiGroupInfoGetModuleInfo(self, i), ref)
      self._infos[i] = mod
      get_ref(mod, ctypes.byref(ref))


  def __init__(self, number_of_modules, shared=None):
    if shared:
      if not (isinstance(shared, GroupInfo)):
        raise TypeError('Parameter shared must be a GroupInfo')
      elif number_of_modules != shared.size:
        raise ValueError('Requested number of modules does not match shared parameter')
      super(GroupInfo, self).__init__(existing=shared)
    else:
      super(GroupInfo, self).__init__(internal=api.hebiGroupInfoCreate(number_of_modules), on_delete=api.hebiGroupInfoRelease)
    self._initialize(number_of_modules)

  def __getitem__(self, key):
    return self._infos[key]



  def copy_from(self, src):
    """
    Copies all fields from the provided message. All fields in the current message are cleared before copied from `src`.
    """
    if self._number_of_modules != src._number_of_modules:
      raise ValueError("Number of modules must be equal")
    elif not isinstance(src, GroupInfo):
      raise TypeError("Input must be a GroupInfo instance")
    return api.hebiGroupInfoCopy(self, src) == enums.StatusSuccess

  def write_gains(self, file):
    """
    Export the gains from this object into a file, creating it if necessary.
    """
    res = api.hebiGroupInfoWriteGains(self, create_str(file))
    if res != enums.StatusSuccess:
      from hebi._internal.errors import HEBI_Exception
      raise HEBI_Exception(res, 'hebiGroupInfoWriteGains failed')

  def write_safety_params(self, file):
    """
    Export the safety params from this object into a file, creating it if necessary.
    """
    res = api.hebiGroupInfoWriteSafetyParameters(self, create_str(file))
    if res != enums.StatusSuccess:
      from hebi._internal.errors import HEBI_Exception
      raise HEBI_Exception(res, 'hebiGroupInfoWriteSafetyParameters failed')

  @property
  def modules(self):
    return self._infos[:]
