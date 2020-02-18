from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import List, Dict, Any, Union, Optional, ClassVar

import attr
from attr import attrs, attrib
from firebase_admin import firestore

from mimosa.validators import valid_timezone, valid_email, valid_phone_number, valid_url

DocumentSnapshot = firestore.firestore.DocumentSnapshot


class FirebaseDocClass(ABC):
    """Abstract class for from_firestore_doc interface"""

    @classmethod
    @abstractmethod
    def from_firestore_doc(cls, doc: DocumentSnapshot):
        return cls


class CraftTypes(Enum):
    """String based enum because of Typer/Click parsing."""

    SCAFFOLDING = "SCAFFOLDING"
    INSULATION = "INSULATION"
    WATERBLASTING = "WATERBLASTING"
    SANDBLASTING = "SANDBLASTING"
    PAINTING = "PAINTING"
    HOISTWELLS = "HOISTWELLS"
    MOBILE_EQUIPMENT = "MOBILE_EQUIPMENT"
    HVAC = "HVAC"
    PERMITTING = "PERMITTING"
    HOUSEKEEPING = "HOUSEKEEPING"

    @property
    def code(self) -> int:
        return craft_type_codes[self]


craft_type_codes = {
    CraftTypes.SCAFFOLDING: 10,
    CraftTypes.INSULATION: 15,
    CraftTypes.WATERBLASTING: 20,
    CraftTypes.SANDBLASTING: 25,
    CraftTypes.PAINTING: 30,
    CraftTypes.HOISTWELLS: 40,
    CraftTypes.MOBILE_EQUIPMENT: 50,
    CraftTypes.HVAC: 60,
    CraftTypes.PERMITTING: 90,
    CraftTypes.HOUSEKEEPING: 99,
}

craft_type_path_strings = {
    CraftTypes.SCAFFOLDING: "scaffoldRecords",
    CraftTypes.INSULATION: "insulationRecords",
    CraftTypes.WATERBLASTING: "waterblastingRecords",
    CraftTypes.SANDBLASTING: "sandblastingRecords",
    CraftTypes.PAINTING: "paintingRecords",
    CraftTypes.HOISTWELLS: "hoistwellRecords",
    CraftTypes.MOBILE_EQUIPMENT: "mobileEquipmentRecords",
    CraftTypes.HVAC: "hvacRecords",
    CraftTypes.PERMITTING: "permittingRecords",
    CraftTypes.HOUSEKEEPING: "housekeepingRecords",
}


class TaskTypes(Enum):
    INSTALLATION = "INSTALLATION"
    MODIFICATION = "MODIFICATION"
    REMOVAL = "REMOVAL"
    INSPECTION = "INSPECTION"
    WATERBLASTING = "WATERBLASTING"
    SANDBLASTING = "SANDBLASTING"
    INSULATION = "INSULATION"
    ABATEMENT = "ABATEMENT"
    PAINTING = "PAINTING"
    REPAIR = "REPAIR"
    LOCKOUT = "LOCKOUT"
    WALKTHROUGH = "WALKTHROUGH"
    PERFORMING_WORK = "PERFORMING_WORK"
    HOUSEKEEPING = "HOUSEKEEPING"


task_type_codes = {
    TaskTypes.INSTALLATION: 10,
    TaskTypes.MODIFICATION: 11,
    TaskTypes.REMOVAL: 12,
    TaskTypes.INSPECTION: 13,
    TaskTypes.WATERBLASTING: 20,
    TaskTypes.SANDBLASTING: 30,
    TaskTypes.INSULATION: 40,
    TaskTypes.ABATEMENT: 50,
    TaskTypes.PAINTING: 60,
    TaskTypes.REPAIR: 70,
    TaskTypes.LOCKOUT: 90,
    TaskTypes.WALKTHROUGH: 91,
    TaskTypes.PERFORMING_WORK: 92,
    TaskTypes.HOUSEKEEPING: 99,
}

task_type_path_strings = {
    TaskTypes.INSTALLATION: "installation",
    TaskTypes.MODIFICATION: "modification",
    TaskTypes.REMOVAL: "removal",
    TaskTypes.INSPECTION: "inspection",
    TaskTypes.WATERBLASTING: "waterblasting",
    TaskTypes.SANDBLASTING: "sandblasting",
    TaskTypes.INSULATION: "insulation",
    TaskTypes.ABATEMENT: "abatement",
    TaskTypes.PAINTING: "painting",
    TaskTypes.REPAIR: "repair",
    TaskTypes.LOCKOUT: "lockout",
    TaskTypes.WALKTHROUGH: "walkthrough",
    TaskTypes.PERFORMING_WORK: "performingWork",
    TaskTypes.HOUSEKEEPING: "housekeeping",
}


