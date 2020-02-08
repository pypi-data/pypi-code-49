"""INSTEON PLM constants for reuse across the module."""

from enum import Enum

DEVICE_CATEGORY_GENERALIZED_CONTROLLERS_0X00 = 0x00
DEVICE_CATEGORY_DIMMABLE_LIGHTING_CONTROL_0X01 = 0x01
DEVICE_CATEGORY_SWITCHED_LIGHTING_CONTROL_0X02 = 0x02
DEVICE_CATEGORY_NETWORK_BRIDGES_0X03 = 0x03
DEVICE_CATEGORY_IRRIGATION_CONTROL_0X04 = 0x04
DEVICE_CATEGORY_CLIMATE_CONTROL_0X05 = 0x05
DEVICE_CATEGORY_SENSORS_AND_ACTUATORS_0X07 = 0x07
DEVICE_CATEGORY_HOME_ENTERTAINMENT_0X08 = 0x08
DEVICE_CATEGORY_ENERGY_MANAGEMENT_0X09 = 0x09
DEVICE_CATEGORY_BUILT_IN_APPLIANCE_CONTROL_0X0A = 0x0A
DEVICE_CATEGORY_PLUMBING_0X0B = 0x0B
DEVICE_CATEGORY_COMMUNICATION_0X0C = 0x0C
DEVICE_CATEGORY_COMPUTER_CONTROL_0X0D = 0x0D
DEVICE_CATEGORY_WINDOW_COVERINGS_0X0E = 0x0E
DEVICE_CATEGORY_ACCESS_CONTROL_0X0F = 0x0F
DEVICE_CATEGORY_SECURITY_HEALTH_SAFETY_0X10 = 0x10
DEVICE_CATEGORY_SURVEILLANCE_0X11 = 0x11
DEVICE_CATEGORY_AUTOMOTIVE_0X12 = 0x12
DEVICE_CATEGORY_PET_CARE_0X13 = 0x13
DEVICE_CATEGORY_TIMEKEEPING_0X15 = 0x15
DEVICE_CATEGORY_HOLIDAY_0X16 = 0x16

