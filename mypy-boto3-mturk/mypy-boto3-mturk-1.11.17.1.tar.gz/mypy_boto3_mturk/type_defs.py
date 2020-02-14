"""
Main interface for mturk service type definitions.

Usage::

    from mypy_boto3.mturk.type_defs import ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef

    data: ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef",
    "ClientCreateHitAssignmentReviewPolicyParametersTypeDef",
    "ClientCreateHitAssignmentReviewPolicyTypeDef",
    "ClientCreateHitHITLayoutParametersTypeDef",
    "ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef",
    "ClientCreateHitHITReviewPolicyParametersTypeDef",
    "ClientCreateHitHITReviewPolicyTypeDef",
    "ClientCreateHitQualificationRequirementsLocaleValuesTypeDef",
    "ClientCreateHitQualificationRequirementsTypeDef",
    "ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef",
    "ClientCreateHitResponseHITQualificationRequirementsTypeDef",
    "ClientCreateHitResponseHITTypeDef",
    "ClientCreateHitResponseTypeDef",
    "ClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef",
    "ClientCreateHitTypeQualificationRequirementsTypeDef",
    "ClientCreateHitTypeResponseTypeDef",
    "ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef",
    "ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef",
    "ClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef",
    "ClientCreateHitWithHitTypeHITLayoutParametersTypeDef",
    "ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef",
    "ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef",
    "ClientCreateHitWithHitTypeHITReviewPolicyTypeDef",
    "ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef",
    "ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef",
    "ClientCreateHitWithHitTypeResponseHITTypeDef",
    "ClientCreateHitWithHitTypeResponseTypeDef",
    "ClientCreateQualificationTypeResponseQualificationTypeTypeDef",
    "ClientCreateQualificationTypeResponseTypeDef",
    "ClientGetAccountBalanceResponseTypeDef",
    "ClientGetAssignmentResponseAssignmentTypeDef",
    "ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef",
    "ClientGetAssignmentResponseHITQualificationRequirementsTypeDef",
    "ClientGetAssignmentResponseHITTypeDef",
    "ClientGetAssignmentResponseTypeDef",
    "ClientGetFileUploadUrlResponseTypeDef",
    "ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef",
    "ClientGetHitResponseHITQualificationRequirementsTypeDef",
    "ClientGetHitResponseHITTypeDef",
    "ClientGetHitResponseTypeDef",
    "ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef",
    "ClientGetQualificationScoreResponseQualificationTypeDef",
    "ClientGetQualificationScoreResponseTypeDef",
    "ClientGetQualificationTypeResponseQualificationTypeTypeDef",
    "ClientGetQualificationTypeResponseTypeDef",
    "ClientListAssignmentsForHitResponseAssignmentsTypeDef",
    "ClientListAssignmentsForHitResponseTypeDef",
    "ClientListBonusPaymentsResponseBonusPaymentsTypeDef",
    "ClientListBonusPaymentsResponseTypeDef",
    "ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    "ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef",
    "ClientListHitsForQualificationTypeResponseHITsTypeDef",
    "ClientListHitsForQualificationTypeResponseTypeDef",
    "ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    "ClientListHitsResponseHITsQualificationRequirementsTypeDef",
    "ClientListHitsResponseHITsTypeDef",
    "ClientListHitsResponseTypeDef",
    "ClientListQualificationRequestsResponseQualificationRequestsTypeDef",
    "ClientListQualificationRequestsResponseTypeDef",
    "ClientListQualificationTypesResponseQualificationTypesTypeDef",
    "ClientListQualificationTypesResponseTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef",
    "ClientListReviewPolicyResultsForHitResponseTypeDef",
    "ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    "ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef",
    "ClientListReviewableHitsResponseHITsTypeDef",
    "ClientListReviewableHitsResponseTypeDef",
    "ClientListWorkerBlocksResponseWorkerBlocksTypeDef",
    "ClientListWorkerBlocksResponseTypeDef",
    "ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef",
    "ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef",
    "ClientListWorkersWithQualificationTypeResponseTypeDef",
    "ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef",
    "ClientNotifyWorkersResponseTypeDef",
    "ClientSendTestEventNotificationNotificationTypeDef",
    "ClientUpdateNotificationSettingsNotificationTypeDef",
    "ClientUpdateQualificationTypeResponseQualificationTypeTypeDef",
    "ClientUpdateQualificationTypeResponseTypeDef",
    "AssignmentTypeDef",
    "ListAssignmentsForHITResponseTypeDef",
    "BonusPaymentTypeDef",
    "ListBonusPaymentsResponseTypeDef",
    "LocaleTypeDef",
    "QualificationRequirementTypeDef",
    "HITTypeDef",
    "ListHITsForQualificationTypeResponseTypeDef",
    "ListHITsResponseTypeDef",
    "QualificationRequestTypeDef",
    "ListQualificationRequestsResponseTypeDef",
    "QualificationTypeTypeDef",
    "ListQualificationTypesResponseTypeDef",
    "ListReviewableHITsResponseTypeDef",
    "WorkerBlockTypeDef",
    "ListWorkerBlocksResponseTypeDef",
    "QualificationTypeDef",
    "ListWorkersWithQualificationTypeResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientCreateHitAssignmentReviewPolicyParametersTypeDef = TypedDict(
    "ClientCreateHitAssignmentReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef],
    },
    total=False,
)

_RequiredClientCreateHitAssignmentReviewPolicyTypeDef = TypedDict(
    "_RequiredClientCreateHitAssignmentReviewPolicyTypeDef", {"PolicyName": str}
)
_OptionalClientCreateHitAssignmentReviewPolicyTypeDef = TypedDict(
    "_OptionalClientCreateHitAssignmentReviewPolicyTypeDef",
    {"Parameters": List[ClientCreateHitAssignmentReviewPolicyParametersTypeDef]},
    total=False,
)


class ClientCreateHitAssignmentReviewPolicyTypeDef(
    _RequiredClientCreateHitAssignmentReviewPolicyTypeDef,
    _OptionalClientCreateHitAssignmentReviewPolicyTypeDef,
):
    pass


_RequiredClientCreateHitHITLayoutParametersTypeDef = TypedDict(
    "_RequiredClientCreateHitHITLayoutParametersTypeDef", {"Name": str}
)
_OptionalClientCreateHitHITLayoutParametersTypeDef = TypedDict(
    "_OptionalClientCreateHitHITLayoutParametersTypeDef", {"Value": str}, total=False
)


class ClientCreateHitHITLayoutParametersTypeDef(
    _RequiredClientCreateHitHITLayoutParametersTypeDef,
    _OptionalClientCreateHitHITLayoutParametersTypeDef,
):
    pass


ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientCreateHitHITReviewPolicyParametersTypeDef = TypedDict(
    "ClientCreateHitHITReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef],
    },
    total=False,
)

_RequiredClientCreateHitHITReviewPolicyTypeDef = TypedDict(
    "_RequiredClientCreateHitHITReviewPolicyTypeDef", {"PolicyName": str}
)
_OptionalClientCreateHitHITReviewPolicyTypeDef = TypedDict(
    "_OptionalClientCreateHitHITReviewPolicyTypeDef",
    {"Parameters": List[ClientCreateHitHITReviewPolicyParametersTypeDef]},
    total=False,
)


class ClientCreateHitHITReviewPolicyTypeDef(
    _RequiredClientCreateHitHITReviewPolicyTypeDef, _OptionalClientCreateHitHITReviewPolicyTypeDef
):
    pass


ClientCreateHitQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "ClientCreateHitQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)

_RequiredClientCreateHitQualificationRequirementsTypeDef = TypedDict(
    "_RequiredClientCreateHitQualificationRequirementsTypeDef", {"QualificationTypeId": str}
)
_OptionalClientCreateHitQualificationRequirementsTypeDef = TypedDict(
    "_OptionalClientCreateHitQualificationRequirementsTypeDef",
    {
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[ClientCreateHitQualificationRequirementsLocaleValuesTypeDef],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)


class ClientCreateHitQualificationRequirementsTypeDef(
    _RequiredClientCreateHitQualificationRequirementsTypeDef,
    _OptionalClientCreateHitQualificationRequirementsTypeDef,
):
    pass


ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)

ClientCreateHitResponseHITQualificationRequirementsTypeDef = TypedDict(
    "ClientCreateHitResponseHITQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)

ClientCreateHitResponseHITTypeDef = TypedDict(
    "ClientCreateHitResponseHITTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientCreateHitResponseHITQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)

ClientCreateHitResponseTypeDef = TypedDict(
    "ClientCreateHitResponseTypeDef", {"HIT": ClientCreateHitResponseHITTypeDef}, total=False
)

ClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "ClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)

_RequiredClientCreateHitTypeQualificationRequirementsTypeDef = TypedDict(
    "_RequiredClientCreateHitTypeQualificationRequirementsTypeDef", {"QualificationTypeId": str}
)
_OptionalClientCreateHitTypeQualificationRequirementsTypeDef = TypedDict(
    "_OptionalClientCreateHitTypeQualificationRequirementsTypeDef",
    {
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[ClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)


class ClientCreateHitTypeQualificationRequirementsTypeDef(
    _RequiredClientCreateHitTypeQualificationRequirementsTypeDef,
    _OptionalClientCreateHitTypeQualificationRequirementsTypeDef,
):
    pass


ClientCreateHitTypeResponseTypeDef = TypedDict(
    "ClientCreateHitTypeResponseTypeDef", {"HITTypeId": str}, total=False
)

ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef = TypedDict(
    "ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[
            ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef
        ],
    },
    total=False,
)

_RequiredClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef = TypedDict(
    "_RequiredClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef", {"PolicyName": str}
)
_OptionalClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef = TypedDict(
    "_OptionalClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef",
    {"Parameters": List[ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef]},
    total=False,
)


class ClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef(
    _RequiredClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef,
    _OptionalClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef,
):
    pass


_RequiredClientCreateHitWithHitTypeHITLayoutParametersTypeDef = TypedDict(
    "_RequiredClientCreateHitWithHitTypeHITLayoutParametersTypeDef", {"Name": str}
)
_OptionalClientCreateHitWithHitTypeHITLayoutParametersTypeDef = TypedDict(
    "_OptionalClientCreateHitWithHitTypeHITLayoutParametersTypeDef", {"Value": str}, total=False
)


class ClientCreateHitWithHitTypeHITLayoutParametersTypeDef(
    _RequiredClientCreateHitWithHitTypeHITLayoutParametersTypeDef,
    _OptionalClientCreateHitWithHitTypeHITLayoutParametersTypeDef,
):
    pass


ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef = TypedDict(
    "ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef],
    },
    total=False,
)

_RequiredClientCreateHitWithHitTypeHITReviewPolicyTypeDef = TypedDict(
    "_RequiredClientCreateHitWithHitTypeHITReviewPolicyTypeDef", {"PolicyName": str}
)
_OptionalClientCreateHitWithHitTypeHITReviewPolicyTypeDef = TypedDict(
    "_OptionalClientCreateHitWithHitTypeHITReviewPolicyTypeDef",
    {"Parameters": List[ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef]},
    total=False,
)


class ClientCreateHitWithHitTypeHITReviewPolicyTypeDef(
    _RequiredClientCreateHitWithHitTypeHITReviewPolicyTypeDef,
    _OptionalClientCreateHitWithHitTypeHITReviewPolicyTypeDef,
):
    pass


ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)

ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef = TypedDict(
    "ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)

ClientCreateHitWithHitTypeResponseHITTypeDef = TypedDict(
    "ClientCreateHitWithHitTypeResponseHITTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)

ClientCreateHitWithHitTypeResponseTypeDef = TypedDict(
    "ClientCreateHitWithHitTypeResponseTypeDef",
    {"HIT": ClientCreateHitWithHitTypeResponseHITTypeDef},
    total=False,
)

ClientCreateQualificationTypeResponseQualificationTypeTypeDef = TypedDict(
    "ClientCreateQualificationTypeResponseQualificationTypeTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": Literal["Active", "Inactive"],
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)

ClientCreateQualificationTypeResponseTypeDef = TypedDict(
    "ClientCreateQualificationTypeResponseTypeDef",
    {"QualificationType": ClientCreateQualificationTypeResponseQualificationTypeTypeDef},
    total=False,
)

ClientGetAccountBalanceResponseTypeDef = TypedDict(
    "ClientGetAccountBalanceResponseTypeDef",
    {"AvailableBalance": str, "OnHoldBalance": str},
    total=False,
)

ClientGetAssignmentResponseAssignmentTypeDef = TypedDict(
    "ClientGetAssignmentResponseAssignmentTypeDef",
    {
        "AssignmentId": str,
        "WorkerId": str,
        "HITId": str,
        "AssignmentStatus": Literal["Submitted", "Approved", "Rejected"],
        "AutoApprovalTime": datetime,
        "AcceptTime": datetime,
        "SubmitTime": datetime,
        "ApprovalTime": datetime,
        "RejectionTime": datetime,
        "Deadline": datetime,
        "Answer": str,
        "RequesterFeedback": str,
    },
    total=False,
)

ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)

ClientGetAssignmentResponseHITQualificationRequirementsTypeDef = TypedDict(
    "ClientGetAssignmentResponseHITQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)

ClientGetAssignmentResponseHITTypeDef = TypedDict(
    "ClientGetAssignmentResponseHITTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientGetAssignmentResponseHITQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)

ClientGetAssignmentResponseTypeDef = TypedDict(
    "ClientGetAssignmentResponseTypeDef",
    {
        "Assignment": ClientGetAssignmentResponseAssignmentTypeDef,
        "HIT": ClientGetAssignmentResponseHITTypeDef,
    },
    total=False,
)

ClientGetFileUploadUrlResponseTypeDef = TypedDict(
    "ClientGetFileUploadUrlResponseTypeDef", {"FileUploadURL": str}, total=False
)

ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)

ClientGetHitResponseHITQualificationRequirementsTypeDef = TypedDict(
    "ClientGetHitResponseHITQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)

ClientGetHitResponseHITTypeDef = TypedDict(
    "ClientGetHitResponseHITTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[ClientGetHitResponseHITQualificationRequirementsTypeDef],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)

ClientGetHitResponseTypeDef = TypedDict(
    "ClientGetHitResponseTypeDef", {"HIT": ClientGetHitResponseHITTypeDef}, total=False
)

ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef = TypedDict(
    "ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)

ClientGetQualificationScoreResponseQualificationTypeDef = TypedDict(
    "ClientGetQualificationScoreResponseQualificationTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
        "GrantTime": datetime,
        "IntegerValue": int,
        "LocaleValue": ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef,
        "Status": Literal["Granted", "Revoked"],
    },
    total=False,
)

ClientGetQualificationScoreResponseTypeDef = TypedDict(
    "ClientGetQualificationScoreResponseTypeDef",
    {"Qualification": ClientGetQualificationScoreResponseQualificationTypeDef},
    total=False,
)

ClientGetQualificationTypeResponseQualificationTypeTypeDef = TypedDict(
    "ClientGetQualificationTypeResponseQualificationTypeTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": Literal["Active", "Inactive"],
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)

ClientGetQualificationTypeResponseTypeDef = TypedDict(
    "ClientGetQualificationTypeResponseTypeDef",
    {"QualificationType": ClientGetQualificationTypeResponseQualificationTypeTypeDef},
    total=False,
)

ClientListAssignmentsForHitResponseAssignmentsTypeDef = TypedDict(
    "ClientListAssignmentsForHitResponseAssignmentsTypeDef",
    {
        "AssignmentId": str,
        "WorkerId": str,
        "HITId": str,
        "AssignmentStatus": Literal["Submitted", "Approved", "Rejected"],
        "AutoApprovalTime": datetime,
        "AcceptTime": datetime,
        "SubmitTime": datetime,
        "ApprovalTime": datetime,
        "RejectionTime": datetime,
        "Deadline": datetime,
        "Answer": str,
        "RequesterFeedback": str,
    },
    total=False,
)

ClientListAssignmentsForHitResponseTypeDef = TypedDict(
    "ClientListAssignmentsForHitResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "Assignments": List[ClientListAssignmentsForHitResponseAssignmentsTypeDef],
    },
    total=False,
)

ClientListBonusPaymentsResponseBonusPaymentsTypeDef = TypedDict(
    "ClientListBonusPaymentsResponseBonusPaymentsTypeDef",
    {
        "WorkerId": str,
        "BonusAmount": str,
        "AssignmentId": str,
        "Reason": str,
        "GrantTime": datetime,
    },
    total=False,
)

ClientListBonusPaymentsResponseTypeDef = TypedDict(
    "ClientListBonusPaymentsResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "BonusPayments": List[ClientListBonusPaymentsResponseBonusPaymentsTypeDef],
    },
    total=False,
)

ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)

ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef = TypedDict(
    "ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)

ClientListHitsForQualificationTypeResponseHITsTypeDef = TypedDict(
    "ClientListHitsForQualificationTypeResponseHITsTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)

ClientListHitsForQualificationTypeResponseTypeDef = TypedDict(
    "ClientListHitsForQualificationTypeResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List[ClientListHitsForQualificationTypeResponseHITsTypeDef],
    },
    total=False,
)

ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)

ClientListHitsResponseHITsQualificationRequirementsTypeDef = TypedDict(
    "ClientListHitsResponseHITsQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)

ClientListHitsResponseHITsTypeDef = TypedDict(
    "ClientListHitsResponseHITsTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientListHitsResponseHITsQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)

ClientListHitsResponseTypeDef = TypedDict(
    "ClientListHitsResponseTypeDef",
    {"NextToken": str, "NumResults": int, "HITs": List[ClientListHitsResponseHITsTypeDef]},
    total=False,
)

ClientListQualificationRequestsResponseQualificationRequestsTypeDef = TypedDict(
    "ClientListQualificationRequestsResponseQualificationRequestsTypeDef",
    {
        "QualificationRequestId": str,
        "QualificationTypeId": str,
        "WorkerId": str,
        "Test": str,
        "Answer": str,
        "SubmitTime": datetime,
    },
    total=False,
)

ClientListQualificationRequestsResponseTypeDef = TypedDict(
    "ClientListQualificationRequestsResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationRequests": List[
            ClientListQualificationRequestsResponseQualificationRequestsTypeDef
        ],
    },
    total=False,
)

ClientListQualificationTypesResponseQualificationTypesTypeDef = TypedDict(
    "ClientListQualificationTypesResponseQualificationTypesTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": Literal["Active", "Inactive"],
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)

ClientListQualificationTypesResponseTypeDef = TypedDict(
    "ClientListQualificationTypesResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationTypes": List[ClientListQualificationTypesResponseQualificationTypesTypeDef],
    },
    total=False,
)

ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef = TypedDict(
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[
            ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef
        ],
    },
    total=False,
)

ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef = TypedDict(
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef",
    {
        "PolicyName": str,
        "Parameters": List[
            ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef
        ],
    },
    total=False,
)

ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef = TypedDict(
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef",
    {
        "ActionId": str,
        "ActionName": str,
        "TargetId": str,
        "TargetType": str,
        "Status": Literal["Intended", "Succeeded", "Failed", "Cancelled"],
        "CompleteTime": datetime,
        "Result": str,
        "ErrorCode": str,
    },
    total=False,
)

ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef = TypedDict(
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef",
    {
        "ActionId": str,
        "SubjectId": str,
        "SubjectType": str,
        "QuestionId": str,
        "Key": str,
        "Value": str,
    },
    total=False,
)

ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef = TypedDict(
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef",
    {
        "ReviewResults": List[
            ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef
        ],
        "ReviewActions": List[
            ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef
        ],
    },
    total=False,
)

ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef = TypedDict(
    "ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[
            ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef
        ],
    },
    total=False,
)

ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef = TypedDict(
    "ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef",
    {
        "PolicyName": str,
        "Parameters": List[
            ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef
        ],
    },
    total=False,
)

ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef = TypedDict(
    "ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef",
    {
        "ActionId": str,
        "ActionName": str,
        "TargetId": str,
        "TargetType": str,
        "Status": Literal["Intended", "Succeeded", "Failed", "Cancelled"],
        "CompleteTime": datetime,
        "Result": str,
        "ErrorCode": str,
    },
    total=False,
)

ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef = TypedDict(
    "ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef",
    {
        "ActionId": str,
        "SubjectId": str,
        "SubjectType": str,
        "QuestionId": str,
        "Key": str,
        "Value": str,
    },
    total=False,
)

ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef = TypedDict(
    "ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef",
    {
        "ReviewResults": List[
            ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef
        ],
        "ReviewActions": List[
            ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef
        ],
    },
    total=False,
)

ClientListReviewPolicyResultsForHitResponseTypeDef = TypedDict(
    "ClientListReviewPolicyResultsForHitResponseTypeDef",
    {
        "HITId": str,
        "AssignmentReviewPolicy": ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef,
        "HITReviewPolicy": ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef,
        "AssignmentReviewReport": ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef,
        "HITReviewReport": ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef,
        "NextToken": str,
    },
    total=False,
)

ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)

ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef = TypedDict(
    "ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)

ClientListReviewableHitsResponseHITsTypeDef = TypedDict(
    "ClientListReviewableHitsResponseHITsTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)

ClientListReviewableHitsResponseTypeDef = TypedDict(
    "ClientListReviewableHitsResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List[ClientListReviewableHitsResponseHITsTypeDef],
    },
    total=False,
)

ClientListWorkerBlocksResponseWorkerBlocksTypeDef = TypedDict(
    "ClientListWorkerBlocksResponseWorkerBlocksTypeDef",
    {"WorkerId": str, "Reason": str},
    total=False,
)

ClientListWorkerBlocksResponseTypeDef = TypedDict(
    "ClientListWorkerBlocksResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "WorkerBlocks": List[ClientListWorkerBlocksResponseWorkerBlocksTypeDef],
    },
    total=False,
)

ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef = TypedDict(
    "ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)

ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef = TypedDict(
    "ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
        "GrantTime": datetime,
        "IntegerValue": int,
        "LocaleValue": ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef,
        "Status": Literal["Granted", "Revoked"],
    },
    total=False,
)

ClientListWorkersWithQualificationTypeResponseTypeDef = TypedDict(
    "ClientListWorkersWithQualificationTypeResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "Qualifications": List[ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef],
    },
    total=False,
)

ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef = TypedDict(
    "ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef",
    {
        "NotifyWorkersFailureCode": Literal["SoftFailure", "HardFailure"],
        "NotifyWorkersFailureMessage": str,
        "WorkerId": str,
    },
    total=False,
)

ClientNotifyWorkersResponseTypeDef = TypedDict(
    "ClientNotifyWorkersResponseTypeDef",
    {
        "NotifyWorkersFailureStatuses": List[
            ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef
        ]
    },
    total=False,
)

_RequiredClientSendTestEventNotificationNotificationTypeDef = TypedDict(
    "_RequiredClientSendTestEventNotificationNotificationTypeDef", {"Destination": str}
)
_OptionalClientSendTestEventNotificationNotificationTypeDef = TypedDict(
    "_OptionalClientSendTestEventNotificationNotificationTypeDef",
    {
        "Transport": Literal["Email", "SQS", "SNS"],
        "Version": str,
        "EventTypes": List[
            Literal[
                "AssignmentAccepted",
                "AssignmentAbandoned",
                "AssignmentReturned",
                "AssignmentSubmitted",
                "AssignmentRejected",
                "AssignmentApproved",
                "HITCreated",
                "HITExpired",
                "HITReviewable",
                "HITExtended",
                "HITDisposed",
                "Ping",
            ]
        ],
    },
    total=False,
)


class ClientSendTestEventNotificationNotificationTypeDef(
    _RequiredClientSendTestEventNotificationNotificationTypeDef,
    _OptionalClientSendTestEventNotificationNotificationTypeDef,
):
    pass


_RequiredClientUpdateNotificationSettingsNotificationTypeDef = TypedDict(
    "_RequiredClientUpdateNotificationSettingsNotificationTypeDef", {"Destination": str}
)
_OptionalClientUpdateNotificationSettingsNotificationTypeDef = TypedDict(
    "_OptionalClientUpdateNotificationSettingsNotificationTypeDef",
    {
        "Transport": Literal["Email", "SQS", "SNS"],
        "Version": str,
        "EventTypes": List[
            Literal[
                "AssignmentAccepted",
                "AssignmentAbandoned",
                "AssignmentReturned",
                "AssignmentSubmitted",
                "AssignmentRejected",
                "AssignmentApproved",
                "HITCreated",
                "HITExpired",
                "HITReviewable",
                "HITExtended",
                "HITDisposed",
                "Ping",
            ]
        ],
    },
    total=False,
)


class ClientUpdateNotificationSettingsNotificationTypeDef(
    _RequiredClientUpdateNotificationSettingsNotificationTypeDef,
    _OptionalClientUpdateNotificationSettingsNotificationTypeDef,
):
    pass


ClientUpdateQualificationTypeResponseQualificationTypeTypeDef = TypedDict(
    "ClientUpdateQualificationTypeResponseQualificationTypeTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": Literal["Active", "Inactive"],
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)

ClientUpdateQualificationTypeResponseTypeDef = TypedDict(
    "ClientUpdateQualificationTypeResponseTypeDef",
    {"QualificationType": ClientUpdateQualificationTypeResponseQualificationTypeTypeDef},
    total=False,
)

AssignmentTypeDef = TypedDict(
    "AssignmentTypeDef",
    {
        "AssignmentId": str,
        "WorkerId": str,
        "HITId": str,
        "AssignmentStatus": Literal["Submitted", "Approved", "Rejected"],
        "AutoApprovalTime": datetime,
        "AcceptTime": datetime,
        "SubmitTime": datetime,
        "ApprovalTime": datetime,
        "RejectionTime": datetime,
        "Deadline": datetime,
        "Answer": str,
        "RequesterFeedback": str,
    },
    total=False,
)

ListAssignmentsForHITResponseTypeDef = TypedDict(
    "ListAssignmentsForHITResponseTypeDef",
    {"NextToken": str, "NumResults": int, "Assignments": List[AssignmentTypeDef]},
    total=False,
)

BonusPaymentTypeDef = TypedDict(
    "BonusPaymentTypeDef",
    {
        "WorkerId": str,
        "BonusAmount": str,
        "AssignmentId": str,
        "Reason": str,
        "GrantTime": datetime,
    },
    total=False,
)

ListBonusPaymentsResponseTypeDef = TypedDict(
    "ListBonusPaymentsResponseTypeDef",
    {"NumResults": int, "NextToken": str, "BonusPayments": List[BonusPaymentTypeDef]},
    total=False,
)

_RequiredLocaleTypeDef = TypedDict("_RequiredLocaleTypeDef", {"Country": str})
_OptionalLocaleTypeDef = TypedDict("_OptionalLocaleTypeDef", {"Subdivision": str}, total=False)


class LocaleTypeDef(_RequiredLocaleTypeDef, _OptionalLocaleTypeDef):
    pass


_RequiredQualificationRequirementTypeDef = TypedDict(
    "_RequiredQualificationRequirementTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
    },
)
_OptionalQualificationRequirementTypeDef = TypedDict(
    "_OptionalQualificationRequirementTypeDef",
    {
        "IntegerValues": List[int],
        "LocaleValues": List[LocaleTypeDef],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)


class QualificationRequirementTypeDef(
    _RequiredQualificationRequirementTypeDef, _OptionalQualificationRequirementTypeDef
):
    pass


HITTypeDef = TypedDict(
    "HITTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[QualificationRequirementTypeDef],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)

ListHITsForQualificationTypeResponseTypeDef = TypedDict(
    "ListHITsForQualificationTypeResponseTypeDef",
    {"NextToken": str, "NumResults": int, "HITs": List[HITTypeDef]},
    total=False,
)

ListHITsResponseTypeDef = TypedDict(
    "ListHITsResponseTypeDef",
    {"NextToken": str, "NumResults": int, "HITs": List[HITTypeDef]},
    total=False,
)

QualificationRequestTypeDef = TypedDict(
    "QualificationRequestTypeDef",
    {
        "QualificationRequestId": str,
        "QualificationTypeId": str,
        "WorkerId": str,
        "Test": str,
        "Answer": str,
        "SubmitTime": datetime,
    },
    total=False,
)

ListQualificationRequestsResponseTypeDef = TypedDict(
    "ListQualificationRequestsResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationRequests": List[QualificationRequestTypeDef],
    },
    total=False,
)

QualificationTypeTypeDef = TypedDict(
    "QualificationTypeTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": Literal["Active", "Inactive"],
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)

ListQualificationTypesResponseTypeDef = TypedDict(
    "ListQualificationTypesResponseTypeDef",
    {"NumResults": int, "NextToken": str, "QualificationTypes": List[QualificationTypeTypeDef]},
    total=False,
)

ListReviewableHITsResponseTypeDef = TypedDict(
    "ListReviewableHITsResponseTypeDef",
    {"NextToken": str, "NumResults": int, "HITs": List[HITTypeDef]},
    total=False,
)

WorkerBlockTypeDef = TypedDict("WorkerBlockTypeDef", {"WorkerId": str, "Reason": str}, total=False)

ListWorkerBlocksResponseTypeDef = TypedDict(
    "ListWorkerBlocksResponseTypeDef",
    {"NextToken": str, "NumResults": int, "WorkerBlocks": List[WorkerBlockTypeDef]},
    total=False,
)

QualificationTypeDef = TypedDict(
    "QualificationTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
        "GrantTime": datetime,
        "IntegerValue": int,
        "LocaleValue": LocaleTypeDef,
        "Status": Literal["Granted", "Revoked"],
    },
    total=False,
)

ListWorkersWithQualificationTypeResponseTypeDef = TypedDict(
    "ListWorkersWithQualificationTypeResponseTypeDef",
    {"NextToken": str, "NumResults": int, "Qualifications": List[QualificationTypeDef]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
