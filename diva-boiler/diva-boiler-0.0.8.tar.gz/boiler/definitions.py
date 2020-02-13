import enum


# This is needed to get mypy to validate enum's correctly.  By default,
# enum's have value type Any, which means that it is never validated.
class StrEnum(enum.Enum):
    @property
    def value(self) -> str:
        return super(StrEnum, self).value


class ActorType(StrEnum):
    BAG = 'Bag'
    BIKE = 'Bike'
    OTHER = 'Other'
    PERSON = 'Person'
    QUEUE = 'Queue'
    RECEPTACLE = 'Receptacle'
    VEHICLE = 'Vehicle'


actor_codes = {
    ActorType.BAG: 'b',
    ActorType.BIKE: 'k',
    ActorType.OTHER: 'o',
    ActorType.PERSON: 'p',
    ActorType.QUEUE: 'q',
    ActorType.RECEPTACLE: 'o',  # https://gitlab.com/diva-mturk/stumpf-diva/issues/32#note_285508683
    ActorType.VEHICLE: 'v',
}


class ActivityType(StrEnum):
    ABANDON_PACKAGE = 'Abandon_Package'
    CARRY_IN_HANDS = 'Carry_in_Hands'
    CARRY_ON_BACK = 'Carry_on_Back'
    CASING_FACILITY = 'Casing_Facility'
    CLOSE_FACILITY_DOOR = 'Close_Facility_Door'
    CLOSE_TRUNK = 'Close_Trunk'
    CLOSE_VEHICLE_DOOR = 'Close_Vehicle_Door'
    EMBRACE_INTERACTION = 'Embrace_Interaction'
    ENTER_FACILITY = 'Enter_Facility'
    ENTER_THROUGH_STRUCTURE = 'Enter_Through_Structure'
    ENTER_VEHICLE = 'Enter_Vehicle'
    EXIT_FACILITY = 'Exit_Facility'
    EXIT_THROUGH_STRUCTURE = 'Exit_Through_Structure'
    EXIT_VEHICLE = 'Exit_Vehicle'
    HAND_INTERACTION = 'Hand_Interaction'
    HEAVY_CARRY = 'Heavy_Carry'
    JOINING_QUEUE = 'Joining_Queue'
    LAPTOP_INTERACTION = 'Laptop_Interaction'
    LOAD_VEHICLE = 'Load_Vehicle'
    OBJECT_TRANSFER = 'Object_Transfer'
    OPEN_FACILITY_DOOR = 'Open_Facility_Door'
    OPEN_TRUNK = 'Open_Trunk'
    OPEN_VEHICLE_DOOR = 'Open_Vehicle_Door'
    PEOPLE_TALKING = 'People_Talking'
    PICK_UP_OBJECT = 'Pick_Up_Object'
    PURCHASING = 'Purchasing'
    PUT_DOWN_OBJECT = 'Put_Down_Object'
    READ_DOCUMENT = 'Read_Document'
    RIDING = 'Riding'
    SIT_DOWN = 'Sit_Down'
    STAND_UP = 'Stand_Up'
    TALK_ON_PHONE = 'Talk_on_Phone'
    TEXT_ON_PHONE = 'Text_On_Phone'
    THEFT = 'Theft'
    UNLOAD_VEHICLE = 'Unload_Vehicle'
    VEHICLE_DROPSOFF_PERSON = 'Vehicle_DropsOff_Person'
    VEHICLE_MOVING = 'Vehicle_Moving'
    VEHICLE_PICKSUP_PERSON = 'Vehicle_PicksUp_Person'
    VEHICLE_REVERSING = 'Vehicle_Reversing'
    VEHICLE_STARTING = 'Vehicle_Starting'
    VEHICLE_STOPPING = 'Vehicle_Stopping'
    VEHICLE_TURNING_LEFT = 'Vehicle_Turning_Left'
    VEHICLE_TURNING_RIGHT = 'Vehicle_Turning_Right'
    VEHICLE_UTURN = 'Vehicle_UTurn'

    @property
    def value(self) -> str:
        return super(ActivityType, self).value