COMMAND_ASSIGN_TO_ALL_LINK_GROUP_0X01_NONE = {"cmd1": 0x01, "cmd2": None}
COMMAND_DELETE_FROM_ALL_LINK_GROUP_0X02_NONE = {"cmd1": 0x02, "cmd2": None}
COMMAND_PRODUCT_DATA_REQUEST_0X03_0X00 = {"cmd1": 0x03, "cmd2": 0x00}
COMMAND_FX_USERNAME_0X03_0X01 = {"cmd1": 0x03, "cmd2": 0x01}
COMMAND_DEVICE_TEXT_STRING_REQUEST_0X03_0X02 = {"cmd1": 0x03, "cmd2": 0x02}
COMMAND_ENTER_LINKING_MODE_0X09_NONE = {"cmd1": 0x09, "cmd2": None}
COMMAND_ENTER_UNLINKING_MODE_0X0A_NONE = {"cmd1": 0x0A, "cmd2": None}
COMMAND_GET_INSTEON_ENGINE_VERSION_0X0D_0X00 = {"cmd1": 0x0D, "cmd2": 0x00}
COMMAND_PING_0X0F_0X00 = {"cmd1": 0x0F, "cmd2": 0x00}
COMMAND_ID_REQUEST_0X10_0X00 = {"cmd1": 0x10, "cmd2": 0x00}
COMMAND_ID_REQUEST_RESPONSE_0X10_0X10 = {"cmd1": 0x10, "cmd2": 0x10}
COMMAND_LIGHT_ON_0X11_NONE = {"cmd1": 0x11, "cmd2": None}
COMMAND_LIGHT_ON_FAST_0X12_NONE = {"cmd1": 0x12, "cmd2": None}
COMMAND_LIGHT_OFF_0X13_0X00 = {"cmd1": 0x13, "cmd2": 0x00}
COMMAND_LIGHT_OFF_FAST_0X14_0X00 = {"cmd1": 0x14, "cmd2": 0x00}
COMMAND_LIGHT_BRIGHTEN_ONE_STEP_0X15_0X00 = {"cmd1": 0x15, "cmd2": 0x00}
COMMAND_LIGHT_DIM_ONE_STEP_0X16_0X00 = {"cmd1": 0x16, "cmd2": 0x00}
COMMAND_LIGHT_START_MANUAL_CHANGEDOWN_0X17_0X00 = {"cmd1": 0x17, "cmd2": 0x00}
COMMAND_LIGHT_START_MANUAL_CHANGEUP_0X17_0X01 = {"cmd1": 0x17, "cmd2": 0x01}
COMMAND_LIGHT_STOP_MANUAL_CHANGE_0X18_0X00 = {"cmd1": 0x18, "cmd2": 0x00}
COMMAND_LIGHT_STATUS_REQUEST_0X19_0X00 = {"cmd1": 0x19, "cmd2": 0x00}
COMMAND_LIGHT_STATUS_REQUEST_0X19_0X01 = {"cmd1": 0x19, "cmd2": 0x01}
COMMAND_LIGHT_STATUS_REQUEST_0X19_NONE = {"cmd1": 0x19, "cmd2": None}
COMMAND_GET_OPERATING_FLAGS_0X1F_NONE = {"cmd1": 0x1F, "cmd2": None}
COMMAND_SET_OPERATING_FLAGS_0X20_NONE = {"cmd1": 0x20, "cmd2": None}
COMMAND_LIGHT_INSTANT_CHANGE_0X21_NONE = {"cmd1": 0x21, "cmd2": None}
COMMAND_LIGHT_MANUALLY_TURNED_OFF_0X22_0X00 = {"cmd1": 0x22, "cmd2": 0x00}
COMMAND_LIGHT_MANUALLY_TURNED_OFF_0X22_0X00 = {"cmd1": 0x22, "cmd2": 0x00}
COMMAND_LIGHT_MANUALLY_TURNED_ON_0X23_0X00 = {"cmd1": 0x23, "cmd2": 0x00}
COMMAND_LIGHT_MANUALLY_TURNED_ON_0X23_0X00 = {"cmd1": 0x23, "cmd2": 0x00}
COMMAND_REMOTE_SET_BUTTON_TAP1_TAP_0X25_0X01 = {"cmd1": 0x25, "cmd2": 0x01}
COMMAND_REMOTE_SET_BUTTON_TAP2_TAP_0X25_0X02 = {"cmd1": 0x25, "cmd2": 0x02}
COMMAND_LIGHT_SET_STATUS_0X27_NONE = {"cmd1": 0x27, "cmd2": None}
COMMAND_SET_ADDRESS_MSB_0X28_NONE = {"cmd1": 0x28, "cmd2": None}
COMMAND_POKE_ONE_BYTE_0X29_NONE = {"cmd1": 0x29, "cmd2": None}
COMMAND_RESERVED_0X2A_NONE = {"cmd1": 0x2A, "cmd2": None}
COMMAND_PEEK_ONE_BYTE_0X2B_NONE = {"cmd1": 0x2B, "cmd2": None}
COMMAND_PEEK_ONE_BYTE_INTERNAL_0X2C_NONE = {"cmd1": 0x2C, "cmd2": None}
COMMAND_POKE_ONE_BYTE_INTERNAL_0X2D_NONE = {"cmd1": 0x2D, "cmd2": None}
COMMAND_LIGHT_ON_AT_RAMP_RATE_0X2E_NONE = {"cmd1": 0x2E, "cmd2": None}
COMMAND_EXTENDED_GET_SET_0X2E_0X00 = {"cmd1": 0x2E, "cmd2": 0x00}
COMMAND_LIGHT_OFF_AT_RAMP_RATE_0X2F_NONE = {"cmd1": 0x2F, "cmd2": None}
COMMAND_EXTENDED_READ_WRITE_ALDB_0X2F_0X00 = {"cmd1": 0x2F, "cmd2": 0x00}
COMMAND_EXTENDED_TRIGGER_ALL_LINK_0X30_0X00 = {"cmd1": 0x30, "cmd2": 0x00}
COMMAND_SPRINKLER_VALVE_ON_0X40_NONE = {"cmd1": 0x40, "cmd2": None}
COMMAND_SPRINKLER_VALVE_OFF_0X41_NONE = {"cmd1": 0x41, "cmd2": None}
COMMAND_SPRINKLER_PROGRAM_ON_0X42_NONE = {"cmd1": 0x42, "cmd2": None}
COMMAND_SPRINKLER_PROGRAM_OFF_0X43_NONE = {"cmd1": 0x43, "cmd2": None}
COMMAND_SPRINKLER_CONTROLLOAD_INITIALIZATION_VALUES_0X44_0X00 = {
    "cmd1": 0x44,
    "cmd2": 0x00,
}
COMMAND_SPRINKLER_CONTROLLOAD_EEPROM_FROM_RAM_0X44_0X01 = {"cmd1": 0x44, "cmd2": 0x01}
COMMAND_SPRINKLER_CONTROLGET_VALVE_STATUS_0X44_0X02 = {"cmd1": 0x44, "cmd2": 0x02}
COMMAND_SPRINKLER_CONTROLINHIBIT_COMMAND_ACCEPTANCE_0X44_0X03 = {
    "cmd1": 0x44,
    "cmd2": 0x03,
}
COMMAND_SPRINKLER_CONTROLRESUME_COMMAND_ACCEPTANCE_0X44_0X04 = {
    "cmd1": 0x44,
    "cmd2": 0x04,
}
COMMAND_SPRINKLER_CONTROLSKIP_FORWARD_0X44_0X05 = {"cmd1": 0x44, "cmd2": 0x05}
COMMAND_SPRINKLER_CONTROLSKIP_BACK_0X44_0X06 = {"cmd1": 0x44, "cmd2": 0x06}
COMMAND_SPRINKLER_CONTROLENABLE_PUMP_ON_V8_0X44_0X07 = {"cmd1": 0x44, "cmd2": 0x07}
COMMAND_SPRINKLER_CONTROLDISABLE_PUMP_ON_V8_0X44_0X08 = {"cmd1": 0x44, "cmd2": 0x08}
COMMAND_SPRINKLER_CONTROLBROADCAST_ON_0X44_0X09 = {"cmd1": 0x44, "cmd2": 0x09}
COMMAND_SPRINKLER_CONTROLBROADCAST_OFF_0X44_0X0A = {"cmd1": 0x44, "cmd2": 0x0A}
COMMAND_SPRINKLER_CONTROLLOAD_RAM_FROM_EEPROM_0X44_0X0B = {"cmd1": 0x44, "cmd2": 0x0B}
COMMAND_SPRINKLER_CONTROLSENSOR_ON_0X44_0X0C = {"cmd1": 0x44, "cmd2": 0x0C}
COMMAND_SPRINKLER_CONTROLSENSOR_OFF_0X44_0X0D = {"cmd1": 0x44, "cmd2": 0x0D}
COMMAND_SPRINKLER_CONTROLDIAGNOSTICS_ON_0X44_0X0E = {"cmd1": 0x44, "cmd2": 0x0E}
COMMAND_SPRINKLER_CONTROLDIAGNOSTICS_OFF_0X44_0X0F = {"cmd1": 0x44, "cmd2": 0x0F}
COMMAND_SPRINKLER_GET_PROGRAM_REQUEST_0X45_NONE = {"cmd1": 0x45, "cmd2": None}
COMMAND_IO_OUTPUT_ON_0X45_NONE = {"cmd1": 0x45, "cmd2": None}
COMMAND_IO_OUTPUT_OFF_0X46_NONE = {"cmd1": 0x46, "cmd2": None}
COMMAND_IO_ALARM_DATA_REQUEST_0X47_0X00 = {"cmd1": 0x47, "cmd2": 0x00}
COMMAND_IO_WRITE_OUTPUT_PORT_0X48_NONE = {"cmd1": 0x48, "cmd2": None}
COMMAND_IO_READ_INPUT_PORT_0X49_0X00 = {"cmd1": 0x49, "cmd2": 0x00}
COMMAND_IO_GET_SENSOR_VALUE_0X4A_NONE = {"cmd1": 0x4A, "cmd2": None}
COMMAND_IO_SET_SENSOR_1_NOMINAL_VALUE_0X4B_NONE = {"cmd1": 0x4B, "cmd2": None}
COMMAND_IO_GET_SENSOR_ALARM_DELTA_0X4C_NONE = {"cmd1": 0x4C, "cmd2": None}
COMMAND_FAN_STATUS_REPORT_0X4C_NONE = {"cmd1": 0x4C, "cmd2": None}
COMMAND_IO_WRITE_CONFIGURATION_PORT_0X4D_NONE = {"cmd1": 0x4D, "cmd2": None}
COMMAND_IO_READ_CONFIGURATION_PORT_0X4E_0X00 = {"cmd1": 0x4E, "cmd2": 0x00}
COMMAND_IO_MODULE_CONTROLLOAD_INITIALIZATION_VALUES_0X4F_0X00 = {
    "cmd1": 0x4F,
    "cmd2": 0x00,
}
COMMAND_IO_MODULE_CONTROLLOAD_EEPROM_FROM_RAM_0X4F_0X01 = {"cmd1": 0x4F, "cmd2": 0x01}
COMMAND_IO_MODULE_CONTROLSTATUS_REQUEST_0X4F_0X02 = {"cmd1": 0x4F, "cmd2": 0x02}
COMMAND_IO_MODULE_CONTROLREAD_ANALOG_ONCE_0X4F_0X03 = {"cmd1": 0x4F, "cmd2": 0x03}
COMMAND_IO_MODULE_CONTROLREAD_ANALOG_ALWAYS_0X4F_0X04 = {"cmd1": 0x4F, "cmd2": 0x04}
COMMAND_IO_MODULE_CONTROLENABLE_STATUS_CHANGE_MESSAGE_0X4F_0X09 = {
    "cmd1": 0x4F,
    "cmd2": 0x09,
}
COMMAND_IO_MODULE_CONTROLDISABLE_STATUS_CHANGE_MESSAGE_0X4F_0X0A = {
    "cmd1": 0x4F,
    "cmd2": 0x0A,
}
COMMAND_IO_MODULE_CONTROLLOAD_RAM_FROM_EEPROM_0X4F_0X0B = {"cmd1": 0x4F, "cmd2": 0x0B}
COMMAND_IO_MODULE_CONTROLSENSOR_ON_0X4F_0X0C = {"cmd1": 0x4F, "cmd2": 0x0C}
COMMAND_IO_MODULE_CONTROLSENSOR_OFF_0X4F_0X0D = {"cmd1": 0x4F, "cmd2": 0x0D}
COMMAND_IO_MODULE_CONTROLDIAGNOSTICS_ON_0X4F_0X0E = {"cmd1": 0x4F, "cmd2": 0x0E}
COMMAND_IO_MODULE_CONTROLDIAGNOSTICS_OFF_0X4F_0X0F = {"cmd1": 0x4F, "cmd2": 0x0F}
COMMAND_POOL_DEVICE_ONPOOL_0X50_0X01 = {"cmd1": 0x50, "cmd2": 0x01}
COMMAND_POOL_DEVICE_ONSPA_0X50_0X02 = {"cmd1": 0x50, "cmd2": 0x02}
COMMAND_POOL_DEVICE_ONHEAT_0X50_0X03 = {"cmd1": 0x50, "cmd2": 0x03}
COMMAND_POOL_DEVICE_ONPUMP_0X50_0X04 = {"cmd1": 0x50, "cmd2": 0x04}
COMMAND_POOL_DEVICE_ONAUX_0X50_NONE = {"cmd1": 0x50, "cmd2": None}
COMMAND_POOL_DEVICE_OFF_0X51_NONE = {"cmd1": 0x51, "cmd2": None}
COMMAND_POOL_TEMPERATURE_UP_0X52_NONE = {"cmd1": 0x52, "cmd2": None}
COMMAND_POOL_TEMPERATURE_DOWN_0X53_NONE = {"cmd1": 0x53, "cmd2": None}
COMMAND_POOL_CONTROLLOAD_INITIALIZATION_VALUES_0X54_0X00 = {"cmd1": 0x54, "cmd2": 0x00}
COMMAND_POOL_CONTROLLOAD_EEPROM_FROM_RAM_0X54_0X01 = {"cmd1": 0x54, "cmd2": 0x01}
COMMAND_POOL_CONTROLGET_POOL_MODE_0X54_0X02 = {"cmd1": 0x54, "cmd2": 0x02}
COMMAND_POOL_CONTROLGET_AMBIENT_TEMPERATURE_0X54_0X03 = {"cmd1": 0x54, "cmd2": 0x03}
COMMAND_POOL_CONTROLGET_WATER_TEMPERATURE_0X54_0X04 = {"cmd1": 0x54, "cmd2": 0x04}
COMMAND_POOL_CONTROLGET_PH_0X54_0X05 = {"cmd1": 0x54, "cmd2": 0x05}
COMMAND_DOOR_MOVERAISE_DOOR_0X58_0X00 = {"cmd1": 0x58, "cmd2": 0x00}
COMMAND_DOOR_MOVELOWER_DOOR_0X58_0X01 = {"cmd1": 0x58, "cmd2": 0x01}
COMMAND_DOOR_MOVEOPEN_DOOR_0X58_0X02 = {"cmd1": 0x58, "cmd2": 0x02}
COMMAND_DOOR_MOVECLOSE_DOOR_0X58_0X03 = {"cmd1": 0x58, "cmd2": 0x03}
COMMAND_DOOR_MOVESTOP_DOOR_0X58_0X04 = {"cmd1": 0x58, "cmd2": 0x04}
COMMAND_DOOR_MOVESINGLE_DOOR_OPEN_0X58_0X05 = {"cmd1": 0x58, "cmd2": 0x05}
COMMAND_DOOR_MOVESINGLE_DOOR_CLOSE_0X58_0X06 = {"cmd1": 0x58, "cmd2": 0x06}
COMMAND_DOOR_STATUS_REPORTRAISE_DOOR_0X59_0X00 = {"cmd1": 0x59, "cmd2": 0x00}
COMMAND_DOOR_STATUS_REPORTLOWER_DOOR_0X59_0X01 = {"cmd1": 0x59, "cmd2": 0x01}
COMMAND_DOOR_STATUS_REPORTOPEN_DOOR_0X59_0X02 = {"cmd1": 0x59, "cmd2": 0x02}
COMMAND_DOOR_STATUS_REPORTCLOSE_DOOR_0X59_0X03 = {"cmd1": 0x59, "cmd2": 0x03}
COMMAND_DOOR_STATUS_REPORTSTOP_DOOR_0X59_0X04 = {"cmd1": 0x59, "cmd2": 0x04}
COMMAND_DOOR_STATUS_REPORTSINGLE_DOOR_OPEN_0X59_0X05 = {"cmd1": 0x59, "cmd2": 0x05}
COMMAND_DOOR_STATUS_REPORTSINGLE_DOOR_CLOSE_0X59_0X06 = {"cmd1": 0x59, "cmd2": 0x06}
COMMAND_WINDOW_COVERINGOPEN_0X60_0X01 = {"cmd1": 0x60, "cmd2": 0x01}
COMMAND_WINDOW_COVERINGCLOSE_0X60_0X02 = {"cmd1": 0x60, "cmd2": 0x02}
COMMAND_WINDOW_COVERINGSTOP_0X60_0X03 = {"cmd1": 0x60, "cmd2": 0x03}
COMMAND_WINDOW_COVERINGPROGRAM_0X60_0X04 = {"cmd1": 0x60, "cmd2": 0x04}
COMMAND_WINDOW_COVERING_POSITION_0X61_NONE = {"cmd1": 0x61, "cmd2": None}
COMMAND_THERMOSTAT_TEMPERATURE_UP_0X68_NONE = {"cmd1": 0x68, "cmd2": None}
COMMAND_THERMOSTAT_TEMPERATURE_DOWN_0X69_NONE = {"cmd1": 0x69, "cmd2": None}
COMMAND_THERMOSTAT_GET_ZONE_INFORMATION_0X6A_NONE = {"cmd1": 0x6A, "cmd2": None}
COMMAND_THERMOSTAT_CONTROL_LOAD_INITIALIZATION_VALUES_0X6B_0X00 = {
    "cmd1": 0x6B,
    "cmd2": 0x00,
}
COMMAND_THERMOSTAT_CONTROL_LOAD_EEPROM_FROM_RAM_0X6B_0X01 = {"cmd1": 0x6B, "cmd2": 0x01}
COMMAND_THERMOSTAT_CONTROL_GET_MODE_0X6B_0X02 = {"cmd1": 0x6B, "cmd2": 0x02}
COMMAND_THERMOSTAT_CONTROL_GET_AMBIENT_TEMPERATURE_0X6B_0X03 = {
    "cmd1": 0x6B,
    "cmd2": 0x03,
}
COMMAND_THERMOSTAT_CONTROL_ON_HEAT_0X6B_0X04 = {"cmd1": 0x6B, "cmd2": 0x04}
COMMAND_THERMOSTAT_CONTROL_ON_COOL_0X6B_0X05 = {"cmd1": 0x6B, "cmd2": 0x05}
COMMAND_THERMOSTAT_CONTROL_ON_AUTO_0X6B_0X06 = {"cmd1": 0x6B, "cmd2": 0x06}
COMMAND_THERMOSTAT_CONTROL_ON_FAN_0X6B_0X07 = {"cmd1": 0x6B, "cmd2": 0x07}
COMMAND_THERMOSTAT_CONTROL_OFF_FAN_0X6B_0X08 = {"cmd1": 0x6B, "cmd2": 0x08}
COMMAND_THERMOSTAT_CONTROL_OFF_ALL_0X6B_0X09 = {"cmd1": 0x6B, "cmd2": 0x09}
COMMAND_THERMOSTAT_CONTROL_PROGRAM_HEAT_0X6B_0X0A = {"cmd1": 0x6B, "cmd2": 0x0A}
COMMAND_THERMOSTAT_CONTROL_PROGRAM_COOL_0X6B_0X0B = {"cmd1": 0x6B, "cmd2": 0x0B}
COMMAND_THERMOSTAT_CONTROL_PROGRAM_AUTO_0X6B_0X0C = {"cmd1": 0x6B, "cmd2": 0x0C}
COMMAND_THERMOSTAT_CONTROL_GET_EQUIPMENT_STATE_0X6B_0X0D = {"cmd1": 0x6B, "cmd2": 0x0D}
COMMAND_THERMOSTAT_CONTROL_SET_EQUIPMENT_STATE_0X6B_0X0E = {"cmd1": 0x6B, "cmd2": 0x0E}
COMMAND_THERMOSTAT_CONTROL_GET_TEMPERATURE_UNITS_0X6B_0X0F = {
    "cmd1": 0x6B,
    "cmd2": 0x0F,
}
COMMAND_THERMOSTAT_CONTROL_SET_FAHRENHEIT_0X6B_0X10 = {"cmd1": 0x6B, "cmd2": 0x10}
COMMAND_THERMOSTAT_CONTROL_SET_CELSIUS_0X6B_0X11 = {"cmd1": 0x6B, "cmd2": 0x11}
COMMAND_THERMOSTAT_CONTROL_GET_FAN_ON_SPEED_0X6B_0X12 = {"cmd1": 0x6B, "cmd2": 0x12}
COMMAND_THERMOSTAT_CONTROL_SET_FAN_ON_SPEED_LOW_0X6B_0X13 = {"cmd1": 0x6B, "cmd2": 0x13}
COMMAND_THERMOSTAT_CONTROL_SET_FAN_ON_SPEED_MEDIUM_0X6B_0X14 = {
    "cmd1": 0x6B,
    "cmd2": 0x14,
}
COMMAND_THERMOSTAT_CONTROL_SET_FAN_ON_SPEED_HIGH_0X6B_0X15 = {
    "cmd1": 0x6B,
    "cmd2": 0x15,
}
COMMAND_THERMOSTAT_CONTROL_ENABLE_STATUS_CHANGE_MESSAGE_0X6B_0X16 = {
    "cmd1": 0x6B,
    "cmd2": 0x16,
}
COMMAND_THERMOSTAT_CONTROL_DISABLE_STATUS_CHANGE_MESSAGE_0X6B_0X17 = {
    "cmd1": 0x6B,
    "cmd2": 0x17,
}
COMMAND_THERMOSTAT_SET_COOL_SETPOINT_0X6C_NONE = {"cmd1": 0x6C, "cmd2": None}
COMMAND_THERMOSTAT_SET_HEAT_SETPOINT_0X6D_NONE = {"cmd1": 0x6D, "cmd2": None}
COMMAND_THERMOSTAT_TEMPERATURE_STATUS_0X6E_NONE = {"cmd1": 0x6E, "cmd2": None}
COMMAND_THERMOSTAT_HUMIDITY_STATUS_0X6F_NONE = {"cmd1": 0x6F, "cmd2": None}
COMMAND_THERMOSTAT_MODE_STATUS_0X70_NONE = {"cmd1": 0x70, "cmd2": None}
COMMAND_THERMOSTAT_COOL_SET_POINT_STATUS_0X71_NONE = {"cmd1": 0x71, "cmd2": None}
COMMAND_THERMOSTAT_HEAT_SET_POINT_STATUS_0X72_NONE = {"cmd1": 0x72, "cmd2": None}