class TaskStatus(Enum):
    AWAITING_ESTIMATE = "AWAITING_ESTIMATE"
    AWAITING_APPROVAL = "AWAITING_APPROVAL"
    AWAITING_SCHEDULE = "AWAITING_SCHEDULE"
    SCHEDULED = "SCHEDULED"
    AWAITING = "AWAITING"
    IN_PROGRESS = "IN_PROGRESS"
    ON_HOLD = "ON_HOLD"
    COMPLETE = "COMPLETE"


task_status_codes = {
    TaskStatus.AWAITING_ESTIMATE: 5,
    TaskStatus.AWAITING_APPROVAL: 8,
    TaskStatus.AWAITING_SCHEDULE: 10,
    TaskStatus.SCHEDULED: 20,
    TaskStatus.AWAITING: 30,
    TaskStatus.IN_PROGRESS: 40,
    TaskStatus.ON_HOLD: 50,
    TaskStatus.COMPLETE: 90,
}


class EventTypes(Enum):
    NEW_USER_APPROVED = "NEW_USER_APPROVED"
    NEW_USER_APPLIED = "NEW_USER_APPLIED"
    CRAFT_RECORD_CREATED = "CRAFT_RECORD_CREATED"
    NEW_TASK_ADDED = "NEW_TASK_ADDED"
    TASK_STATUS_UPDATED = "TASK_STATUS_UPDATED"
    TASK_REASSIGNED_COMPANY = "TASK_REASSIGNED_COMPANY"
    TASK_DESCRIPTION_UPDATED = "TASK_DESCRIPTION_UPDATED"
    TASK_WORK_ORDER_UPDATED = "TASK_WORK_ORDER_UPDATED"
    TASK_DETAILS_UPDATED = "TASK_DETAILS_UPDATED"
    UPDATED_TITLE = "UPDATED_TITLE"
    UPDATED_DESCRIPTION = "UPDATED_DESCRIPTION"
    ADDED_PHOTO = "ADDED_PHOTO"
    REMOVED_PHOTO = "REMOVED_PHOTO"
    CHANGED_ASSET = "CHANGED_ASSET"
    UPDATED_CRAFT_DETAILS = "UPDATED_CRAFT_DETAILS"
    CHANGED_LOCATION_ID = "CHANGED_LOCATION_ID"
    UPDATED_LOCATION_ON_MAP = "UPDATED_LOCATION_ON_MAP"


event_type_codes = {
    EventTypes.NEW_USER_APPROVED: 10,
    EventTypes.NEW_USER_APPLIED: 11,
    EventTypes.CRAFT_RECORD_CREATED: 20,
    EventTypes.NEW_TASK_ADDED: 30,
    EventTypes.TASK_STATUS_UPDATED: 31,
    EventTypes.TASK_REASSIGNED_COMPANY: 32,
    EventTypes.TASK_DESCRIPTION_UPDATED: 33,
    EventTypes.TASK_WORK_ORDER_UPDATED: 34,
    EventTypes.TASK_DETAILS_UPDATED: 36,
    EventTypes.UPDATED_TITLE: 40,
    EventTypes.UPDATED_DESCRIPTION: 41,
    EventTypes.ADDED_PHOTO: 42,
    EventTypes.REMOVED_PHOTO: 43,
    EventTypes.CHANGED_ASSET: 44,
    EventTypes.UPDATED_CRAFT_DETAILS: 45,
    EventTypes.CHANGED_LOCATION_ID: 46,
    EventTypes.UPDATED_LOCATION_ON_MAP: 47,
}


class DetailDataType(str, Enum):
    string = "string"
    boolean = "bool"
    number = "number"
    timestamp = "timestamp"


