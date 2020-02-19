"""
Main interface for devicefarm service type definitions.

Usage::

    from mypy_boto3.devicefarm.type_defs import ClientCreateDevicePoolResponsedevicePoolrulesTypeDef

    data: ClientCreateDevicePoolResponsedevicePoolrulesTypeDef = {...}
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
    "ClientCreateDevicePoolResponsedevicePoolrulesTypeDef",
    "ClientCreateDevicePoolResponsedevicePoolTypeDef",
    "ClientCreateDevicePoolResponseTypeDef",
    "ClientCreateDevicePoolRulesTypeDef",
    "ClientCreateInstanceProfileResponseinstanceProfileTypeDef",
    "ClientCreateInstanceProfileResponseTypeDef",
    "ClientCreateNetworkProfileResponsenetworkProfileTypeDef",
    "ClientCreateNetworkProfileResponseTypeDef",
    "ClientCreateProjectResponseprojectTypeDef",
    "ClientCreateProjectResponseTypeDef",
    "ClientCreateRemoteAccessSessionConfigurationTypeDef",
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef",
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef",
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef",
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef",
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef",
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef",
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessionTypeDef",
    "ClientCreateRemoteAccessSessionResponseTypeDef",
    "ClientCreateTestGridProjectResponsetestGridProjectTypeDef",
    "ClientCreateTestGridProjectResponseTypeDef",
    "ClientCreateTestGridUrlResponseTypeDef",
    "ClientCreateUploadResponseuploadTypeDef",
    "ClientCreateUploadResponseTypeDef",
    "ClientCreateVpceConfigurationResponsevpceConfigurationTypeDef",
    "ClientCreateVpceConfigurationResponseTypeDef",
    "ClientGetAccountSettingsResponseaccountSettingstrialMinutesTypeDef",
    "ClientGetAccountSettingsResponseaccountSettingsTypeDef",
    "ClientGetAccountSettingsResponseTypeDef",
    "ClientGetDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef",
    "ClientGetDeviceInstanceResponsedeviceInstanceTypeDef",
    "ClientGetDeviceInstanceResponseTypeDef",
    "ClientGetDevicePoolCompatibilityConfigurationcustomerArtifactPathsTypeDef",
    "ClientGetDevicePoolCompatibilityConfigurationlocationTypeDef",
    "ClientGetDevicePoolCompatibilityConfigurationradiosTypeDef",
    "ClientGetDevicePoolCompatibilityConfigurationTypeDef",
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdevicecpuTypeDef",
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesinstanceProfileTypeDef",
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesTypeDef",
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceresolutionTypeDef",
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceTypeDef",
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesincompatibilityMessagesTypeDef",
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesTypeDef",
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdevicecpuTypeDef",
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesinstanceProfileTypeDef",
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesTypeDef",
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceresolutionTypeDef",
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceTypeDef",
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesincompatibilityMessagesTypeDef",
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesTypeDef",
    "ClientGetDevicePoolCompatibilityResponseTypeDef",
    "ClientGetDevicePoolCompatibilityTestTypeDef",
    "ClientGetDevicePoolResponsedevicePoolrulesTypeDef",
    "ClientGetDevicePoolResponsedevicePoolTypeDef",
    "ClientGetDevicePoolResponseTypeDef",
    "ClientGetDeviceResponsedevicecpuTypeDef",
    "ClientGetDeviceResponsedeviceinstancesinstanceProfileTypeDef",
    "ClientGetDeviceResponsedeviceinstancesTypeDef",
    "ClientGetDeviceResponsedeviceresolutionTypeDef",
    "ClientGetDeviceResponsedeviceTypeDef",
    "ClientGetDeviceResponseTypeDef",
    "ClientGetInstanceProfileResponseinstanceProfileTypeDef",
    "ClientGetInstanceProfileResponseTypeDef",
    "ClientGetJobResponsejobcountersTypeDef",
    "ClientGetJobResponsejobdeviceMinutesTypeDef",
    "ClientGetJobResponsejobdevicecpuTypeDef",
    "ClientGetJobResponsejobdeviceinstancesinstanceProfileTypeDef",
    "ClientGetJobResponsejobdeviceinstancesTypeDef",
    "ClientGetJobResponsejobdeviceresolutionTypeDef",
    "ClientGetJobResponsejobdeviceTypeDef",
    "ClientGetJobResponsejobTypeDef",
    "ClientGetJobResponseTypeDef",
    "ClientGetNetworkProfileResponsenetworkProfileTypeDef",
    "ClientGetNetworkProfileResponseTypeDef",
    "ClientGetOfferingStatusResponsecurrentofferingrecurringChargescostTypeDef",
    "ClientGetOfferingStatusResponsecurrentofferingrecurringChargesTypeDef",
    "ClientGetOfferingStatusResponsecurrentofferingTypeDef",
    "ClientGetOfferingStatusResponsecurrentTypeDef",
    "ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargescostTypeDef",
    "ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargesTypeDef",
    "ClientGetOfferingStatusResponsenextPeriodofferingTypeDef",
    "ClientGetOfferingStatusResponsenextPeriodTypeDef",
    "ClientGetOfferingStatusResponseTypeDef",
    "ClientGetProjectResponseprojectTypeDef",
    "ClientGetProjectResponseTypeDef",
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef",
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef",
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef",
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef",
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef",
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef",
    "ClientGetRemoteAccessSessionResponseremoteAccessSessionTypeDef",
    "ClientGetRemoteAccessSessionResponseTypeDef",
    "ClientGetRunResponseruncountersTypeDef",
    "ClientGetRunResponseruncustomerArtifactPathsTypeDef",
    "ClientGetRunResponserundeviceMinutesTypeDef",
    "ClientGetRunResponserundeviceSelectionResultfiltersTypeDef",
    "ClientGetRunResponserundeviceSelectionResultTypeDef",
    "ClientGetRunResponserunlocationTypeDef",
    "ClientGetRunResponserunnetworkProfileTypeDef",
    "ClientGetRunResponserunradiosTypeDef",
    "ClientGetRunResponserunTypeDef",
    "ClientGetRunResponseTypeDef",
    "ClientGetSuiteResponsesuitecountersTypeDef",
    "ClientGetSuiteResponsesuitedeviceMinutesTypeDef",
    "ClientGetSuiteResponsesuiteTypeDef",
    "ClientGetSuiteResponseTypeDef",
    "ClientGetTestGridProjectResponsetestGridProjectTypeDef",
    "ClientGetTestGridProjectResponseTypeDef",
    "ClientGetTestGridSessionResponsetestGridSessionTypeDef",
    "ClientGetTestGridSessionResponseTypeDef",
    "ClientGetTestResponsetestcountersTypeDef",
    "ClientGetTestResponsetestdeviceMinutesTypeDef",
    "ClientGetTestResponsetestTypeDef",
    "ClientGetTestResponseTypeDef",
    "ClientGetUploadResponseuploadTypeDef",
    "ClientGetUploadResponseTypeDef",
    "ClientGetVpceConfigurationResponsevpceConfigurationTypeDef",
    "ClientGetVpceConfigurationResponseTypeDef",
    "ClientInstallToRemoteAccessSessionResponseappUploadTypeDef",
    "ClientInstallToRemoteAccessSessionResponseTypeDef",
    "ClientListArtifactsResponseartifactsTypeDef",
    "ClientListArtifactsResponseTypeDef",
    "ClientListDeviceInstancesResponsedeviceInstancesinstanceProfileTypeDef",
    "ClientListDeviceInstancesResponsedeviceInstancesTypeDef",
    "ClientListDeviceInstancesResponseTypeDef",
    "ClientListDevicePoolsResponsedevicePoolsrulesTypeDef",
    "ClientListDevicePoolsResponsedevicePoolsTypeDef",
    "ClientListDevicePoolsResponseTypeDef",
    "ClientListDevicesFiltersTypeDef",
    "ClientListDevicesResponsedevicescpuTypeDef",
    "ClientListDevicesResponsedevicesinstancesinstanceProfileTypeDef",
    "ClientListDevicesResponsedevicesinstancesTypeDef",
    "ClientListDevicesResponsedevicesresolutionTypeDef",
    "ClientListDevicesResponsedevicesTypeDef",
    "ClientListDevicesResponseTypeDef",
    "ClientListInstanceProfilesResponseinstanceProfilesTypeDef",
    "ClientListInstanceProfilesResponseTypeDef",
    "ClientListJobsResponsejobscountersTypeDef",
    "ClientListJobsResponsejobsdeviceMinutesTypeDef",
    "ClientListJobsResponsejobsdevicecpuTypeDef",
    "ClientListJobsResponsejobsdeviceinstancesinstanceProfileTypeDef",
    "ClientListJobsResponsejobsdeviceinstancesTypeDef",
    "ClientListJobsResponsejobsdeviceresolutionTypeDef",
    "ClientListJobsResponsejobsdeviceTypeDef",
    "ClientListJobsResponsejobsTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientListNetworkProfilesResponsenetworkProfilesTypeDef",
    "ClientListNetworkProfilesResponseTypeDef",
    "ClientListOfferingPromotionsResponseofferingPromotionsTypeDef",
    "ClientListOfferingPromotionsResponseTypeDef",
    "ClientListOfferingTransactionsResponseofferingTransactionscostTypeDef",
    "ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef",
    "ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef",
    "ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingTypeDef",
    "ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusTypeDef",
    "ClientListOfferingTransactionsResponseofferingTransactionsTypeDef",
    "ClientListOfferingTransactionsResponseTypeDef",
    "ClientListOfferingsResponseofferingsrecurringChargescostTypeDef",
    "ClientListOfferingsResponseofferingsrecurringChargesTypeDef",
    "ClientListOfferingsResponseofferingsTypeDef",
    "ClientListOfferingsResponseTypeDef",
    "ClientListProjectsResponseprojectsTypeDef",
    "ClientListProjectsResponseTypeDef",
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceMinutesTypeDef",
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdevicecpuTypeDef",
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef",
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesTypeDef",
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceresolutionTypeDef",
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceTypeDef",
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsTypeDef",
    "ClientListRemoteAccessSessionsResponseTypeDef",
    "ClientListRunsResponserunscountersTypeDef",
    "ClientListRunsResponserunscustomerArtifactPathsTypeDef",
    "ClientListRunsResponserunsdeviceMinutesTypeDef",
    "ClientListRunsResponserunsdeviceSelectionResultfiltersTypeDef",
    "ClientListRunsResponserunsdeviceSelectionResultTypeDef",
    "ClientListRunsResponserunslocationTypeDef",
    "ClientListRunsResponserunsnetworkProfileTypeDef",
    "ClientListRunsResponserunsradiosTypeDef",
    "ClientListRunsResponserunsTypeDef",
    "ClientListRunsResponseTypeDef",
    "ClientListSamplesResponsesamplesTypeDef",
    "ClientListSamplesResponseTypeDef",
    "ClientListSuitesResponsesuitescountersTypeDef",
    "ClientListSuitesResponsesuitesdeviceMinutesTypeDef",
    "ClientListSuitesResponsesuitesTypeDef",
    "ClientListSuitesResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTestGridProjectsResponsetestGridProjectsTypeDef",
    "ClientListTestGridProjectsResponseTypeDef",
    "ClientListTestGridSessionActionsResponseactionsTypeDef",
    "ClientListTestGridSessionActionsResponseTypeDef",
    "ClientListTestGridSessionArtifactsResponseartifactsTypeDef",
    "ClientListTestGridSessionArtifactsResponseTypeDef",
    "ClientListTestGridSessionsResponsetestGridSessionsTypeDef",
    "ClientListTestGridSessionsResponseTypeDef",
    "ClientListTestsResponsetestscountersTypeDef",
    "ClientListTestsResponsetestsdeviceMinutesTypeDef",
    "ClientListTestsResponsetestsTypeDef",
    "ClientListTestsResponseTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsdevicecpuTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceresolutionTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsjobTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsrunTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemssuiteTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemstestTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsTypeDef",
    "ClientListUniqueProblemsResponseTypeDef",
    "ClientListUploadsResponseuploadsTypeDef",
    "ClientListUploadsResponseTypeDef",
    "ClientListVpceConfigurationsResponsevpceConfigurationsTypeDef",
    "ClientListVpceConfigurationsResponseTypeDef",
    "ClientPurchaseOfferingResponseofferingTransactioncostTypeDef",
    "ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef",
    "ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef",
    "ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingTypeDef",
    "ClientPurchaseOfferingResponseofferingTransactionofferingStatusTypeDef",
    "ClientPurchaseOfferingResponseofferingTransactionTypeDef",
    "ClientPurchaseOfferingResponseTypeDef",
    "ClientRenewOfferingResponseofferingTransactioncostTypeDef",
    "ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef",
    "ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef",
    "ClientRenewOfferingResponseofferingTransactionofferingStatusofferingTypeDef",
    "ClientRenewOfferingResponseofferingTransactionofferingStatusTypeDef",
    "ClientRenewOfferingResponseofferingTransactionTypeDef",
    "ClientRenewOfferingResponseTypeDef",
    "ClientScheduleRunConfigurationcustomerArtifactPathsTypeDef",
    "ClientScheduleRunConfigurationlocationTypeDef",
    "ClientScheduleRunConfigurationradiosTypeDef",
    "ClientScheduleRunConfigurationTypeDef",
    "ClientScheduleRunDeviceSelectionConfigurationfiltersTypeDef",
    "ClientScheduleRunDeviceSelectionConfigurationTypeDef",
    "ClientScheduleRunExecutionConfigurationTypeDef",
    "ClientScheduleRunResponseruncountersTypeDef",
    "ClientScheduleRunResponseruncustomerArtifactPathsTypeDef",
    "ClientScheduleRunResponserundeviceMinutesTypeDef",
    "ClientScheduleRunResponserundeviceSelectionResultfiltersTypeDef",
    "ClientScheduleRunResponserundeviceSelectionResultTypeDef",
    "ClientScheduleRunResponserunlocationTypeDef",
    "ClientScheduleRunResponserunnetworkProfileTypeDef",
    "ClientScheduleRunResponserunradiosTypeDef",
    "ClientScheduleRunResponserunTypeDef",
    "ClientScheduleRunResponseTypeDef",
    "ClientScheduleRunTestTypeDef",
    "ClientStopJobResponsejobcountersTypeDef",
    "ClientStopJobResponsejobdeviceMinutesTypeDef",
    "ClientStopJobResponsejobdevicecpuTypeDef",
    "ClientStopJobResponsejobdeviceinstancesinstanceProfileTypeDef",
    "ClientStopJobResponsejobdeviceinstancesTypeDef",
    "ClientStopJobResponsejobdeviceresolutionTypeDef",
    "ClientStopJobResponsejobdeviceTypeDef",
    "ClientStopJobResponsejobTypeDef",
    "ClientStopJobResponseTypeDef",
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef",
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef",
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef",
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef",
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef",
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef",
    "ClientStopRemoteAccessSessionResponseremoteAccessSessionTypeDef",
    "ClientStopRemoteAccessSessionResponseTypeDef",
    "ClientStopRunResponseruncountersTypeDef",
    "ClientStopRunResponseruncustomerArtifactPathsTypeDef",
    "ClientStopRunResponserundeviceMinutesTypeDef",
    "ClientStopRunResponserundeviceSelectionResultfiltersTypeDef",
    "ClientStopRunResponserundeviceSelectionResultTypeDef",
    "ClientStopRunResponserunlocationTypeDef",
    "ClientStopRunResponserunnetworkProfileTypeDef",
    "ClientStopRunResponserunradiosTypeDef",
    "ClientStopRunResponserunTypeDef",
    "ClientStopRunResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef",
    "ClientUpdateDeviceInstanceResponsedeviceInstanceTypeDef",
    "ClientUpdateDeviceInstanceResponseTypeDef",
    "ClientUpdateDevicePoolResponsedevicePoolrulesTypeDef",
    "ClientUpdateDevicePoolResponsedevicePoolTypeDef",
    "ClientUpdateDevicePoolResponseTypeDef",
    "ClientUpdateDevicePoolRulesTypeDef",
    "ClientUpdateInstanceProfileResponseinstanceProfileTypeDef",
    "ClientUpdateInstanceProfileResponseTypeDef",
    "ClientUpdateNetworkProfileResponsenetworkProfileTypeDef",
    "ClientUpdateNetworkProfileResponseTypeDef",
    "ClientUpdateProjectResponseprojectTypeDef",
    "ClientUpdateProjectResponseTypeDef",
    "ClientUpdateTestGridProjectResponsetestGridProjectTypeDef",
    "ClientUpdateTestGridProjectResponseTypeDef",
    "ClientUpdateUploadResponseuploadTypeDef",
    "ClientUpdateUploadResponseTypeDef",
    "ClientUpdateVpceConfigurationResponsevpceConfigurationTypeDef",
    "ClientUpdateVpceConfigurationResponseTypeDef",
    "DeviceFilterTypeDef",
    "MonetaryAmountTypeDef",
    "RecurringChargeTypeDef",
    "OfferingTypeDef",
    "OfferingStatusTypeDef",
    "GetOfferingStatusResultTypeDef",
    "ArtifactTypeDef",
    "ListArtifactsResultTypeDef",
    "InstanceProfileTypeDef",
    "DeviceInstanceTypeDef",
    "ListDeviceInstancesResultTypeDef",
    "RuleTypeDef",
    "DevicePoolTypeDef",
    "ListDevicePoolsResultTypeDef",
    "CPUTypeDef",
    "ResolutionTypeDef",
    "DeviceTypeDef",
    "ListDevicesResultTypeDef",
    "ListInstanceProfilesResultTypeDef",
    "CountersTypeDef",
    "DeviceMinutesTypeDef",
    "JobTypeDef",
    "ListJobsResultTypeDef",
    "NetworkProfileTypeDef",
    "ListNetworkProfilesResultTypeDef",
    "OfferingPromotionTypeDef",
    "ListOfferingPromotionsResultTypeDef",
    "OfferingTransactionTypeDef",
    "ListOfferingTransactionsResultTypeDef",
    "ListOfferingsResultTypeDef",
    "ProjectTypeDef",
    "ListProjectsResultTypeDef",
    "RemoteAccessSessionTypeDef",
    "ListRemoteAccessSessionsResultTypeDef",
    "CustomerArtifactPathsTypeDef",
    "DeviceSelectionResultTypeDef",
    "LocationTypeDef",
    "RadiosTypeDef",
    "RunTypeDef",
    "ListRunsResultTypeDef",
    "SampleTypeDef",
    "ListSamplesResultTypeDef",
    "SuiteTypeDef",
    "ListSuitesResultTypeDef",
    "TestTypeDef",
    "ListTestsResultTypeDef",
    "ProblemDetailTypeDef",
    "ProblemTypeDef",
    "UniqueProblemTypeDef",
    "ListUniqueProblemsResultTypeDef",
    "UploadTypeDef",
    "ListUploadsResultTypeDef",
    "VPCEConfigurationTypeDef",
    "ListVPCEConfigurationsResultTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateDevicePoolResponsedevicePoolrulesTypeDef = TypedDict(
    "ClientCreateDevicePoolResponsedevicePoolrulesTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "value": str,
    },
    total=False,
)

ClientCreateDevicePoolResponsedevicePoolTypeDef = TypedDict(
    "ClientCreateDevicePoolResponsedevicePoolTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "rules": List[ClientCreateDevicePoolResponsedevicePoolrulesTypeDef],
        "maxDevices": int,
    },
    total=False,
)

ClientCreateDevicePoolResponseTypeDef = TypedDict(
    "ClientCreateDevicePoolResponseTypeDef",
    {"devicePool": ClientCreateDevicePoolResponsedevicePoolTypeDef},
    total=False,
)

ClientCreateDevicePoolRulesTypeDef = TypedDict(
    "ClientCreateDevicePoolRulesTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "value": str,
    },
    total=False,
)

ClientCreateInstanceProfileResponseinstanceProfileTypeDef = TypedDict(
    "ClientCreateInstanceProfileResponseinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientCreateInstanceProfileResponseTypeDef = TypedDict(
    "ClientCreateInstanceProfileResponseTypeDef",
    {"instanceProfile": ClientCreateInstanceProfileResponseinstanceProfileTypeDef},
    total=False,
)

ClientCreateNetworkProfileResponsenetworkProfileTypeDef = TypedDict(
    "ClientCreateNetworkProfileResponsenetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)

ClientCreateNetworkProfileResponseTypeDef = TypedDict(
    "ClientCreateNetworkProfileResponseTypeDef",
    {"networkProfile": ClientCreateNetworkProfileResponsenetworkProfileTypeDef},
    total=False,
)

ClientCreateProjectResponseprojectTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectTypeDef",
    {"arn": str, "name": str, "defaultJobTimeoutMinutes": int, "created": datetime},
    total=False,
)

ClientCreateProjectResponseTypeDef = TypedDict(
    "ClientCreateProjectResponseTypeDef",
    {"project": ClientCreateProjectResponseprojectTypeDef},
    total=False,
)

ClientCreateRemoteAccessSessionConfigurationTypeDef = TypedDict(
    "ClientCreateRemoteAccessSessionConfigurationTypeDef",
    {"billingMethod": Literal["METERED", "UNMETERED"], "vpceConfigurationArns": List[str]},
    total=False,
)

ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef = TypedDict(
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)

ClientCreateRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef = TypedDict(
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)

ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef = TypedDict(
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef = TypedDict(
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)

ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef = TypedDict(
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)

ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef = TypedDict(
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientCreateRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef,
        "resolution": ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)

ClientCreateRemoteAccessSessionResponseremoteAccessSessionTypeDef = TypedDict(
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessionTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
        "started": datetime,
        "stopped": datetime,
        "device": ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef,
        "instanceArn": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "hostAddress": str,
        "clientId": str,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef,
        "endpoint": str,
        "deviceUdid": str,
        "interactionMode": Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"],
        "skipAppResign": bool,
    },
    total=False,
)

ClientCreateRemoteAccessSessionResponseTypeDef = TypedDict(
    "ClientCreateRemoteAccessSessionResponseTypeDef",
    {"remoteAccessSession": ClientCreateRemoteAccessSessionResponseremoteAccessSessionTypeDef},
    total=False,
)

ClientCreateTestGridProjectResponsetestGridProjectTypeDef = TypedDict(
    "ClientCreateTestGridProjectResponsetestGridProjectTypeDef",
    {"arn": str, "name": str, "description": str, "created": datetime},
    total=False,
)

ClientCreateTestGridProjectResponseTypeDef = TypedDict(
    "ClientCreateTestGridProjectResponseTypeDef",
    {"testGridProject": ClientCreateTestGridProjectResponsetestGridProjectTypeDef},
    total=False,
)

ClientCreateTestGridUrlResponseTypeDef = TypedDict(
    "ClientCreateTestGridUrlResponseTypeDef", {"url": str, "expires": datetime}, total=False
)

ClientCreateUploadResponseuploadTypeDef = TypedDict(
    "ClientCreateUploadResponseuploadTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ],
        "status": Literal["INITIALIZED", "PROCESSING", "SUCCEEDED", "FAILED"],
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": Literal["CURATED", "PRIVATE"],
    },
    total=False,
)

ClientCreateUploadResponseTypeDef = TypedDict(
    "ClientCreateUploadResponseTypeDef",
    {"upload": ClientCreateUploadResponseuploadTypeDef},
    total=False,
)

ClientCreateVpceConfigurationResponsevpceConfigurationTypeDef = TypedDict(
    "ClientCreateVpceConfigurationResponsevpceConfigurationTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)

ClientCreateVpceConfigurationResponseTypeDef = TypedDict(
    "ClientCreateVpceConfigurationResponseTypeDef",
    {"vpceConfiguration": ClientCreateVpceConfigurationResponsevpceConfigurationTypeDef},
    total=False,
)

ClientGetAccountSettingsResponseaccountSettingstrialMinutesTypeDef = TypedDict(
    "ClientGetAccountSettingsResponseaccountSettingstrialMinutesTypeDef",
    {"total": float, "remaining": float},
    total=False,
)

ClientGetAccountSettingsResponseaccountSettingsTypeDef = TypedDict(
    "ClientGetAccountSettingsResponseaccountSettingsTypeDef",
    {
        "awsAccountNumber": str,
        "unmeteredDevices": Dict[str, int],
        "unmeteredRemoteAccessDevices": Dict[str, int],
        "maxJobTimeoutMinutes": int,
        "trialMinutes": ClientGetAccountSettingsResponseaccountSettingstrialMinutesTypeDef,
        "maxSlots": Dict[str, int],
        "defaultJobTimeoutMinutes": int,
        "skipAppResign": bool,
    },
    total=False,
)

ClientGetAccountSettingsResponseTypeDef = TypedDict(
    "ClientGetAccountSettingsResponseTypeDef",
    {"accountSettings": ClientGetAccountSettingsResponseaccountSettingsTypeDef},
    total=False,
)

ClientGetDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef = TypedDict(
    "ClientGetDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientGetDeviceInstanceResponsedeviceInstanceTypeDef = TypedDict(
    "ClientGetDeviceInstanceResponsedeviceInstanceTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientGetDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef,
    },
    total=False,
)

ClientGetDeviceInstanceResponseTypeDef = TypedDict(
    "ClientGetDeviceInstanceResponseTypeDef",
    {"deviceInstance": ClientGetDeviceInstanceResponsedeviceInstanceTypeDef},
    total=False,
)

ClientGetDevicePoolCompatibilityConfigurationcustomerArtifactPathsTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityConfigurationcustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)

ClientGetDevicePoolCompatibilityConfigurationlocationTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityConfigurationlocationTypeDef",
    {"latitude": float, "longitude": float},
    total=False,
)

ClientGetDevicePoolCompatibilityConfigurationradiosTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityConfigurationradiosTypeDef",
    {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool},
    total=False,
)

ClientGetDevicePoolCompatibilityConfigurationTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityConfigurationTypeDef",
    {
        "extraDataPackageArn": str,
        "networkProfileArn": str,
        "locale": str,
        "location": ClientGetDevicePoolCompatibilityConfigurationlocationTypeDef,
        "vpceConfigurationArns": List[str],
        "customerArtifactPaths": ClientGetDevicePoolCompatibilityConfigurationcustomerArtifactPathsTypeDef,
        "radios": ClientGetDevicePoolCompatibilityConfigurationradiosTypeDef,
        "auxiliaryApps": List[str],
        "billingMethod": Literal["METERED", "UNMETERED"],
    },
    total=False,
)

ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdevicecpuTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)

ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)

ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceresolutionTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)

ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdevicecpuTypeDef,
        "resolution": ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)

ClientGetDevicePoolCompatibilityResponsecompatibleDevicesincompatibilityMessagesTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesincompatibilityMessagesTypeDef",
    {
        "message": str,
        "type": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
    },
    total=False,
)

ClientGetDevicePoolCompatibilityResponsecompatibleDevicesTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesTypeDef",
    {
        "device": ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceTypeDef,
        "compatible": bool,
        "incompatibilityMessages": List[
            ClientGetDevicePoolCompatibilityResponsecompatibleDevicesincompatibilityMessagesTypeDef
        ],
    },
    total=False,
)

ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdevicecpuTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)

ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)

ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceresolutionTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)

ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdevicecpuTypeDef,
        "resolution": ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)

ClientGetDevicePoolCompatibilityResponseincompatibleDevicesincompatibilityMessagesTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesincompatibilityMessagesTypeDef",
    {
        "message": str,
        "type": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
    },
    total=False,
)

ClientGetDevicePoolCompatibilityResponseincompatibleDevicesTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesTypeDef",
    {
        "device": ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceTypeDef,
        "compatible": bool,
        "incompatibilityMessages": List[
            ClientGetDevicePoolCompatibilityResponseincompatibleDevicesincompatibilityMessagesTypeDef
        ],
    },
    total=False,
)

ClientGetDevicePoolCompatibilityResponseTypeDef = TypedDict(
    "ClientGetDevicePoolCompatibilityResponseTypeDef",
    {
        "compatibleDevices": List[ClientGetDevicePoolCompatibilityResponsecompatibleDevicesTypeDef],
        "incompatibleDevices": List[
            ClientGetDevicePoolCompatibilityResponseincompatibleDevicesTypeDef
        ],
    },
    total=False,
)

_RequiredClientGetDevicePoolCompatibilityTestTypeDef = TypedDict(
    "_RequiredClientGetDevicePoolCompatibilityTestTypeDef",
    {
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ]
    },
)
_OptionalClientGetDevicePoolCompatibilityTestTypeDef = TypedDict(
    "_OptionalClientGetDevicePoolCompatibilityTestTypeDef",
    {"testPackageArn": str, "testSpecArn": str, "filter": str, "parameters": Dict[str, str]},
    total=False,
)


class ClientGetDevicePoolCompatibilityTestTypeDef(
    _RequiredClientGetDevicePoolCompatibilityTestTypeDef,
    _OptionalClientGetDevicePoolCompatibilityTestTypeDef,
):
    pass


ClientGetDevicePoolResponsedevicePoolrulesTypeDef = TypedDict(
    "ClientGetDevicePoolResponsedevicePoolrulesTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "value": str,
    },
    total=False,
)

ClientGetDevicePoolResponsedevicePoolTypeDef = TypedDict(
    "ClientGetDevicePoolResponsedevicePoolTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "rules": List[ClientGetDevicePoolResponsedevicePoolrulesTypeDef],
        "maxDevices": int,
    },
    total=False,
)

ClientGetDevicePoolResponseTypeDef = TypedDict(
    "ClientGetDevicePoolResponseTypeDef",
    {"devicePool": ClientGetDevicePoolResponsedevicePoolTypeDef},
    total=False,
)

ClientGetDeviceResponsedevicecpuTypeDef = TypedDict(
    "ClientGetDeviceResponsedevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)

ClientGetDeviceResponsedeviceinstancesinstanceProfileTypeDef = TypedDict(
    "ClientGetDeviceResponsedeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientGetDeviceResponsedeviceinstancesTypeDef = TypedDict(
    "ClientGetDeviceResponsedeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientGetDeviceResponsedeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)

ClientGetDeviceResponsedeviceresolutionTypeDef = TypedDict(
    "ClientGetDeviceResponsedeviceresolutionTypeDef", {"width": int, "height": int}, total=False
)

ClientGetDeviceResponsedeviceTypeDef = TypedDict(
    "ClientGetDeviceResponsedeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientGetDeviceResponsedevicecpuTypeDef,
        "resolution": ClientGetDeviceResponsedeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[ClientGetDeviceResponsedeviceinstancesTypeDef],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)

ClientGetDeviceResponseTypeDef = TypedDict(
    "ClientGetDeviceResponseTypeDef", {"device": ClientGetDeviceResponsedeviceTypeDef}, total=False
)

ClientGetInstanceProfileResponseinstanceProfileTypeDef = TypedDict(
    "ClientGetInstanceProfileResponseinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientGetInstanceProfileResponseTypeDef = TypedDict(
    "ClientGetInstanceProfileResponseTypeDef",
    {"instanceProfile": ClientGetInstanceProfileResponseinstanceProfileTypeDef},
    total=False,
)

ClientGetJobResponsejobcountersTypeDef = TypedDict(
    "ClientGetJobResponsejobcountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

ClientGetJobResponsejobdeviceMinutesTypeDef = TypedDict(
    "ClientGetJobResponsejobdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)

ClientGetJobResponsejobdevicecpuTypeDef = TypedDict(
    "ClientGetJobResponsejobdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)

ClientGetJobResponsejobdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "ClientGetJobResponsejobdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientGetJobResponsejobdeviceinstancesTypeDef = TypedDict(
    "ClientGetJobResponsejobdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientGetJobResponsejobdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)

ClientGetJobResponsejobdeviceresolutionTypeDef = TypedDict(
    "ClientGetJobResponsejobdeviceresolutionTypeDef", {"width": int, "height": int}, total=False
)

ClientGetJobResponsejobdeviceTypeDef = TypedDict(
    "ClientGetJobResponsejobdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientGetJobResponsejobdevicecpuTypeDef,
        "resolution": ClientGetJobResponsejobdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[ClientGetJobResponsejobdeviceinstancesTypeDef],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)

ClientGetJobResponsejobTypeDef = TypedDict(
    "ClientGetJobResponsejobTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientGetJobResponsejobcountersTypeDef,
        "message": str,
        "device": ClientGetJobResponsejobdeviceTypeDef,
        "instanceArn": str,
        "deviceMinutes": ClientGetJobResponsejobdeviceMinutesTypeDef,
        "videoEndpoint": str,
        "videoCapture": bool,
    },
    total=False,
)

ClientGetJobResponseTypeDef = TypedDict(
    "ClientGetJobResponseTypeDef", {"job": ClientGetJobResponsejobTypeDef}, total=False
)

ClientGetNetworkProfileResponsenetworkProfileTypeDef = TypedDict(
    "ClientGetNetworkProfileResponsenetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)

ClientGetNetworkProfileResponseTypeDef = TypedDict(
    "ClientGetNetworkProfileResponseTypeDef",
    {"networkProfile": ClientGetNetworkProfileResponsenetworkProfileTypeDef},
    total=False,
)

ClientGetOfferingStatusResponsecurrentofferingrecurringChargescostTypeDef = TypedDict(
    "ClientGetOfferingStatusResponsecurrentofferingrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)

ClientGetOfferingStatusResponsecurrentofferingrecurringChargesTypeDef = TypedDict(
    "ClientGetOfferingStatusResponsecurrentofferingrecurringChargesTypeDef",
    {
        "cost": ClientGetOfferingStatusResponsecurrentofferingrecurringChargescostTypeDef,
        "frequency": str,
    },
    total=False,
)

ClientGetOfferingStatusResponsecurrentofferingTypeDef = TypedDict(
    "ClientGetOfferingStatusResponsecurrentofferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[
            ClientGetOfferingStatusResponsecurrentofferingrecurringChargesTypeDef
        ],
    },
    total=False,
)

ClientGetOfferingStatusResponsecurrentTypeDef = TypedDict(
    "ClientGetOfferingStatusResponsecurrentTypeDef",
    {
        "type": Literal["PURCHASE", "RENEW", "SYSTEM"],
        "offering": ClientGetOfferingStatusResponsecurrentofferingTypeDef,
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)

ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargescostTypeDef = TypedDict(
    "ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)

ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargesTypeDef = TypedDict(
    "ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargesTypeDef",
    {
        "cost": ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargescostTypeDef,
        "frequency": str,
    },
    total=False,
)

ClientGetOfferingStatusResponsenextPeriodofferingTypeDef = TypedDict(
    "ClientGetOfferingStatusResponsenextPeriodofferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[
            ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargesTypeDef
        ],
    },
    total=False,
)

ClientGetOfferingStatusResponsenextPeriodTypeDef = TypedDict(
    "ClientGetOfferingStatusResponsenextPeriodTypeDef",
    {
        "type": Literal["PURCHASE", "RENEW", "SYSTEM"],
        "offering": ClientGetOfferingStatusResponsenextPeriodofferingTypeDef,
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)

ClientGetOfferingStatusResponseTypeDef = TypedDict(
    "ClientGetOfferingStatusResponseTypeDef",
    {
        "current": Dict[str, ClientGetOfferingStatusResponsecurrentTypeDef],
        "nextPeriod": Dict[str, ClientGetOfferingStatusResponsenextPeriodTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientGetProjectResponseprojectTypeDef = TypedDict(
    "ClientGetProjectResponseprojectTypeDef",
    {"arn": str, "name": str, "defaultJobTimeoutMinutes": int, "created": datetime},
    total=False,
)

ClientGetProjectResponseTypeDef = TypedDict(
    "ClientGetProjectResponseTypeDef",
    {"project": ClientGetProjectResponseprojectTypeDef},
    total=False,
)

ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef = TypedDict(
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)

ClientGetRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef = TypedDict(
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)

ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef = TypedDict(
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef = TypedDict(
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)

ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef = TypedDict(
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)

ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef = TypedDict(
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientGetRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef,
        "resolution": ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)

ClientGetRemoteAccessSessionResponseremoteAccessSessionTypeDef = TypedDict(
    "ClientGetRemoteAccessSessionResponseremoteAccessSessionTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
        "started": datetime,
        "stopped": datetime,
        "device": ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef,
        "instanceArn": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "hostAddress": str,
        "clientId": str,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef,
        "endpoint": str,
        "deviceUdid": str,
        "interactionMode": Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"],
        "skipAppResign": bool,
    },
    total=False,
)

ClientGetRemoteAccessSessionResponseTypeDef = TypedDict(
    "ClientGetRemoteAccessSessionResponseTypeDef",
    {"remoteAccessSession": ClientGetRemoteAccessSessionResponseremoteAccessSessionTypeDef},
    total=False,
)

ClientGetRunResponseruncountersTypeDef = TypedDict(
    "ClientGetRunResponseruncountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

ClientGetRunResponseruncustomerArtifactPathsTypeDef = TypedDict(
    "ClientGetRunResponseruncustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)

ClientGetRunResponserundeviceMinutesTypeDef = TypedDict(
    "ClientGetRunResponserundeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)

ClientGetRunResponserundeviceSelectionResultfiltersTypeDef = TypedDict(
    "ClientGetRunResponserundeviceSelectionResultfiltersTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)

ClientGetRunResponserundeviceSelectionResultTypeDef = TypedDict(
    "ClientGetRunResponserundeviceSelectionResultTypeDef",
    {
        "filters": List[ClientGetRunResponserundeviceSelectionResultfiltersTypeDef],
        "matchedDevicesCount": int,
        "maxDevices": int,
    },
    total=False,
)

ClientGetRunResponserunlocationTypeDef = TypedDict(
    "ClientGetRunResponserunlocationTypeDef", {"latitude": float, "longitude": float}, total=False
)

ClientGetRunResponserunnetworkProfileTypeDef = TypedDict(
    "ClientGetRunResponserunnetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)

ClientGetRunResponserunradiosTypeDef = TypedDict(
    "ClientGetRunResponserunradiosTypeDef",
    {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool},
    total=False,
)

ClientGetRunResponserunTypeDef = TypedDict(
    "ClientGetRunResponserunTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "platform": Literal["ANDROID", "IOS"],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientGetRunResponseruncountersTypeDef,
        "message": str,
        "totalJobs": int,
        "completedJobs": int,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientGetRunResponserundeviceMinutesTypeDef,
        "networkProfile": ClientGetRunResponserunnetworkProfileTypeDef,
        "parsingResultUrl": str,
        "resultCode": Literal["PARSING_FAILED", "VPC_ENDPOINT_SETUP_FAILED"],
        "seed": int,
        "appUpload": str,
        "eventCount": int,
        "jobTimeoutMinutes": int,
        "devicePoolArn": str,
        "locale": str,
        "radios": ClientGetRunResponserunradiosTypeDef,
        "location": ClientGetRunResponserunlocationTypeDef,
        "customerArtifactPaths": ClientGetRunResponseruncustomerArtifactPathsTypeDef,
        "webUrl": str,
        "skipAppResign": bool,
        "testSpecArn": str,
        "deviceSelectionResult": ClientGetRunResponserundeviceSelectionResultTypeDef,
    },
    total=False,
)

ClientGetRunResponseTypeDef = TypedDict(
    "ClientGetRunResponseTypeDef", {"run": ClientGetRunResponserunTypeDef}, total=False
)

ClientGetSuiteResponsesuitecountersTypeDef = TypedDict(
    "ClientGetSuiteResponsesuitecountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

ClientGetSuiteResponsesuitedeviceMinutesTypeDef = TypedDict(
    "ClientGetSuiteResponsesuitedeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)

ClientGetSuiteResponsesuiteTypeDef = TypedDict(
    "ClientGetSuiteResponsesuiteTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientGetSuiteResponsesuitecountersTypeDef,
        "message": str,
        "deviceMinutes": ClientGetSuiteResponsesuitedeviceMinutesTypeDef,
    },
    total=False,
)

ClientGetSuiteResponseTypeDef = TypedDict(
    "ClientGetSuiteResponseTypeDef", {"suite": ClientGetSuiteResponsesuiteTypeDef}, total=False
)

ClientGetTestGridProjectResponsetestGridProjectTypeDef = TypedDict(
    "ClientGetTestGridProjectResponsetestGridProjectTypeDef",
    {"arn": str, "name": str, "description": str, "created": datetime},
    total=False,
)

ClientGetTestGridProjectResponseTypeDef = TypedDict(
    "ClientGetTestGridProjectResponseTypeDef",
    {"testGridProject": ClientGetTestGridProjectResponsetestGridProjectTypeDef},
    total=False,
)

ClientGetTestGridSessionResponsetestGridSessionTypeDef = TypedDict(
    "ClientGetTestGridSessionResponsetestGridSessionTypeDef",
    {
        "arn": str,
        "status": Literal["ACTIVE", "CLOSED", "ERRORED"],
        "created": datetime,
        "ended": datetime,
        "billingMinutes": float,
        "seleniumProperties": str,
    },
    total=False,
)

ClientGetTestGridSessionResponseTypeDef = TypedDict(
    "ClientGetTestGridSessionResponseTypeDef",
    {"testGridSession": ClientGetTestGridSessionResponsetestGridSessionTypeDef},
    total=False,
)

ClientGetTestResponsetestcountersTypeDef = TypedDict(
    "ClientGetTestResponsetestcountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

ClientGetTestResponsetestdeviceMinutesTypeDef = TypedDict(
    "ClientGetTestResponsetestdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)

ClientGetTestResponsetestTypeDef = TypedDict(
    "ClientGetTestResponsetestTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientGetTestResponsetestcountersTypeDef,
        "message": str,
        "deviceMinutes": ClientGetTestResponsetestdeviceMinutesTypeDef,
    },
    total=False,
)

ClientGetTestResponseTypeDef = TypedDict(
    "ClientGetTestResponseTypeDef", {"test": ClientGetTestResponsetestTypeDef}, total=False
)

ClientGetUploadResponseuploadTypeDef = TypedDict(
    "ClientGetUploadResponseuploadTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ],
        "status": Literal["INITIALIZED", "PROCESSING", "SUCCEEDED", "FAILED"],
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": Literal["CURATED", "PRIVATE"],
    },
    total=False,
)

ClientGetUploadResponseTypeDef = TypedDict(
    "ClientGetUploadResponseTypeDef", {"upload": ClientGetUploadResponseuploadTypeDef}, total=False
)

ClientGetVpceConfigurationResponsevpceConfigurationTypeDef = TypedDict(
    "ClientGetVpceConfigurationResponsevpceConfigurationTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)

ClientGetVpceConfigurationResponseTypeDef = TypedDict(
    "ClientGetVpceConfigurationResponseTypeDef",
    {"vpceConfiguration": ClientGetVpceConfigurationResponsevpceConfigurationTypeDef},
    total=False,
)

ClientInstallToRemoteAccessSessionResponseappUploadTypeDef = TypedDict(
    "ClientInstallToRemoteAccessSessionResponseappUploadTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ],
        "status": Literal["INITIALIZED", "PROCESSING", "SUCCEEDED", "FAILED"],
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": Literal["CURATED", "PRIVATE"],
    },
    total=False,
)

ClientInstallToRemoteAccessSessionResponseTypeDef = TypedDict(
    "ClientInstallToRemoteAccessSessionResponseTypeDef",
    {"appUpload": ClientInstallToRemoteAccessSessionResponseappUploadTypeDef},
    total=False,
)

ClientListArtifactsResponseartifactsTypeDef = TypedDict(
    "ClientListArtifactsResponseartifactsTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "UNKNOWN",
            "SCREENSHOT",
            "DEVICE_LOG",
            "MESSAGE_LOG",
            "VIDEO_LOG",
            "RESULT_LOG",
            "SERVICE_LOG",
            "WEBKIT_LOG",
            "INSTRUMENTATION_OUTPUT",
            "EXERCISER_MONKEY_OUTPUT",
            "CALABASH_JSON_OUTPUT",
            "CALABASH_PRETTY_OUTPUT",
            "CALABASH_STANDARD_OUTPUT",
            "CALABASH_JAVA_XML_OUTPUT",
            "AUTOMATION_OUTPUT",
            "APPIUM_SERVER_OUTPUT",
            "APPIUM_JAVA_OUTPUT",
            "APPIUM_JAVA_XML_OUTPUT",
            "APPIUM_PYTHON_OUTPUT",
            "APPIUM_PYTHON_XML_OUTPUT",
            "EXPLORER_EVENT_LOG",
            "EXPLORER_SUMMARY_LOG",
            "APPLICATION_CRASH_REPORT",
            "XCTEST_LOG",
            "VIDEO",
            "CUSTOMER_ARTIFACT",
            "CUSTOMER_ARTIFACT_LOG",
            "TESTSPEC_OUTPUT",
        ],
        "extension": str,
        "url": str,
    },
    total=False,
)

ClientListArtifactsResponseTypeDef = TypedDict(
    "ClientListArtifactsResponseTypeDef",
    {"artifacts": List[ClientListArtifactsResponseartifactsTypeDef], "nextToken": str},
    total=False,
)

ClientListDeviceInstancesResponsedeviceInstancesinstanceProfileTypeDef = TypedDict(
    "ClientListDeviceInstancesResponsedeviceInstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientListDeviceInstancesResponsedeviceInstancesTypeDef = TypedDict(
    "ClientListDeviceInstancesResponsedeviceInstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientListDeviceInstancesResponsedeviceInstancesinstanceProfileTypeDef,
    },
    total=False,
)

ClientListDeviceInstancesResponseTypeDef = TypedDict(
    "ClientListDeviceInstancesResponseTypeDef",
    {
        "deviceInstances": List[ClientListDeviceInstancesResponsedeviceInstancesTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListDevicePoolsResponsedevicePoolsrulesTypeDef = TypedDict(
    "ClientListDevicePoolsResponsedevicePoolsrulesTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "value": str,
    },
    total=False,
)

ClientListDevicePoolsResponsedevicePoolsTypeDef = TypedDict(
    "ClientListDevicePoolsResponsedevicePoolsTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "rules": List[ClientListDevicePoolsResponsedevicePoolsrulesTypeDef],
        "maxDevices": int,
    },
    total=False,
)

ClientListDevicePoolsResponseTypeDef = TypedDict(
    "ClientListDevicePoolsResponseTypeDef",
    {"devicePools": List[ClientListDevicePoolsResponsedevicePoolsTypeDef], "nextToken": str},
    total=False,
)

ClientListDevicesFiltersTypeDef = TypedDict(
    "ClientListDevicesFiltersTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)

ClientListDevicesResponsedevicescpuTypeDef = TypedDict(
    "ClientListDevicesResponsedevicescpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)

ClientListDevicesResponsedevicesinstancesinstanceProfileTypeDef = TypedDict(
    "ClientListDevicesResponsedevicesinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientListDevicesResponsedevicesinstancesTypeDef = TypedDict(
    "ClientListDevicesResponsedevicesinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientListDevicesResponsedevicesinstancesinstanceProfileTypeDef,
    },
    total=False,
)

ClientListDevicesResponsedevicesresolutionTypeDef = TypedDict(
    "ClientListDevicesResponsedevicesresolutionTypeDef", {"width": int, "height": int}, total=False
)

ClientListDevicesResponsedevicesTypeDef = TypedDict(
    "ClientListDevicesResponsedevicesTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientListDevicesResponsedevicescpuTypeDef,
        "resolution": ClientListDevicesResponsedevicesresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[ClientListDevicesResponsedevicesinstancesTypeDef],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)

ClientListDevicesResponseTypeDef = TypedDict(
    "ClientListDevicesResponseTypeDef",
    {"devices": List[ClientListDevicesResponsedevicesTypeDef], "nextToken": str},
    total=False,
)

ClientListInstanceProfilesResponseinstanceProfilesTypeDef = TypedDict(
    "ClientListInstanceProfilesResponseinstanceProfilesTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientListInstanceProfilesResponseTypeDef = TypedDict(
    "ClientListInstanceProfilesResponseTypeDef",
    {
        "instanceProfiles": List[ClientListInstanceProfilesResponseinstanceProfilesTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListJobsResponsejobscountersTypeDef = TypedDict(
    "ClientListJobsResponsejobscountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

ClientListJobsResponsejobsdeviceMinutesTypeDef = TypedDict(
    "ClientListJobsResponsejobsdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)

ClientListJobsResponsejobsdevicecpuTypeDef = TypedDict(
    "ClientListJobsResponsejobsdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)

ClientListJobsResponsejobsdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "ClientListJobsResponsejobsdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientListJobsResponsejobsdeviceinstancesTypeDef = TypedDict(
    "ClientListJobsResponsejobsdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientListJobsResponsejobsdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)

ClientListJobsResponsejobsdeviceresolutionTypeDef = TypedDict(
    "ClientListJobsResponsejobsdeviceresolutionTypeDef", {"width": int, "height": int}, total=False
)

ClientListJobsResponsejobsdeviceTypeDef = TypedDict(
    "ClientListJobsResponsejobsdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientListJobsResponsejobsdevicecpuTypeDef,
        "resolution": ClientListJobsResponsejobsdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[ClientListJobsResponsejobsdeviceinstancesTypeDef],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)

ClientListJobsResponsejobsTypeDef = TypedDict(
    "ClientListJobsResponsejobsTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientListJobsResponsejobscountersTypeDef,
        "message": str,
        "device": ClientListJobsResponsejobsdeviceTypeDef,
        "instanceArn": str,
        "deviceMinutes": ClientListJobsResponsejobsdeviceMinutesTypeDef,
        "videoEndpoint": str,
        "videoCapture": bool,
    },
    total=False,
)

ClientListJobsResponseTypeDef = TypedDict(
    "ClientListJobsResponseTypeDef",
    {"jobs": List[ClientListJobsResponsejobsTypeDef], "nextToken": str},
    total=False,
)

ClientListNetworkProfilesResponsenetworkProfilesTypeDef = TypedDict(
    "ClientListNetworkProfilesResponsenetworkProfilesTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)

ClientListNetworkProfilesResponseTypeDef = TypedDict(
    "ClientListNetworkProfilesResponseTypeDef",
    {
        "networkProfiles": List[ClientListNetworkProfilesResponsenetworkProfilesTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListOfferingPromotionsResponseofferingPromotionsTypeDef = TypedDict(
    "ClientListOfferingPromotionsResponseofferingPromotionsTypeDef",
    {"id": str, "description": str},
    total=False,
)

ClientListOfferingPromotionsResponseTypeDef = TypedDict(
    "ClientListOfferingPromotionsResponseTypeDef",
    {
        "offeringPromotions": List[ClientListOfferingPromotionsResponseofferingPromotionsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListOfferingTransactionsResponseofferingTransactionscostTypeDef = TypedDict(
    "ClientListOfferingTransactionsResponseofferingTransactionscostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)

ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef = TypedDict(
    "ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)

ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef = TypedDict(
    "ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef",
    {
        "cost": ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef,
        "frequency": str,
    },
    total=False,
)

ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingTypeDef = TypedDict(
    "ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[
            ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef
        ],
    },
    total=False,
)

ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusTypeDef = TypedDict(
    "ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusTypeDef",
    {
        "type": Literal["PURCHASE", "RENEW", "SYSTEM"],
        "offering": ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingTypeDef,
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)

ClientListOfferingTransactionsResponseofferingTransactionsTypeDef = TypedDict(
    "ClientListOfferingTransactionsResponseofferingTransactionsTypeDef",
    {
        "offeringStatus": ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusTypeDef,
        "transactionId": str,
        "offeringPromotionId": str,
        "createdOn": datetime,
        "cost": ClientListOfferingTransactionsResponseofferingTransactionscostTypeDef,
    },
    total=False,
)

ClientListOfferingTransactionsResponseTypeDef = TypedDict(
    "ClientListOfferingTransactionsResponseTypeDef",
    {
        "offeringTransactions": List[
            ClientListOfferingTransactionsResponseofferingTransactionsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListOfferingsResponseofferingsrecurringChargescostTypeDef = TypedDict(
    "ClientListOfferingsResponseofferingsrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)

ClientListOfferingsResponseofferingsrecurringChargesTypeDef = TypedDict(
    "ClientListOfferingsResponseofferingsrecurringChargesTypeDef",
    {"cost": ClientListOfferingsResponseofferingsrecurringChargescostTypeDef, "frequency": str},
    total=False,
)

ClientListOfferingsResponseofferingsTypeDef = TypedDict(
    "ClientListOfferingsResponseofferingsTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[ClientListOfferingsResponseofferingsrecurringChargesTypeDef],
    },
    total=False,
)

ClientListOfferingsResponseTypeDef = TypedDict(
    "ClientListOfferingsResponseTypeDef",
    {"offerings": List[ClientListOfferingsResponseofferingsTypeDef], "nextToken": str},
    total=False,
)

ClientListProjectsResponseprojectsTypeDef = TypedDict(
    "ClientListProjectsResponseprojectsTypeDef",
    {"arn": str, "name": str, "defaultJobTimeoutMinutes": int, "created": datetime},
    total=False,
)

ClientListProjectsResponseTypeDef = TypedDict(
    "ClientListProjectsResponseTypeDef",
    {"projects": List[ClientListProjectsResponseprojectsTypeDef], "nextToken": str},
    total=False,
)

ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceMinutesTypeDef = TypedDict(
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)

ClientListRemoteAccessSessionsResponseremoteAccessSessionsdevicecpuTypeDef = TypedDict(
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)

ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesTypeDef = TypedDict(
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)

ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceresolutionTypeDef = TypedDict(
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)

ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceTypeDef = TypedDict(
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientListRemoteAccessSessionsResponseremoteAccessSessionsdevicecpuTypeDef,
        "resolution": ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)

ClientListRemoteAccessSessionsResponseremoteAccessSessionsTypeDef = TypedDict(
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
        "started": datetime,
        "stopped": datetime,
        "device": ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceTypeDef,
        "instanceArn": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "hostAddress": str,
        "clientId": str,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceMinutesTypeDef,
        "endpoint": str,
        "deviceUdid": str,
        "interactionMode": Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"],
        "skipAppResign": bool,
    },
    total=False,
)

ClientListRemoteAccessSessionsResponseTypeDef = TypedDict(
    "ClientListRemoteAccessSessionsResponseTypeDef",
    {
        "remoteAccessSessions": List[
            ClientListRemoteAccessSessionsResponseremoteAccessSessionsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListRunsResponserunscountersTypeDef = TypedDict(
    "ClientListRunsResponserunscountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

ClientListRunsResponserunscustomerArtifactPathsTypeDef = TypedDict(
    "ClientListRunsResponserunscustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)

ClientListRunsResponserunsdeviceMinutesTypeDef = TypedDict(
    "ClientListRunsResponserunsdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)

ClientListRunsResponserunsdeviceSelectionResultfiltersTypeDef = TypedDict(
    "ClientListRunsResponserunsdeviceSelectionResultfiltersTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)

ClientListRunsResponserunsdeviceSelectionResultTypeDef = TypedDict(
    "ClientListRunsResponserunsdeviceSelectionResultTypeDef",
    {
        "filters": List[ClientListRunsResponserunsdeviceSelectionResultfiltersTypeDef],
        "matchedDevicesCount": int,
        "maxDevices": int,
    },
    total=False,
)

ClientListRunsResponserunslocationTypeDef = TypedDict(
    "ClientListRunsResponserunslocationTypeDef",
    {"latitude": float, "longitude": float},
    total=False,
)

ClientListRunsResponserunsnetworkProfileTypeDef = TypedDict(
    "ClientListRunsResponserunsnetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)

ClientListRunsResponserunsradiosTypeDef = TypedDict(
    "ClientListRunsResponserunsradiosTypeDef",
    {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool},
    total=False,
)

ClientListRunsResponserunsTypeDef = TypedDict(
    "ClientListRunsResponserunsTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "platform": Literal["ANDROID", "IOS"],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientListRunsResponserunscountersTypeDef,
        "message": str,
        "totalJobs": int,
        "completedJobs": int,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientListRunsResponserunsdeviceMinutesTypeDef,
        "networkProfile": ClientListRunsResponserunsnetworkProfileTypeDef,
        "parsingResultUrl": str,
        "resultCode": Literal["PARSING_FAILED", "VPC_ENDPOINT_SETUP_FAILED"],
        "seed": int,
        "appUpload": str,
        "eventCount": int,
        "jobTimeoutMinutes": int,
        "devicePoolArn": str,
        "locale": str,
        "radios": ClientListRunsResponserunsradiosTypeDef,
        "location": ClientListRunsResponserunslocationTypeDef,
        "customerArtifactPaths": ClientListRunsResponserunscustomerArtifactPathsTypeDef,
        "webUrl": str,
        "skipAppResign": bool,
        "testSpecArn": str,
        "deviceSelectionResult": ClientListRunsResponserunsdeviceSelectionResultTypeDef,
    },
    total=False,
)

ClientListRunsResponseTypeDef = TypedDict(
    "ClientListRunsResponseTypeDef",
    {"runs": List[ClientListRunsResponserunsTypeDef], "nextToken": str},
    total=False,
)

ClientListSamplesResponsesamplesTypeDef = TypedDict(
    "ClientListSamplesResponsesamplesTypeDef",
    {
        "arn": str,
        "type": Literal[
            "CPU",
            "MEMORY",
            "THREADS",
            "RX_RATE",
            "TX_RATE",
            "RX",
            "TX",
            "NATIVE_FRAMES",
            "NATIVE_FPS",
            "NATIVE_MIN_DRAWTIME",
            "NATIVE_AVG_DRAWTIME",
            "NATIVE_MAX_DRAWTIME",
            "OPENGL_FRAMES",
            "OPENGL_FPS",
            "OPENGL_MIN_DRAWTIME",
            "OPENGL_AVG_DRAWTIME",
            "OPENGL_MAX_DRAWTIME",
        ],
        "url": str,
    },
    total=False,
)

ClientListSamplesResponseTypeDef = TypedDict(
    "ClientListSamplesResponseTypeDef",
    {"samples": List[ClientListSamplesResponsesamplesTypeDef], "nextToken": str},
    total=False,
)

ClientListSuitesResponsesuitescountersTypeDef = TypedDict(
    "ClientListSuitesResponsesuitescountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

ClientListSuitesResponsesuitesdeviceMinutesTypeDef = TypedDict(
    "ClientListSuitesResponsesuitesdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)

ClientListSuitesResponsesuitesTypeDef = TypedDict(
    "ClientListSuitesResponsesuitesTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientListSuitesResponsesuitescountersTypeDef,
        "message": str,
        "deviceMinutes": ClientListSuitesResponsesuitesdeviceMinutesTypeDef,
    },
    total=False,
)

ClientListSuitesResponseTypeDef = TypedDict(
    "ClientListSuitesResponseTypeDef",
    {"suites": List[ClientListSuitesResponsesuitesTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)

ClientListTestGridProjectsResponsetestGridProjectsTypeDef = TypedDict(
    "ClientListTestGridProjectsResponsetestGridProjectsTypeDef",
    {"arn": str, "name": str, "description": str, "created": datetime},
    total=False,
)

ClientListTestGridProjectsResponseTypeDef = TypedDict(
    "ClientListTestGridProjectsResponseTypeDef",
    {
        "testGridProjects": List[ClientListTestGridProjectsResponsetestGridProjectsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListTestGridSessionActionsResponseactionsTypeDef = TypedDict(
    "ClientListTestGridSessionActionsResponseactionsTypeDef",
    {"action": str, "started": datetime, "duration": int, "statusCode": str, "requestMethod": str},
    total=False,
)

ClientListTestGridSessionActionsResponseTypeDef = TypedDict(
    "ClientListTestGridSessionActionsResponseTypeDef",
    {"actions": List[ClientListTestGridSessionActionsResponseactionsTypeDef], "nextToken": str},
    total=False,
)

ClientListTestGridSessionArtifactsResponseartifactsTypeDef = TypedDict(
    "ClientListTestGridSessionArtifactsResponseartifactsTypeDef",
    {"filename": str, "type": Literal["UNKNOWN", "VIDEO", "SELENIUM_LOG"], "url": str},
    total=False,
)

ClientListTestGridSessionArtifactsResponseTypeDef = TypedDict(
    "ClientListTestGridSessionArtifactsResponseTypeDef",
    {
        "artifacts": List[ClientListTestGridSessionArtifactsResponseartifactsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListTestGridSessionsResponsetestGridSessionsTypeDef = TypedDict(
    "ClientListTestGridSessionsResponsetestGridSessionsTypeDef",
    {
        "arn": str,
        "status": Literal["ACTIVE", "CLOSED", "ERRORED"],
        "created": datetime,
        "ended": datetime,
        "billingMinutes": float,
        "seleniumProperties": str,
    },
    total=False,
)

ClientListTestGridSessionsResponseTypeDef = TypedDict(
    "ClientListTestGridSessionsResponseTypeDef",
    {
        "testGridSessions": List[ClientListTestGridSessionsResponsetestGridSessionsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListTestsResponsetestscountersTypeDef = TypedDict(
    "ClientListTestsResponsetestscountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

ClientListTestsResponsetestsdeviceMinutesTypeDef = TypedDict(
    "ClientListTestsResponsetestsdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)

ClientListTestsResponsetestsTypeDef = TypedDict(
    "ClientListTestsResponsetestsTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientListTestsResponsetestscountersTypeDef,
        "message": str,
        "deviceMinutes": ClientListTestsResponsetestsdeviceMinutesTypeDef,
    },
    total=False,
)

ClientListTestsResponseTypeDef = TypedDict(
    "ClientListTestsResponseTypeDef",
    {"tests": List[ClientListTestsResponsetestsTypeDef], "nextToken": str},
    total=False,
)

ClientListUniqueProblemsResponseuniqueProblemsproblemsdevicecpuTypeDef = TypedDict(
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)

ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesTypeDef = TypedDict(
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)

ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceresolutionTypeDef = TypedDict(
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)

ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceTypeDef = TypedDict(
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientListUniqueProblemsResponseuniqueProblemsproblemsdevicecpuTypeDef,
        "resolution": ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)

ClientListUniqueProblemsResponseuniqueProblemsproblemsjobTypeDef = TypedDict(
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsjobTypeDef",
    {"arn": str, "name": str},
    total=False,
)

ClientListUniqueProblemsResponseuniqueProblemsproblemsrunTypeDef = TypedDict(
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsrunTypeDef",
    {"arn": str, "name": str},
    total=False,
)

ClientListUniqueProblemsResponseuniqueProblemsproblemssuiteTypeDef = TypedDict(
    "ClientListUniqueProblemsResponseuniqueProblemsproblemssuiteTypeDef",
    {"arn": str, "name": str},
    total=False,
)

ClientListUniqueProblemsResponseuniqueProblemsproblemstestTypeDef = TypedDict(
    "ClientListUniqueProblemsResponseuniqueProblemsproblemstestTypeDef",
    {"arn": str, "name": str},
    total=False,
)

ClientListUniqueProblemsResponseuniqueProblemsproblemsTypeDef = TypedDict(
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsTypeDef",
    {
        "run": ClientListUniqueProblemsResponseuniqueProblemsproblemsrunTypeDef,
        "job": ClientListUniqueProblemsResponseuniqueProblemsproblemsjobTypeDef,
        "suite": ClientListUniqueProblemsResponseuniqueProblemsproblemssuiteTypeDef,
        "test": ClientListUniqueProblemsResponseuniqueProblemsproblemstestTypeDef,
        "device": ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceTypeDef,
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
    },
    total=False,
)

ClientListUniqueProblemsResponseuniqueProblemsTypeDef = TypedDict(
    "ClientListUniqueProblemsResponseuniqueProblemsTypeDef",
    {
        "message": str,
        "problems": List[ClientListUniqueProblemsResponseuniqueProblemsproblemsTypeDef],
    },
    total=False,
)

ClientListUniqueProblemsResponseTypeDef = TypedDict(
    "ClientListUniqueProblemsResponseTypeDef",
    {
        "uniqueProblems": Dict[str, List[ClientListUniqueProblemsResponseuniqueProblemsTypeDef]],
        "nextToken": str,
    },
    total=False,
)

ClientListUploadsResponseuploadsTypeDef = TypedDict(
    "ClientListUploadsResponseuploadsTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ],
        "status": Literal["INITIALIZED", "PROCESSING", "SUCCEEDED", "FAILED"],
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": Literal["CURATED", "PRIVATE"],
    },
    total=False,
)

ClientListUploadsResponseTypeDef = TypedDict(
    "ClientListUploadsResponseTypeDef",
    {"uploads": List[ClientListUploadsResponseuploadsTypeDef], "nextToken": str},
    total=False,
)

ClientListVpceConfigurationsResponsevpceConfigurationsTypeDef = TypedDict(
    "ClientListVpceConfigurationsResponsevpceConfigurationsTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)

ClientListVpceConfigurationsResponseTypeDef = TypedDict(
    "ClientListVpceConfigurationsResponseTypeDef",
    {
        "vpceConfigurations": List[ClientListVpceConfigurationsResponsevpceConfigurationsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientPurchaseOfferingResponseofferingTransactioncostTypeDef = TypedDict(
    "ClientPurchaseOfferingResponseofferingTransactioncostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)

ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef = TypedDict(
    "ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)

ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef = TypedDict(
    "ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef",
    {
        "cost": ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef,
        "frequency": str,
    },
    total=False,
)

ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingTypeDef = TypedDict(
    "ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[
            ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef
        ],
    },
    total=False,
)

ClientPurchaseOfferingResponseofferingTransactionofferingStatusTypeDef = TypedDict(
    "ClientPurchaseOfferingResponseofferingTransactionofferingStatusTypeDef",
    {
        "type": Literal["PURCHASE", "RENEW", "SYSTEM"],
        "offering": ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingTypeDef,
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)

ClientPurchaseOfferingResponseofferingTransactionTypeDef = TypedDict(
    "ClientPurchaseOfferingResponseofferingTransactionTypeDef",
    {
        "offeringStatus": ClientPurchaseOfferingResponseofferingTransactionofferingStatusTypeDef,
        "transactionId": str,
        "offeringPromotionId": str,
        "createdOn": datetime,
        "cost": ClientPurchaseOfferingResponseofferingTransactioncostTypeDef,
    },
    total=False,
)

ClientPurchaseOfferingResponseTypeDef = TypedDict(
    "ClientPurchaseOfferingResponseTypeDef",
    {"offeringTransaction": ClientPurchaseOfferingResponseofferingTransactionTypeDef},
    total=False,
)

ClientRenewOfferingResponseofferingTransactioncostTypeDef = TypedDict(
    "ClientRenewOfferingResponseofferingTransactioncostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)

ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef = TypedDict(
    "ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)

ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef = TypedDict(
    "ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef",
    {
        "cost": ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef,
        "frequency": str,
    },
    total=False,
)

ClientRenewOfferingResponseofferingTransactionofferingStatusofferingTypeDef = TypedDict(
    "ClientRenewOfferingResponseofferingTransactionofferingStatusofferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[
            ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef
        ],
    },
    total=False,
)

ClientRenewOfferingResponseofferingTransactionofferingStatusTypeDef = TypedDict(
    "ClientRenewOfferingResponseofferingTransactionofferingStatusTypeDef",
    {
        "type": Literal["PURCHASE", "RENEW", "SYSTEM"],
        "offering": ClientRenewOfferingResponseofferingTransactionofferingStatusofferingTypeDef,
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)

ClientRenewOfferingResponseofferingTransactionTypeDef = TypedDict(
    "ClientRenewOfferingResponseofferingTransactionTypeDef",
    {
        "offeringStatus": ClientRenewOfferingResponseofferingTransactionofferingStatusTypeDef,
        "transactionId": str,
        "offeringPromotionId": str,
        "createdOn": datetime,
        "cost": ClientRenewOfferingResponseofferingTransactioncostTypeDef,
    },
    total=False,
)

ClientRenewOfferingResponseTypeDef = TypedDict(
    "ClientRenewOfferingResponseTypeDef",
    {"offeringTransaction": ClientRenewOfferingResponseofferingTransactionTypeDef},
    total=False,
)

ClientScheduleRunConfigurationcustomerArtifactPathsTypeDef = TypedDict(
    "ClientScheduleRunConfigurationcustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)

ClientScheduleRunConfigurationlocationTypeDef = TypedDict(
    "ClientScheduleRunConfigurationlocationTypeDef",
    {"latitude": float, "longitude": float},
    total=False,
)

ClientScheduleRunConfigurationradiosTypeDef = TypedDict(
    "ClientScheduleRunConfigurationradiosTypeDef",
    {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool},
    total=False,
)

ClientScheduleRunConfigurationTypeDef = TypedDict(
    "ClientScheduleRunConfigurationTypeDef",
    {
        "extraDataPackageArn": str,
        "networkProfileArn": str,
        "locale": str,
        "location": ClientScheduleRunConfigurationlocationTypeDef,
        "vpceConfigurationArns": List[str],
        "customerArtifactPaths": ClientScheduleRunConfigurationcustomerArtifactPathsTypeDef,
        "radios": ClientScheduleRunConfigurationradiosTypeDef,
        "auxiliaryApps": List[str],
        "billingMethod": Literal["METERED", "UNMETERED"],
    },
    total=False,
)

ClientScheduleRunDeviceSelectionConfigurationfiltersTypeDef = TypedDict(
    "ClientScheduleRunDeviceSelectionConfigurationfiltersTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)

_RequiredClientScheduleRunDeviceSelectionConfigurationTypeDef = TypedDict(
    "_RequiredClientScheduleRunDeviceSelectionConfigurationTypeDef",
    {"filters": List[ClientScheduleRunDeviceSelectionConfigurationfiltersTypeDef]},
)
_OptionalClientScheduleRunDeviceSelectionConfigurationTypeDef = TypedDict(
    "_OptionalClientScheduleRunDeviceSelectionConfigurationTypeDef",
    {"maxDevices": int},
    total=False,
)


class ClientScheduleRunDeviceSelectionConfigurationTypeDef(
    _RequiredClientScheduleRunDeviceSelectionConfigurationTypeDef,
    _OptionalClientScheduleRunDeviceSelectionConfigurationTypeDef,
):
    pass


ClientScheduleRunExecutionConfigurationTypeDef = TypedDict(
    "ClientScheduleRunExecutionConfigurationTypeDef",
    {
        "jobTimeoutMinutes": int,
        "accountsCleanup": bool,
        "appPackagesCleanup": bool,
        "videoCapture": bool,
        "skipAppResign": bool,
    },
    total=False,
)

ClientScheduleRunResponseruncountersTypeDef = TypedDict(
    "ClientScheduleRunResponseruncountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

ClientScheduleRunResponseruncustomerArtifactPathsTypeDef = TypedDict(
    "ClientScheduleRunResponseruncustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)

ClientScheduleRunResponserundeviceMinutesTypeDef = TypedDict(
    "ClientScheduleRunResponserundeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)

ClientScheduleRunResponserundeviceSelectionResultfiltersTypeDef = TypedDict(
    "ClientScheduleRunResponserundeviceSelectionResultfiltersTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)

ClientScheduleRunResponserundeviceSelectionResultTypeDef = TypedDict(
    "ClientScheduleRunResponserundeviceSelectionResultTypeDef",
    {
        "filters": List[ClientScheduleRunResponserundeviceSelectionResultfiltersTypeDef],
        "matchedDevicesCount": int,
        "maxDevices": int,
    },
    total=False,
)

ClientScheduleRunResponserunlocationTypeDef = TypedDict(
    "ClientScheduleRunResponserunlocationTypeDef",
    {"latitude": float, "longitude": float},
    total=False,
)

ClientScheduleRunResponserunnetworkProfileTypeDef = TypedDict(
    "ClientScheduleRunResponserunnetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)

ClientScheduleRunResponserunradiosTypeDef = TypedDict(
    "ClientScheduleRunResponserunradiosTypeDef",
    {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool},
    total=False,
)

ClientScheduleRunResponserunTypeDef = TypedDict(
    "ClientScheduleRunResponserunTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "platform": Literal["ANDROID", "IOS"],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientScheduleRunResponseruncountersTypeDef,
        "message": str,
        "totalJobs": int,
        "completedJobs": int,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientScheduleRunResponserundeviceMinutesTypeDef,
        "networkProfile": ClientScheduleRunResponserunnetworkProfileTypeDef,
        "parsingResultUrl": str,
        "resultCode": Literal["PARSING_FAILED", "VPC_ENDPOINT_SETUP_FAILED"],
        "seed": int,
        "appUpload": str,
        "eventCount": int,
        "jobTimeoutMinutes": int,
        "devicePoolArn": str,
        "locale": str,
        "radios": ClientScheduleRunResponserunradiosTypeDef,
        "location": ClientScheduleRunResponserunlocationTypeDef,
        "customerArtifactPaths": ClientScheduleRunResponseruncustomerArtifactPathsTypeDef,
        "webUrl": str,
        "skipAppResign": bool,
        "testSpecArn": str,
        "deviceSelectionResult": ClientScheduleRunResponserundeviceSelectionResultTypeDef,
    },
    total=False,
)

ClientScheduleRunResponseTypeDef = TypedDict(
    "ClientScheduleRunResponseTypeDef", {"run": ClientScheduleRunResponserunTypeDef}, total=False
)

_RequiredClientScheduleRunTestTypeDef = TypedDict(
    "_RequiredClientScheduleRunTestTypeDef",
    {
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ]
    },
)
_OptionalClientScheduleRunTestTypeDef = TypedDict(
    "_OptionalClientScheduleRunTestTypeDef",
    {"testPackageArn": str, "testSpecArn": str, "filter": str, "parameters": Dict[str, str]},
    total=False,
)


class ClientScheduleRunTestTypeDef(
    _RequiredClientScheduleRunTestTypeDef, _OptionalClientScheduleRunTestTypeDef
):
    pass


ClientStopJobResponsejobcountersTypeDef = TypedDict(
    "ClientStopJobResponsejobcountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

ClientStopJobResponsejobdeviceMinutesTypeDef = TypedDict(
    "ClientStopJobResponsejobdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)

ClientStopJobResponsejobdevicecpuTypeDef = TypedDict(
    "ClientStopJobResponsejobdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)

ClientStopJobResponsejobdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "ClientStopJobResponsejobdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientStopJobResponsejobdeviceinstancesTypeDef = TypedDict(
    "ClientStopJobResponsejobdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientStopJobResponsejobdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)

ClientStopJobResponsejobdeviceresolutionTypeDef = TypedDict(
    "ClientStopJobResponsejobdeviceresolutionTypeDef", {"width": int, "height": int}, total=False
)

ClientStopJobResponsejobdeviceTypeDef = TypedDict(
    "ClientStopJobResponsejobdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientStopJobResponsejobdevicecpuTypeDef,
        "resolution": ClientStopJobResponsejobdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[ClientStopJobResponsejobdeviceinstancesTypeDef],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)

ClientStopJobResponsejobTypeDef = TypedDict(
    "ClientStopJobResponsejobTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientStopJobResponsejobcountersTypeDef,
        "message": str,
        "device": ClientStopJobResponsejobdeviceTypeDef,
        "instanceArn": str,
        "deviceMinutes": ClientStopJobResponsejobdeviceMinutesTypeDef,
        "videoEndpoint": str,
        "videoCapture": bool,
    },
    total=False,
)

ClientStopJobResponseTypeDef = TypedDict(
    "ClientStopJobResponseTypeDef", {"job": ClientStopJobResponsejobTypeDef}, total=False
)

ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef = TypedDict(
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)

ClientStopRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef = TypedDict(
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)

ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef = TypedDict(
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef = TypedDict(
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)

ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef = TypedDict(
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)

ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef = TypedDict(
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientStopRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef,
        "resolution": ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)

ClientStopRemoteAccessSessionResponseremoteAccessSessionTypeDef = TypedDict(
    "ClientStopRemoteAccessSessionResponseremoteAccessSessionTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
        "started": datetime,
        "stopped": datetime,
        "device": ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef,
        "instanceArn": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "hostAddress": str,
        "clientId": str,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef,
        "endpoint": str,
        "deviceUdid": str,
        "interactionMode": Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"],
        "skipAppResign": bool,
    },
    total=False,
)

ClientStopRemoteAccessSessionResponseTypeDef = TypedDict(
    "ClientStopRemoteAccessSessionResponseTypeDef",
    {"remoteAccessSession": ClientStopRemoteAccessSessionResponseremoteAccessSessionTypeDef},
    total=False,
)

ClientStopRunResponseruncountersTypeDef = TypedDict(
    "ClientStopRunResponseruncountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

ClientStopRunResponseruncustomerArtifactPathsTypeDef = TypedDict(
    "ClientStopRunResponseruncustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)

ClientStopRunResponserundeviceMinutesTypeDef = TypedDict(
    "ClientStopRunResponserundeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)

ClientStopRunResponserundeviceSelectionResultfiltersTypeDef = TypedDict(
    "ClientStopRunResponserundeviceSelectionResultfiltersTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)

ClientStopRunResponserundeviceSelectionResultTypeDef = TypedDict(
    "ClientStopRunResponserundeviceSelectionResultTypeDef",
    {
        "filters": List[ClientStopRunResponserundeviceSelectionResultfiltersTypeDef],
        "matchedDevicesCount": int,
        "maxDevices": int,
    },
    total=False,
)

ClientStopRunResponserunlocationTypeDef = TypedDict(
    "ClientStopRunResponserunlocationTypeDef", {"latitude": float, "longitude": float}, total=False
)

ClientStopRunResponserunnetworkProfileTypeDef = TypedDict(
    "ClientStopRunResponserunnetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)

ClientStopRunResponserunradiosTypeDef = TypedDict(
    "ClientStopRunResponserunradiosTypeDef",
    {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool},
    total=False,
)

ClientStopRunResponserunTypeDef = TypedDict(
    "ClientStopRunResponserunTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "platform": Literal["ANDROID", "IOS"],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientStopRunResponseruncountersTypeDef,
        "message": str,
        "totalJobs": int,
        "completedJobs": int,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientStopRunResponserundeviceMinutesTypeDef,
        "networkProfile": ClientStopRunResponserunnetworkProfileTypeDef,
        "parsingResultUrl": str,
        "resultCode": Literal["PARSING_FAILED", "VPC_ENDPOINT_SETUP_FAILED"],
        "seed": int,
        "appUpload": str,
        "eventCount": int,
        "jobTimeoutMinutes": int,
        "devicePoolArn": str,
        "locale": str,
        "radios": ClientStopRunResponserunradiosTypeDef,
        "location": ClientStopRunResponserunlocationTypeDef,
        "customerArtifactPaths": ClientStopRunResponseruncustomerArtifactPathsTypeDef,
        "webUrl": str,
        "skipAppResign": bool,
        "testSpecArn": str,
        "deviceSelectionResult": ClientStopRunResponserundeviceSelectionResultTypeDef,
    },
    total=False,
)

ClientStopRunResponseTypeDef = TypedDict(
    "ClientStopRunResponseTypeDef", {"run": ClientStopRunResponserunTypeDef}, total=False
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientUpdateDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef = TypedDict(
    "ClientUpdateDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientUpdateDeviceInstanceResponsedeviceInstanceTypeDef = TypedDict(
    "ClientUpdateDeviceInstanceResponsedeviceInstanceTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientUpdateDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef,
    },
    total=False,
)

ClientUpdateDeviceInstanceResponseTypeDef = TypedDict(
    "ClientUpdateDeviceInstanceResponseTypeDef",
    {"deviceInstance": ClientUpdateDeviceInstanceResponsedeviceInstanceTypeDef},
    total=False,
)

ClientUpdateDevicePoolResponsedevicePoolrulesTypeDef = TypedDict(
    "ClientUpdateDevicePoolResponsedevicePoolrulesTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "value": str,
    },
    total=False,
)

ClientUpdateDevicePoolResponsedevicePoolTypeDef = TypedDict(
    "ClientUpdateDevicePoolResponsedevicePoolTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "rules": List[ClientUpdateDevicePoolResponsedevicePoolrulesTypeDef],
        "maxDevices": int,
    },
    total=False,
)

ClientUpdateDevicePoolResponseTypeDef = TypedDict(
    "ClientUpdateDevicePoolResponseTypeDef",
    {"devicePool": ClientUpdateDevicePoolResponsedevicePoolTypeDef},
    total=False,
)

ClientUpdateDevicePoolRulesTypeDef = TypedDict(
    "ClientUpdateDevicePoolRulesTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "value": str,
    },
    total=False,
)

ClientUpdateInstanceProfileResponseinstanceProfileTypeDef = TypedDict(
    "ClientUpdateInstanceProfileResponseinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

ClientUpdateInstanceProfileResponseTypeDef = TypedDict(
    "ClientUpdateInstanceProfileResponseTypeDef",
    {"instanceProfile": ClientUpdateInstanceProfileResponseinstanceProfileTypeDef},
    total=False,
)

ClientUpdateNetworkProfileResponsenetworkProfileTypeDef = TypedDict(
    "ClientUpdateNetworkProfileResponsenetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)

ClientUpdateNetworkProfileResponseTypeDef = TypedDict(
    "ClientUpdateNetworkProfileResponseTypeDef",
    {"networkProfile": ClientUpdateNetworkProfileResponsenetworkProfileTypeDef},
    total=False,
)

ClientUpdateProjectResponseprojectTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectTypeDef",
    {"arn": str, "name": str, "defaultJobTimeoutMinutes": int, "created": datetime},
    total=False,
)

ClientUpdateProjectResponseTypeDef = TypedDict(
    "ClientUpdateProjectResponseTypeDef",
    {"project": ClientUpdateProjectResponseprojectTypeDef},
    total=False,
)

ClientUpdateTestGridProjectResponsetestGridProjectTypeDef = TypedDict(
    "ClientUpdateTestGridProjectResponsetestGridProjectTypeDef",
    {"arn": str, "name": str, "description": str, "created": datetime},
    total=False,
)

ClientUpdateTestGridProjectResponseTypeDef = TypedDict(
    "ClientUpdateTestGridProjectResponseTypeDef",
    {"testGridProject": ClientUpdateTestGridProjectResponsetestGridProjectTypeDef},
    total=False,
)

ClientUpdateUploadResponseuploadTypeDef = TypedDict(
    "ClientUpdateUploadResponseuploadTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ],
        "status": Literal["INITIALIZED", "PROCESSING", "SUCCEEDED", "FAILED"],
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": Literal["CURATED", "PRIVATE"],
    },
    total=False,
)

ClientUpdateUploadResponseTypeDef = TypedDict(
    "ClientUpdateUploadResponseTypeDef",
    {"upload": ClientUpdateUploadResponseuploadTypeDef},
    total=False,
)

ClientUpdateVpceConfigurationResponsevpceConfigurationTypeDef = TypedDict(
    "ClientUpdateVpceConfigurationResponsevpceConfigurationTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)

ClientUpdateVpceConfigurationResponseTypeDef = TypedDict(
    "ClientUpdateVpceConfigurationResponseTypeDef",
    {"vpceConfiguration": ClientUpdateVpceConfigurationResponsevpceConfigurationTypeDef},
    total=False,
)

DeviceFilterTypeDef = TypedDict(
    "DeviceFilterTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)

MonetaryAmountTypeDef = TypedDict(
    "MonetaryAmountTypeDef", {"amount": float, "currencyCode": Literal["USD"]}, total=False
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {"cost": MonetaryAmountTypeDef, "frequency": Literal["MONTHLY"]},
    total=False,
)

OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": Literal["RECURRING"],
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[RecurringChargeTypeDef],
    },
    total=False,
)

OfferingStatusTypeDef = TypedDict(
    "OfferingStatusTypeDef",
    {
        "type": Literal["PURCHASE", "RENEW", "SYSTEM"],
        "offering": OfferingTypeDef,
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)

GetOfferingStatusResultTypeDef = TypedDict(
    "GetOfferingStatusResultTypeDef",
    {
        "current": Dict[str, OfferingStatusTypeDef],
        "nextPeriod": Dict[str, OfferingStatusTypeDef],
        "nextToken": str,
    },
    total=False,
)

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "UNKNOWN",
            "SCREENSHOT",
            "DEVICE_LOG",
            "MESSAGE_LOG",
            "VIDEO_LOG",
            "RESULT_LOG",
            "SERVICE_LOG",
            "WEBKIT_LOG",
            "INSTRUMENTATION_OUTPUT",
            "EXERCISER_MONKEY_OUTPUT",
            "CALABASH_JSON_OUTPUT",
            "CALABASH_PRETTY_OUTPUT",
            "CALABASH_STANDARD_OUTPUT",
            "CALABASH_JAVA_XML_OUTPUT",
            "AUTOMATION_OUTPUT",
            "APPIUM_SERVER_OUTPUT",
            "APPIUM_JAVA_OUTPUT",
            "APPIUM_JAVA_XML_OUTPUT",
            "APPIUM_PYTHON_OUTPUT",
            "APPIUM_PYTHON_XML_OUTPUT",
            "EXPLORER_EVENT_LOG",
            "EXPLORER_SUMMARY_LOG",
            "APPLICATION_CRASH_REPORT",
            "XCTEST_LOG",
            "VIDEO",
            "CUSTOMER_ARTIFACT",
            "CUSTOMER_ARTIFACT_LOG",
            "TESTSPEC_OUTPUT",
        ],
        "extension": str,
        "url": str,
    },
    total=False,
)

ListArtifactsResultTypeDef = TypedDict(
    "ListArtifactsResultTypeDef",
    {"artifacts": List[ArtifactTypeDef], "nextToken": str},
    total=False,
)

InstanceProfileTypeDef = TypedDict(
    "InstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

DeviceInstanceTypeDef = TypedDict(
    "DeviceInstanceTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": InstanceProfileTypeDef,
    },
    total=False,
)

ListDeviceInstancesResultTypeDef = TypedDict(
    "ListDeviceInstancesResultTypeDef",
    {"deviceInstances": List[DeviceInstanceTypeDef], "nextToken": str},
    total=False,
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "value": str,
    },
    total=False,
)

DevicePoolTypeDef = TypedDict(
    "DevicePoolTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "rules": List[RuleTypeDef],
        "maxDevices": int,
    },
    total=False,
)

ListDevicePoolsResultTypeDef = TypedDict(
    "ListDevicePoolsResultTypeDef",
    {"devicePools": List[DevicePoolTypeDef], "nextToken": str},
    total=False,
)

CPUTypeDef = TypedDict(
    "CPUTypeDef", {"frequency": str, "architecture": str, "clock": float}, total=False
)

ResolutionTypeDef = TypedDict("ResolutionTypeDef", {"width": int, "height": int}, total=False)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": CPUTypeDef,
        "resolution": ResolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[DeviceInstanceTypeDef],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)

ListDevicesResultTypeDef = TypedDict(
    "ListDevicesResultTypeDef", {"devices": List[DeviceTypeDef], "nextToken": str}, total=False
)

ListInstanceProfilesResultTypeDef = TypedDict(
    "ListInstanceProfilesResultTypeDef",
    {"instanceProfiles": List[InstanceProfileTypeDef], "nextToken": str},
    total=False,
)

CountersTypeDef = TypedDict(
    "CountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

DeviceMinutesTypeDef = TypedDict(
    "DeviceMinutesTypeDef", {"total": float, "metered": float, "unmetered": float}, total=False
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": CountersTypeDef,
        "message": str,
        "device": DeviceTypeDef,
        "instanceArn": str,
        "deviceMinutes": DeviceMinutesTypeDef,
        "videoEndpoint": str,
        "videoCapture": bool,
    },
    total=False,
)

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef", {"jobs": List[JobTypeDef], "nextToken": str}, total=False
)

NetworkProfileTypeDef = TypedDict(
    "NetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)

ListNetworkProfilesResultTypeDef = TypedDict(
    "ListNetworkProfilesResultTypeDef",
    {"networkProfiles": List[NetworkProfileTypeDef], "nextToken": str},
    total=False,
)

OfferingPromotionTypeDef = TypedDict(
    "OfferingPromotionTypeDef", {"id": str, "description": str}, total=False
)

ListOfferingPromotionsResultTypeDef = TypedDict(
    "ListOfferingPromotionsResultTypeDef",
    {"offeringPromotions": List[OfferingPromotionTypeDef], "nextToken": str},
    total=False,
)

OfferingTransactionTypeDef = TypedDict(
    "OfferingTransactionTypeDef",
    {
        "offeringStatus": OfferingStatusTypeDef,
        "transactionId": str,
        "offeringPromotionId": str,
        "createdOn": datetime,
        "cost": MonetaryAmountTypeDef,
    },
    total=False,
)

ListOfferingTransactionsResultTypeDef = TypedDict(
    "ListOfferingTransactionsResultTypeDef",
    {"offeringTransactions": List[OfferingTransactionTypeDef], "nextToken": str},
    total=False,
)

ListOfferingsResultTypeDef = TypedDict(
    "ListOfferingsResultTypeDef",
    {"offerings": List[OfferingTypeDef], "nextToken": str},
    total=False,
)

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {"arn": str, "name": str, "defaultJobTimeoutMinutes": int, "created": datetime},
    total=False,
)

ListProjectsResultTypeDef = TypedDict(
    "ListProjectsResultTypeDef", {"projects": List[ProjectTypeDef], "nextToken": str}, total=False
)

RemoteAccessSessionTypeDef = TypedDict(
    "RemoteAccessSessionTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
        "started": datetime,
        "stopped": datetime,
        "device": DeviceTypeDef,
        "instanceArn": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "hostAddress": str,
        "clientId": str,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": DeviceMinutesTypeDef,
        "endpoint": str,
        "deviceUdid": str,
        "interactionMode": Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"],
        "skipAppResign": bool,
    },
    total=False,
)

ListRemoteAccessSessionsResultTypeDef = TypedDict(
    "ListRemoteAccessSessionsResultTypeDef",
    {"remoteAccessSessions": List[RemoteAccessSessionTypeDef], "nextToken": str},
    total=False,
)

CustomerArtifactPathsTypeDef = TypedDict(
    "CustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)

DeviceSelectionResultTypeDef = TypedDict(
    "DeviceSelectionResultTypeDef",
    {"filters": List[DeviceFilterTypeDef], "matchedDevicesCount": int, "maxDevices": int},
    total=False,
)

LocationTypeDef = TypedDict("LocationTypeDef", {"latitude": float, "longitude": float})

RadiosTypeDef = TypedDict(
    "RadiosTypeDef", {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool}, total=False
)

RunTypeDef = TypedDict(
    "RunTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "platform": Literal["ANDROID", "IOS"],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": CountersTypeDef,
        "message": str,
        "totalJobs": int,
        "completedJobs": int,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": DeviceMinutesTypeDef,
        "networkProfile": NetworkProfileTypeDef,
        "parsingResultUrl": str,
        "resultCode": Literal["PARSING_FAILED", "VPC_ENDPOINT_SETUP_FAILED"],
        "seed": int,
        "appUpload": str,
        "eventCount": int,
        "jobTimeoutMinutes": int,
        "devicePoolArn": str,
        "locale": str,
        "radios": RadiosTypeDef,
        "location": LocationTypeDef,
        "customerArtifactPaths": CustomerArtifactPathsTypeDef,
        "webUrl": str,
        "skipAppResign": bool,
        "testSpecArn": str,
        "deviceSelectionResult": DeviceSelectionResultTypeDef,
    },
    total=False,
)

ListRunsResultTypeDef = TypedDict(
    "ListRunsResultTypeDef", {"runs": List[RunTypeDef], "nextToken": str}, total=False
)

SampleTypeDef = TypedDict(
    "SampleTypeDef",
    {
        "arn": str,
        "type": Literal[
            "CPU",
            "MEMORY",
            "THREADS",
            "RX_RATE",
            "TX_RATE",
            "RX",
            "TX",
            "NATIVE_FRAMES",
            "NATIVE_FPS",
            "NATIVE_MIN_DRAWTIME",
            "NATIVE_AVG_DRAWTIME",
            "NATIVE_MAX_DRAWTIME",
            "OPENGL_FRAMES",
            "OPENGL_FPS",
            "OPENGL_MIN_DRAWTIME",
            "OPENGL_AVG_DRAWTIME",
            "OPENGL_MAX_DRAWTIME",
        ],
        "url": str,
    },
    total=False,
)

ListSamplesResultTypeDef = TypedDict(
    "ListSamplesResultTypeDef", {"samples": List[SampleTypeDef], "nextToken": str}, total=False
)

SuiteTypeDef = TypedDict(
    "SuiteTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": CountersTypeDef,
        "message": str,
        "deviceMinutes": DeviceMinutesTypeDef,
    },
    total=False,
)

ListSuitesResultTypeDef = TypedDict(
    "ListSuitesResultTypeDef", {"suites": List[SuiteTypeDef], "nextToken": str}, total=False
)

TestTypeDef = TypedDict(
    "TestTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": CountersTypeDef,
        "message": str,
        "deviceMinutes": DeviceMinutesTypeDef,
    },
    total=False,
)

ListTestsResultTypeDef = TypedDict(
    "ListTestsResultTypeDef", {"tests": List[TestTypeDef], "nextToken": str}, total=False
)

ProblemDetailTypeDef = TypedDict("ProblemDetailTypeDef", {"arn": str, "name": str}, total=False)

ProblemTypeDef = TypedDict(
    "ProblemTypeDef",
    {
        "run": ProblemDetailTypeDef,
        "job": ProblemDetailTypeDef,
        "suite": ProblemDetailTypeDef,
        "test": ProblemDetailTypeDef,
        "device": DeviceTypeDef,
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
    },
    total=False,
)

UniqueProblemTypeDef = TypedDict(
    "UniqueProblemTypeDef", {"message": str, "problems": List[ProblemTypeDef]}, total=False
)

ListUniqueProblemsResultTypeDef = TypedDict(
    "ListUniqueProblemsResultTypeDef",
    {
        "uniqueProblems": Dict[
            Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
            List[UniqueProblemTypeDef],
        ],
        "nextToken": str,
    },
    total=False,
)

UploadTypeDef = TypedDict(
    "UploadTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ],
        "status": Literal["INITIALIZED", "PROCESSING", "SUCCEEDED", "FAILED"],
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": Literal["CURATED", "PRIVATE"],
    },
    total=False,
)

ListUploadsResultTypeDef = TypedDict(
    "ListUploadsResultTypeDef", {"uploads": List[UploadTypeDef], "nextToken": str}, total=False
)

VPCEConfigurationTypeDef = TypedDict(
    "VPCEConfigurationTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)

ListVPCEConfigurationsResultTypeDef = TypedDict(
    "ListVPCEConfigurationsResultTypeDef",
    {"vpceConfigurations": List[VPCEConfigurationTypeDef], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