COMMAND_LEAK_DETECTOR_ANNOUNCE_0X70_NONE = {"cmd1": 0x70, "cmd2": None}
COMMAND_ASSIGN_TO_COMPANION_GROUP_0X81_0X00 = {"cmd1": 0x81, "cmd2": 0x00}

MESSAGE_START_CODE_0X02 = 0x02

MESSAGE_STANDARD_MESSAGE_RECEIVED_0X50 = 0x50
MESSAGE_EXTENDED_MESSAGE_RECEIVED_0X51 = 0x51
MESSAGE_X10_MESSAGE_RECEIVED_0X52 = 0x52
MESSAGE_ALL_LINKING_COMPLETED_0X53 = 0x53
MESSAGE_BUTTON_EVENT_REPORT_0X54 = 0x54
MESSAGE_USER_RESET_DETECTED_0X55 = 0x55
MESSAGE_ALL_LINK_CEANUP_FAILURE_REPORT_0X56 = 0x56
MESSAGE_ALL_LINK_RECORD_RESPONSE_0X57 = 0x57
MESSAGE_ALL_LINK_CLEANUP_STATUS_REPORT_0X58 = 0x58
MESSAGE_GET_IM_INFO_0X60 = 0x60
MESSAGE_SEND_ALL_LINK_COMMAND_0X61 = 0x61
MESSAGE_SEND_STANDARD_MESSAGE_0X62 = 0x62
MESSAGE_SEND_EXTENDED_MESSAGE_0X62 = 0x62
MESSAGE_X10_MESSAGE_SEND_0X63 = 0x63
MESSAGE_START_ALL_LINKING_0X64 = 0x64
MESSAGE_CANCEL_ALL_LINKING_0X65 = 0x65
MESSAGE_RESET_IM_0X67 = 0x67
MESSAGE_GET_FIRST_ALL_LINK_RECORD_0X69 = 0x69
MESSAGE_GET_NEXT_ALL_LINK_RECORD_0X6A = 0x6A
MESSAGE_SET_IM_CONFIGURATION_0X6B = 0x6B
MESSAGE_MANAGE_ALL_LINK_RECORD_0X6F = 0x6F
MESSAGE_GET_IM_CONFIGURATION_0X73 = 0x73

