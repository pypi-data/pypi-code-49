"""
Main interface for devicefarm service client

Usage::

    import boto3
    from mypy_boto3.devicefarm import DeviceFarmClient

    session = boto3.Session()

    client: DeviceFarmClient = boto3.client("devicefarm")
    session_client: DeviceFarmClient = session.client("devicefarm")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_devicefarm.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_devicefarm.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_devicefarm.type_defs import (
    ClientCreateDevicePoolResponseTypeDef,
    ClientCreateDevicePoolRulesTypeDef,
    ClientCreateInstanceProfileResponseTypeDef,
    ClientCreateNetworkProfileResponseTypeDef,
    ClientCreateProjectResponseTypeDef,
    ClientCreateRemoteAccessSessionConfigurationTypeDef,
    ClientCreateRemoteAccessSessionResponseTypeDef,
    ClientCreateTestGridProjectResponseTypeDef,
    ClientCreateTestGridUrlResponseTypeDef,
    ClientCreateUploadResponseTypeDef,
    ClientCreateVpceConfigurationResponseTypeDef,
    ClientGetAccountSettingsResponseTypeDef,
    ClientGetDeviceInstanceResponseTypeDef,
    ClientGetDevicePoolCompatibilityConfigurationTypeDef,
    ClientGetDevicePoolCompatibilityResponseTypeDef,
    ClientGetDevicePoolCompatibilityTestTypeDef,
    ClientGetDevicePoolResponseTypeDef,
    ClientGetDeviceResponseTypeDef,
    ClientGetInstanceProfileResponseTypeDef,
    ClientGetJobResponseTypeDef,
    ClientGetNetworkProfileResponseTypeDef,
    ClientGetOfferingStatusResponseTypeDef,
    ClientGetProjectResponseTypeDef,
    ClientGetRemoteAccessSessionResponseTypeDef,
    ClientGetRunResponseTypeDef,
    ClientGetSuiteResponseTypeDef,
    ClientGetTestGridProjectResponseTypeDef,
    ClientGetTestGridSessionResponseTypeDef,
    ClientGetTestResponseTypeDef,
    ClientGetUploadResponseTypeDef,
    ClientGetVpceConfigurationResponseTypeDef,
    ClientInstallToRemoteAccessSessionResponseTypeDef,
    ClientListArtifactsResponseTypeDef,
    ClientListDeviceInstancesResponseTypeDef,
    ClientListDevicePoolsResponseTypeDef,
    ClientListDevicesFiltersTypeDef,
    ClientListDevicesResponseTypeDef,
    ClientListInstanceProfilesResponseTypeDef,
    ClientListJobsResponseTypeDef,
    ClientListNetworkProfilesResponseTypeDef,
    ClientListOfferingPromotionsResponseTypeDef,
    ClientListOfferingTransactionsResponseTypeDef,
    ClientListOfferingsResponseTypeDef,
    ClientListProjectsResponseTypeDef,
    ClientListRemoteAccessSessionsResponseTypeDef,
    ClientListRunsResponseTypeDef,
    ClientListSamplesResponseTypeDef,
    ClientListSuitesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTestGridProjectsResponseTypeDef,
    ClientListTestGridSessionActionsResponseTypeDef,
    ClientListTestGridSessionArtifactsResponseTypeDef,
    ClientListTestGridSessionsResponseTypeDef,
    ClientListTestsResponseTypeDef,
    ClientListUniqueProblemsResponseTypeDef,
    ClientListUploadsResponseTypeDef,
    ClientListVpceConfigurationsResponseTypeDef,
    ClientPurchaseOfferingResponseTypeDef,
    ClientRenewOfferingResponseTypeDef,
    ClientScheduleRunConfigurationTypeDef,
    ClientScheduleRunDeviceSelectionConfigurationTypeDef,
    ClientScheduleRunExecutionConfigurationTypeDef,
    ClientScheduleRunResponseTypeDef,
    ClientScheduleRunTestTypeDef,
    ClientStopJobResponseTypeDef,
    ClientStopRemoteAccessSessionResponseTypeDef,
    ClientStopRunResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateDeviceInstanceResponseTypeDef,
    ClientUpdateDevicePoolResponseTypeDef,
    ClientUpdateDevicePoolRulesTypeDef,
    ClientUpdateInstanceProfileResponseTypeDef,
    ClientUpdateNetworkProfileResponseTypeDef,
    ClientUpdateProjectResponseTypeDef,
    ClientUpdateTestGridProjectResponseTypeDef,
    ClientUpdateUploadResponseTypeDef,
    ClientUpdateVpceConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DeviceFarmClient",)


class DeviceFarmClient:
    """
    [DeviceFarm.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.can_paginate)
        """

    def create_device_pool(
        self,
        projectArn: str,
        name: str,
        rules: List[ClientCreateDevicePoolRulesTypeDef],
        description: str = None,
        maxDevices: int = None,
    ) -> ClientCreateDevicePoolResponseTypeDef:
        """
        [Client.create_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.create_device_pool)
        """

    def create_instance_profile(
        self,
        name: str,
        description: str = None,
        packageCleanup: bool = None,
        excludeAppPackagesFromCleanup: List[str] = None,
        rebootAfterUse: bool = None,
    ) -> ClientCreateInstanceProfileResponseTypeDef:
        """
        [Client.create_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.create_instance_profile)
        """

    def create_network_profile(
        self,
        projectArn: str,
        name: str,
        description: str = None,
        type: Literal["CURATED", "PRIVATE"] = None,
        uplinkBandwidthBits: int = None,
        downlinkBandwidthBits: int = None,
        uplinkDelayMs: int = None,
        downlinkDelayMs: int = None,
        uplinkJitterMs: int = None,
        downlinkJitterMs: int = None,
        uplinkLossPercent: int = None,
        downlinkLossPercent: int = None,
    ) -> ClientCreateNetworkProfileResponseTypeDef:
        """
        [Client.create_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.create_network_profile)
        """

    def create_project(
        self, name: str, defaultJobTimeoutMinutes: int = None
    ) -> ClientCreateProjectResponseTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.create_project)
        """

    def create_remote_access_session(
        self,
        projectArn: str,
        deviceArn: str,
        instanceArn: str = None,
        sshPublicKey: str = None,
        remoteDebugEnabled: bool = None,
        remoteRecordEnabled: bool = None,
        remoteRecordAppArn: str = None,
        name: str = None,
        clientId: str = None,
        configuration: ClientCreateRemoteAccessSessionConfigurationTypeDef = None,
        interactionMode: Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"] = None,
        skipAppResign: bool = None,
    ) -> ClientCreateRemoteAccessSessionResponseTypeDef:
        """
        [Client.create_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.create_remote_access_session)
        """

    def create_test_grid_project(
        self, name: str, description: str = None
    ) -> ClientCreateTestGridProjectResponseTypeDef:
        """
        [Client.create_test_grid_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.create_test_grid_project)
        """

    def create_test_grid_url(
        self, projectArn: str, expiresInSeconds: int
    ) -> ClientCreateTestGridUrlResponseTypeDef:
        """
        [Client.create_test_grid_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.create_test_grid_url)
        """

    def create_upload(
        self,
        projectArn: str,
        name: str,
        type: Literal[
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
        contentType: str = None,
    ) -> ClientCreateUploadResponseTypeDef:
        """
        [Client.create_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.create_upload)
        """

    def create_vpce_configuration(
        self,
        vpceConfigurationName: str,
        vpceServiceName: str,
        serviceDnsName: str,
        vpceConfigurationDescription: str = None,
    ) -> ClientCreateVpceConfigurationResponseTypeDef:
        """
        [Client.create_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.create_vpce_configuration)
        """

    def delete_device_pool(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.delete_device_pool)
        """

    def delete_instance_profile(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.delete_instance_profile)
        """

    def delete_network_profile(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.delete_network_profile)
        """

    def delete_project(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.delete_project)
        """

    def delete_remote_access_session(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.delete_remote_access_session)
        """

    def delete_run(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.delete_run)
        """

    def delete_test_grid_project(self, projectArn: str) -> Dict[str, Any]:
        """
        [Client.delete_test_grid_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.delete_test_grid_project)
        """

    def delete_upload(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.delete_upload)
        """

    def delete_vpce_configuration(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.delete_vpce_configuration)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.generate_presigned_url)
        """

    def get_account_settings(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetAccountSettingsResponseTypeDef:
        """
        [Client.get_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_account_settings)
        """

    def get_device(self, arn: str) -> ClientGetDeviceResponseTypeDef:
        """
        [Client.get_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_device)
        """

    def get_device_instance(self, arn: str) -> ClientGetDeviceInstanceResponseTypeDef:
        """
        [Client.get_device_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_device_instance)
        """

    def get_device_pool(self, arn: str) -> ClientGetDevicePoolResponseTypeDef:
        """
        [Client.get_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_device_pool)
        """

    def get_device_pool_compatibility(
        self,
        devicePoolArn: str,
        appArn: str = None,
        testType: Literal[
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
        ] = None,
        test: ClientGetDevicePoolCompatibilityTestTypeDef = None,
        configuration: ClientGetDevicePoolCompatibilityConfigurationTypeDef = None,
    ) -> ClientGetDevicePoolCompatibilityResponseTypeDef:
        """
        [Client.get_device_pool_compatibility documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_device_pool_compatibility)
        """

    def get_instance_profile(self, arn: str) -> ClientGetInstanceProfileResponseTypeDef:
        """
        [Client.get_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_instance_profile)
        """

    def get_job(self, arn: str) -> ClientGetJobResponseTypeDef:
        """
        [Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_job)
        """

    def get_network_profile(self, arn: str) -> ClientGetNetworkProfileResponseTypeDef:
        """
        [Client.get_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_network_profile)
        """

    def get_offering_status(self, nextToken: str = None) -> ClientGetOfferingStatusResponseTypeDef:
        """
        [Client.get_offering_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_offering_status)
        """

    def get_project(self, arn: str) -> ClientGetProjectResponseTypeDef:
        """
        [Client.get_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_project)
        """

    def get_remote_access_session(self, arn: str) -> ClientGetRemoteAccessSessionResponseTypeDef:
        """
        [Client.get_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_remote_access_session)
        """

    def get_run(self, arn: str) -> ClientGetRunResponseTypeDef:
        """
        [Client.get_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_run)
        """

    def get_suite(self, arn: str) -> ClientGetSuiteResponseTypeDef:
        """
        [Client.get_suite documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_suite)
        """

    def get_test(self, arn: str) -> ClientGetTestResponseTypeDef:
        """
        [Client.get_test documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_test)
        """

    def get_test_grid_project(self, projectArn: str) -> ClientGetTestGridProjectResponseTypeDef:
        """
        [Client.get_test_grid_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_test_grid_project)
        """

    def get_test_grid_session(
        self, projectArn: str = None, sessionId: str = None, sessionArn: str = None
    ) -> ClientGetTestGridSessionResponseTypeDef:
        """
        [Client.get_test_grid_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_test_grid_session)
        """

    def get_upload(self, arn: str) -> ClientGetUploadResponseTypeDef:
        """
        [Client.get_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_upload)
        """

    def get_vpce_configuration(self, arn: str) -> ClientGetVpceConfigurationResponseTypeDef:
        """
        [Client.get_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.get_vpce_configuration)
        """

    def install_to_remote_access_session(
        self, remoteAccessSessionArn: str, appArn: str
    ) -> ClientInstallToRemoteAccessSessionResponseTypeDef:
        """
        [Client.install_to_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.install_to_remote_access_session)
        """

    def list_artifacts(
        self, arn: str, type: Literal["SCREENSHOT", "FILE", "LOG"], nextToken: str = None
    ) -> ClientListArtifactsResponseTypeDef:
        """
        [Client.list_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_artifacts)
        """

    def list_device_instances(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListDeviceInstancesResponseTypeDef:
        """
        [Client.list_device_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_device_instances)
        """

    def list_device_pools(
        self, arn: str, type: Literal["CURATED", "PRIVATE"] = None, nextToken: str = None
    ) -> ClientListDevicePoolsResponseTypeDef:
        """
        [Client.list_device_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_device_pools)
        """

    def list_devices(
        self,
        arn: str = None,
        nextToken: str = None,
        filters: List[ClientListDevicesFiltersTypeDef] = None,
    ) -> ClientListDevicesResponseTypeDef:
        """
        [Client.list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_devices)
        """

    def list_instance_profiles(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListInstanceProfilesResponseTypeDef:
        """
        [Client.list_instance_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_instance_profiles)
        """

    def list_jobs(self, arn: str, nextToken: str = None) -> ClientListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_jobs)
        """

    def list_network_profiles(
        self, arn: str, type: Literal["CURATED", "PRIVATE"] = None, nextToken: str = None
    ) -> ClientListNetworkProfilesResponseTypeDef:
        """
        [Client.list_network_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_network_profiles)
        """

    def list_offering_promotions(
        self, nextToken: str = None
    ) -> ClientListOfferingPromotionsResponseTypeDef:
        """
        [Client.list_offering_promotions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_offering_promotions)
        """

    def list_offering_transactions(
        self, nextToken: str = None
    ) -> ClientListOfferingTransactionsResponseTypeDef:
        """
        [Client.list_offering_transactions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_offering_transactions)
        """

    def list_offerings(self, nextToken: str = None) -> ClientListOfferingsResponseTypeDef:
        """
        [Client.list_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_offerings)
        """

    def list_projects(
        self, arn: str = None, nextToken: str = None
    ) -> ClientListProjectsResponseTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_projects)
        """

    def list_remote_access_sessions(
        self, arn: str, nextToken: str = None
    ) -> ClientListRemoteAccessSessionsResponseTypeDef:
        """
        [Client.list_remote_access_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_remote_access_sessions)
        """

    def list_runs(self, arn: str, nextToken: str = None) -> ClientListRunsResponseTypeDef:
        """
        [Client.list_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_runs)
        """

    def list_samples(self, arn: str, nextToken: str = None) -> ClientListSamplesResponseTypeDef:
        """
        [Client.list_samples documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_samples)
        """

    def list_suites(self, arn: str, nextToken: str = None) -> ClientListSuitesResponseTypeDef:
        """
        [Client.list_suites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_suites)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_tags_for_resource)
        """

    def list_test_grid_projects(
        self, maxResult: int = None, nextToken: str = None
    ) -> ClientListTestGridProjectsResponseTypeDef:
        """
        [Client.list_test_grid_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_projects)
        """

    def list_test_grid_session_actions(
        self, sessionArn: str, maxResult: int = None, nextToken: str = None
    ) -> ClientListTestGridSessionActionsResponseTypeDef:
        """
        [Client.list_test_grid_session_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_session_actions)
        """

    def list_test_grid_session_artifacts(
        self,
        sessionArn: str,
        type: Literal["VIDEO", "LOG"] = None,
        maxResult: int = None,
        nextToken: str = None,
    ) -> ClientListTestGridSessionArtifactsResponseTypeDef:
        """
        [Client.list_test_grid_session_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_session_artifacts)
        """

    def list_test_grid_sessions(
        self,
        projectArn: str,
        status: Literal["ACTIVE", "CLOSED", "ERRORED"] = None,
        creationTimeAfter: datetime = None,
        creationTimeBefore: datetime = None,
        endTimeAfter: datetime = None,
        endTimeBefore: datetime = None,
        maxResult: int = None,
        nextToken: str = None,
    ) -> ClientListTestGridSessionsResponseTypeDef:
        """
        [Client.list_test_grid_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_sessions)
        """

    def list_tests(self, arn: str, nextToken: str = None) -> ClientListTestsResponseTypeDef:
        """
        [Client.list_tests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_tests)
        """

    def list_unique_problems(
        self, arn: str, nextToken: str = None
    ) -> ClientListUniqueProblemsResponseTypeDef:
        """
        [Client.list_unique_problems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_unique_problems)
        """

    def list_uploads(
        self,
        arn: str,
        type: Literal[
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
        ] = None,
        nextToken: str = None,
    ) -> ClientListUploadsResponseTypeDef:
        """
        [Client.list_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_uploads)
        """

    def list_vpce_configurations(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListVpceConfigurationsResponseTypeDef:
        """
        [Client.list_vpce_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.list_vpce_configurations)
        """

    def purchase_offering(
        self, offeringId: str = None, quantity: int = None, offeringPromotionId: str = None
    ) -> ClientPurchaseOfferingResponseTypeDef:
        """
        [Client.purchase_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.purchase_offering)
        """

    def renew_offering(
        self, offeringId: str = None, quantity: int = None
    ) -> ClientRenewOfferingResponseTypeDef:
        """
        [Client.renew_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.renew_offering)
        """

    def schedule_run(
        self,
        projectArn: str,
        test: ClientScheduleRunTestTypeDef,
        appArn: str = None,
        devicePoolArn: str = None,
        deviceSelectionConfiguration: ClientScheduleRunDeviceSelectionConfigurationTypeDef = None,
        name: str = None,
        configuration: ClientScheduleRunConfigurationTypeDef = None,
        executionConfiguration: ClientScheduleRunExecutionConfigurationTypeDef = None,
    ) -> ClientScheduleRunResponseTypeDef:
        """
        [Client.schedule_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.schedule_run)
        """

    def stop_job(self, arn: str) -> ClientStopJobResponseTypeDef:
        """
        [Client.stop_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.stop_job)
        """

    def stop_remote_access_session(self, arn: str) -> ClientStopRemoteAccessSessionResponseTypeDef:
        """
        [Client.stop_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.stop_remote_access_session)
        """

    def stop_run(self, arn: str) -> ClientStopRunResponseTypeDef:
        """
        [Client.stop_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.stop_run)
        """

    def tag_resource(
        self, ResourceARN: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.untag_resource)
        """

    def update_device_instance(
        self, arn: str, profileArn: str = None, labels: List[str] = None
    ) -> ClientUpdateDeviceInstanceResponseTypeDef:
        """
        [Client.update_device_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.update_device_instance)
        """

    def update_device_pool(
        self,
        arn: str,
        name: str = None,
        description: str = None,
        rules: List[ClientUpdateDevicePoolRulesTypeDef] = None,
        maxDevices: int = None,
        clearMaxDevices: bool = None,
    ) -> ClientUpdateDevicePoolResponseTypeDef:
        """
        [Client.update_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.update_device_pool)
        """

    def update_instance_profile(
        self,
        arn: str,
        name: str = None,
        description: str = None,
        packageCleanup: bool = None,
        excludeAppPackagesFromCleanup: List[str] = None,
        rebootAfterUse: bool = None,
    ) -> ClientUpdateInstanceProfileResponseTypeDef:
        """
        [Client.update_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.update_instance_profile)
        """

    def update_network_profile(
        self,
        arn: str,
        name: str = None,
        description: str = None,
        type: Literal["CURATED", "PRIVATE"] = None,
        uplinkBandwidthBits: int = None,
        downlinkBandwidthBits: int = None,
        uplinkDelayMs: int = None,
        downlinkDelayMs: int = None,
        uplinkJitterMs: int = None,
        downlinkJitterMs: int = None,
        uplinkLossPercent: int = None,
        downlinkLossPercent: int = None,
    ) -> ClientUpdateNetworkProfileResponseTypeDef:
        """
        [Client.update_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.update_network_profile)
        """

    def update_project(
        self, arn: str, name: str = None, defaultJobTimeoutMinutes: int = None
    ) -> ClientUpdateProjectResponseTypeDef:
        """
        [Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.update_project)
        """

    def update_test_grid_project(
        self, projectArn: str, name: str = None, description: str = None
    ) -> ClientUpdateTestGridProjectResponseTypeDef:
        """
        [Client.update_test_grid_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.update_test_grid_project)
        """

    def update_upload(
        self, arn: str, name: str = None, contentType: str = None, editContent: bool = None
    ) -> ClientUpdateUploadResponseTypeDef:
        """
        [Client.update_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.update_upload)
        """

    def update_vpce_configuration(
        self,
        arn: str,
        vpceConfigurationName: str = None,
        vpceServiceName: str = None,
        serviceDnsName: str = None,
        vpceConfigurationDescription: str = None,
    ) -> ClientUpdateVpceConfigurationResponseTypeDef:
        """
        [Client.update_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Client.update_vpce_configuration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_offering_status"]
    ) -> "paginator_scope.GetOfferingStatusPaginator":
        """
        [Paginator.GetOfferingStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.GetOfferingStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_artifacts"]
    ) -> "paginator_scope.ListArtifactsPaginator":
        """
        [Paginator.ListArtifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListArtifacts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_instances"]
    ) -> "paginator_scope.ListDeviceInstancesPaginator":
        """
        [Paginator.ListDeviceInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDeviceInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_pools"]
    ) -> "paginator_scope.ListDevicePoolsPaginator":
        """
        [Paginator.ListDevicePools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevicePools)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_devices"]
    ) -> "paginator_scope.ListDevicesPaginator":
        """
        [Paginator.ListDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_profiles"]
    ) -> "paginator_scope.ListInstanceProfilesPaginator":
        """
        [Paginator.ListInstanceProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListInstanceProfiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> "paginator_scope.ListJobsPaginator":
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_network_profiles"]
    ) -> "paginator_scope.ListNetworkProfilesPaginator":
        """
        [Paginator.ListNetworkProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListNetworkProfiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_offering_promotions"]
    ) -> "paginator_scope.ListOfferingPromotionsPaginator":
        """
        [Paginator.ListOfferingPromotions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingPromotions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_offering_transactions"]
    ) -> "paginator_scope.ListOfferingTransactionsPaginator":
        """
        [Paginator.ListOfferingTransactions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingTransactions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_offerings"]
    ) -> "paginator_scope.ListOfferingsPaginator":
        """
        [Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_projects"]
    ) -> "paginator_scope.ListProjectsPaginator":
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListProjects)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_remote_access_sessions"]
    ) -> "paginator_scope.ListRemoteAccessSessionsPaginator":
        """
        [Paginator.ListRemoteAccessSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRemoteAccessSessions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_runs"]
    ) -> "paginator_scope.ListRunsPaginator":
        """
        [Paginator.ListRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRuns)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_samples"]
    ) -> "paginator_scope.ListSamplesPaginator":
        """
        [Paginator.ListSamples documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSamples)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_suites"]
    ) -> "paginator_scope.ListSuitesPaginator":
        """
        [Paginator.ListSuites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSuites)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tests"]
    ) -> "paginator_scope.ListTestsPaginator":
        """
        [Paginator.ListTests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListTests)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_unique_problems"]
    ) -> "paginator_scope.ListUniqueProblemsPaginator":
        """
        [Paginator.ListUniqueProblems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUniqueProblems)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_uploads"]
    ) -> "paginator_scope.ListUploadsPaginator":
        """
        [Paginator.ListUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUploads)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_vpce_configurations"]
    ) -> "paginator_scope.ListVPCEConfigurationsPaginator":
        """
        [Paginator.ListVPCEConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/devicefarm.html#DeviceFarm.Paginator.ListVPCEConfigurations)
        """


class Exceptions:
    ArgumentException: Boto3ClientError
    CannotDeleteException: Boto3ClientError
    ClientError: Boto3ClientError
    IdempotencyException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidOperationException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotEligibleException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceAccountException: Boto3ClientError
    TagOperationException: Boto3ClientError
    TagPolicyException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