@attrs
class BaseDynamicDetailData:
    """Common properties in dynamic details"""

    data_type: DetailDataType = attrib(
        validator=attr.validators.in_([string for string in DetailDataType])
    )
    title: str = attrib(validator=attr.validators.instance_of(str))
    default_value: Union[str, bool, int, float, datetime, None] = attrib(
        validator=attr.validators.instance_of(
            (str, bool, int, float, datetime, type(None))
        )
    )
    required: bool = attrib(validator=attr.validators.instance_of(bool))
    editable: bool = attrib(validator=attr.validators.instance_of(bool))
    min_value: Union[int, float, None] = attrib(
        default=None, validator=attr.validators.instance_of((int, float, type(None)))
    )
    max_value: Union[int, float, None] = attrib(
        default=None, validator=attr.validators.instance_of((int, float, type(None)))
    )
    min_length: Union[int, None] = attrib(
        default=None, validator=attr.validators.instance_of((int, type(None)))
    )
    max_length: Union[int, None] = attrib(
        default=None, validator=attr.validators.instance_of((int, type(None)))
    )

    @default_value.validator
    def must_match_data_type(self, attribute, value):
        if self.data_type == DetailDataType.boolean:
            if type(value) is not bool:
                raise ValueError("Expected default_value to be a boolean")

        elif self.data_type == DetailDataType.number:
            if type(value) not in [int, float]:
                raise ValueError("Expected default_value to be a number")

        elif self.data_type == DetailDataType.string:
            if type(value) is not str:
                raise ValueError("Expected default_value to be a string")

        elif self.data_type == DetailDataType.timestamp:
            if value is not None:
                raise ValueError("Expected default_value to be None")

        else:
            raise ValueError("Unexpected condition for DetailDataType.")

    @min_value.validator
    def min_value_must_be_present_for_numbers(self, attribute, value):
        if self.data_type == DetailDataType.number:
            if value is None:
                raise ValueError("Expected a value for min_value")

    @max_value.validator
    def max_value_must_be_present_for_numbers(self, attribute, value):
        if self.data_type == DetailDataType.number:
            if value is None:
                raise ValueError("Expected a value for max_value")

    @min_length.validator
    def min_length_must_be_present_for_strings(self, attribute, value):
        if self.data_type == DetailDataType.string:
            if value is None:
                raise ValueError("Expected a value for min_length")

    @max_length.validator
    def max_length_must_be_present_for_numbers(self, attribute, value):
        if self.data_type == DetailDataType.string:
            if value is None:
                raise ValueError("Expected a value for max_length")


@attrs
class TaskDynamicDetailData:
    """Data specific to dynamic task specific details"""

    on_task_status: List[int] = attrib(
        factory=list, validator=attr.validators.instance_of(list)
    )

    @on_task_status.validator
    def must_be_in_task_status_list(self, attribute, value):
        errors: List[str] = []
        for item in value:
            if item not in task_status_codes.values():
                errors.append(f"Value {item} not found in task status enum.")
        if len(errors) > 0:
            raise ValueError(f"{errors}")


@attrs
class CraftDetail:
    """
    Represents a dynamic craft detail

    base: Contains data common to all dynamic details.
    """

    base: BaseDynamicDetailData = attrib(
        validator=attr.validators.instance_of(BaseDynamicDetailData)
    )

    @classmethod
    def from_raw_data(
        cls,
        type: DetailDataType,
        title: str,
        defaultValue: Union[str, bool, int, float, datetime, None],
        required: bool,
        editable: bool,
        minValue: Union[int, float, None] = None,
        maxValue: Union[int, float, None] = None,
        minLength: Optional[int] = None,
        maxLength: Optional[int] = None,
    ):
        """Create a CraftDetail from raw data."""
        return cls(
            BaseDynamicDetailData(
                data_type=type,
                title=title,
                default_value=defaultValue,
                required=required,
                editable=editable,
                min_value=minValue,
                max_value=maxValue,
                min_length=minLength,
                max_length=maxLength,
            )
        )

    def to_firestore(self) -> dict:
        """Output a dictionary ready to be written to Firestore"""
        output = {
            "type": self.base.data_type,
            "title": self.base.title,
            "defaultValue": self.base.default_value,
            "required": self.base.required,
            "editable": self.base.editable,
        }
        if self.base.min_value is not None:
            output["minValue"] = self.base.min_value

        if self.base.max_value is not None:
            output["maxValue"] = self.base.max_value

        if self.base.min_length is not None:
            output["minLength"] = self.base.min_length

        if self.base.max_length is not None:
            output["maxLength"] = self.base.max_length

        return output


@attrs
class TaskDetail:
    """
    Represents a dynamic Task Specific Detail.

    base: Contains common data present in all dynamic details.
    task_data: Contains data specific to dynamic task details.
    """

    base: BaseDynamicDetailData = attrib(
        validator=attr.validators.instance_of(BaseDynamicDetailData)
    )
    task_data: TaskDynamicDetailData = attrib(
        validator=attr.validators.instance_of(TaskDynamicDetailData)
    )

    @classmethod
    def from_raw_data(
        cls,
        type: DetailDataType,
        title: str,
        defaultValue: Union[str, bool, int, float, datetime, None],
        required: bool,
        editable: bool,
        minValue: Union[int, float, None] = None,
        maxValue: Union[int, float, None] = None,
        minLength: Optional[int] = None,
        maxLength: Optional[int] = None,
        onTaskStatus: List[int] = None,
    ):
        """Build a TaskDetail from raw data."""
        if onTaskStatus is None:
            onTaskStatus = []
        return cls(
            BaseDynamicDetailData(
                data_type=type,
                title=title,
                default_value=defaultValue,
                required=required,
                editable=editable,
                min_value=minValue,
                max_value=maxValue,
                min_length=minLength,
                max_length=maxLength,
            ),
            TaskDynamicDetailData(on_task_status=onTaskStatus),
        )

    def to_firestore(self) -> dict:
        """Output a dictionary ready to be written to Firestore"""
        output = {
            "type": self.base.data_type,
            "title": self.base.title,
            "defaultValue": self.base.default_value,
            "required": self.base.required,
            "editable": self.base.editable,
            "onTaskStatus": self.task_data.on_task_status,
        }

        if self.base.min_value is not None:
            output["minValue"] = self.base.min_value

        if self.base.max_value is not None:
            output["maxValue"] = self.base.max_value

        if self.base.min_length is not None:
            output["minLength"] = self.base.min_length

        if self.base.max_length is not None:
            output["maxLength"] = self.base.max_length

        return output