MESSAGE_STANDARD_MESSAGE_RECIEVED_SIZE = 11
MESSAGE_EXTENDED_MESSAGE_RECEIVED_SIZE = 25
MESSAGE_X10_MESSAGE_RECEIVED_SIZE = 4
MESSAGE_X10_MESSAGE_SEND_SIZE = 4
MESSAGE_X10_MESSAGE_SEND_RECEIVED_SIZE = 5
MESSAGE_ALL_LINKING_COMPLETED_SIZE = 10
MESSAGE_BUTTON_EVENT_REPORT_SIZE = 3
MESSAGE_USER_RESET_DETECTED_SIZE = 2
MESSAGE_ALL_LINK_CEANUP_FAILURE_REPORT_SIZE = 7
MESSAGE_ALL_LINK_RECORD_RESPONSE_SIZE = 10
MESSAGE_ALL_LINK_CLEANUP_STATUS_REPORT_SIZE = 3
MESSAGE_GET_IM_INFO_SIZE = 2
MESSAGE_GET_IM_INFO_RECEIVED_SIZE = 9
MESSAGE_SEND_ALL_LINK_COMMAND_SIZE = 5
MESSAGE_SEND_ALL_LINK_COMMAND_RECEIVED_SIZE = 6
MESSAGE_SEND_STANDARD_MESSAGE_SIZE = 8
MESSAGE_SEND_STANDARD_MESSAGE_RECEIVED_SIZE = 9
MESSAGE_SEND_EXTENDED_MESSAGE_SIZE = 22
MESSAGE_SEND_EXTENDED_MESSAGE_RECEIVED_SIZE = 23
MESSAGE_START_ALL_LINKING_SIZE = 4
MESSAGE_START_ALL_LINKING_RECEIVED_SIZE = 5
MESSAGE_CANCEL_ALL_LINKING_SIZE = 2
MESSAGE_CANCEL_ALL_LINKING_RECEIVED_SIZE = 3
MESSAGE_RESET_IM_SIZE = 2
MESSAGE_RESET_IM_RECEIVED_SIZE = 3
MESSAGE_GET_FIRST_ALL_LINK_RECORD_SIZE = 2
MESSAGE_GET_FIRST_ALL_LINK_RECORD_RECEIVED_SIZE = 3
MESSAGE_GET_NEXT_ALL_LINK_RECORD_SIZE = 2
MESSAGE_GET_NEXT_ALL_LINK_RECORD_RECEIVED_SIZE = 3
MESSAGE_SET_IM_CONFIGURATION_SIZE = 3
MESSAGE_SET_IM_CONFIGURATION_RECEIVED_SIZE = 4
MESSAGE_MANAGE_ALL_LINK_RECORD_SIZE = 11
MESSAGE_MANAGE_ALL_LINK_RECORD_RECEIVED_SIZE = 12
MESSAGE_GET_IM_CONFIGURATION_SIZE = 2
MESSAGE_GET_IM_CONFIGURATION_RECEIVED_SIZE = 6