# activity validations are described as regular expressions
# individual actors are encoded as single characters (mapping below)
# words separated by | must be internally sorted in alphabetical order
# because candidates will be sorted before testing to avoid using regex
# lookaround.
#
# for example:
#   `bop` is a valid spec, but `pob` is not.
#   `(kpv|bo)` is valid because each individual word is sorted.
activity_spec = {
    ActivityType.ABANDON_PACKAGE: '(bp|op)',
    ActivityType.CARRY_IN_HANDS: None,
    ActivityType.CARRY_ON_BACK: None,
    ActivityType.CASING_FACILITY: None,
    ActivityType.CLOSE_FACILITY_DOOR: 'p',
    ActivityType.CLOSE_TRUNK: 'p?v',
    ActivityType.CLOSE_VEHICLE_DOOR: 'p?v',
    ActivityType.EMBRACE_INTERACTION: 'p{2,}',
    ActivityType.ENTER_FACILITY: 'p',
    ActivityType.ENTER_THROUGH_STRUCTURE: 'p',
    ActivityType.ENTER_VEHICLE: 'pv',
    ActivityType.EXIT_FACILITY: 'p',
    ActivityType.EXIT_THROUGH_STRUCTURE: 'p',
    ActivityType.EXIT_VEHICLE: 'pv',
    ActivityType.HAND_INTERACTION: 'p{2,}',
    ActivityType.HEAVY_CARRY: '(bp+|o+p+|p{2,})',
    ActivityType.JOINING_QUEUE: None,
    ActivityType.LAPTOP_INTERACTION: 'p',
    ActivityType.LOAD_VEHICLE: '(o*pv|b*pv)',
    ActivityType.OBJECT_TRANSFER: '(o*p{2}|b*p{2}|o*pv|b*pv)',
    ActivityType.OPEN_FACILITY_DOOR: 'p',
    ActivityType.OPEN_TRUNK: 'p?v',
    ActivityType.OPEN_VEHICLE_DOOR: 'pv',
    ActivityType.PEOPLE_TALKING: 'p{2,}',
    ActivityType.PICK_UP_OBJECT: '(bp|op+)',
    ActivityType.PURCHASING: 'p+',
    ActivityType.PUT_DOWN_OBJECT: '(bp|op+)',
    ActivityType.READ_DOCUMENT: 'p',
    ActivityType.RIDING: 'kp',
    ActivityType.SIT_DOWN: 'p',
    ActivityType.STAND_UP: 'p',
    ActivityType.TALK_ON_PHONE: 'p',
    ActivityType.TEXT_ON_PHONE: 'p',
    ActivityType.THEFT: '(bo*p|o+p)',
    ActivityType.UNLOAD_VEHICLE: '(o*pv|b*pv)',
    ActivityType.VEHICLE_DROPSOFF_PERSON: 'p+v',
    ActivityType.VEHICLE_MOVING: 'v',
    ActivityType.VEHICLE_PICKSUP_PERSON: 'p+v',
    ActivityType.VEHICLE_REVERSING: 'v',
    ActivityType.VEHICLE_STARTING: 'v',
    ActivityType.VEHICLE_STOPPING: 'v',
    ActivityType.VEHICLE_TURNING_LEFT: 'v',
    ActivityType.VEHICLE_TURNING_RIGHT: 'v',
    ActivityType.VEHICLE_UTURN: 'v',
}

