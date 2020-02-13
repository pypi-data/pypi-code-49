from .wrappers import MessageEnumTraits, EnumTraits, EnumType, FieldDetails


# CommandFloatField
CommandFloatVelocity = MessageEnumTraits(0, 'CommandFloatVelocity', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad/s', 'velocity', 'Velocity', 'velocity', True))
CommandFloatEffort = MessageEnumTraits(1, 'CommandFloatEffort', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('N*m', 'effort', 'Effort', 'effort', True))
CommandFloatPositionKp = MessageEnumTraits(2, 'CommandFloatPositionKp', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionKp', 'PositionKp', 'position_kp', True))
CommandFloatPositionKi = MessageEnumTraits(3, 'CommandFloatPositionKi', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionKi', 'PositionKi', 'position_ki', True))
CommandFloatPositionKd = MessageEnumTraits(4, 'CommandFloatPositionKd', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionKd', 'PositionKd', 'position_kd', True))
CommandFloatPositionFeedForward = MessageEnumTraits(5, 'CommandFloatPositionFeedForward', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionFeedForward', 'PositionFeedForward', 'position_feed_forward', True))
CommandFloatPositionDeadZone = MessageEnumTraits(6, 'CommandFloatPositionDeadZone', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionDeadZone', 'PositionDeadZone', 'position_dead_zone', True))
CommandFloatPositionIClamp = MessageEnumTraits(7, 'CommandFloatPositionIClamp', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionIClamp', 'PositionIClamp', 'position_i_clamp', True))
CommandFloatPositionPunch = MessageEnumTraits(8, 'CommandFloatPositionPunch', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionPunch', 'PositionPunch', 'position_punch', True))
CommandFloatPositionMinTarget = MessageEnumTraits(9, 'CommandFloatPositionMinTarget', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionMinTarget', 'PositionMinTarget', 'position_min_target', True))
CommandFloatPositionMaxTarget = MessageEnumTraits(10, 'CommandFloatPositionMaxTarget', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionMaxTarget', 'PositionMaxTarget', 'position_max_target', True))
CommandFloatPositionTargetLowpass = MessageEnumTraits(11, 'CommandFloatPositionTargetLowpass', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionTargetLowpass', 'PositionTargetLowpass', 'position_target_lowpass', True))
CommandFloatPositionMinOutput = MessageEnumTraits(12, 'CommandFloatPositionMinOutput', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionMinOutput', 'PositionMinOutput', 'position_min_output', True))
CommandFloatPositionMaxOutput = MessageEnumTraits(13, 'CommandFloatPositionMaxOutput', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionMaxOutput', 'PositionMaxOutput', 'position_max_output', True))
CommandFloatPositionOutputLowpass = MessageEnumTraits(14, 'CommandFloatPositionOutputLowpass', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionOutputLowpass', 'PositionOutputLowpass', 'position_output_lowpass', True))
CommandFloatVelocityKp = MessageEnumTraits(15, 'CommandFloatVelocityKp', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityKp', 'VelocityKp', 'velocity_kp', True))
CommandFloatVelocityKi = MessageEnumTraits(16, 'CommandFloatVelocityKi', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityKi', 'VelocityKi', 'velocity_ki', True))
CommandFloatVelocityKd = MessageEnumTraits(17, 'CommandFloatVelocityKd', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityKd', 'VelocityKd', 'velocity_kd', True))
CommandFloatVelocityFeedForward = MessageEnumTraits(18, 'CommandFloatVelocityFeedForward', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityFeedForward', 'VelocityFeedForward', 'velocity_feed_forward', True))
CommandFloatVelocityDeadZone = MessageEnumTraits(19, 'CommandFloatVelocityDeadZone', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityDeadZone', 'VelocityDeadZone', 'velocity_dead_zone', True))
CommandFloatVelocityIClamp = MessageEnumTraits(20, 'CommandFloatVelocityIClamp', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityIClamp', 'VelocityIClamp', 'velocity_i_clamp', True))
CommandFloatVelocityPunch = MessageEnumTraits(21, 'CommandFloatVelocityPunch', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityPunch', 'VelocityPunch', 'velocity_punch', True))
CommandFloatVelocityMinTarget = MessageEnumTraits(22, 'CommandFloatVelocityMinTarget', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityMinTarget', 'VelocityMinTarget', 'velocity_min_target', True))
CommandFloatVelocityMaxTarget = MessageEnumTraits(23, 'CommandFloatVelocityMaxTarget', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityMaxTarget', 'VelocityMaxTarget', 'velocity_max_target', True))
CommandFloatVelocityTargetLowpass = MessageEnumTraits(24, 'CommandFloatVelocityTargetLowpass', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityTargetLowpass', 'VelocityTargetLowpass', 'velocity_target_lowpass', True))
CommandFloatVelocityMinOutput = MessageEnumTraits(25, 'CommandFloatVelocityMinOutput', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityMinOutput', 'VelocityMinOutput', 'velocity_min_output', True))
CommandFloatVelocityMaxOutput = MessageEnumTraits(26, 'CommandFloatVelocityMaxOutput', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityMaxOutput', 'VelocityMaxOutput', 'velocity_max_output', True))
CommandFloatVelocityOutputLowpass = MessageEnumTraits(27, 'CommandFloatVelocityOutputLowpass', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityOutputLowpass', 'VelocityOutputLowpass', 'velocity_output_lowpass', True))
CommandFloatEffortKp = MessageEnumTraits(28, 'CommandFloatEffortKp', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortKp', 'EffortKp', 'effort_kp', True))
CommandFloatEffortKi = MessageEnumTraits(29, 'CommandFloatEffortKi', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortKi', 'EffortKi', 'effort_ki', True))
CommandFloatEffortKd = MessageEnumTraits(30, 'CommandFloatEffortKd', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortKd', 'EffortKd', 'effort_kd', True))
CommandFloatEffortFeedForward = MessageEnumTraits(31, 'CommandFloatEffortFeedForward', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortFeedForward', 'EffortFeedForward', 'effort_feed_forward', True))
CommandFloatEffortDeadZone = MessageEnumTraits(32, 'CommandFloatEffortDeadZone', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortDeadZone', 'EffortDeadZone', 'effort_dead_zone', True))
CommandFloatEffortIClamp = MessageEnumTraits(33, 'CommandFloatEffortIClamp', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortIClamp', 'EffortIClamp', 'effort_i_clamp', True))
CommandFloatEffortPunch = MessageEnumTraits(34, 'CommandFloatEffortPunch', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortPunch', 'EffortPunch', 'effort_punch', True))
CommandFloatEffortMinTarget = MessageEnumTraits(35, 'CommandFloatEffortMinTarget', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortMinTarget', 'EffortMinTarget', 'effort_min_target', True))
CommandFloatEffortMaxTarget = MessageEnumTraits(36, 'CommandFloatEffortMaxTarget', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortMaxTarget', 'EffortMaxTarget', 'effort_max_target', True))
CommandFloatEffortTargetLowpass = MessageEnumTraits(37, 'CommandFloatEffortTargetLowpass', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortTargetLowpass', 'EffortTargetLowpass', 'effort_target_lowpass', True))
CommandFloatEffortMinOutput = MessageEnumTraits(38, 'CommandFloatEffortMinOutput', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortMinOutput', 'EffortMinOutput', 'effort_min_output', True))
CommandFloatEffortMaxOutput = MessageEnumTraits(39, 'CommandFloatEffortMaxOutput', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortMaxOutput', 'EffortMaxOutput', 'effort_max_output', True))
CommandFloatEffortOutputLowpass = MessageEnumTraits(40, 'CommandFloatEffortOutputLowpass', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortOutputLowpass', 'EffortOutputLowpass', 'effort_output_lowpass', True))
CommandFloatSpringConstant = MessageEnumTraits(41, 'CommandFloatSpringConstant', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('N/m', 'springConstant', 'SpringConstant', 'spring_constant', True))
CommandFloatReferencePosition = MessageEnumTraits(42, 'CommandFloatReferencePosition', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad', 'referencePosition', 'ReferencePosition', 'reference_position', True))
CommandFloatReferenceEffort = MessageEnumTraits(43, 'CommandFloatReferenceEffort', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('N*m', 'referenceEffort', 'ReferenceEffort', 'reference_effort', True))
CommandFloatVelocityLimitMin = MessageEnumTraits(44, 'CommandFloatVelocityLimitMin', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad/s', 'velocityLimitMin', 'VelocityLimitMin', 'velocity_limit_min', True))
CommandFloatVelocityLimitMax = MessageEnumTraits(45, 'CommandFloatVelocityLimitMax', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad/s', 'velocityLimitMax', 'VelocityLimitMax', 'velocity_limit_max', True))
CommandFloatEffortLimitMin = MessageEnumTraits(46, 'CommandFloatEffortLimitMin', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('N*m', 'effortLimitMin', 'EffortLimitMin', 'effort_limit_min', True))
CommandFloatEffortLimitMax = MessageEnumTraits(47, 'CommandFloatEffortLimitMax', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('N*m', 'effortLimitMax', 'EffortLimitMax', 'effort_limit_max', True))
CommandFloatField = EnumType('CommandFloatField', [ CommandFloatVelocity, CommandFloatEffort, CommandFloatPositionKp, CommandFloatPositionKi, CommandFloatPositionKd, CommandFloatPositionFeedForward, CommandFloatPositionDeadZone, CommandFloatPositionIClamp, CommandFloatPositionPunch, CommandFloatPositionMinTarget, CommandFloatPositionMaxTarget, CommandFloatPositionTargetLowpass, CommandFloatPositionMinOutput, CommandFloatPositionMaxOutput, CommandFloatPositionOutputLowpass, CommandFloatVelocityKp, CommandFloatVelocityKi, CommandFloatVelocityKd, CommandFloatVelocityFeedForward, CommandFloatVelocityDeadZone, CommandFloatVelocityIClamp, CommandFloatVelocityPunch, CommandFloatVelocityMinTarget, CommandFloatVelocityMaxTarget, CommandFloatVelocityTargetLowpass, CommandFloatVelocityMinOutput, CommandFloatVelocityMaxOutput, CommandFloatVelocityOutputLowpass, CommandFloatEffortKp, CommandFloatEffortKi, CommandFloatEffortKd, CommandFloatEffortFeedForward, CommandFloatEffortDeadZone, CommandFloatEffortIClamp, CommandFloatEffortPunch, CommandFloatEffortMinTarget, CommandFloatEffortMaxTarget, CommandFloatEffortTargetLowpass, CommandFloatEffortMinOutput, CommandFloatEffortMaxOutput, CommandFloatEffortOutputLowpass, CommandFloatSpringConstant, CommandFloatReferencePosition, CommandFloatReferenceEffort, CommandFloatVelocityLimitMin, CommandFloatVelocityLimitMax, CommandFloatEffortLimitMin, CommandFloatEffortLimitMax, ])

# CommandHighResAngleField
CommandHighResAnglePosition = MessageEnumTraits(0, 'CommandHighResAnglePosition', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad', 'position', 'Position', 'position', True))
CommandHighResAnglePositionLimitMin = MessageEnumTraits(1, 'CommandHighResAnglePositionLimitMin', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad', 'positionLimitMin', 'PositionLimitMin', 'position_limit_min', True))
CommandHighResAnglePositionLimitMax = MessageEnumTraits(2, 'CommandHighResAnglePositionLimitMax', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad', 'positionLimitMax', 'PositionLimitMax', 'position_limit_max', True))
CommandHighResAngleField = EnumType('CommandHighResAngleField', [ CommandHighResAnglePosition, CommandHighResAnglePositionLimitMin, CommandHighResAnglePositionLimitMax, ])




# CommandEnumField
CommandEnumControlStrategy = MessageEnumTraits(0, 'CommandEnumControlStrategy', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'controlStrategy', 'ControlStrategy', 'control_strategy', True))
CommandEnumMstopStrategy = MessageEnumTraits(1, 'CommandEnumMstopStrategy', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'mstopStrategy', 'MstopStrategy', 'mstop_strategy', True))
CommandEnumMinPositionLimitStrategy = MessageEnumTraits(2, 'CommandEnumMinPositionLimitStrategy', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'minPositionLimitStrategy', 'MinPositionLimitStrategy', 'min_position_limit_strategy', True))
CommandEnumMaxPositionLimitStrategy = MessageEnumTraits(3, 'CommandEnumMaxPositionLimitStrategy', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'maxPositionLimitStrategy', 'MaxPositionLimitStrategy', 'max_position_limit_strategy', True))
CommandEnumField = EnumType('CommandEnumField', [ CommandEnumControlStrategy, CommandEnumMstopStrategy, CommandEnumMinPositionLimitStrategy, CommandEnumMaxPositionLimitStrategy, ])

# CommandBoolField
CommandBoolPositionDOnError = MessageEnumTraits(0, 'CommandBoolPositionDOnError', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionDOnError', 'PositionDOnError', 'position_d_on_error', True))
CommandBoolVelocityDOnError = MessageEnumTraits(1, 'CommandBoolVelocityDOnError', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityDOnError', 'VelocityDOnError', 'velocity_d_on_error', True))
CommandBoolEffortDOnError = MessageEnumTraits(2, 'CommandBoolEffortDOnError', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortDOnError', 'EffortDOnError', 'effort_d_on_error', True))
CommandBoolAccelIncludesGravity = MessageEnumTraits(3, 'CommandBoolAccelIncludesGravity', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'accelIncludesGravity', 'AccelIncludesGravity', 'accel_includes_gravity', True))
CommandBoolField = EnumType('CommandBoolField', [ CommandBoolPositionDOnError, CommandBoolVelocityDOnError, CommandBoolEffortDOnError, CommandBoolAccelIncludesGravity, ])

# CommandNumberedFloatField
CommandNumberedFloatDebug = MessageEnumTraits(0, 'CommandNumberedFloatDebug', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
CommandNumberedFloatField = EnumType('CommandNumberedFloatField', [ CommandNumberedFloatDebug, ])

# CommandIoBankField
CommandIoBankA = MessageEnumTraits(0, 'CommandIoBankA', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
CommandIoBankB = MessageEnumTraits(1, 'CommandIoBankB', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
CommandIoBankC = MessageEnumTraits(2, 'CommandIoBankC', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
CommandIoBankD = MessageEnumTraits(3, 'CommandIoBankD', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
CommandIoBankE = MessageEnumTraits(4, 'CommandIoBankE', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
CommandIoBankF = MessageEnumTraits(5, 'CommandIoBankF', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
CommandIoBankField = EnumType('CommandIoBankField', [ CommandIoBankA, CommandIoBankB, CommandIoBankC, CommandIoBankD, CommandIoBankE, CommandIoBankF, ])

# CommandLedField
CommandLedLed = MessageEnumTraits(0, 'CommandLedLed', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'led', 'Led', 'led', True))
CommandLedField = EnumType('CommandLedField', [ CommandLedLed, ])

# CommandStringField
CommandStringName = MessageEnumTraits(0, 'CommandStringName', allow_broadcast=False, not_bcastable_reason='Cannot set same name for all modules in a group.', yields_dict=None, field_details=None)
CommandStringFamily = MessageEnumTraits(1, 'CommandStringFamily', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
CommandStringAppendLog = MessageEnumTraits(2, 'CommandStringAppendLog', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
CommandStringField = EnumType('CommandStringField', [ CommandStringName, CommandStringFamily, CommandStringAppendLog, ])

# CommandFlagField
CommandFlagSaveCurrentSettings = MessageEnumTraits(0, 'CommandFlagSaveCurrentSettings', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'saveCurrentSettings', 'SaveCurrentSettings', 'save_current_settings', True))
CommandFlagReset = MessageEnumTraits(1, 'CommandFlagReset', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'reset', 'Reset', 'reset', True))
CommandFlagBoot = MessageEnumTraits(2, 'CommandFlagBoot', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'boot', 'Boot', 'boot', True))
CommandFlagStopBoot = MessageEnumTraits(3, 'CommandFlagStopBoot', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'stopBoot', 'StopBoot', 'stop_boot', True))
CommandFlagClearLog = MessageEnumTraits(4, 'CommandFlagClearLog', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'clearLog', 'ClearLog', 'clear_log', True))
CommandFlagField = EnumType('CommandFlagField', [ CommandFlagSaveCurrentSettings, CommandFlagReset, CommandFlagBoot, CommandFlagStopBoot, CommandFlagClearLog, ])
# FeedbackFloatField
FeedbackFloatBoardTemperature = MessageEnumTraits(0, 'FeedbackFloatBoardTemperature', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('C', 'boardTemperature', 'BoardTemperature', 'board_temperature', True))
FeedbackFloatProcessorTemperature = MessageEnumTraits(1, 'FeedbackFloatProcessorTemperature', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('C', 'processorTemperature', 'ProcessorTemperature', 'processor_temperature', True))
FeedbackFloatVoltage = MessageEnumTraits(2, 'FeedbackFloatVoltage', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('V', 'voltage', 'Voltage', 'voltage', True))
FeedbackFloatVelocity = MessageEnumTraits(3, 'FeedbackFloatVelocity', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad/s', 'velocity', 'Velocity', 'velocity', True))
FeedbackFloatEffort = MessageEnumTraits(4, 'FeedbackFloatEffort', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('N*m', 'effort', 'Effort', 'effort', True))
FeedbackFloatVelocityCommand = MessageEnumTraits(5, 'FeedbackFloatVelocityCommand', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad/s', 'velocityCommand', 'VelocityCommand', 'velocity_command', True))
FeedbackFloatEffortCommand = MessageEnumTraits(6, 'FeedbackFloatEffortCommand', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('N*m', 'effortCommand', 'EffortCommand', 'effort_command', True))
FeedbackFloatDeflection = MessageEnumTraits(7, 'FeedbackFloatDeflection', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad', 'deflection', 'Deflection', 'deflection', True))
FeedbackFloatDeflectionVelocity = MessageEnumTraits(8, 'FeedbackFloatDeflectionVelocity', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad/s', 'deflectionVelocity', 'DeflectionVelocity', 'deflection_velocity', True))
FeedbackFloatMotorVelocity = MessageEnumTraits(9, 'FeedbackFloatMotorVelocity', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad/s', 'motorVelocity', 'MotorVelocity', 'motor_velocity', True))
FeedbackFloatMotorCurrent = MessageEnumTraits(10, 'FeedbackFloatMotorCurrent', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('A', 'motorCurrent', 'MotorCurrent', 'motor_current', True))
FeedbackFloatMotorSensorTemperature = MessageEnumTraits(11, 'FeedbackFloatMotorSensorTemperature', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('C', 'motorSensorTemperature', 'MotorSensorTemperature', 'motor_sensor_temperature', True))
FeedbackFloatMotorWindingCurrent = MessageEnumTraits(12, 'FeedbackFloatMotorWindingCurrent', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('A', 'motorWindingCurrent', 'MotorWindingCurrent', 'motor_winding_current', True))
FeedbackFloatMotorWindingTemperature = MessageEnumTraits(13, 'FeedbackFloatMotorWindingTemperature', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('C', 'motorWindingTemperature', 'MotorWindingTemperature', 'motor_winding_temperature', True))
FeedbackFloatMotorHousingTemperature = MessageEnumTraits(14, 'FeedbackFloatMotorHousingTemperature', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('C', 'motorHousingTemperature', 'MotorHousingTemperature', 'motor_housing_temperature', True))
FeedbackFloatBatteryLevel = MessageEnumTraits(15, 'FeedbackFloatBatteryLevel', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'batteryLevel', 'BatteryLevel', 'battery_level', True))
FeedbackFloatPwmCommand = MessageEnumTraits(16, 'FeedbackFloatPwmCommand', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'pwmCommand', 'PwmCommand', 'pwm_command', True))
FeedbackFloatField = EnumType('FeedbackFloatField', [ FeedbackFloatBoardTemperature, FeedbackFloatProcessorTemperature, FeedbackFloatVoltage, FeedbackFloatVelocity, FeedbackFloatEffort, FeedbackFloatVelocityCommand, FeedbackFloatEffortCommand, FeedbackFloatDeflection, FeedbackFloatDeflectionVelocity, FeedbackFloatMotorVelocity, FeedbackFloatMotorCurrent, FeedbackFloatMotorSensorTemperature, FeedbackFloatMotorWindingCurrent, FeedbackFloatMotorWindingTemperature, FeedbackFloatMotorHousingTemperature, FeedbackFloatBatteryLevel, FeedbackFloatPwmCommand, ])

# FeedbackHighResAngleField
FeedbackHighResAnglePosition = MessageEnumTraits(0, 'FeedbackHighResAnglePosition', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad', 'position', 'Position', 'position', True))
FeedbackHighResAnglePositionCommand = MessageEnumTraits(1, 'FeedbackHighResAnglePositionCommand', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad', 'positionCommand', 'PositionCommand', 'position_command', True))
FeedbackHighResAngleMotorPosition = MessageEnumTraits(2, 'FeedbackHighResAngleMotorPosition', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad', 'motorPosition', 'MotorPosition', 'motor_position', True))
FeedbackHighResAngleField = EnumType('FeedbackHighResAngleField', [ FeedbackHighResAnglePosition, FeedbackHighResAnglePositionCommand, FeedbackHighResAngleMotorPosition, ])

# FeedbackVector3fField
FeedbackVector3fAccelerometer = MessageEnumTraits(0, 'FeedbackVector3fAccelerometer', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
FeedbackVector3fGyro = MessageEnumTraits(1, 'FeedbackVector3fGyro', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
FeedbackVector3fArPosition = MessageEnumTraits(2, 'FeedbackVector3fArPosition', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
FeedbackVector3fField = EnumType('FeedbackVector3fField', [ FeedbackVector3fAccelerometer, FeedbackVector3fGyro, FeedbackVector3fArPosition, ])

# FeedbackQuaternionfField
FeedbackQuaternionfOrientation = MessageEnumTraits(0, 'FeedbackQuaternionfOrientation', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
FeedbackQuaternionfArOrientation = MessageEnumTraits(1, 'FeedbackQuaternionfArOrientation', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
FeedbackQuaternionfField = EnumType('FeedbackQuaternionfField', [ FeedbackQuaternionfOrientation, FeedbackQuaternionfArOrientation, ])

# FeedbackUInt64Field
FeedbackUInt64SequenceNumber = MessageEnumTraits(0, 'FeedbackUInt64SequenceNumber', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'sequenceNumber', 'SequenceNumber', 'sequence_number', True))
FeedbackUInt64ReceiveTime = MessageEnumTraits(1, 'FeedbackUInt64ReceiveTime', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('us', 'receiveTime', 'ReceiveTime', 'receive_time', True))
FeedbackUInt64TransmitTime = MessageEnumTraits(2, 'FeedbackUInt64TransmitTime', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('us', 'transmitTime', 'TransmitTime', 'transmit_time', True))
FeedbackUInt64HardwareReceiveTime = MessageEnumTraits(3, 'FeedbackUInt64HardwareReceiveTime', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('us', 'hardwareReceiveTime', 'HardwareReceiveTime', 'hardware_receive_time', True))
FeedbackUInt64HardwareTransmitTime = MessageEnumTraits(4, 'FeedbackUInt64HardwareTransmitTime', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('us', 'hardwareTransmitTime', 'HardwareTransmitTime', 'hardware_transmit_time', True))
FeedbackUInt64SenderId = MessageEnumTraits(5, 'FeedbackUInt64SenderId', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'senderId', 'SenderId', 'sender_id', True))
FeedbackUInt64Field = EnumType('FeedbackUInt64Field', [ FeedbackUInt64SequenceNumber, FeedbackUInt64ReceiveTime, FeedbackUInt64TransmitTime, FeedbackUInt64HardwareReceiveTime, FeedbackUInt64HardwareTransmitTime, FeedbackUInt64SenderId, ])

# FeedbackEnumField
FeedbackEnumTemperatureState = MessageEnumTraits(0, 'FeedbackEnumTemperatureState', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'temperatureState', 'TemperatureState', 'temperature_state', True))
FeedbackEnumMstopState = MessageEnumTraits(1, 'FeedbackEnumMstopState', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'mstopState', 'MstopState', 'mstop_state', True))
FeedbackEnumPositionLimitState = MessageEnumTraits(2, 'FeedbackEnumPositionLimitState', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionLimitState', 'PositionLimitState', 'position_limit_state', True))
FeedbackEnumVelocityLimitState = MessageEnumTraits(3, 'FeedbackEnumVelocityLimitState', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityLimitState', 'VelocityLimitState', 'velocity_limit_state', True))
FeedbackEnumEffortLimitState = MessageEnumTraits(4, 'FeedbackEnumEffortLimitState', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortLimitState', 'EffortLimitState', 'effort_limit_state', True))
FeedbackEnumCommandLifetimeState = MessageEnumTraits(5, 'FeedbackEnumCommandLifetimeState', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'commandLifetimeState', 'CommandLifetimeState', 'command_lifetime_state', True))
FeedbackEnumArQuality = MessageEnumTraits(6, 'FeedbackEnumArQuality', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'arQuality', 'ArQuality', 'ar_quality', True))
FeedbackEnumField = EnumType('FeedbackEnumField', [ FeedbackEnumTemperatureState, FeedbackEnumMstopState, FeedbackEnumPositionLimitState, FeedbackEnumVelocityLimitState, FeedbackEnumEffortLimitState, FeedbackEnumCommandLifetimeState, FeedbackEnumArQuality, ])


# FeedbackNumberedFloatField
FeedbackNumberedFloatDebug = MessageEnumTraits(0, 'FeedbackNumberedFloatDebug', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
FeedbackNumberedFloatField = EnumType('FeedbackNumberedFloatField', [ FeedbackNumberedFloatDebug, ])

# FeedbackIoBankField
FeedbackIoBankA = MessageEnumTraits(0, 'FeedbackIoBankA', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
FeedbackIoBankB = MessageEnumTraits(1, 'FeedbackIoBankB', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
FeedbackIoBankC = MessageEnumTraits(2, 'FeedbackIoBankC', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
FeedbackIoBankD = MessageEnumTraits(3, 'FeedbackIoBankD', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
FeedbackIoBankE = MessageEnumTraits(4, 'FeedbackIoBankE', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
FeedbackIoBankF = MessageEnumTraits(5, 'FeedbackIoBankF', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
FeedbackIoBankField = EnumType('FeedbackIoBankField', [ FeedbackIoBankA, FeedbackIoBankB, FeedbackIoBankC, FeedbackIoBankD, FeedbackIoBankE, FeedbackIoBankF, ])

# FeedbackLedField
FeedbackLedLed = MessageEnumTraits(0, 'FeedbackLedLed', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'led', 'Led', 'led', True))
FeedbackLedField = EnumType('FeedbackLedField', [ FeedbackLedLed, ])



# InfoFloatField
InfoFloatPositionKp = MessageEnumTraits(0, 'InfoFloatPositionKp', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionKp', 'PositionKp', 'position_kp', True))
InfoFloatPositionKi = MessageEnumTraits(1, 'InfoFloatPositionKi', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionKi', 'PositionKi', 'position_ki', True))
InfoFloatPositionKd = MessageEnumTraits(2, 'InfoFloatPositionKd', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionKd', 'PositionKd', 'position_kd', True))
InfoFloatPositionFeedForward = MessageEnumTraits(3, 'InfoFloatPositionFeedForward', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionFeedForward', 'PositionFeedForward', 'position_feed_forward', True))
InfoFloatPositionDeadZone = MessageEnumTraits(4, 'InfoFloatPositionDeadZone', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionDeadZone', 'PositionDeadZone', 'position_dead_zone', True))
InfoFloatPositionIClamp = MessageEnumTraits(5, 'InfoFloatPositionIClamp', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionIClamp', 'PositionIClamp', 'position_i_clamp', True))
InfoFloatPositionPunch = MessageEnumTraits(6, 'InfoFloatPositionPunch', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionPunch', 'PositionPunch', 'position_punch', True))
InfoFloatPositionMinTarget = MessageEnumTraits(7, 'InfoFloatPositionMinTarget', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionMinTarget', 'PositionMinTarget', 'position_min_target', True))
InfoFloatPositionMaxTarget = MessageEnumTraits(8, 'InfoFloatPositionMaxTarget', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionMaxTarget', 'PositionMaxTarget', 'position_max_target', True))
InfoFloatPositionTargetLowpass = MessageEnumTraits(9, 'InfoFloatPositionTargetLowpass', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionTargetLowpass', 'PositionTargetLowpass', 'position_target_lowpass', True))
InfoFloatPositionMinOutput = MessageEnumTraits(10, 'InfoFloatPositionMinOutput', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionMinOutput', 'PositionMinOutput', 'position_min_output', True))
InfoFloatPositionMaxOutput = MessageEnumTraits(11, 'InfoFloatPositionMaxOutput', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionMaxOutput', 'PositionMaxOutput', 'position_max_output', True))
InfoFloatPositionOutputLowpass = MessageEnumTraits(12, 'InfoFloatPositionOutputLowpass', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionOutputLowpass', 'PositionOutputLowpass', 'position_output_lowpass', True))
InfoFloatVelocityKp = MessageEnumTraits(13, 'InfoFloatVelocityKp', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityKp', 'VelocityKp', 'velocity_kp', True))
InfoFloatVelocityKi = MessageEnumTraits(14, 'InfoFloatVelocityKi', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityKi', 'VelocityKi', 'velocity_ki', True))
InfoFloatVelocityKd = MessageEnumTraits(15, 'InfoFloatVelocityKd', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityKd', 'VelocityKd', 'velocity_kd', True))
InfoFloatVelocityFeedForward = MessageEnumTraits(16, 'InfoFloatVelocityFeedForward', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityFeedForward', 'VelocityFeedForward', 'velocity_feed_forward', True))
InfoFloatVelocityDeadZone = MessageEnumTraits(17, 'InfoFloatVelocityDeadZone', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityDeadZone', 'VelocityDeadZone', 'velocity_dead_zone', True))
InfoFloatVelocityIClamp = MessageEnumTraits(18, 'InfoFloatVelocityIClamp', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityIClamp', 'VelocityIClamp', 'velocity_i_clamp', True))
InfoFloatVelocityPunch = MessageEnumTraits(19, 'InfoFloatVelocityPunch', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityPunch', 'VelocityPunch', 'velocity_punch', True))
InfoFloatVelocityMinTarget = MessageEnumTraits(20, 'InfoFloatVelocityMinTarget', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityMinTarget', 'VelocityMinTarget', 'velocity_min_target', True))
InfoFloatVelocityMaxTarget = MessageEnumTraits(21, 'InfoFloatVelocityMaxTarget', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityMaxTarget', 'VelocityMaxTarget', 'velocity_max_target', True))
InfoFloatVelocityTargetLowpass = MessageEnumTraits(22, 'InfoFloatVelocityTargetLowpass', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityTargetLowpass', 'VelocityTargetLowpass', 'velocity_target_lowpass', True))
InfoFloatVelocityMinOutput = MessageEnumTraits(23, 'InfoFloatVelocityMinOutput', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityMinOutput', 'VelocityMinOutput', 'velocity_min_output', True))
InfoFloatVelocityMaxOutput = MessageEnumTraits(24, 'InfoFloatVelocityMaxOutput', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityMaxOutput', 'VelocityMaxOutput', 'velocity_max_output', True))
InfoFloatVelocityOutputLowpass = MessageEnumTraits(25, 'InfoFloatVelocityOutputLowpass', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityOutputLowpass', 'VelocityOutputLowpass', 'velocity_output_lowpass', True))
InfoFloatEffortKp = MessageEnumTraits(26, 'InfoFloatEffortKp', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortKp', 'EffortKp', 'effort_kp', True))
InfoFloatEffortKi = MessageEnumTraits(27, 'InfoFloatEffortKi', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortKi', 'EffortKi', 'effort_ki', True))
InfoFloatEffortKd = MessageEnumTraits(28, 'InfoFloatEffortKd', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortKd', 'EffortKd', 'effort_kd', True))
InfoFloatEffortFeedForward = MessageEnumTraits(29, 'InfoFloatEffortFeedForward', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortFeedForward', 'EffortFeedForward', 'effort_feed_forward', True))
InfoFloatEffortDeadZone = MessageEnumTraits(30, 'InfoFloatEffortDeadZone', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortDeadZone', 'EffortDeadZone', 'effort_dead_zone', True))
InfoFloatEffortIClamp = MessageEnumTraits(31, 'InfoFloatEffortIClamp', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortIClamp', 'EffortIClamp', 'effort_i_clamp', True))
InfoFloatEffortPunch = MessageEnumTraits(32, 'InfoFloatEffortPunch', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortPunch', 'EffortPunch', 'effort_punch', True))
InfoFloatEffortMinTarget = MessageEnumTraits(33, 'InfoFloatEffortMinTarget', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortMinTarget', 'EffortMinTarget', 'effort_min_target', True))
InfoFloatEffortMaxTarget = MessageEnumTraits(34, 'InfoFloatEffortMaxTarget', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortMaxTarget', 'EffortMaxTarget', 'effort_max_target', True))
InfoFloatEffortTargetLowpass = MessageEnumTraits(35, 'InfoFloatEffortTargetLowpass', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortTargetLowpass', 'EffortTargetLowpass', 'effort_target_lowpass', True))
InfoFloatEffortMinOutput = MessageEnumTraits(36, 'InfoFloatEffortMinOutput', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortMinOutput', 'EffortMinOutput', 'effort_min_output', True))
InfoFloatEffortMaxOutput = MessageEnumTraits(37, 'InfoFloatEffortMaxOutput', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortMaxOutput', 'EffortMaxOutput', 'effort_max_output', True))
InfoFloatEffortOutputLowpass = MessageEnumTraits(38, 'InfoFloatEffortOutputLowpass', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortOutputLowpass', 'EffortOutputLowpass', 'effort_output_lowpass', True))
InfoFloatSpringConstant = MessageEnumTraits(39, 'InfoFloatSpringConstant', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('N/m', 'springConstant', 'SpringConstant', 'spring_constant', True))
InfoFloatVelocityLimitMin = MessageEnumTraits(40, 'InfoFloatVelocityLimitMin', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad/s', 'velocityLimitMin', 'VelocityLimitMin', 'velocity_limit_min', True))
InfoFloatVelocityLimitMax = MessageEnumTraits(41, 'InfoFloatVelocityLimitMax', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad/s', 'velocityLimitMax', 'VelocityLimitMax', 'velocity_limit_max', True))
InfoFloatEffortLimitMin = MessageEnumTraits(42, 'InfoFloatEffortLimitMin', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('N*m', 'effortLimitMin', 'EffortLimitMin', 'effort_limit_min', True))
InfoFloatEffortLimitMax = MessageEnumTraits(43, 'InfoFloatEffortLimitMax', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('N*m', 'effortLimitMax', 'EffortLimitMax', 'effort_limit_max', True))
InfoFloatField = EnumType('InfoFloatField', [ InfoFloatPositionKp, InfoFloatPositionKi, InfoFloatPositionKd, InfoFloatPositionFeedForward, InfoFloatPositionDeadZone, InfoFloatPositionIClamp, InfoFloatPositionPunch, InfoFloatPositionMinTarget, InfoFloatPositionMaxTarget, InfoFloatPositionTargetLowpass, InfoFloatPositionMinOutput, InfoFloatPositionMaxOutput, InfoFloatPositionOutputLowpass, InfoFloatVelocityKp, InfoFloatVelocityKi, InfoFloatVelocityKd, InfoFloatVelocityFeedForward, InfoFloatVelocityDeadZone, InfoFloatVelocityIClamp, InfoFloatVelocityPunch, InfoFloatVelocityMinTarget, InfoFloatVelocityMaxTarget, InfoFloatVelocityTargetLowpass, InfoFloatVelocityMinOutput, InfoFloatVelocityMaxOutput, InfoFloatVelocityOutputLowpass, InfoFloatEffortKp, InfoFloatEffortKi, InfoFloatEffortKd, InfoFloatEffortFeedForward, InfoFloatEffortDeadZone, InfoFloatEffortIClamp, InfoFloatEffortPunch, InfoFloatEffortMinTarget, InfoFloatEffortMaxTarget, InfoFloatEffortTargetLowpass, InfoFloatEffortMinOutput, InfoFloatEffortMaxOutput, InfoFloatEffortOutputLowpass, InfoFloatSpringConstant, InfoFloatVelocityLimitMin, InfoFloatVelocityLimitMax, InfoFloatEffortLimitMin, InfoFloatEffortLimitMax, ])

# InfoHighResAngleField
InfoHighResAnglePositionLimitMin = MessageEnumTraits(0, 'InfoHighResAnglePositionLimitMin', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad', 'positionLimitMin', 'PositionLimitMin', 'position_limit_min', True))
InfoHighResAnglePositionLimitMax = MessageEnumTraits(1, 'InfoHighResAnglePositionLimitMax', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('rad', 'positionLimitMax', 'PositionLimitMax', 'position_limit_max', True))
InfoHighResAngleField = EnumType('InfoHighResAngleField', [ InfoHighResAnglePositionLimitMin, InfoHighResAnglePositionLimitMax, ])




# InfoEnumField
InfoEnumControlStrategy = MessageEnumTraits(0, 'InfoEnumControlStrategy', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'controlStrategy', 'ControlStrategy', 'control_strategy', True))
InfoEnumCalibrationState = MessageEnumTraits(1, 'InfoEnumCalibrationState', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'calibrationState', 'CalibrationState', 'calibration_state', True))
InfoEnumMstopStrategy = MessageEnumTraits(2, 'InfoEnumMstopStrategy', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'mstopStrategy', 'MstopStrategy', 'mstop_strategy', True))
InfoEnumMinPositionLimitStrategy = MessageEnumTraits(3, 'InfoEnumMinPositionLimitStrategy', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'minPositionLimitStrategy', 'MinPositionLimitStrategy', 'min_position_limit_strategy', True))
InfoEnumMaxPositionLimitStrategy = MessageEnumTraits(4, 'InfoEnumMaxPositionLimitStrategy', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'maxPositionLimitStrategy', 'MaxPositionLimitStrategy', 'max_position_limit_strategy', True))
InfoEnumField = EnumType('InfoEnumField', [ InfoEnumControlStrategy, InfoEnumCalibrationState, InfoEnumMstopStrategy, InfoEnumMinPositionLimitStrategy, InfoEnumMaxPositionLimitStrategy, ])

# InfoBoolField
InfoBoolPositionDOnError = MessageEnumTraits(0, 'InfoBoolPositionDOnError', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'positionDOnError', 'PositionDOnError', 'position_d_on_error', True))
InfoBoolVelocityDOnError = MessageEnumTraits(1, 'InfoBoolVelocityDOnError', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'velocityDOnError', 'VelocityDOnError', 'velocity_d_on_error', True))
InfoBoolEffortDOnError = MessageEnumTraits(2, 'InfoBoolEffortDOnError', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'effortDOnError', 'EffortDOnError', 'effort_d_on_error', True))
InfoBoolAccelIncludesGravity = MessageEnumTraits(3, 'InfoBoolAccelIncludesGravity', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'accelIncludesGravity', 'AccelIncludesGravity', 'accel_includes_gravity', True))
InfoBoolField = EnumType('InfoBoolField', [ InfoBoolPositionDOnError, InfoBoolVelocityDOnError, InfoBoolEffortDOnError, InfoBoolAccelIncludesGravity, ])



# InfoLedField
InfoLedLed = MessageEnumTraits(0, 'InfoLedLed', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'led', 'Led', 'led', True))
InfoLedField = EnumType('InfoLedField', [ InfoLedLed, ])

# InfoStringField
InfoStringName = MessageEnumTraits(0, 'InfoStringName', allow_broadcast=False, not_bcastable_reason='Cannot set same name for all modules in a group.', yields_dict=None, field_details=None)
InfoStringFamily = MessageEnumTraits(1, 'InfoStringFamily', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
InfoStringSerial = MessageEnumTraits(2, 'InfoStringSerial', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=None)
InfoStringField = EnumType('InfoStringField', [ InfoStringName, InfoStringFamily, InfoStringSerial, ])

# InfoFlagField
InfoFlagSaveCurrentSettings = MessageEnumTraits(0, 'InfoFlagSaveCurrentSettings', allow_broadcast=True, not_bcastable_reason=None, yields_dict=None, field_details=FieldDetails('None', 'saveCurrentSettings', 'SaveCurrentSettings', 'save_current_settings', True))
InfoFlagField = EnumType('InfoFlagField', [ InfoFlagSaveCurrentSettings, ])