MESSAGE_ACK = 0x06
MESSAGE_NAK = 0x15

MESSAGE_FLAG_BROADCAST_0X80 = 0x80
MESSAGE_FLAG_GROUP_0X40 = 0x40
MESSAGE_FLAG_NAK_0X20 = 0x20

# USE CAREFULLY. ACK is defined as 0x20 bit set to Zero.
# See isackflag for proper use.
MESSAGE_FLAG_DIRECT_MESSAGE_ACK_0X20 = 0x20
MESSAGE_FLAG_DIRECT_MESSAGE_NAK_0XA0 = 0xA0

MESSAGE_FLAG_ALL_LINK_BROADCAST_0XC0 = 0xC0
MESSAGE_FLAG_ALL_LINK_CLEANUP_0X40 = 0x40
MESSAGE_FLAG_ALL_LINK_CLEANUP_ACK_0X60 = 0x60
MESSAGE_FLAG_ALL_LINK_CLEANUP_NAK_0XE0 = 0xE0

MESSAGE_FLAG_GROUP_BROADCAST_0XC0 = 0xC0
MESSAGE_FLAG_GROUP_CLEANUP_0X40 = 0x40
MESSAGE_FLAG_GROUP_CLEANUP_ACK_0X60 = 0x60
MESSAGE_FLAG_GROUP_CLEANUP_NAK_0XE0 = 0xE0