all_activity_codes = {
    2: ActivityType.VEHICLE_MOVING,
    3: ActivityType.STAND_UP,
    4: ActivityType.SIT_DOWN,
    5: ActivityType.CARRY_IN_HANDS,
    6: ActivityType.CARRY_ON_BACK,
    7: ActivityType.TALK_ON_PHONE,
    8: ActivityType.READ_DOCUMENT,
    9: ActivityType.TEXT_ON_PHONE,
    10: ActivityType.VEHICLE_STOPPING,
    11: ActivityType.VEHICLE_STARTING,
    12: ActivityType.VEHICLE_TURNING_LEFT,
    13: ActivityType.VEHICLE_TURNING_RIGHT,
    14: ActivityType.VEHICLE_UTURN,
    15: ActivityType.OBJECT_TRANSFER,
    16: ActivityType.PICK_UP_OBJECT,
    17: ActivityType.PUT_DOWN_OBJECT,
    18: ActivityType.HEAVY_CARRY,
    19: ActivityType.HAND_INTERACTION,
    20: ActivityType.EMBRACE_INTERACTION,
    21: ActivityType.OPEN_FACILITY_DOOR,
    22: ActivityType.CLOSE_FACILITY_DOOR,
    23: ActivityType.ENTER_FACILITY,
    24: ActivityType.EXIT_FACILITY,
    25: ActivityType.OPEN_VEHICLE_DOOR,
    26: ActivityType.CLOSE_VEHICLE_DOOR,
    27: ActivityType.ENTER_VEHICLE,
    28: ActivityType.EXIT_VEHICLE,
    29: ActivityType.OPEN_TRUNK,
    30: ActivityType.CLOSE_TRUNK,
    31: ActivityType.LOAD_VEHICLE,
    32: ActivityType.UNLOAD_VEHICLE,
    33: ActivityType.VEHICLE_PICKSUP_PERSON,
    34: ActivityType.VEHICLE_DROPSOFF_PERSON,
    35: ActivityType.PEOPLE_TALKING,
    36: ActivityType.JOINING_QUEUE,
    37: ActivityType.RIDING,
    38: ActivityType.PURCHASING,
    39: ActivityType.LAPTOP_INTERACTION,
    40: ActivityType.ABANDON_PACKAGE,
    41: ActivityType.CASING_FACILITY,
    43: ActivityType.THEFT,
    44: ActivityType.VEHICLE_REVERSING,
    # Codes below this comment are made-up
    # because these activities have no documented codes
    -1000: ActivityType.ENTER_THROUGH_STRUCTURE,
    -1001: ActivityType.EXIT_THROUGH_STRUCTURE,
}


class ActivityPipelineStatuses(StrEnum):
    UNAUDITED = 'unaudited'
    AUDITED = 'audited'
    GLADIATOR_1 = 'gladiator_1'
    REFINER_1 = 'refiner_1'
    GLADIATOR_2 = 'gladiator_2'
    REFINER_2 = 'refiner_2'
    GLADIATOR_3 = 'gladiator_3'
    JANITOR = 'janitor'
    GOOD = 'good'


class AnnotationVendors(StrEnum):
    IMERIT = 'imerit'
    KITWARE = 'kitware'


class CameraLocation(StrEnum):
    ADMIN = 'admin'
    BUS = 'bus'
    SCHOOL = 'school'
    HOSPITAL = 'hospital'


class DataCollects(StrEnum):
    M1 = 'm1'
    M2 = 'm2'


class ReleaseBatches(StrEnum):
    SEQUESTERED = 'sequestered'
    MEVA = 'meva'
    TESTING = 'testing'


class CameraTypes(StrEnum):
    VISIBLE = 'eo'
    INFRARED = 'ir'


class VideoPipelineStatuses(StrEnum):
    ANNOTATION = 'annotation'
    AUDIT = 'audit'
    GUNRUNNER = 'gunrunner'
    REMEDIATION = 'remediation'
    COMPLETE = 'complete'


class Scenarios(StrEnum):
    BASKETBALL = 'basketball'
    CONFERENCE = 'conference'
    CONTROL = 'control'
    DEBATE_TEAM = 'debate team'
    DENSE_SUBWAY = 'dense subway'
    FOOTRACE = 'footrace'
    PANEL_DEBATE = 'panel debate'
    POLITICAL_DEBATE = 'political debate'
    POLITICAL_RALLY = 'political rally'
    THREAT = 'threat'
    TRAVEL = 'travel'