@attrs(auto_attribs=True)
class SiteKey:
    name: str
    timezone: str
    managingCompanyID: str
    validCraftTypes: List[int]
    validTaskTypes: List[int]
    validTaskStatusCodes: List[int]
    validEventTypes: List[int]
    customizations: Dict[str, Any]

    schema: ClassVar[Dict] = {
        "name": {"type": "string", "required": True},
        "timezone": {"type": "string", "required": True, "check_with": valid_timezone},
        "managingCompanyID": {"type": "string", "required": True},
        "validCraftTypes": {
            "type": "list",
            "required": True,
            "schema": {"type": "integer", "allowed": list(craft_type_codes.values())},
        },
        "validTaskTypes": {
            "type": "list",
            "required": True,
            "schema": {"type": "integer", "allowed": list(task_type_codes.values())},
        },
        "validTaskStatusCodes": {
            "type": "list",
            "required": True,
            "schema": {"type": "integer", "allowed": list(task_status_codes.values())},
        },
        "validEventTypes": {
            "type": "list",
            "required": True,
            "schema": {"type": "integer", "allowed": list(event_type_codes.values())},
        },
        "customizations": {
            "type": "dict",
            "required": True,
            "keysrules": {"type": "string"},
        },
    }

    def to_firestore(self) -> Dict:
        """Create a dictionary of data ready to be written to Firestore."""
        return {
            "name": self.name,
            "timezone": self.timezone,
            "managingCompanyID": self.managingCompanyID,
            "validCraftTypes": self.validCraftTypes,
            "validTaskTypes": self.validTaskTypes,
            "validTaskStatusCodes": self.validTaskStatusCodes,
            "validEventTypes": self.validEventTypes,
            "customizations": self.customizations,
        }


@attrs(auto_attribs=True)
class SiteKeyCompany:
    name: str
    craftTypes: List[int]
    mainPointOfContact: Optional[str]
    logoPhotoURL: Optional[str]
    members: List[str]

    schema: ClassVar[Dict] = {
        "name": {"type": "string", "maxlength": 200, "required": True},
        "craftTypes": {
            "type": "list",
            "required": True,
            "schema": {"type": "integer", "allowed": list(craft_type_codes.values())},
        },
        "mainPointOfContact": {
            "type": "string",
            "required": True,
            "maxlength": 200,
            "nullable": True,
        },
        "logoPhotoURL": {
            "type": "string",
            "required": True,
            "maxlength": 1000,
            "nullable": True,
        },
        "members": {"type": "list", "required": True, "schema": {"type": "string"}},
    }

    def to_firestore(self):
        """Return a dictionary ready to be written to Firestore"""
        return {
            "name": self.name,
            "craftTypes": self.craftTypes,
            "mainPointOfContact": self.mainPointOfContact,
            "logoPhotoURL": self.logoPhotoURL,
            "members": self.members,
        }


@attrs(auto_attribs=True)
class SiteKeyUser:
    id: Union[str, None]
    refPath: Union[str, None]
    displayName: str
    companyName: str
    jobTitle: str
    email: str
    department: str
    phone: str
    userPhoto_URL: Union[str, None]

    schema: ClassVar[dict] = {
        "id": {"type": "string"},
        "refPath": {"type": "string"},
        "displayName": {"type": "string", "required": True, "maxlength": 200},
        "companyName": {"type": "string", "required": True, "maxlength": 200},
        "jobTitle": {"type": "string", "required": True, "maxlength": 200},
        "email": {
            "type": "string",
            "required": True,
            "maxlength": 200,
            "check_with": valid_email,
        },
        "department": {"type": "string", "required": True, "maxlength": 200},
        "phone": {"type": "string", "required": True, "check_with": valid_phone_number},
        "userPhoto_URL": {
            "type": "string",
            "required": True,
            "nullable": True,
            "check_with": valid_url,
        },
    }

    def to_firestore(self):
        """Return a dictionary ready to be written to Firestore"""
        return {
            "displayName": self.displayName,
            "companyName": self.companyName,
            "jobTitle": self.jobTitle,
            "email": self.email,
            "department": self.department,
            "phone": self.phone,
            "userPhoto_URL": self.userPhoto_URL,
        }
