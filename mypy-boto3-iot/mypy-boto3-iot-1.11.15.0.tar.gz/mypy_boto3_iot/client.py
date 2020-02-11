"""
Main interface for iot service client

Usage::

    import boto3
    from mypy_boto3.iot import IoTClient

    session = boto3.Session()

    client: IoTClient = boto3.client("iot")
    session_client: IoTClient = session.client("iot")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_iot.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_iot.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_iot.type_defs import (
    ClientAssociateTargetsWithJobResponseTypeDef,
    ClientCancelJobResponseTypeDef,
    ClientCreateAuthorizerResponseTypeDef,
    ClientCreateBillingGroupBillingGroupPropertiesTypeDef,
    ClientCreateBillingGroupResponseTypeDef,
    ClientCreateBillingGroupTagsTypeDef,
    ClientCreateCertificateFromCsrResponseTypeDef,
    ClientCreateDomainConfigurationAuthorizerConfigTypeDef,
    ClientCreateDomainConfigurationResponseTypeDef,
    ClientCreateDynamicThingGroupResponseTypeDef,
    ClientCreateDynamicThingGroupTagsTypeDef,
    ClientCreateDynamicThingGroupThingGroupPropertiesTypeDef,
    ClientCreateJobAbortConfigTypeDef,
    ClientCreateJobJobExecutionsRolloutConfigTypeDef,
    ClientCreateJobPresignedUrlConfigTypeDef,
    ClientCreateJobResponseTypeDef,
    ClientCreateJobTagsTypeDef,
    ClientCreateJobTimeoutConfigTypeDef,
    ClientCreateKeysAndCertificateResponseTypeDef,
    ClientCreateMitigationActionActionParamsTypeDef,
    ClientCreateMitigationActionResponseTypeDef,
    ClientCreateMitigationActionTagsTypeDef,
    ClientCreateOtaUpdateAwsJobExecutionsRolloutConfigTypeDef,
    ClientCreateOtaUpdateAwsJobPresignedUrlConfigTypeDef,
    ClientCreateOtaUpdateFilesTypeDef,
    ClientCreateOtaUpdateResponseTypeDef,
    ClientCreateOtaUpdateTagsTypeDef,
    ClientCreatePolicyResponseTypeDef,
    ClientCreatePolicyVersionResponseTypeDef,
    ClientCreateProvisioningClaimResponseTypeDef,
    ClientCreateProvisioningTemplateResponseTypeDef,
    ClientCreateProvisioningTemplateTagsTypeDef,
    ClientCreateProvisioningTemplateVersionResponseTypeDef,
    ClientCreateRoleAliasResponseTypeDef,
    ClientCreateScheduledAuditResponseTypeDef,
    ClientCreateScheduledAuditTagsTypeDef,
    ClientCreateSecurityProfileAlertTargetsTypeDef,
    ClientCreateSecurityProfileBehaviorsTypeDef,
    ClientCreateSecurityProfileResponseTypeDef,
    ClientCreateSecurityProfileTagsTypeDef,
    ClientCreateStreamFilesTypeDef,
    ClientCreateStreamResponseTypeDef,
    ClientCreateStreamTagsTypeDef,
    ClientCreateThingAttributePayloadTypeDef,
    ClientCreateThingGroupResponseTypeDef,
    ClientCreateThingGroupTagsTypeDef,
    ClientCreateThingGroupThingGroupPropertiesTypeDef,
    ClientCreateThingResponseTypeDef,
    ClientCreateThingTypeResponseTypeDef,
    ClientCreateThingTypeTagsTypeDef,
    ClientCreateThingTypeThingTypePropertiesTypeDef,
    ClientCreateTopicRuleDestinationDestinationConfigurationTypeDef,
    ClientCreateTopicRuleDestinationResponseTypeDef,
    ClientCreateTopicRuleTopicRulePayloadTypeDef,
    ClientDescribeAccountAuditConfigurationResponseTypeDef,
    ClientDescribeAuditFindingResponseTypeDef,
    ClientDescribeAuditMitigationActionsTaskResponseTypeDef,
    ClientDescribeAuditTaskResponseTypeDef,
    ClientDescribeAuthorizerResponseTypeDef,
    ClientDescribeBillingGroupResponseTypeDef,
    ClientDescribeCaCertificateResponseTypeDef,
    ClientDescribeCertificateResponseTypeDef,
    ClientDescribeDefaultAuthorizerResponseTypeDef,
    ClientDescribeDomainConfigurationResponseTypeDef,
    ClientDescribeEndpointResponseTypeDef,
    ClientDescribeEventConfigurationsResponseTypeDef,
    ClientDescribeIndexResponseTypeDef,
    ClientDescribeJobExecutionResponseTypeDef,
    ClientDescribeJobResponseTypeDef,
    ClientDescribeMitigationActionResponseTypeDef,
    ClientDescribeProvisioningTemplateResponseTypeDef,
    ClientDescribeProvisioningTemplateVersionResponseTypeDef,
    ClientDescribeRoleAliasResponseTypeDef,
    ClientDescribeScheduledAuditResponseTypeDef,
    ClientDescribeSecurityProfileResponseTypeDef,
    ClientDescribeStreamResponseTypeDef,
    ClientDescribeThingGroupResponseTypeDef,
    ClientDescribeThingRegistrationTaskResponseTypeDef,
    ClientDescribeThingResponseTypeDef,
    ClientDescribeThingTypeResponseTypeDef,
    ClientGetCardinalityResponseTypeDef,
    ClientGetEffectivePoliciesResponseTypeDef,
    ClientGetIndexingConfigurationResponseTypeDef,
    ClientGetJobDocumentResponseTypeDef,
    ClientGetLoggingOptionsResponseTypeDef,
    ClientGetOtaUpdateResponseTypeDef,
    ClientGetPercentilesResponseTypeDef,
    ClientGetPolicyResponseTypeDef,
    ClientGetPolicyVersionResponseTypeDef,
    ClientGetRegistrationCodeResponseTypeDef,
    ClientGetStatisticsResponseTypeDef,
    ClientGetTopicRuleDestinationResponseTypeDef,
    ClientGetTopicRuleResponseTypeDef,
    ClientGetV2LoggingOptionsResponseTypeDef,
    ClientListActiveViolationsResponseTypeDef,
    ClientListAttachedPoliciesResponseTypeDef,
    ClientListAuditFindingsResourceIdentifierTypeDef,
    ClientListAuditFindingsResponseTypeDef,
    ClientListAuditMitigationActionsExecutionsResponseTypeDef,
    ClientListAuditMitigationActionsTasksResponseTypeDef,
    ClientListAuditTasksResponseTypeDef,
    ClientListAuthorizersResponseTypeDef,
    ClientListBillingGroupsResponseTypeDef,
    ClientListCaCertificatesResponseTypeDef,
    ClientListCertificatesByCaResponseTypeDef,
    ClientListCertificatesResponseTypeDef,
    ClientListDomainConfigurationsResponseTypeDef,
    ClientListIndicesResponseTypeDef,
    ClientListJobExecutionsForJobResponseTypeDef,
    ClientListJobExecutionsForThingResponseTypeDef,
    ClientListJobsResponseTypeDef,
    ClientListMitigationActionsResponseTypeDef,
    ClientListOtaUpdatesResponseTypeDef,
    ClientListOutgoingCertificatesResponseTypeDef,
    ClientListPoliciesResponseTypeDef,
    ClientListPolicyPrincipalsResponseTypeDef,
    ClientListPolicyVersionsResponseTypeDef,
    ClientListPrincipalPoliciesResponseTypeDef,
    ClientListPrincipalThingsResponseTypeDef,
    ClientListProvisioningTemplateVersionsResponseTypeDef,
    ClientListProvisioningTemplatesResponseTypeDef,
    ClientListRoleAliasesResponseTypeDef,
    ClientListScheduledAuditsResponseTypeDef,
    ClientListSecurityProfilesForTargetResponseTypeDef,
    ClientListSecurityProfilesResponseTypeDef,
    ClientListStreamsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTargetsForPolicyResponseTypeDef,
    ClientListTargetsForSecurityProfileResponseTypeDef,
    ClientListThingGroupsForThingResponseTypeDef,
    ClientListThingGroupsResponseTypeDef,
    ClientListThingPrincipalsResponseTypeDef,
    ClientListThingRegistrationTaskReportsResponseTypeDef,
    ClientListThingRegistrationTasksResponseTypeDef,
    ClientListThingTypesResponseTypeDef,
    ClientListThingsInBillingGroupResponseTypeDef,
    ClientListThingsInThingGroupResponseTypeDef,
    ClientListThingsResponseTypeDef,
    ClientListTopicRuleDestinationsResponseTypeDef,
    ClientListTopicRulesResponseTypeDef,
    ClientListV2LoggingLevelsResponseTypeDef,
    ClientListViolationEventsResponseTypeDef,
    ClientRegisterCaCertificateRegistrationConfigTypeDef,
    ClientRegisterCaCertificateResponseTypeDef,
    ClientRegisterCertificateResponseTypeDef,
    ClientRegisterThingResponseTypeDef,
    ClientReplaceTopicRuleTopicRulePayloadTypeDef,
    ClientSearchIndexResponseTypeDef,
    ClientSetDefaultAuthorizerResponseTypeDef,
    ClientSetLoggingOptionsLoggingOptionsPayloadTypeDef,
    ClientSetV2LoggingLevelLogTargetTypeDef,
    ClientStartAuditMitigationActionsTaskResponseTypeDef,
    ClientStartAuditMitigationActionsTaskTargetTypeDef,
    ClientStartOnDemandAuditTaskResponseTypeDef,
    ClientStartThingRegistrationTaskResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientTestAuthorizationAuthInfosTypeDef,
    ClientTestAuthorizationResponseTypeDef,
    ClientTestInvokeAuthorizerHttpContextTypeDef,
    ClientTestInvokeAuthorizerMqttContextTypeDef,
    ClientTestInvokeAuthorizerResponseTypeDef,
    ClientTestInvokeAuthorizerTlsContextTypeDef,
    ClientTransferCertificateResponseTypeDef,
    ClientUpdateAccountAuditConfigurationAuditCheckConfigurationsTypeDef,
    ClientUpdateAccountAuditConfigurationAuditNotificationTargetConfigurationsTypeDef,
    ClientUpdateAuthorizerResponseTypeDef,
    ClientUpdateBillingGroupBillingGroupPropertiesTypeDef,
    ClientUpdateBillingGroupResponseTypeDef,
    ClientUpdateCaCertificateRegistrationConfigTypeDef,
    ClientUpdateDomainConfigurationAuthorizerConfigTypeDef,
    ClientUpdateDomainConfigurationResponseTypeDef,
    ClientUpdateDynamicThingGroupResponseTypeDef,
    ClientUpdateDynamicThingGroupThingGroupPropertiesTypeDef,
    ClientUpdateEventConfigurationsEventConfigurationsTypeDef,
    ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef,
    ClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef,
    ClientUpdateJobAbortConfigTypeDef,
    ClientUpdateJobJobExecutionsRolloutConfigTypeDef,
    ClientUpdateJobPresignedUrlConfigTypeDef,
    ClientUpdateJobTimeoutConfigTypeDef,
    ClientUpdateMitigationActionActionParamsTypeDef,
    ClientUpdateMitigationActionResponseTypeDef,
    ClientUpdateRoleAliasResponseTypeDef,
    ClientUpdateScheduledAuditResponseTypeDef,
    ClientUpdateSecurityProfileAlertTargetsTypeDef,
    ClientUpdateSecurityProfileBehaviorsTypeDef,
    ClientUpdateSecurityProfileResponseTypeDef,
    ClientUpdateStreamFilesTypeDef,
    ClientUpdateStreamResponseTypeDef,
    ClientUpdateThingAttributePayloadTypeDef,
    ClientUpdateThingGroupResponseTypeDef,
    ClientUpdateThingGroupThingGroupPropertiesTypeDef,
    ClientValidateSecurityProfileBehaviorsBehaviorsTypeDef,
    ClientValidateSecurityProfileBehaviorsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoTClient",)


class IoTClient:
    """
    [IoT.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client)
    """

    exceptions: "client_scope.Exceptions"

    def accept_certificate_transfer(self, certificateId: str, setAsActive: bool = None) -> None:
        """
        [Client.accept_certificate_transfer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.accept_certificate_transfer)
        """

    def add_thing_to_billing_group(
        self,
        billingGroupName: str = None,
        billingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.add_thing_to_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.add_thing_to_billing_group)
        """

    def add_thing_to_thing_group(
        self,
        thingGroupName: str = None,
        thingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
        overrideDynamicGroups: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.add_thing_to_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.add_thing_to_thing_group)
        """

    def associate_targets_with_job(
        self, targets: List[str], jobId: str, comment: str = None
    ) -> ClientAssociateTargetsWithJobResponseTypeDef:
        """
        [Client.associate_targets_with_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.associate_targets_with_job)
        """

    def attach_policy(self, policyName: str, target: str) -> None:
        """
        [Client.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.attach_policy)
        """

    def attach_principal_policy(self, policyName: str, principal: str) -> None:
        """
        [Client.attach_principal_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.attach_principal_policy)
        """

    def attach_security_profile(
        self, securityProfileName: str, securityProfileTargetArn: str
    ) -> Dict[str, Any]:
        """
        [Client.attach_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.attach_security_profile)
        """

    def attach_thing_principal(self, thingName: str, principal: str) -> Dict[str, Any]:
        """
        [Client.attach_thing_principal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.attach_thing_principal)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.can_paginate)
        """

    def cancel_audit_mitigation_actions_task(self, taskId: str) -> Dict[str, Any]:
        """
        [Client.cancel_audit_mitigation_actions_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.cancel_audit_mitigation_actions_task)
        """

    def cancel_audit_task(self, taskId: str) -> Dict[str, Any]:
        """
        [Client.cancel_audit_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.cancel_audit_task)
        """

    def cancel_certificate_transfer(self, certificateId: str) -> None:
        """
        [Client.cancel_certificate_transfer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.cancel_certificate_transfer)
        """

    def cancel_job(
        self, jobId: str, reasonCode: str = None, comment: str = None, force: bool = None
    ) -> ClientCancelJobResponseTypeDef:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.cancel_job)
        """

    def cancel_job_execution(
        self,
        jobId: str,
        thingName: str,
        force: bool = None,
        expectedVersion: int = None,
        statusDetails: Dict[str, str] = None,
    ) -> None:
        """
        [Client.cancel_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.cancel_job_execution)
        """

    def clear_default_authorizer(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.clear_default_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.clear_default_authorizer)
        """

    def confirm_topic_rule_destination(self, confirmationToken: str) -> Dict[str, Any]:
        """
        [Client.confirm_topic_rule_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.confirm_topic_rule_destination)
        """

    def create_authorizer(
        self,
        authorizerName: str,
        authorizerFunctionArn: str,
        tokenKeyName: str = None,
        tokenSigningPublicKeys: Dict[str, str] = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
        signingDisabled: bool = None,
    ) -> ClientCreateAuthorizerResponseTypeDef:
        """
        [Client.create_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_authorizer)
        """

    def create_billing_group(
        self,
        billingGroupName: str,
        billingGroupProperties: ClientCreateBillingGroupBillingGroupPropertiesTypeDef = None,
        tags: List[ClientCreateBillingGroupTagsTypeDef] = None,
    ) -> ClientCreateBillingGroupResponseTypeDef:
        """
        [Client.create_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_billing_group)
        """

    def create_certificate_from_csr(
        self, certificateSigningRequest: str, setAsActive: bool = None
    ) -> ClientCreateCertificateFromCsrResponseTypeDef:
        """
        [Client.create_certificate_from_csr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_certificate_from_csr)
        """

    def create_domain_configuration(
        self,
        domainConfigurationName: str,
        domainName: str = None,
        serverCertificateArns: List[str] = None,
        validationCertificateArn: str = None,
        authorizerConfig: ClientCreateDomainConfigurationAuthorizerConfigTypeDef = None,
        serviceType: Literal["DATA", "CREDENTIAL_PROVIDER", "JOBS"] = None,
    ) -> ClientCreateDomainConfigurationResponseTypeDef:
        """
        [Client.create_domain_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_domain_configuration)
        """

    def create_dynamic_thing_group(
        self,
        thingGroupName: str,
        queryString: str,
        thingGroupProperties: ClientCreateDynamicThingGroupThingGroupPropertiesTypeDef = None,
        indexName: str = None,
        queryVersion: str = None,
        tags: List[ClientCreateDynamicThingGroupTagsTypeDef] = None,
    ) -> ClientCreateDynamicThingGroupResponseTypeDef:
        """
        [Client.create_dynamic_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_dynamic_thing_group)
        """

    def create_job(
        self,
        jobId: str,
        targets: List[str],
        documentSource: str = None,
        document: str = None,
        description: str = None,
        presignedUrlConfig: ClientCreateJobPresignedUrlConfigTypeDef = None,
        targetSelection: Literal["CONTINUOUS", "SNAPSHOT"] = None,
        jobExecutionsRolloutConfig: ClientCreateJobJobExecutionsRolloutConfigTypeDef = None,
        abortConfig: ClientCreateJobAbortConfigTypeDef = None,
        timeoutConfig: ClientCreateJobTimeoutConfigTypeDef = None,
        tags: List[ClientCreateJobTagsTypeDef] = None,
    ) -> ClientCreateJobResponseTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_job)
        """

    def create_keys_and_certificate(
        self, setAsActive: bool = None
    ) -> ClientCreateKeysAndCertificateResponseTypeDef:
        """
        [Client.create_keys_and_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_keys_and_certificate)
        """

    def create_mitigation_action(
        self,
        actionName: str,
        roleArn: str,
        actionParams: ClientCreateMitigationActionActionParamsTypeDef,
        tags: List[ClientCreateMitigationActionTagsTypeDef] = None,
    ) -> ClientCreateMitigationActionResponseTypeDef:
        """
        [Client.create_mitigation_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_mitigation_action)
        """

    def create_ota_update(
        self,
        otaUpdateId: str,
        targets: List[str],
        files: List[ClientCreateOtaUpdateFilesTypeDef],
        roleArn: str,
        description: str = None,
        protocols: List[Literal["MQTT", "HTTP"]] = None,
        targetSelection: Literal["CONTINUOUS", "SNAPSHOT"] = None,
        awsJobExecutionsRolloutConfig: ClientCreateOtaUpdateAwsJobExecutionsRolloutConfigTypeDef = None,
        awsJobPresignedUrlConfig: ClientCreateOtaUpdateAwsJobPresignedUrlConfigTypeDef = None,
        additionalParameters: Dict[str, str] = None,
        tags: List[ClientCreateOtaUpdateTagsTypeDef] = None,
    ) -> ClientCreateOtaUpdateResponseTypeDef:
        """
        [Client.create_ota_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_ota_update)
        """

    def create_policy(
        self, policyName: str, policyDocument: str
    ) -> ClientCreatePolicyResponseTypeDef:
        """
        [Client.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_policy)
        """

    def create_policy_version(
        self, policyName: str, policyDocument: str, setAsDefault: bool = None
    ) -> ClientCreatePolicyVersionResponseTypeDef:
        """
        [Client.create_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_policy_version)
        """

    def create_provisioning_claim(
        self, templateName: str
    ) -> ClientCreateProvisioningClaimResponseTypeDef:
        """
        [Client.create_provisioning_claim documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_provisioning_claim)
        """

    def create_provisioning_template(
        self,
        templateName: str,
        templateBody: str,
        provisioningRoleArn: str,
        description: str = None,
        enabled: bool = None,
        tags: List[ClientCreateProvisioningTemplateTagsTypeDef] = None,
    ) -> ClientCreateProvisioningTemplateResponseTypeDef:
        """
        [Client.create_provisioning_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_provisioning_template)
        """

    def create_provisioning_template_version(
        self, templateName: str, templateBody: str, setAsDefault: bool = None
    ) -> ClientCreateProvisioningTemplateVersionResponseTypeDef:
        """
        [Client.create_provisioning_template_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_provisioning_template_version)
        """

    def create_role_alias(
        self, roleAlias: str, roleArn: str, credentialDurationSeconds: int = None
    ) -> ClientCreateRoleAliasResponseTypeDef:
        """
        [Client.create_role_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_role_alias)
        """

    def create_scheduled_audit(
        self,
        frequency: Literal["DAILY", "WEEKLY", "BIWEEKLY", "MONTHLY"],
        targetCheckNames: List[str],
        scheduledAuditName: str,
        dayOfMonth: str = None,
        dayOfWeek: Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"] = None,
        tags: List[ClientCreateScheduledAuditTagsTypeDef] = None,
    ) -> ClientCreateScheduledAuditResponseTypeDef:
        """
        [Client.create_scheduled_audit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_scheduled_audit)
        """

    def create_security_profile(
        self,
        securityProfileName: str,
        securityProfileDescription: str = None,
        behaviors: List[ClientCreateSecurityProfileBehaviorsTypeDef] = None,
        alertTargets: Dict[str, ClientCreateSecurityProfileAlertTargetsTypeDef] = None,
        additionalMetricsToRetain: List[str] = None,
        tags: List[ClientCreateSecurityProfileTagsTypeDef] = None,
    ) -> ClientCreateSecurityProfileResponseTypeDef:
        """
        [Client.create_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_security_profile)
        """

    def create_stream(
        self,
        streamId: str,
        files: List[ClientCreateStreamFilesTypeDef],
        roleArn: str,
        description: str = None,
        tags: List[ClientCreateStreamTagsTypeDef] = None,
    ) -> ClientCreateStreamResponseTypeDef:
        """
        [Client.create_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_stream)
        """

    def create_thing(
        self,
        thingName: str,
        thingTypeName: str = None,
        attributePayload: ClientCreateThingAttributePayloadTypeDef = None,
        billingGroupName: str = None,
    ) -> ClientCreateThingResponseTypeDef:
        """
        [Client.create_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_thing)
        """

    def create_thing_group(
        self,
        thingGroupName: str,
        parentGroupName: str = None,
        thingGroupProperties: ClientCreateThingGroupThingGroupPropertiesTypeDef = None,
        tags: List[ClientCreateThingGroupTagsTypeDef] = None,
    ) -> ClientCreateThingGroupResponseTypeDef:
        """
        [Client.create_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_thing_group)
        """

    def create_thing_type(
        self,
        thingTypeName: str,
        thingTypeProperties: ClientCreateThingTypeThingTypePropertiesTypeDef = None,
        tags: List[ClientCreateThingTypeTagsTypeDef] = None,
    ) -> ClientCreateThingTypeResponseTypeDef:
        """
        [Client.create_thing_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_thing_type)
        """

    def create_topic_rule(
        self,
        ruleName: str,
        topicRulePayload: ClientCreateTopicRuleTopicRulePayloadTypeDef,
        tags: str = None,
    ) -> None:
        """
        [Client.create_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_topic_rule)
        """

    def create_topic_rule_destination(
        self,
        destinationConfiguration: ClientCreateTopicRuleDestinationDestinationConfigurationTypeDef,
    ) -> ClientCreateTopicRuleDestinationResponseTypeDef:
        """
        [Client.create_topic_rule_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.create_topic_rule_destination)
        """

    def delete_account_audit_configuration(
        self, deleteScheduledAudits: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_account_audit_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_account_audit_configuration)
        """

    def delete_authorizer(self, authorizerName: str) -> Dict[str, Any]:
        """
        [Client.delete_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_authorizer)
        """

    def delete_billing_group(
        self, billingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_billing_group)
        """

    def delete_ca_certificate(self, certificateId: str) -> Dict[str, Any]:
        """
        [Client.delete_ca_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_ca_certificate)
        """

    def delete_certificate(self, certificateId: str, forceDelete: bool = None) -> None:
        """
        [Client.delete_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_certificate)
        """

    def delete_domain_configuration(self, domainConfigurationName: str) -> Dict[str, Any]:
        """
        [Client.delete_domain_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_domain_configuration)
        """

    def delete_dynamic_thing_group(
        self, thingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_dynamic_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_dynamic_thing_group)
        """

    def delete_job(self, jobId: str, force: bool = None) -> None:
        """
        [Client.delete_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_job)
        """

    def delete_job_execution(
        self, jobId: str, thingName: str, executionNumber: int, force: bool = None
    ) -> None:
        """
        [Client.delete_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_job_execution)
        """

    def delete_mitigation_action(self, actionName: str) -> Dict[str, Any]:
        """
        [Client.delete_mitigation_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_mitigation_action)
        """

    def delete_ota_update(
        self, otaUpdateId: str, deleteStream: bool = None, forceDeleteAWSJob: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_ota_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_ota_update)
        """

    def delete_policy(self, policyName: str) -> None:
        """
        [Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_policy)
        """

    def delete_policy_version(self, policyName: str, policyVersionId: str) -> None:
        """
        [Client.delete_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_policy_version)
        """

    def delete_provisioning_template(self, templateName: str) -> Dict[str, Any]:
        """
        [Client.delete_provisioning_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_provisioning_template)
        """

    def delete_provisioning_template_version(
        self, templateName: str, versionId: int
    ) -> Dict[str, Any]:
        """
        [Client.delete_provisioning_template_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_provisioning_template_version)
        """

    def delete_registration_code(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.delete_registration_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_registration_code)
        """

    def delete_role_alias(self, roleAlias: str) -> Dict[str, Any]:
        """
        [Client.delete_role_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_role_alias)
        """

    def delete_scheduled_audit(self, scheduledAuditName: str) -> Dict[str, Any]:
        """
        [Client.delete_scheduled_audit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_scheduled_audit)
        """

    def delete_security_profile(
        self, securityProfileName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_security_profile)
        """

    def delete_stream(self, streamId: str) -> Dict[str, Any]:
        """
        [Client.delete_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_stream)
        """

    def delete_thing(self, thingName: str, expectedVersion: int = None) -> Dict[str, Any]:
        """
        [Client.delete_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_thing)
        """

    def delete_thing_group(
        self, thingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_thing_group)
        """

    def delete_thing_type(self, thingTypeName: str) -> Dict[str, Any]:
        """
        [Client.delete_thing_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_thing_type)
        """

    def delete_topic_rule(self, ruleName: str) -> None:
        """
        [Client.delete_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_topic_rule)
        """

    def delete_topic_rule_destination(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_topic_rule_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_topic_rule_destination)
        """

    def delete_v2_logging_level(
        self, targetType: Literal["DEFAULT", "THING_GROUP"], targetName: str
    ) -> None:
        """
        [Client.delete_v2_logging_level documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.delete_v2_logging_level)
        """

    def deprecate_thing_type(
        self, thingTypeName: str, undoDeprecate: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.deprecate_thing_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.deprecate_thing_type)
        """

    def describe_account_audit_configuration(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeAccountAuditConfigurationResponseTypeDef:
        """
        [Client.describe_account_audit_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_account_audit_configuration)
        """

    def describe_audit_finding(self, findingId: str) -> ClientDescribeAuditFindingResponseTypeDef:
        """
        [Client.describe_audit_finding documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_audit_finding)
        """

    def describe_audit_mitigation_actions_task(
        self, taskId: str
    ) -> ClientDescribeAuditMitigationActionsTaskResponseTypeDef:
        """
        [Client.describe_audit_mitigation_actions_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_audit_mitigation_actions_task)
        """

    def describe_audit_task(self, taskId: str) -> ClientDescribeAuditTaskResponseTypeDef:
        """
        [Client.describe_audit_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_audit_task)
        """

    def describe_authorizer(self, authorizerName: str) -> ClientDescribeAuthorizerResponseTypeDef:
        """
        [Client.describe_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_authorizer)
        """

    def describe_billing_group(
        self, billingGroupName: str
    ) -> ClientDescribeBillingGroupResponseTypeDef:
        """
        [Client.describe_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_billing_group)
        """

    def describe_ca_certificate(
        self, certificateId: str
    ) -> ClientDescribeCaCertificateResponseTypeDef:
        """
        [Client.describe_ca_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_ca_certificate)
        """

    def describe_certificate(self, certificateId: str) -> ClientDescribeCertificateResponseTypeDef:
        """
        [Client.describe_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_certificate)
        """

    def describe_default_authorizer(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeDefaultAuthorizerResponseTypeDef:
        """
        [Client.describe_default_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_default_authorizer)
        """

    def describe_domain_configuration(
        self, domainConfigurationName: str
    ) -> ClientDescribeDomainConfigurationResponseTypeDef:
        """
        [Client.describe_domain_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_domain_configuration)
        """

    def describe_endpoint(self, endpointType: str = None) -> ClientDescribeEndpointResponseTypeDef:
        """
        [Client.describe_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_endpoint)
        """

    def describe_event_configurations(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeEventConfigurationsResponseTypeDef:
        """
        [Client.describe_event_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_event_configurations)
        """

    def describe_index(self, indexName: str) -> ClientDescribeIndexResponseTypeDef:
        """
        [Client.describe_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_index)
        """

    def describe_job(self, jobId: str) -> ClientDescribeJobResponseTypeDef:
        """
        [Client.describe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_job)
        """

    def describe_job_execution(
        self, jobId: str, thingName: str, executionNumber: int = None
    ) -> ClientDescribeJobExecutionResponseTypeDef:
        """
        [Client.describe_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_job_execution)
        """

    def describe_mitigation_action(
        self, actionName: str
    ) -> ClientDescribeMitigationActionResponseTypeDef:
        """
        [Client.describe_mitigation_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_mitigation_action)
        """

    def describe_provisioning_template(
        self, templateName: str
    ) -> ClientDescribeProvisioningTemplateResponseTypeDef:
        """
        [Client.describe_provisioning_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_provisioning_template)
        """

    def describe_provisioning_template_version(
        self, templateName: str, versionId: int
    ) -> ClientDescribeProvisioningTemplateVersionResponseTypeDef:
        """
        [Client.describe_provisioning_template_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_provisioning_template_version)
        """

    def describe_role_alias(self, roleAlias: str) -> ClientDescribeRoleAliasResponseTypeDef:
        """
        [Client.describe_role_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_role_alias)
        """

    def describe_scheduled_audit(
        self, scheduledAuditName: str
    ) -> ClientDescribeScheduledAuditResponseTypeDef:
        """
        [Client.describe_scheduled_audit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_scheduled_audit)
        """

    def describe_security_profile(
        self, securityProfileName: str
    ) -> ClientDescribeSecurityProfileResponseTypeDef:
        """
        [Client.describe_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_security_profile)
        """

    def describe_stream(self, streamId: str) -> ClientDescribeStreamResponseTypeDef:
        """
        [Client.describe_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_stream)
        """

    def describe_thing(self, thingName: str) -> ClientDescribeThingResponseTypeDef:
        """
        [Client.describe_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_thing)
        """

    def describe_thing_group(self, thingGroupName: str) -> ClientDescribeThingGroupResponseTypeDef:
        """
        [Client.describe_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_thing_group)
        """

    def describe_thing_registration_task(
        self, taskId: str
    ) -> ClientDescribeThingRegistrationTaskResponseTypeDef:
        """
        [Client.describe_thing_registration_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_thing_registration_task)
        """

    def describe_thing_type(self, thingTypeName: str) -> ClientDescribeThingTypeResponseTypeDef:
        """
        [Client.describe_thing_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.describe_thing_type)
        """

    def detach_policy(self, policyName: str, target: str) -> None:
        """
        [Client.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.detach_policy)
        """

    def detach_principal_policy(self, policyName: str, principal: str) -> None:
        """
        [Client.detach_principal_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.detach_principal_policy)
        """

    def detach_security_profile(
        self, securityProfileName: str, securityProfileTargetArn: str
    ) -> Dict[str, Any]:
        """
        [Client.detach_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.detach_security_profile)
        """

    def detach_thing_principal(self, thingName: str, principal: str) -> Dict[str, Any]:
        """
        [Client.detach_thing_principal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.detach_thing_principal)
        """

    def disable_topic_rule(self, ruleName: str) -> None:
        """
        [Client.disable_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.disable_topic_rule)
        """

    def enable_topic_rule(self, ruleName: str) -> None:
        """
        [Client.enable_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.enable_topic_rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.generate_presigned_url)
        """

    def get_cardinality(
        self,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None,
    ) -> ClientGetCardinalityResponseTypeDef:
        """
        [Client.get_cardinality documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.get_cardinality)
        """

    def get_effective_policies(
        self, principal: str = None, cognitoIdentityPoolId: str = None, thingName: str = None
    ) -> ClientGetEffectivePoliciesResponseTypeDef:
        """
        [Client.get_effective_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.get_effective_policies)
        """

    def get_indexing_configuration(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetIndexingConfigurationResponseTypeDef:
        """
        [Client.get_indexing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.get_indexing_configuration)
        """

    def get_job_document(self, jobId: str) -> ClientGetJobDocumentResponseTypeDef:
        """
        [Client.get_job_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.get_job_document)
        """

    def get_logging_options(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetLoggingOptionsResponseTypeDef:
        """
        [Client.get_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.get_logging_options)
        """

    def get_ota_update(self, otaUpdateId: str) -> ClientGetOtaUpdateResponseTypeDef:
        """
        [Client.get_ota_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.get_ota_update)
        """

    def get_percentiles(
        self,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None,
        percents: List[float] = None,
    ) -> ClientGetPercentilesResponseTypeDef:
        """
        [Client.get_percentiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.get_percentiles)
        """

    def get_policy(self, policyName: str) -> ClientGetPolicyResponseTypeDef:
        """
        [Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.get_policy)
        """

    def get_policy_version(
        self, policyName: str, policyVersionId: str
    ) -> ClientGetPolicyVersionResponseTypeDef:
        """
        [Client.get_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.get_policy_version)
        """

    def get_registration_code(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetRegistrationCodeResponseTypeDef:
        """
        [Client.get_registration_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.get_registration_code)
        """

    def get_statistics(
        self,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None,
    ) -> ClientGetStatisticsResponseTypeDef:
        """
        [Client.get_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.get_statistics)
        """

    def get_topic_rule(self, ruleName: str) -> ClientGetTopicRuleResponseTypeDef:
        """
        [Client.get_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.get_topic_rule)
        """

    def get_topic_rule_destination(self, arn: str) -> ClientGetTopicRuleDestinationResponseTypeDef:
        """
        [Client.get_topic_rule_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.get_topic_rule_destination)
        """

    def get_v2_logging_options(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetV2LoggingOptionsResponseTypeDef:
        """
        [Client.get_v2_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.get_v2_logging_options)
        """

    def list_active_violations(
        self,
        thingName: str = None,
        securityProfileName: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListActiveViolationsResponseTypeDef:
        """
        [Client.list_active_violations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_active_violations)
        """

    def list_attached_policies(
        self, target: str, recursive: bool = None, marker: str = None, pageSize: int = None
    ) -> ClientListAttachedPoliciesResponseTypeDef:
        """
        [Client.list_attached_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_attached_policies)
        """

    def list_audit_findings(
        self,
        taskId: str = None,
        checkName: str = None,
        resourceIdentifier: ClientListAuditFindingsResourceIdentifierTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
    ) -> ClientListAuditFindingsResponseTypeDef:
        """
        [Client.list_audit_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_audit_findings)
        """

    def list_audit_mitigation_actions_executions(
        self,
        taskId: str,
        findingId: str,
        actionStatus: Literal[
            "IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED", "SKIPPED", "PENDING"
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListAuditMitigationActionsExecutionsResponseTypeDef:
        """
        [Client.list_audit_mitigation_actions_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_audit_mitigation_actions_executions)
        """

    def list_audit_mitigation_actions_tasks(
        self,
        startTime: datetime,
        endTime: datetime,
        auditTaskId: str = None,
        findingId: str = None,
        taskStatus: Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListAuditMitigationActionsTasksResponseTypeDef:
        """
        [Client.list_audit_mitigation_actions_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_audit_mitigation_actions_tasks)
        """

    def list_audit_tasks(
        self,
        startTime: datetime,
        endTime: datetime,
        taskType: Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"] = None,
        taskStatus: Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListAuditTasksResponseTypeDef:
        """
        [Client.list_audit_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_audit_tasks)
        """

    def list_authorizers(
        self,
        pageSize: int = None,
        marker: str = None,
        ascendingOrder: bool = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
    ) -> ClientListAuthorizersResponseTypeDef:
        """
        [Client.list_authorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_authorizers)
        """

    def list_billing_groups(
        self, nextToken: str = None, maxResults: int = None, namePrefixFilter: str = None
    ) -> ClientListBillingGroupsResponseTypeDef:
        """
        [Client.list_billing_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_billing_groups)
        """

    def list_ca_certificates(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ClientListCaCertificatesResponseTypeDef:
        """
        [Client.list_ca_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_ca_certificates)
        """

    def list_certificates(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ClientListCertificatesResponseTypeDef:
        """
        [Client.list_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_certificates)
        """

    def list_certificates_by_ca(
        self,
        caCertificateId: str,
        pageSize: int = None,
        marker: str = None,
        ascendingOrder: bool = None,
    ) -> ClientListCertificatesByCaResponseTypeDef:
        """
        [Client.list_certificates_by_ca documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_certificates_by_ca)
        """

    def list_domain_configurations(
        self,
        marker: str = None,
        pageSize: int = None,
        serviceType: Literal["DATA", "CREDENTIAL_PROVIDER", "JOBS"] = None,
    ) -> ClientListDomainConfigurationsResponseTypeDef:
        """
        [Client.list_domain_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_domain_configurations)
        """

    def list_indices(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListIndicesResponseTypeDef:
        """
        [Client.list_indices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_indices)
        """

    def list_job_executions_for_job(
        self,
        jobId: str,
        status: Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListJobExecutionsForJobResponseTypeDef:
        """
        [Client.list_job_executions_for_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_job_executions_for_job)
        """

    def list_job_executions_for_thing(
        self,
        thingName: str,
        status: Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListJobExecutionsForThingResponseTypeDef:
        """
        [Client.list_job_executions_for_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_job_executions_for_thing)
        """

    def list_jobs(
        self,
        status: Literal["IN_PROGRESS", "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS"] = None,
        targetSelection: Literal["CONTINUOUS", "SNAPSHOT"] = None,
        maxResults: int = None,
        nextToken: str = None,
        thingGroupName: str = None,
        thingGroupId: str = None,
    ) -> ClientListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_jobs)
        """

    def list_mitigation_actions(
        self,
        actionType: Literal[
            "UPDATE_DEVICE_CERTIFICATE",
            "UPDATE_CA_CERTIFICATE",
            "ADD_THINGS_TO_THING_GROUP",
            "REPLACE_DEFAULT_POLICY_VERSION",
            "ENABLE_IOT_LOGGING",
            "PUBLISH_FINDING_TO_SNS",
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListMitigationActionsResponseTypeDef:
        """
        [Client.list_mitigation_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_mitigation_actions)
        """

    def list_ota_updates(
        self,
        maxResults: int = None,
        nextToken: str = None,
        otaUpdateStatus: Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "CREATE_FAILED"
        ] = None,
    ) -> ClientListOtaUpdatesResponseTypeDef:
        """
        [Client.list_ota_updates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_ota_updates)
        """

    def list_outgoing_certificates(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ClientListOutgoingCertificatesResponseTypeDef:
        """
        [Client.list_outgoing_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_outgoing_certificates)
        """

    def list_policies(
        self, marker: str = None, pageSize: int = None, ascendingOrder: bool = None
    ) -> ClientListPoliciesResponseTypeDef:
        """
        [Client.list_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_policies)
        """

    def list_policy_principals(
        self, policyName: str, marker: str = None, pageSize: int = None, ascendingOrder: bool = None
    ) -> ClientListPolicyPrincipalsResponseTypeDef:
        """
        [Client.list_policy_principals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_policy_principals)
        """

    def list_policy_versions(self, policyName: str) -> ClientListPolicyVersionsResponseTypeDef:
        """
        [Client.list_policy_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_policy_versions)
        """

    def list_principal_policies(
        self, principal: str, marker: str = None, pageSize: int = None, ascendingOrder: bool = None
    ) -> ClientListPrincipalPoliciesResponseTypeDef:
        """
        [Client.list_principal_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_principal_policies)
        """

    def list_principal_things(
        self, principal: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListPrincipalThingsResponseTypeDef:
        """
        [Client.list_principal_things documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_principal_things)
        """

    def list_provisioning_template_versions(
        self, templateName: str, maxResults: int = None, nextToken: str = None
    ) -> ClientListProvisioningTemplateVersionsResponseTypeDef:
        """
        [Client.list_provisioning_template_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_provisioning_template_versions)
        """

    def list_provisioning_templates(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListProvisioningTemplatesResponseTypeDef:
        """
        [Client.list_provisioning_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_provisioning_templates)
        """

    def list_role_aliases(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ClientListRoleAliasesResponseTypeDef:
        """
        [Client.list_role_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_role_aliases)
        """

    def list_scheduled_audits(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListScheduledAuditsResponseTypeDef:
        """
        [Client.list_scheduled_audits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_scheduled_audits)
        """

    def list_security_profiles(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListSecurityProfilesResponseTypeDef:
        """
        [Client.list_security_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_security_profiles)
        """

    def list_security_profiles_for_target(
        self,
        securityProfileTargetArn: str,
        nextToken: str = None,
        maxResults: int = None,
        recursive: bool = None,
    ) -> ClientListSecurityProfilesForTargetResponseTypeDef:
        """
        [Client.list_security_profiles_for_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_security_profiles_for_target)
        """

    def list_streams(
        self, maxResults: int = None, nextToken: str = None, ascendingOrder: bool = None
    ) -> ClientListStreamsResponseTypeDef:
        """
        [Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_streams)
        """

    def list_tags_for_resource(
        self, resourceArn: str, nextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_tags_for_resource)
        """

    def list_targets_for_policy(
        self, policyName: str, marker: str = None, pageSize: int = None
    ) -> ClientListTargetsForPolicyResponseTypeDef:
        """
        [Client.list_targets_for_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_targets_for_policy)
        """

    def list_targets_for_security_profile(
        self, securityProfileName: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListTargetsForSecurityProfileResponseTypeDef:
        """
        [Client.list_targets_for_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_targets_for_security_profile)
        """

    def list_thing_groups(
        self,
        nextToken: str = None,
        maxResults: int = None,
        parentGroup: str = None,
        namePrefixFilter: str = None,
        recursive: bool = None,
    ) -> ClientListThingGroupsResponseTypeDef:
        """
        [Client.list_thing_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_thing_groups)
        """

    def list_thing_groups_for_thing(
        self, thingName: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListThingGroupsForThingResponseTypeDef:
        """
        [Client.list_thing_groups_for_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_thing_groups_for_thing)
        """

    def list_thing_principals(self, thingName: str) -> ClientListThingPrincipalsResponseTypeDef:
        """
        [Client.list_thing_principals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_thing_principals)
        """

    def list_thing_registration_task_reports(
        self,
        taskId: str,
        reportType: Literal["ERRORS", "RESULTS"],
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListThingRegistrationTaskReportsResponseTypeDef:
        """
        [Client.list_thing_registration_task_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_thing_registration_task_reports)
        """

    def list_thing_registration_tasks(
        self,
        nextToken: str = None,
        maxResults: int = None,
        status: Literal["InProgress", "Completed", "Failed", "Cancelled", "Cancelling"] = None,
    ) -> ClientListThingRegistrationTasksResponseTypeDef:
        """
        [Client.list_thing_registration_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_thing_registration_tasks)
        """

    def list_thing_types(
        self, nextToken: str = None, maxResults: int = None, thingTypeName: str = None
    ) -> ClientListThingTypesResponseTypeDef:
        """
        [Client.list_thing_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_thing_types)
        """

    def list_things(
        self,
        nextToken: str = None,
        maxResults: int = None,
        attributeName: str = None,
        attributeValue: str = None,
        thingTypeName: str = None,
    ) -> ClientListThingsResponseTypeDef:
        """
        [Client.list_things documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_things)
        """

    def list_things_in_billing_group(
        self, billingGroupName: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListThingsInBillingGroupResponseTypeDef:
        """
        [Client.list_things_in_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_things_in_billing_group)
        """

    def list_things_in_thing_group(
        self,
        thingGroupName: str,
        recursive: bool = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListThingsInThingGroupResponseTypeDef:
        """
        [Client.list_things_in_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_things_in_thing_group)
        """

    def list_topic_rule_destinations(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListTopicRuleDestinationsResponseTypeDef:
        """
        [Client.list_topic_rule_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_topic_rule_destinations)
        """

    def list_topic_rules(
        self,
        topic: str = None,
        maxResults: int = None,
        nextToken: str = None,
        ruleDisabled: bool = None,
    ) -> ClientListTopicRulesResponseTypeDef:
        """
        [Client.list_topic_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_topic_rules)
        """

    def list_v2_logging_levels(
        self,
        targetType: Literal["DEFAULT", "THING_GROUP"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListV2LoggingLevelsResponseTypeDef:
        """
        [Client.list_v2_logging_levels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_v2_logging_levels)
        """

    def list_violation_events(
        self,
        startTime: datetime,
        endTime: datetime,
        thingName: str = None,
        securityProfileName: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListViolationEventsResponseTypeDef:
        """
        [Client.list_violation_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.list_violation_events)
        """

    def register_ca_certificate(
        self,
        caCertificate: str,
        verificationCertificate: str,
        setAsActive: bool = None,
        allowAutoRegistration: bool = None,
        registrationConfig: ClientRegisterCaCertificateRegistrationConfigTypeDef = None,
    ) -> ClientRegisterCaCertificateResponseTypeDef:
        """
        [Client.register_ca_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.register_ca_certificate)
        """

    def register_certificate(
        self,
        certificatePem: str,
        caCertificatePem: str = None,
        setAsActive: bool = None,
        status: Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ] = None,
    ) -> ClientRegisterCertificateResponseTypeDef:
        """
        [Client.register_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.register_certificate)
        """

    def register_thing(
        self, templateBody: str, parameters: Dict[str, str] = None
    ) -> ClientRegisterThingResponseTypeDef:
        """
        [Client.register_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.register_thing)
        """

    def reject_certificate_transfer(self, certificateId: str, rejectReason: str = None) -> None:
        """
        [Client.reject_certificate_transfer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.reject_certificate_transfer)
        """

    def remove_thing_from_billing_group(
        self,
        billingGroupName: str = None,
        billingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.remove_thing_from_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.remove_thing_from_billing_group)
        """

    def remove_thing_from_thing_group(
        self,
        thingGroupName: str = None,
        thingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.remove_thing_from_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.remove_thing_from_thing_group)
        """

    def replace_topic_rule(
        self, ruleName: str, topicRulePayload: ClientReplaceTopicRuleTopicRulePayloadTypeDef
    ) -> None:
        """
        [Client.replace_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.replace_topic_rule)
        """

    def search_index(
        self,
        queryString: str,
        indexName: str = None,
        nextToken: str = None,
        maxResults: int = None,
        queryVersion: str = None,
    ) -> ClientSearchIndexResponseTypeDef:
        """
        [Client.search_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.search_index)
        """

    def set_default_authorizer(
        self, authorizerName: str
    ) -> ClientSetDefaultAuthorizerResponseTypeDef:
        """
        [Client.set_default_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.set_default_authorizer)
        """

    def set_default_policy_version(self, policyName: str, policyVersionId: str) -> None:
        """
        [Client.set_default_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.set_default_policy_version)
        """

    def set_logging_options(
        self, loggingOptionsPayload: ClientSetLoggingOptionsLoggingOptionsPayloadTypeDef
    ) -> None:
        """
        [Client.set_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.set_logging_options)
        """

    def set_v2_logging_level(
        self,
        logTarget: ClientSetV2LoggingLevelLogTargetTypeDef,
        logLevel: Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"],
    ) -> None:
        """
        [Client.set_v2_logging_level documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.set_v2_logging_level)
        """

    def set_v2_logging_options(
        self,
        roleArn: str = None,
        defaultLogLevel: Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"] = None,
        disableAllLogs: bool = None,
    ) -> None:
        """
        [Client.set_v2_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.set_v2_logging_options)
        """

    def start_audit_mitigation_actions_task(
        self,
        taskId: str,
        target: ClientStartAuditMitigationActionsTaskTargetTypeDef,
        auditCheckToActionsMapping: Dict[str, List[str]],
        clientRequestToken: str,
    ) -> ClientStartAuditMitigationActionsTaskResponseTypeDef:
        """
        [Client.start_audit_mitigation_actions_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.start_audit_mitigation_actions_task)
        """

    def start_on_demand_audit_task(
        self, targetCheckNames: List[str]
    ) -> ClientStartOnDemandAuditTaskResponseTypeDef:
        """
        [Client.start_on_demand_audit_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.start_on_demand_audit_task)
        """

    def start_thing_registration_task(
        self, templateBody: str, inputFileBucket: str, inputFileKey: str, roleArn: str
    ) -> ClientStartThingRegistrationTaskResponseTypeDef:
        """
        [Client.start_thing_registration_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.start_thing_registration_task)
        """

    def stop_thing_registration_task(self, taskId: str) -> Dict[str, Any]:
        """
        [Client.stop_thing_registration_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.stop_thing_registration_task)
        """

    def tag_resource(
        self, resourceArn: str, tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.tag_resource)
        """

    def test_authorization(
        self,
        authInfos: List[ClientTestAuthorizationAuthInfosTypeDef],
        principal: str = None,
        cognitoIdentityPoolId: str = None,
        clientId: str = None,
        policyNamesToAdd: List[str] = None,
        policyNamesToSkip: List[str] = None,
    ) -> ClientTestAuthorizationResponseTypeDef:
        """
        [Client.test_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.test_authorization)
        """

    def test_invoke_authorizer(
        self,
        authorizerName: str,
        token: str = None,
        tokenSignature: str = None,
        httpContext: ClientTestInvokeAuthorizerHttpContextTypeDef = None,
        mqttContext: ClientTestInvokeAuthorizerMqttContextTypeDef = None,
        tlsContext: ClientTestInvokeAuthorizerTlsContextTypeDef = None,
    ) -> ClientTestInvokeAuthorizerResponseTypeDef:
        """
        [Client.test_invoke_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.test_invoke_authorizer)
        """

    def transfer_certificate(
        self, certificateId: str, targetAwsAccount: str, transferMessage: str = None
    ) -> ClientTransferCertificateResponseTypeDef:
        """
        [Client.transfer_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.transfer_certificate)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.untag_resource)
        """

    def update_account_audit_configuration(
        self,
        roleArn: str = None,
        auditNotificationTargetConfigurations: Dict[
            str, ClientUpdateAccountAuditConfigurationAuditNotificationTargetConfigurationsTypeDef
        ] = None,
        auditCheckConfigurations: Dict[
            str, ClientUpdateAccountAuditConfigurationAuditCheckConfigurationsTypeDef
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_account_audit_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_account_audit_configuration)
        """

    def update_authorizer(
        self,
        authorizerName: str,
        authorizerFunctionArn: str = None,
        tokenKeyName: str = None,
        tokenSigningPublicKeys: Dict[str, str] = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
    ) -> ClientUpdateAuthorizerResponseTypeDef:
        """
        [Client.update_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_authorizer)
        """

    def update_billing_group(
        self,
        billingGroupName: str,
        billingGroupProperties: ClientUpdateBillingGroupBillingGroupPropertiesTypeDef,
        expectedVersion: int = None,
    ) -> ClientUpdateBillingGroupResponseTypeDef:
        """
        [Client.update_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_billing_group)
        """

    def update_ca_certificate(
        self,
        certificateId: str,
        newStatus: Literal["ACTIVE", "INACTIVE"] = None,
        newAutoRegistrationStatus: Literal["ENABLE", "DISABLE"] = None,
        registrationConfig: ClientUpdateCaCertificateRegistrationConfigTypeDef = None,
        removeAutoRegistration: bool = None,
    ) -> None:
        """
        [Client.update_ca_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_ca_certificate)
        """

    def update_certificate(
        self,
        certificateId: str,
        newStatus: Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ],
    ) -> None:
        """
        [Client.update_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_certificate)
        """

    def update_domain_configuration(
        self,
        domainConfigurationName: str,
        authorizerConfig: ClientUpdateDomainConfigurationAuthorizerConfigTypeDef = None,
        domainConfigurationStatus: Literal["ENABLED", "DISABLED"] = None,
        removeAuthorizerConfig: bool = None,
    ) -> ClientUpdateDomainConfigurationResponseTypeDef:
        """
        [Client.update_domain_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_domain_configuration)
        """

    def update_dynamic_thing_group(
        self,
        thingGroupName: str,
        thingGroupProperties: ClientUpdateDynamicThingGroupThingGroupPropertiesTypeDef,
        expectedVersion: int = None,
        indexName: str = None,
        queryString: str = None,
        queryVersion: str = None,
    ) -> ClientUpdateDynamicThingGroupResponseTypeDef:
        """
        [Client.update_dynamic_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_dynamic_thing_group)
        """

    def update_event_configurations(
        self,
        eventConfigurations: Dict[
            str, ClientUpdateEventConfigurationsEventConfigurationsTypeDef
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_event_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_event_configurations)
        """

    def update_indexing_configuration(
        self,
        thingIndexingConfiguration: ClientUpdateIndexingConfigurationThingIndexingConfigurationTypeDef = None,
        thingGroupIndexingConfiguration: ClientUpdateIndexingConfigurationThingGroupIndexingConfigurationTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_indexing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_indexing_configuration)
        """

    def update_job(
        self,
        jobId: str,
        description: str = None,
        presignedUrlConfig: ClientUpdateJobPresignedUrlConfigTypeDef = None,
        jobExecutionsRolloutConfig: ClientUpdateJobJobExecutionsRolloutConfigTypeDef = None,
        abortConfig: ClientUpdateJobAbortConfigTypeDef = None,
        timeoutConfig: ClientUpdateJobTimeoutConfigTypeDef = None,
    ) -> None:
        """
        [Client.update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_job)
        """

    def update_mitigation_action(
        self,
        actionName: str,
        roleArn: str = None,
        actionParams: ClientUpdateMitigationActionActionParamsTypeDef = None,
    ) -> ClientUpdateMitigationActionResponseTypeDef:
        """
        [Client.update_mitigation_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_mitigation_action)
        """

    def update_provisioning_template(
        self,
        templateName: str,
        description: str = None,
        enabled: bool = None,
        defaultVersionId: int = None,
        provisioningRoleArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_provisioning_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_provisioning_template)
        """

    def update_role_alias(
        self, roleAlias: str, roleArn: str = None, credentialDurationSeconds: int = None
    ) -> ClientUpdateRoleAliasResponseTypeDef:
        """
        [Client.update_role_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_role_alias)
        """

    def update_scheduled_audit(
        self,
        scheduledAuditName: str,
        frequency: Literal["DAILY", "WEEKLY", "BIWEEKLY", "MONTHLY"] = None,
        dayOfMonth: str = None,
        dayOfWeek: Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"] = None,
        targetCheckNames: List[str] = None,
    ) -> ClientUpdateScheduledAuditResponseTypeDef:
        """
        [Client.update_scheduled_audit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_scheduled_audit)
        """

    def update_security_profile(
        self,
        securityProfileName: str,
        securityProfileDescription: str = None,
        behaviors: List[ClientUpdateSecurityProfileBehaviorsTypeDef] = None,
        alertTargets: Dict[str, ClientUpdateSecurityProfileAlertTargetsTypeDef] = None,
        additionalMetricsToRetain: List[str] = None,
        deleteBehaviors: bool = None,
        deleteAlertTargets: bool = None,
        deleteAdditionalMetricsToRetain: bool = None,
        expectedVersion: int = None,
    ) -> ClientUpdateSecurityProfileResponseTypeDef:
        """
        [Client.update_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_security_profile)
        """

    def update_stream(
        self,
        streamId: str,
        description: str = None,
        files: List[ClientUpdateStreamFilesTypeDef] = None,
        roleArn: str = None,
    ) -> ClientUpdateStreamResponseTypeDef:
        """
        [Client.update_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_stream)
        """

    def update_thing(
        self,
        thingName: str,
        thingTypeName: str = None,
        attributePayload: ClientUpdateThingAttributePayloadTypeDef = None,
        expectedVersion: int = None,
        removeThingType: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_thing)
        """

    def update_thing_group(
        self,
        thingGroupName: str,
        thingGroupProperties: ClientUpdateThingGroupThingGroupPropertiesTypeDef,
        expectedVersion: int = None,
    ) -> ClientUpdateThingGroupResponseTypeDef:
        """
        [Client.update_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_thing_group)
        """

    def update_thing_groups_for_thing(
        self,
        thingName: str = None,
        thingGroupsToAdd: List[str] = None,
        thingGroupsToRemove: List[str] = None,
        overrideDynamicGroups: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_thing_groups_for_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_thing_groups_for_thing)
        """

    def update_topic_rule_destination(
        self, arn: str, status: Literal["ENABLED", "IN_PROGRESS", "DISABLED", "ERROR"]
    ) -> Dict[str, Any]:
        """
        [Client.update_topic_rule_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.update_topic_rule_destination)
        """

    def validate_security_profile_behaviors(
        self, behaviors: List[ClientValidateSecurityProfileBehaviorsBehaviorsTypeDef]
    ) -> ClientValidateSecurityProfileBehaviorsResponseTypeDef:
        """
        [Client.validate_security_profile_behaviors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Client.validate_security_profile_behaviors)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_active_violations"]
    ) -> "paginator_scope.ListActiveViolationsPaginator":
        """
        [Paginator.ListActiveViolations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListActiveViolations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_policies"]
    ) -> "paginator_scope.ListAttachedPoliciesPaginator":
        """
        [Paginator.ListAttachedPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListAttachedPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audit_findings"]
    ) -> "paginator_scope.ListAuditFindingsPaginator":
        """
        [Paginator.ListAuditFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListAuditFindings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audit_tasks"]
    ) -> "paginator_scope.ListAuditTasksPaginator":
        """
        [Paginator.ListAuditTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListAuditTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_authorizers"]
    ) -> "paginator_scope.ListAuthorizersPaginator":
        """
        [Paginator.ListAuthorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListAuthorizers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_billing_groups"]
    ) -> "paginator_scope.ListBillingGroupsPaginator":
        """
        [Paginator.ListBillingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListBillingGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ca_certificates"]
    ) -> "paginator_scope.ListCACertificatesPaginator":
        """
        [Paginator.ListCACertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListCACertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_certificates"]
    ) -> "paginator_scope.ListCertificatesPaginator":
        """
        [Paginator.ListCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListCertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_certificates_by_ca"]
    ) -> "paginator_scope.ListCertificatesByCAPaginator":
        """
        [Paginator.ListCertificatesByCA documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListCertificatesByCA)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_indices"]
    ) -> "paginator_scope.ListIndicesPaginator":
        """
        [Paginator.ListIndices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListIndices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_job_executions_for_job"]
    ) -> "paginator_scope.ListJobExecutionsForJobPaginator":
        """
        [Paginator.ListJobExecutionsForJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForJob)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_job_executions_for_thing"]
    ) -> "paginator_scope.ListJobExecutionsForThingPaginator":
        """
        [Paginator.ListJobExecutionsForThing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForThing)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> "paginator_scope.ListJobsPaginator":
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ota_updates"]
    ) -> "paginator_scope.ListOTAUpdatesPaginator":
        """
        [Paginator.ListOTAUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListOTAUpdates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_outgoing_certificates"]
    ) -> "paginator_scope.ListOutgoingCertificatesPaginator":
        """
        [Paginator.ListOutgoingCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListOutgoingCertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policies"]
    ) -> "paginator_scope.ListPoliciesPaginator":
        """
        [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policy_principals"]
    ) -> "paginator_scope.ListPolicyPrincipalsPaginator":
        """
        [Paginator.ListPolicyPrincipals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListPolicyPrincipals)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_principal_policies"]
    ) -> "paginator_scope.ListPrincipalPoliciesPaginator":
        """
        [Paginator.ListPrincipalPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListPrincipalPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_principal_things"]
    ) -> "paginator_scope.ListPrincipalThingsPaginator":
        """
        [Paginator.ListPrincipalThings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListPrincipalThings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_role_aliases"]
    ) -> "paginator_scope.ListRoleAliasesPaginator":
        """
        [Paginator.ListRoleAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListRoleAliases)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_scheduled_audits"]
    ) -> "paginator_scope.ListScheduledAuditsPaginator":
        """
        [Paginator.ListScheduledAudits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListScheduledAudits)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profiles"]
    ) -> "paginator_scope.ListSecurityProfilesPaginator":
        """
        [Paginator.ListSecurityProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListSecurityProfiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profiles_for_target"]
    ) -> "paginator_scope.ListSecurityProfilesForTargetPaginator":
        """
        [Paginator.ListSecurityProfilesForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListSecurityProfilesForTarget)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_streams"]
    ) -> "paginator_scope.ListStreamsPaginator":
        """
        [Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListStreams)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> "paginator_scope.ListTagsForResourcePaginator":
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListTagsForResource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_targets_for_policy"]
    ) -> "paginator_scope.ListTargetsForPolicyPaginator":
        """
        [Paginator.ListTargetsForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListTargetsForPolicy)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_targets_for_security_profile"]
    ) -> "paginator_scope.ListTargetsForSecurityProfilePaginator":
        """
        [Paginator.ListTargetsForSecurityProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListTargetsForSecurityProfile)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_groups"]
    ) -> "paginator_scope.ListThingGroupsPaginator":
        """
        [Paginator.ListThingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListThingGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_groups_for_thing"]
    ) -> "paginator_scope.ListThingGroupsForThingPaginator":
        """
        [Paginator.ListThingGroupsForThing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListThingGroupsForThing)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_registration_tasks"]
    ) -> "paginator_scope.ListThingRegistrationTasksPaginator":
        """
        [Paginator.ListThingRegistrationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_types"]
    ) -> "paginator_scope.ListThingTypesPaginator":
        """
        [Paginator.ListThingTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListThingTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_things"]
    ) -> "paginator_scope.ListThingsPaginator":
        """
        [Paginator.ListThings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListThings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_things_in_billing_group"]
    ) -> "paginator_scope.ListThingsInBillingGroupPaginator":
        """
        [Paginator.ListThingsInBillingGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListThingsInBillingGroup)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_things_in_thing_group"]
    ) -> "paginator_scope.ListThingsInThingGroupPaginator":
        """
        [Paginator.ListThingsInThingGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListThingsInThingGroup)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_topic_rules"]
    ) -> "paginator_scope.ListTopicRulesPaginator":
        """
        [Paginator.ListTopicRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListTopicRules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_v2_logging_levels"]
    ) -> "paginator_scope.ListV2LoggingLevelsPaginator":
        """
        [Paginator.ListV2LoggingLevels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListV2LoggingLevels)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_violation_events"]
    ) -> "paginator_scope.ListViolationEventsPaginator":
        """
        [Paginator.ListViolationEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot.html#IoT.Paginator.ListViolationEvents)
        """


class Exceptions:
    CertificateConflictException: Boto3ClientError
    CertificateStateException: Boto3ClientError
    CertificateValidationException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictingResourceUpdateException: Boto3ClientError
    DeleteConflictException: Boto3ClientError
    IndexNotReadyException: Boto3ClientError
    InternalException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    InvalidAggregationException: Boto3ClientError
    InvalidQueryException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    InvalidResponseException: Boto3ClientError
    InvalidStateTransitionException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MalformedPolicyException: Boto3ClientError
    NotConfiguredException: Boto3ClientError
    RegistrationCodeValidationException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceRegistrationFailureException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    SqlParseException: Boto3ClientError
    TaskAlreadyExistsException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    TransferAlreadyCompletedException: Boto3ClientError
    TransferConflictException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
    VersionConflictException: Boto3ClientError
    VersionsLimitExceededException: Boto3ClientError