MESSAGE_FLAG_EXTENDED_0X10 = 0x10
# Need to shift two bits right to get the actual count
MESSAGE_FLAG_HOPS_LEFT_0X0C = 0x0C
MESSAGE_FLAG_MAX_HOPS_0X03 = 0x03

MESSAGE_TYPE_DIRECT_MESSAGE = 0
MESSAGE_TYPE_DIRECT_MESSAGE_ACK = 1
MESSAGE_TYPE_ALL_LINK_CLEANUP = 2
MESSAGE_TYPE_ALL_LINK_CLEANUP_ACK = 3
MESSAGE_TYPE_BROADCAST_MESSAGE = 4
MESSAGE_TYPE_DIRECT_MESSAGE_NAK = 5
MESSAGE_TYPE_ALL_LINK_BROADCAST = 6
MESSAGE_TYPE_ALL_LINK_CLEANUP_NAK = 7

CONTROL_FLAG_RECORD_IN_USE_0X80 = 0x80
CONTROL_FLAG_CONTROLER_0X40 = 0x40
CONTROL_FLAG_RECORD_HAS_BEEN_USED_0X02 = 0x02

FAN_SPEED_OFF = 0x00
FAN_SPEED_LOW = 0x3F
FAN_SPEED_MEDIUM = 0xBE
FAN_SPEED_HIGH = 0xFF

