"""
Main interface for health service type definitions.

Usage::

    from mypy_boto3.health.type_defs import ClientDescribeAffectedAccountsForOrganizationResponseTypeDef

    data: ClientDescribeAffectedAccountsForOrganizationResponseTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeAffectedAccountsForOrganizationResponseTypeDef",
    "ClientDescribeAffectedEntitiesFilterlastUpdatedTimesTypeDef",
    "ClientDescribeAffectedEntitiesFilterTypeDef",
    "ClientDescribeAffectedEntitiesForOrganizationOrganizationEntityFiltersTypeDef",
    "ClientDescribeAffectedEntitiesForOrganizationResponseentitiesTypeDef",
    "ClientDescribeAffectedEntitiesForOrganizationResponsefailedSetTypeDef",
    "ClientDescribeAffectedEntitiesForOrganizationResponseTypeDef",
    "ClientDescribeAffectedEntitiesResponseentitiesTypeDef",
    "ClientDescribeAffectedEntitiesResponseTypeDef",
    "ClientDescribeEntityAggregatesResponseentityAggregatesTypeDef",
    "ClientDescribeEntityAggregatesResponseTypeDef",
    "ClientDescribeEventAggregatesFilterendTimesTypeDef",
    "ClientDescribeEventAggregatesFilterlastUpdatedTimesTypeDef",
    "ClientDescribeEventAggregatesFilterstartTimesTypeDef",
    "ClientDescribeEventAggregatesFilterTypeDef",
    "ClientDescribeEventAggregatesResponseeventAggregatesTypeDef",
    "ClientDescribeEventAggregatesResponseTypeDef",
    "ClientDescribeEventDetailsForOrganizationOrganizationEventDetailFiltersTypeDef",
    "ClientDescribeEventDetailsForOrganizationResponsefailedSetTypeDef",
    "ClientDescribeEventDetailsForOrganizationResponsesuccessfulSeteventDescriptionTypeDef",
    "ClientDescribeEventDetailsForOrganizationResponsesuccessfulSeteventTypeDef",
    "ClientDescribeEventDetailsForOrganizationResponsesuccessfulSetTypeDef",
    "ClientDescribeEventDetailsForOrganizationResponseTypeDef",
    "ClientDescribeEventDetailsResponsefailedSetTypeDef",
    "ClientDescribeEventDetailsResponsesuccessfulSeteventDescriptionTypeDef",
    "ClientDescribeEventDetailsResponsesuccessfulSeteventTypeDef",
    "ClientDescribeEventDetailsResponsesuccessfulSetTypeDef",
    "ClientDescribeEventDetailsResponseTypeDef",
    "ClientDescribeEventTypesFilterTypeDef",
    "ClientDescribeEventTypesResponseeventTypesTypeDef",
    "ClientDescribeEventTypesResponseTypeDef",
    "ClientDescribeEventsFilterendTimesTypeDef",
    "ClientDescribeEventsFilterlastUpdatedTimesTypeDef",
    "ClientDescribeEventsFilterstartTimesTypeDef",
    "ClientDescribeEventsFilterTypeDef",
    "ClientDescribeEventsForOrganizationFilterendTimeTypeDef",
    "ClientDescribeEventsForOrganizationFilterlastUpdatedTimeTypeDef",
    "ClientDescribeEventsForOrganizationFilterstartTimeTypeDef",
    "ClientDescribeEventsForOrganizationFilterTypeDef",
    "ClientDescribeEventsForOrganizationResponseeventsTypeDef",
    "ClientDescribeEventsForOrganizationResponseTypeDef",
    "ClientDescribeEventsResponseeventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeHealthServiceStatusForOrganizationResponseTypeDef",
    "DescribeAffectedAccountsForOrganizationResponseTypeDef",
    "AffectedEntityTypeDef",
    "OrganizationAffectedEntitiesErrorItemTypeDef",
    "DescribeAffectedEntitiesForOrganizationResponseTypeDef",
    "DescribeAffectedEntitiesResponseTypeDef",
    "EventAggregateTypeDef",
    "DescribeEventAggregatesResponseTypeDef",
    "EventTypeTypeDef",
    "DescribeEventTypesResponseTypeDef",
    "OrganizationEventTypeDef",
    "DescribeEventsForOrganizationResponseTypeDef",
    "EventTypeDef",
    "DescribeEventsResponseTypeDef",
    "DateTimeRangeTypeDef",
    "EntityFilterTypeDef",
    "EventAccountFilterTypeDef",
    "EventFilterTypeDef",
    "EventTypeFilterTypeDef",
    "OrganizationEventFilterTypeDef",
    "PaginatorConfigTypeDef",
)

ClientDescribeAffectedAccountsForOrganizationResponseTypeDef = TypedDict(
    "ClientDescribeAffectedAccountsForOrganizationResponseTypeDef",
    {"affectedAccounts": List[str], "nextToken": str},
    total=False,
)

ClientDescribeAffectedEntitiesFilterlastUpdatedTimesTypeDef = TypedDict(
    "ClientDescribeAffectedEntitiesFilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

_RequiredClientDescribeAffectedEntitiesFilterTypeDef = TypedDict(
    "_RequiredClientDescribeAffectedEntitiesFilterTypeDef", {"eventArns": List[str]}
)
_OptionalClientDescribeAffectedEntitiesFilterTypeDef = TypedDict(
    "_OptionalClientDescribeAffectedEntitiesFilterTypeDef",
    {
        "entityArns": List[str],
        "entityValues": List[str],
        "lastUpdatedTimes": List[ClientDescribeAffectedEntitiesFilterlastUpdatedTimesTypeDef],
        "tags": List[Dict[str, str]],
        "statusCodes": List[Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"]],
    },
    total=False,
)


class ClientDescribeAffectedEntitiesFilterTypeDef(
    _RequiredClientDescribeAffectedEntitiesFilterTypeDef,
    _OptionalClientDescribeAffectedEntitiesFilterTypeDef,
):
    pass


_RequiredClientDescribeAffectedEntitiesForOrganizationOrganizationEntityFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeAffectedEntitiesForOrganizationOrganizationEntityFiltersTypeDef",
    {"eventArn": str},
)
_OptionalClientDescribeAffectedEntitiesForOrganizationOrganizationEntityFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeAffectedEntitiesForOrganizationOrganizationEntityFiltersTypeDef",
    {"awsAccountId": str},
    total=False,
)


class ClientDescribeAffectedEntitiesForOrganizationOrganizationEntityFiltersTypeDef(
    _RequiredClientDescribeAffectedEntitiesForOrganizationOrganizationEntityFiltersTypeDef,
    _OptionalClientDescribeAffectedEntitiesForOrganizationOrganizationEntityFiltersTypeDef,
):
    pass


ClientDescribeAffectedEntitiesForOrganizationResponseentitiesTypeDef = TypedDict(
    "ClientDescribeAffectedEntitiesForOrganizationResponseentitiesTypeDef",
    {
        "entityArn": str,
        "eventArn": str,
        "entityValue": str,
        "entityUrl": str,
        "awsAccountId": str,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeAffectedEntitiesForOrganizationResponsefailedSetTypeDef = TypedDict(
    "ClientDescribeAffectedEntitiesForOrganizationResponsefailedSetTypeDef",
    {"awsAccountId": str, "eventArn": str, "errorName": str, "errorMessage": str},
    total=False,
)

ClientDescribeAffectedEntitiesForOrganizationResponseTypeDef = TypedDict(
    "ClientDescribeAffectedEntitiesForOrganizationResponseTypeDef",
    {
        "entities": List[ClientDescribeAffectedEntitiesForOrganizationResponseentitiesTypeDef],
        "failedSet": List[ClientDescribeAffectedEntitiesForOrganizationResponsefailedSetTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeAffectedEntitiesResponseentitiesTypeDef = TypedDict(
    "ClientDescribeAffectedEntitiesResponseentitiesTypeDef",
    {
        "entityArn": str,
        "eventArn": str,
        "entityValue": str,
        "entityUrl": str,
        "awsAccountId": str,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeAffectedEntitiesResponseTypeDef = TypedDict(
    "ClientDescribeAffectedEntitiesResponseTypeDef",
    {"entities": List[ClientDescribeAffectedEntitiesResponseentitiesTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeEntityAggregatesResponseentityAggregatesTypeDef = TypedDict(
    "ClientDescribeEntityAggregatesResponseentityAggregatesTypeDef",
    {"eventArn": str, "count": int},
    total=False,
)

ClientDescribeEntityAggregatesResponseTypeDef = TypedDict(
    "ClientDescribeEntityAggregatesResponseTypeDef",
    {"entityAggregates": List[ClientDescribeEntityAggregatesResponseentityAggregatesTypeDef]},
    total=False,
)

ClientDescribeEventAggregatesFilterendTimesTypeDef = TypedDict(
    "ClientDescribeEventAggregatesFilterendTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

ClientDescribeEventAggregatesFilterlastUpdatedTimesTypeDef = TypedDict(
    "ClientDescribeEventAggregatesFilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

ClientDescribeEventAggregatesFilterstartTimesTypeDef = TypedDict(
    "ClientDescribeEventAggregatesFilterstartTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

ClientDescribeEventAggregatesFilterTypeDef = TypedDict(
    "ClientDescribeEventAggregatesFilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[ClientDescribeEventAggregatesFilterstartTimesTypeDef],
        "endTimes": List[ClientDescribeEventAggregatesFilterendTimesTypeDef],
        "lastUpdatedTimes": List[ClientDescribeEventAggregatesFilterlastUpdatedTimesTypeDef],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[Literal["open", "closed", "upcoming"]],
    },
    total=False,
)

ClientDescribeEventAggregatesResponseeventAggregatesTypeDef = TypedDict(
    "ClientDescribeEventAggregatesResponseeventAggregatesTypeDef",
    {"aggregateValue": str, "count": int},
    total=False,
)

ClientDescribeEventAggregatesResponseTypeDef = TypedDict(
    "ClientDescribeEventAggregatesResponseTypeDef",
    {
        "eventAggregates": List[ClientDescribeEventAggregatesResponseeventAggregatesTypeDef],
        "nextToken": str,
    },
    total=False,
)

_RequiredClientDescribeEventDetailsForOrganizationOrganizationEventDetailFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEventDetailsForOrganizationOrganizationEventDetailFiltersTypeDef",
    {"eventArn": str},
)
_OptionalClientDescribeEventDetailsForOrganizationOrganizationEventDetailFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEventDetailsForOrganizationOrganizationEventDetailFiltersTypeDef",
    {"awsAccountId": str},
    total=False,
)


class ClientDescribeEventDetailsForOrganizationOrganizationEventDetailFiltersTypeDef(
    _RequiredClientDescribeEventDetailsForOrganizationOrganizationEventDetailFiltersTypeDef,
    _OptionalClientDescribeEventDetailsForOrganizationOrganizationEventDetailFiltersTypeDef,
):
    pass


ClientDescribeEventDetailsForOrganizationResponsefailedSetTypeDef = TypedDict(
    "ClientDescribeEventDetailsForOrganizationResponsefailedSetTypeDef",
    {"awsAccountId": str, "eventArn": str, "errorName": str, "errorMessage": str},
    total=False,
)

ClientDescribeEventDetailsForOrganizationResponsesuccessfulSeteventDescriptionTypeDef = TypedDict(
    "ClientDescribeEventDetailsForOrganizationResponsesuccessfulSeteventDescriptionTypeDef",
    {"latestDescription": str},
    total=False,
)

ClientDescribeEventDetailsForOrganizationResponsesuccessfulSeteventTypeDef = TypedDict(
    "ClientDescribeEventDetailsForOrganizationResponsesuccessfulSeteventTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": Literal[
            "issue", "accountNotification", "scheduledChange", "investigation"
        ],
        "region": str,
        "availabilityZone": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["open", "closed", "upcoming"],
    },
    total=False,
)

ClientDescribeEventDetailsForOrganizationResponsesuccessfulSetTypeDef = TypedDict(
    "ClientDescribeEventDetailsForOrganizationResponsesuccessfulSetTypeDef",
    {
        "awsAccountId": str,
        "event": ClientDescribeEventDetailsForOrganizationResponsesuccessfulSeteventTypeDef,
        "eventDescription": ClientDescribeEventDetailsForOrganizationResponsesuccessfulSeteventDescriptionTypeDef,
        "eventMetadata": Dict[str, str],
    },
    total=False,
)

ClientDescribeEventDetailsForOrganizationResponseTypeDef = TypedDict(
    "ClientDescribeEventDetailsForOrganizationResponseTypeDef",
    {
        "successfulSet": List[
            ClientDescribeEventDetailsForOrganizationResponsesuccessfulSetTypeDef
        ],
        "failedSet": List[ClientDescribeEventDetailsForOrganizationResponsefailedSetTypeDef],
    },
    total=False,
)

ClientDescribeEventDetailsResponsefailedSetTypeDef = TypedDict(
    "ClientDescribeEventDetailsResponsefailedSetTypeDef",
    {"eventArn": str, "errorName": str, "errorMessage": str},
    total=False,
)

ClientDescribeEventDetailsResponsesuccessfulSeteventDescriptionTypeDef = TypedDict(
    "ClientDescribeEventDetailsResponsesuccessfulSeteventDescriptionTypeDef",
    {"latestDescription": str},
    total=False,
)

ClientDescribeEventDetailsResponsesuccessfulSeteventTypeDef = TypedDict(
    "ClientDescribeEventDetailsResponsesuccessfulSeteventTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": Literal[
            "issue", "accountNotification", "scheduledChange", "investigation"
        ],
        "region": str,
        "availabilityZone": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["open", "closed", "upcoming"],
    },
    total=False,
)

ClientDescribeEventDetailsResponsesuccessfulSetTypeDef = TypedDict(
    "ClientDescribeEventDetailsResponsesuccessfulSetTypeDef",
    {
        "event": ClientDescribeEventDetailsResponsesuccessfulSeteventTypeDef,
        "eventDescription": ClientDescribeEventDetailsResponsesuccessfulSeteventDescriptionTypeDef,
        "eventMetadata": Dict[str, str],
    },
    total=False,
)

ClientDescribeEventDetailsResponseTypeDef = TypedDict(
    "ClientDescribeEventDetailsResponseTypeDef",
    {
        "successfulSet": List[ClientDescribeEventDetailsResponsesuccessfulSetTypeDef],
        "failedSet": List[ClientDescribeEventDetailsResponsefailedSetTypeDef],
    },
    total=False,
)

ClientDescribeEventTypesFilterTypeDef = TypedDict(
    "ClientDescribeEventTypesFilterTypeDef",
    {
        "eventTypeCodes": List[str],
        "services": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
    },
    total=False,
)

ClientDescribeEventTypesResponseeventTypesTypeDef = TypedDict(
    "ClientDescribeEventTypesResponseeventTypesTypeDef",
    {
        "service": str,
        "code": str,
        "category": Literal["issue", "accountNotification", "scheduledChange", "investigation"],
    },
    total=False,
)

ClientDescribeEventTypesResponseTypeDef = TypedDict(
    "ClientDescribeEventTypesResponseTypeDef",
    {"eventTypes": List[ClientDescribeEventTypesResponseeventTypesTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeEventsFilterendTimesTypeDef = TypedDict(
    "ClientDescribeEventsFilterendTimesTypeDef", {"from": datetime, "to": datetime}, total=False
)

ClientDescribeEventsFilterlastUpdatedTimesTypeDef = TypedDict(
    "ClientDescribeEventsFilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

ClientDescribeEventsFilterstartTimesTypeDef = TypedDict(
    "ClientDescribeEventsFilterstartTimesTypeDef", {"from": datetime, "to": datetime}, total=False
)

ClientDescribeEventsFilterTypeDef = TypedDict(
    "ClientDescribeEventsFilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[ClientDescribeEventsFilterstartTimesTypeDef],
        "endTimes": List[ClientDescribeEventsFilterendTimesTypeDef],
        "lastUpdatedTimes": List[ClientDescribeEventsFilterlastUpdatedTimesTypeDef],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[Literal["open", "closed", "upcoming"]],
    },
    total=False,
)

ClientDescribeEventsForOrganizationFilterendTimeTypeDef = TypedDict(
    "ClientDescribeEventsForOrganizationFilterendTimeTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

ClientDescribeEventsForOrganizationFilterlastUpdatedTimeTypeDef = TypedDict(
    "ClientDescribeEventsForOrganizationFilterlastUpdatedTimeTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

ClientDescribeEventsForOrganizationFilterstartTimeTypeDef = TypedDict(
    "ClientDescribeEventsForOrganizationFilterstartTimeTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)

ClientDescribeEventsForOrganizationFilterTypeDef = TypedDict(
    "ClientDescribeEventsForOrganizationFilterTypeDef",
    {
        "eventTypeCodes": List[str],
        "awsAccountIds": List[str],
        "services": List[str],
        "regions": List[str],
        "startTime": ClientDescribeEventsForOrganizationFilterstartTimeTypeDef,
        "endTime": ClientDescribeEventsForOrganizationFilterendTimeTypeDef,
        "lastUpdatedTime": ClientDescribeEventsForOrganizationFilterlastUpdatedTimeTypeDef,
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
        "eventStatusCodes": List[Literal["open", "closed", "upcoming"]],
    },
    total=False,
)

ClientDescribeEventsForOrganizationResponseeventsTypeDef = TypedDict(
    "ClientDescribeEventsForOrganizationResponseeventsTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": Literal[
            "issue", "accountNotification", "scheduledChange", "investigation"
        ],
        "region": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["open", "closed", "upcoming"],
    },
    total=False,
)

ClientDescribeEventsForOrganizationResponseTypeDef = TypedDict(
    "ClientDescribeEventsForOrganizationResponseTypeDef",
    {"events": List[ClientDescribeEventsForOrganizationResponseeventsTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeEventsResponseeventsTypeDef = TypedDict(
    "ClientDescribeEventsResponseeventsTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": Literal[
            "issue", "accountNotification", "scheduledChange", "investigation"
        ],
        "region": str,
        "availabilityZone": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["open", "closed", "upcoming"],
    },
    total=False,
)

ClientDescribeEventsResponseTypeDef = TypedDict(
    "ClientDescribeEventsResponseTypeDef",
    {"events": List[ClientDescribeEventsResponseeventsTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeHealthServiceStatusForOrganizationResponseTypeDef = TypedDict(
    "ClientDescribeHealthServiceStatusForOrganizationResponseTypeDef",
    {"healthServiceAccessStatusForOrganization": str},
    total=False,
)

DescribeAffectedAccountsForOrganizationResponseTypeDef = TypedDict(
    "DescribeAffectedAccountsForOrganizationResponseTypeDef",
    {"affectedAccounts": List[str], "nextToken": str},
    total=False,
)

AffectedEntityTypeDef = TypedDict(
    "AffectedEntityTypeDef",
    {
        "entityArn": str,
        "eventArn": str,
        "entityValue": str,
        "entityUrl": str,
        "awsAccountId": str,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"],
        "tags": Dict[str, str],
    },
    total=False,
)

OrganizationAffectedEntitiesErrorItemTypeDef = TypedDict(
    "OrganizationAffectedEntitiesErrorItemTypeDef",
    {"awsAccountId": str, "eventArn": str, "errorName": str, "errorMessage": str},
    total=False,
)

DescribeAffectedEntitiesForOrganizationResponseTypeDef = TypedDict(
    "DescribeAffectedEntitiesForOrganizationResponseTypeDef",
    {
        "entities": List[AffectedEntityTypeDef],
        "failedSet": List[OrganizationAffectedEntitiesErrorItemTypeDef],
        "nextToken": str,
    },
    total=False,
)

DescribeAffectedEntitiesResponseTypeDef = TypedDict(
    "DescribeAffectedEntitiesResponseTypeDef",
    {"entities": List[AffectedEntityTypeDef], "nextToken": str},
    total=False,
)

EventAggregateTypeDef = TypedDict(
    "EventAggregateTypeDef", {"aggregateValue": str, "count": int}, total=False
)

DescribeEventAggregatesResponseTypeDef = TypedDict(
    "DescribeEventAggregatesResponseTypeDef",
    {"eventAggregates": List[EventAggregateTypeDef], "nextToken": str},
    total=False,
)

EventTypeTypeDef = TypedDict(
    "EventTypeTypeDef",
    {
        "service": str,
        "code": str,
        "category": Literal["issue", "accountNotification", "scheduledChange", "investigation"],
    },
    total=False,
)

DescribeEventTypesResponseTypeDef = TypedDict(
    "DescribeEventTypesResponseTypeDef",
    {"eventTypes": List[EventTypeTypeDef], "nextToken": str},
    total=False,
)

OrganizationEventTypeDef = TypedDict(
    "OrganizationEventTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": Literal[
            "issue", "accountNotification", "scheduledChange", "investigation"
        ],
        "region": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["open", "closed", "upcoming"],
    },
    total=False,
)

DescribeEventsForOrganizationResponseTypeDef = TypedDict(
    "DescribeEventsForOrganizationResponseTypeDef",
    {"events": List[OrganizationEventTypeDef], "nextToken": str},
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": Literal[
            "issue", "accountNotification", "scheduledChange", "investigation"
        ],
        "region": str,
        "availabilityZone": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["open", "closed", "upcoming"],
    },
    total=False,
)

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef", {"events": List[EventTypeDef], "nextToken": str}, total=False
)

DateTimeRangeTypeDef = TypedDict(
    "DateTimeRangeTypeDef", {"from": datetime, "to": datetime}, total=False
)

_RequiredEntityFilterTypeDef = TypedDict("_RequiredEntityFilterTypeDef", {"eventArns": List[str]})
_OptionalEntityFilterTypeDef = TypedDict(
    "_OptionalEntityFilterTypeDef",
    {
        "entityArns": List[str],
        "entityValues": List[str],
        "lastUpdatedTimes": List[DateTimeRangeTypeDef],
        "tags": List[Dict[str, str]],
        "statusCodes": List[Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"]],
    },
    total=False,
)


class EntityFilterTypeDef(_RequiredEntityFilterTypeDef, _OptionalEntityFilterTypeDef):
    pass


EventAccountFilterTypeDef = TypedDict(
    "EventAccountFilterTypeDef", {"eventArn": str, "awsAccountId": str}
)

EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[DateTimeRangeTypeDef],
        "endTimes": List[DateTimeRangeTypeDef],
        "lastUpdatedTimes": List[DateTimeRangeTypeDef],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[Literal["open", "closed", "upcoming"]],
    },
    total=False,
)

EventTypeFilterTypeDef = TypedDict(
    "EventTypeFilterTypeDef",
    {
        "eventTypeCodes": List[str],
        "services": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
    },
    total=False,
)

OrganizationEventFilterTypeDef = TypedDict(
    "OrganizationEventFilterTypeDef",
    {
        "eventTypeCodes": List[str],
        "awsAccountIds": List[str],
        "services": List[str],
        "regions": List[str],
        "startTime": DateTimeRangeTypeDef,
        "endTime": DateTimeRangeTypeDef,
        "lastUpdatedTime": DateTimeRangeTypeDef,
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
        "eventStatusCodes": List[Literal["open", "closed", "upcoming"]],
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