# X10 House code lookup
HC_LOOKUP = {
    "a": 0x06,
    "b": 0x0E,
    "c": 0x02,
    "d": 0x0A,
    "e": 0x01,
    "f": 0x09,
    "g": 0x05,
    "h": 0x0D,
    "i": 0x07,
    "j": 0x0F,
    "k": 0x03,
    "l": 0x0B,
    "m": 0x00,
    "n": 0x08,
    "o": 0x04,
    "p": 0x0C,
}

# X10 Unit code lookup
UC_LOOKUP = {
    1: 0x06,
    2: 0x0E,
    3: 0x02,
    4: 0x0A,
    5: 0x01,
    6: 0x09,
    7: 0x05,
    8: 0x0D,
    9: 0x07,
    10: 0x0F,
    11: 0x03,
    12: 0x0B,
    13: 0x00,
    14: 0x08,
    15: 0x04,
    16: 0x0C,
    20: 0x20,  # All Units Off fake device
    21: 0x21,  # All Lights On fake device
    22: 0x22,
}  # All Lights Off fake device

X10_COMMAND_ALL_UNITS_OFF = 0x00
X10_COMMAND_ALL_LIGHTS_ON = 0x01
X10_COMMAND_ALL_LIGHTS_OFF = 0x06
X10_COMMAND_ON = 0x02
X10_COMMAND_OFF = 0x03
X10_COMMAND_DIM = 0x04
X10_COMMAND_BRIGHT = 0x05
X10_COMMAND_EXTENDED_CODE = 0x07
X10_COMMAND_HAIL_REQUEST = 0x08
X10_COMMAND_HAIL_ACKNOWLEDGE = 0x09
X10_COMMAND_PRE_SET_DIM = 0x0A
X10_COMMAND_STATUS_IS_ON = 0x0B
X10_COMMAND_STATUS_IS_OFF = 0x0C
X10_COMMAND_STATUS_REQUEST = 0x0D


class X10CommandType(Enum):
    """X10 command types."""

    DIRECT = 0
    BROADCAST = 1


class ThermostatMode(Enum):
    """Thermostat system modes."""

    OFF = 0x00
    HEAT = 0x01
    COOL = 0x02
    AUTO = 0x03
    FAN_AUTO = 0x04
    FAN_ALWAYS_ON = 0x8
