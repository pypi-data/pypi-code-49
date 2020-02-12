"""
Main interface for ses service client

Usage::

    import boto3
    from mypy_boto3.ses import SESClient

    session = boto3.Session()

    client: SESClient = boto3.client("ses")
    session_client: SESClient = session.client("ses")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ses.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ses.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_ses.type_defs import (
    ClientCreateConfigurationSetConfigurationSetTypeDef,
    ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef,
    ClientCreateConfigurationSetTrackingOptionsTrackingOptionsTypeDef,
    ClientCreateReceiptFilterFilterTypeDef,
    ClientCreateReceiptRuleRuleTypeDef,
    ClientCreateTemplateTemplateTypeDef,
    ClientDescribeActiveReceiptRuleSetResponseTypeDef,
    ClientDescribeConfigurationSetResponseTypeDef,
    ClientDescribeReceiptRuleResponseTypeDef,
    ClientDescribeReceiptRuleSetResponseTypeDef,
    ClientGetAccountSendingEnabledResponseTypeDef,
    ClientGetCustomVerificationEmailTemplateResponseTypeDef,
    ClientGetIdentityDkimAttributesResponseTypeDef,
    ClientGetIdentityMailFromDomainAttributesResponseTypeDef,
    ClientGetIdentityNotificationAttributesResponseTypeDef,
    ClientGetIdentityPoliciesResponseTypeDef,
    ClientGetIdentityVerificationAttributesResponseTypeDef,
    ClientGetSendQuotaResponseTypeDef,
    ClientGetSendStatisticsResponseTypeDef,
    ClientGetTemplateResponseTypeDef,
    ClientListConfigurationSetsResponseTypeDef,
    ClientListCustomVerificationEmailTemplatesResponseTypeDef,
    ClientListIdentitiesResponseTypeDef,
    ClientListIdentityPoliciesResponseTypeDef,
    ClientListReceiptFiltersResponseTypeDef,
    ClientListReceiptRuleSetsResponseTypeDef,
    ClientListTemplatesResponseTypeDef,
    ClientListVerifiedEmailAddressesResponseTypeDef,
    ClientPutConfigurationSetDeliveryOptionsDeliveryOptionsTypeDef,
    ClientSendBounceBouncedRecipientInfoListTypeDef,
    ClientSendBounceMessageDsnTypeDef,
    ClientSendBounceResponseTypeDef,
    ClientSendBulkTemplatedEmailDefaultTagsTypeDef,
    ClientSendBulkTemplatedEmailDestinationsTypeDef,
    ClientSendBulkTemplatedEmailResponseTypeDef,
    ClientSendCustomVerificationEmailResponseTypeDef,
    ClientSendEmailDestinationTypeDef,
    ClientSendEmailMessageTypeDef,
    ClientSendEmailResponseTypeDef,
    ClientSendEmailTagsTypeDef,
    ClientSendRawEmailRawMessageTypeDef,
    ClientSendRawEmailResponseTypeDef,
    ClientSendRawEmailTagsTypeDef,
    ClientSendTemplatedEmailDestinationTypeDef,
    ClientSendTemplatedEmailResponseTypeDef,
    ClientSendTemplatedEmailTagsTypeDef,
    ClientTestRenderTemplateResponseTypeDef,
    ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef,
    ClientUpdateConfigurationSetTrackingOptionsTrackingOptionsTypeDef,
    ClientUpdateReceiptRuleRuleTypeDef,
    ClientUpdateTemplateTemplateTypeDef,
    ClientVerifyDomainDkimResponseTypeDef,
    ClientVerifyDomainIdentityResponseTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ses.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SESClient",)


class SESClient:
    """
    [SES.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.can_paginate)
        """

    def clone_receipt_rule_set(self, RuleSetName: str, OriginalRuleSetName: str) -> Dict[str, Any]:
        """
        [Client.clone_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.clone_receipt_rule_set)
        """

    def create_configuration_set(
        self, ConfigurationSet: ClientCreateConfigurationSetConfigurationSetTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.create_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.create_configuration_set)
        """

    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestination: ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.create_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.create_configuration_set_event_destination)
        """

    def create_configuration_set_tracking_options(
        self,
        ConfigurationSetName: str,
        TrackingOptions: ClientCreateConfigurationSetTrackingOptionsTrackingOptionsTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.create_configuration_set_tracking_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.create_configuration_set_tracking_options)
        """

    def create_custom_verification_email_template(
        self,
        TemplateName: str,
        FromEmailAddress: str,
        TemplateSubject: str,
        TemplateContent: str,
        SuccessRedirectionURL: str,
        FailureRedirectionURL: str,
    ) -> None:
        """
        [Client.create_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.create_custom_verification_email_template)
        """

    def create_receipt_filter(
        self, Filter: ClientCreateReceiptFilterFilterTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.create_receipt_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.create_receipt_filter)
        """

    def create_receipt_rule(
        self, RuleSetName: str, Rule: ClientCreateReceiptRuleRuleTypeDef, After: str = None
    ) -> Dict[str, Any]:
        """
        [Client.create_receipt_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.create_receipt_rule)
        """

    def create_receipt_rule_set(self, RuleSetName: str) -> Dict[str, Any]:
        """
        [Client.create_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.create_receipt_rule_set)
        """

    def create_template(self, Template: ClientCreateTemplateTemplateTypeDef) -> Dict[str, Any]:
        """
        [Client.create_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.create_template)
        """

    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.delete_configuration_set)
        """

    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.delete_configuration_set_event_destination)
        """

    def delete_configuration_set_tracking_options(
        self, ConfigurationSetName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set_tracking_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.delete_configuration_set_tracking_options)
        """

    def delete_custom_verification_email_template(self, TemplateName: str) -> None:
        """
        [Client.delete_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.delete_custom_verification_email_template)
        """

    def delete_identity(self, Identity: str) -> Dict[str, Any]:
        """
        [Client.delete_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.delete_identity)
        """

    def delete_identity_policy(self, Identity: str, PolicyName: str) -> Dict[str, Any]:
        """
        [Client.delete_identity_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.delete_identity_policy)
        """

    def delete_receipt_filter(self, FilterName: str) -> Dict[str, Any]:
        """
        [Client.delete_receipt_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.delete_receipt_filter)
        """

    def delete_receipt_rule(self, RuleSetName: str, RuleName: str) -> Dict[str, Any]:
        """
        [Client.delete_receipt_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.delete_receipt_rule)
        """

    def delete_receipt_rule_set(self, RuleSetName: str) -> Dict[str, Any]:
        """
        [Client.delete_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.delete_receipt_rule_set)
        """

    def delete_template(self, TemplateName: str) -> Dict[str, Any]:
        """
        [Client.delete_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.delete_template)
        """

    def delete_verified_email_address(self, EmailAddress: str) -> None:
        """
        [Client.delete_verified_email_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.delete_verified_email_address)
        """

    def describe_active_receipt_rule_set(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeActiveReceiptRuleSetResponseTypeDef:
        """
        [Client.describe_active_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.describe_active_receipt_rule_set)
        """

    def describe_configuration_set(
        self,
        ConfigurationSetName: str,
        ConfigurationSetAttributeNames: List[
            Literal["eventDestinations", "trackingOptions", "deliveryOptions", "reputationOptions"]
        ] = None,
    ) -> ClientDescribeConfigurationSetResponseTypeDef:
        """
        [Client.describe_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.describe_configuration_set)
        """

    def describe_receipt_rule(
        self, RuleSetName: str, RuleName: str
    ) -> ClientDescribeReceiptRuleResponseTypeDef:
        """
        [Client.describe_receipt_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.describe_receipt_rule)
        """

    def describe_receipt_rule_set(
        self, RuleSetName: str
    ) -> ClientDescribeReceiptRuleSetResponseTypeDef:
        """
        [Client.describe_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.describe_receipt_rule_set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.generate_presigned_url)
        """

    def get_account_sending_enabled(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetAccountSendingEnabledResponseTypeDef:
        """
        [Client.get_account_sending_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.get_account_sending_enabled)
        """

    def get_custom_verification_email_template(
        self, TemplateName: str
    ) -> ClientGetCustomVerificationEmailTemplateResponseTypeDef:
        """
        [Client.get_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.get_custom_verification_email_template)
        """

    def get_identity_dkim_attributes(
        self, Identities: List[str]
    ) -> ClientGetIdentityDkimAttributesResponseTypeDef:
        """
        [Client.get_identity_dkim_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.get_identity_dkim_attributes)
        """

    def get_identity_mail_from_domain_attributes(
        self, Identities: List[str]
    ) -> ClientGetIdentityMailFromDomainAttributesResponseTypeDef:
        """
        [Client.get_identity_mail_from_domain_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.get_identity_mail_from_domain_attributes)
        """

    def get_identity_notification_attributes(
        self, Identities: List[str]
    ) -> ClientGetIdentityNotificationAttributesResponseTypeDef:
        """
        [Client.get_identity_notification_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.get_identity_notification_attributes)
        """

    def get_identity_policies(
        self, Identity: str, PolicyNames: List[str]
    ) -> ClientGetIdentityPoliciesResponseTypeDef:
        """
        [Client.get_identity_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.get_identity_policies)
        """

    def get_identity_verification_attributes(
        self, Identities: List[str]
    ) -> ClientGetIdentityVerificationAttributesResponseTypeDef:
        """
        [Client.get_identity_verification_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.get_identity_verification_attributes)
        """

    def get_send_quota(self, *args: Any, **kwargs: Any) -> ClientGetSendQuotaResponseTypeDef:
        """
        [Client.get_send_quota documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.get_send_quota)
        """

    def get_send_statistics(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetSendStatisticsResponseTypeDef:
        """
        [Client.get_send_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.get_send_statistics)
        """

    def get_template(self, TemplateName: str) -> ClientGetTemplateResponseTypeDef:
        """
        [Client.get_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.get_template)
        """

    def list_configuration_sets(
        self, NextToken: str = None, MaxItems: int = None
    ) -> ClientListConfigurationSetsResponseTypeDef:
        """
        [Client.list_configuration_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.list_configuration_sets)
        """

    def list_custom_verification_email_templates(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListCustomVerificationEmailTemplatesResponseTypeDef:
        """
        [Client.list_custom_verification_email_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.list_custom_verification_email_templates)
        """

    def list_identities(
        self,
        IdentityType: Literal["EmailAddress", "Domain"] = None,
        NextToken: str = None,
        MaxItems: int = None,
    ) -> ClientListIdentitiesResponseTypeDef:
        """
        [Client.list_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.list_identities)
        """

    def list_identity_policies(self, Identity: str) -> ClientListIdentityPoliciesResponseTypeDef:
        """
        [Client.list_identity_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.list_identity_policies)
        """

    def list_receipt_filters(
        self, *args: Any, **kwargs: Any
    ) -> ClientListReceiptFiltersResponseTypeDef:
        """
        [Client.list_receipt_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.list_receipt_filters)
        """

    def list_receipt_rule_sets(
        self, NextToken: str = None
    ) -> ClientListReceiptRuleSetsResponseTypeDef:
        """
        [Client.list_receipt_rule_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.list_receipt_rule_sets)
        """

    def list_templates(
        self, NextToken: str = None, MaxItems: int = None
    ) -> ClientListTemplatesResponseTypeDef:
        """
        [Client.list_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.list_templates)
        """

    def list_verified_email_addresses(
        self, *args: Any, **kwargs: Any
    ) -> ClientListVerifiedEmailAddressesResponseTypeDef:
        """
        [Client.list_verified_email_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.list_verified_email_addresses)
        """

    def put_configuration_set_delivery_options(
        self,
        ConfigurationSetName: str,
        DeliveryOptions: ClientPutConfigurationSetDeliveryOptionsDeliveryOptionsTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_delivery_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.put_configuration_set_delivery_options)
        """

    def put_identity_policy(self, Identity: str, PolicyName: str, Policy: str) -> Dict[str, Any]:
        """
        [Client.put_identity_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.put_identity_policy)
        """

    def reorder_receipt_rule_set(self, RuleSetName: str, RuleNames: List[str]) -> Dict[str, Any]:
        """
        [Client.reorder_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.reorder_receipt_rule_set)
        """

    def send_bounce(
        self,
        OriginalMessageId: str,
        BounceSender: str,
        BouncedRecipientInfoList: List[ClientSendBounceBouncedRecipientInfoListTypeDef],
        Explanation: str = None,
        MessageDsn: ClientSendBounceMessageDsnTypeDef = None,
        BounceSenderArn: str = None,
    ) -> ClientSendBounceResponseTypeDef:
        """
        [Client.send_bounce documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.send_bounce)
        """

    def send_bulk_templated_email(
        self,
        Source: str,
        Template: str,
        Destinations: List[ClientSendBulkTemplatedEmailDestinationsTypeDef],
        SourceArn: str = None,
        ReplyToAddresses: List[str] = None,
        ReturnPath: str = None,
        ReturnPathArn: str = None,
        ConfigurationSetName: str = None,
        DefaultTags: List[ClientSendBulkTemplatedEmailDefaultTagsTypeDef] = None,
        TemplateArn: str = None,
        DefaultTemplateData: str = None,
    ) -> ClientSendBulkTemplatedEmailResponseTypeDef:
        """
        [Client.send_bulk_templated_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.send_bulk_templated_email)
        """

    def send_custom_verification_email(
        self, EmailAddress: str, TemplateName: str, ConfigurationSetName: str = None
    ) -> ClientSendCustomVerificationEmailResponseTypeDef:
        """
        [Client.send_custom_verification_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.send_custom_verification_email)
        """

    def send_email(
        self,
        Source: str,
        Destination: ClientSendEmailDestinationTypeDef,
        Message: ClientSendEmailMessageTypeDef,
        ReplyToAddresses: List[str] = None,
        ReturnPath: str = None,
        SourceArn: str = None,
        ReturnPathArn: str = None,
        Tags: List[ClientSendEmailTagsTypeDef] = None,
        ConfigurationSetName: str = None,
    ) -> ClientSendEmailResponseTypeDef:
        """
        [Client.send_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.send_email)
        """

    def send_raw_email(
        self,
        RawMessage: ClientSendRawEmailRawMessageTypeDef,
        Source: str = None,
        Destinations: List[str] = None,
        FromArn: str = None,
        SourceArn: str = None,
        ReturnPathArn: str = None,
        Tags: List[ClientSendRawEmailTagsTypeDef] = None,
        ConfigurationSetName: str = None,
    ) -> ClientSendRawEmailResponseTypeDef:
        """
        [Client.send_raw_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.send_raw_email)
        """

    def send_templated_email(
        self,
        Source: str,
        Destination: ClientSendTemplatedEmailDestinationTypeDef,
        Template: str,
        TemplateData: str,
        ReplyToAddresses: List[str] = None,
        ReturnPath: str = None,
        SourceArn: str = None,
        ReturnPathArn: str = None,
        Tags: List[ClientSendTemplatedEmailTagsTypeDef] = None,
        ConfigurationSetName: str = None,
        TemplateArn: str = None,
    ) -> ClientSendTemplatedEmailResponseTypeDef:
        """
        [Client.send_templated_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.send_templated_email)
        """

    def set_active_receipt_rule_set(self, RuleSetName: str = None) -> Dict[str, Any]:
        """
        [Client.set_active_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.set_active_receipt_rule_set)
        """

    def set_identity_dkim_enabled(self, Identity: str, DkimEnabled: bool) -> Dict[str, Any]:
        """
        [Client.set_identity_dkim_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.set_identity_dkim_enabled)
        """

    def set_identity_feedback_forwarding_enabled(
        self, Identity: str, ForwardingEnabled: bool
    ) -> Dict[str, Any]:
        """
        [Client.set_identity_feedback_forwarding_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.set_identity_feedback_forwarding_enabled)
        """

    def set_identity_headers_in_notifications_enabled(
        self,
        Identity: str,
        NotificationType: Literal["Bounce", "Complaint", "Delivery"],
        Enabled: bool,
    ) -> Dict[str, Any]:
        """
        [Client.set_identity_headers_in_notifications_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.set_identity_headers_in_notifications_enabled)
        """

    def set_identity_mail_from_domain(
        self,
        Identity: str,
        MailFromDomain: str = None,
        BehaviorOnMXFailure: Literal["UseDefaultValue", "RejectMessage"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.set_identity_mail_from_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.set_identity_mail_from_domain)
        """

    def set_identity_notification_topic(
        self,
        Identity: str,
        NotificationType: Literal["Bounce", "Complaint", "Delivery"],
        SnsTopic: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.set_identity_notification_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.set_identity_notification_topic)
        """

    def set_receipt_rule_position(
        self, RuleSetName: str, RuleName: str, After: str = None
    ) -> Dict[str, Any]:
        """
        [Client.set_receipt_rule_position documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.set_receipt_rule_position)
        """

    def test_render_template(
        self, TemplateName: str, TemplateData: str
    ) -> ClientTestRenderTemplateResponseTypeDef:
        """
        [Client.test_render_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.test_render_template)
        """

    def update_account_sending_enabled(self, Enabled: bool = None) -> None:
        """
        [Client.update_account_sending_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.update_account_sending_enabled)
        """

    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestination: ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.update_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.update_configuration_set_event_destination)
        """

    def update_configuration_set_reputation_metrics_enabled(
        self, ConfigurationSetName: str, Enabled: bool
    ) -> None:
        """
        [Client.update_configuration_set_reputation_metrics_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.update_configuration_set_reputation_metrics_enabled)
        """

    def update_configuration_set_sending_enabled(
        self, ConfigurationSetName: str, Enabled: bool
    ) -> None:
        """
        [Client.update_configuration_set_sending_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.update_configuration_set_sending_enabled)
        """

    def update_configuration_set_tracking_options(
        self,
        ConfigurationSetName: str,
        TrackingOptions: ClientUpdateConfigurationSetTrackingOptionsTrackingOptionsTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.update_configuration_set_tracking_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.update_configuration_set_tracking_options)
        """

    def update_custom_verification_email_template(
        self,
        TemplateName: str,
        FromEmailAddress: str = None,
        TemplateSubject: str = None,
        TemplateContent: str = None,
        SuccessRedirectionURL: str = None,
        FailureRedirectionURL: str = None,
    ) -> None:
        """
        [Client.update_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.update_custom_verification_email_template)
        """

    def update_receipt_rule(
        self, RuleSetName: str, Rule: ClientUpdateReceiptRuleRuleTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.update_receipt_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.update_receipt_rule)
        """

    def update_template(self, Template: ClientUpdateTemplateTemplateTypeDef) -> Dict[str, Any]:
        """
        [Client.update_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.update_template)
        """

    def verify_domain_dkim(self, Domain: str) -> ClientVerifyDomainDkimResponseTypeDef:
        """
        [Client.verify_domain_dkim documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.verify_domain_dkim)
        """

    def verify_domain_identity(self, Domain: str) -> ClientVerifyDomainIdentityResponseTypeDef:
        """
        [Client.verify_domain_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.verify_domain_identity)
        """

    def verify_email_address(self, EmailAddress: str) -> None:
        """
        [Client.verify_email_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.verify_email_address)
        """

    def verify_email_identity(self, EmailAddress: str) -> Dict[str, Any]:
        """
        [Client.verify_email_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Client.verify_email_identity)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configuration_sets"]
    ) -> "paginator_scope.ListConfigurationSetsPaginator":
        """
        [Paginator.ListConfigurationSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Paginator.ListConfigurationSets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_verification_email_templates"]
    ) -> "paginator_scope.ListCustomVerificationEmailTemplatesPaginator":
        """
        [Paginator.ListCustomVerificationEmailTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Paginator.ListCustomVerificationEmailTemplates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_identities"]
    ) -> "paginator_scope.ListIdentitiesPaginator":
        """
        [Paginator.ListIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Paginator.ListIdentities)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_receipt_rule_sets"]
    ) -> "paginator_scope.ListReceiptRuleSetsPaginator":
        """
        [Paginator.ListReceiptRuleSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Paginator.ListReceiptRuleSets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_templates"]
    ) -> "paginator_scope.ListTemplatesPaginator":
        """
        [Paginator.ListTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Paginator.ListTemplates)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["identity_exists"]
    ) -> "waiter_scope.IdentityExistsWaiter":
        """
        [Waiter.IdentityExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ses.html#SES.Waiter.IdentityExists)
        """


class Exceptions:
    AccountSendingPausedException: Boto3ClientError
    AlreadyExistsException: Boto3ClientError
    CannotDeleteException: Boto3ClientError
    ClientError: Boto3ClientError
    ConfigurationSetAlreadyExistsException: Boto3ClientError
    ConfigurationSetDoesNotExistException: Boto3ClientError
    ConfigurationSetSendingPausedException: Boto3ClientError
    CustomVerificationEmailInvalidContentException: Boto3ClientError
    CustomVerificationEmailTemplateAlreadyExistsException: Boto3ClientError
    CustomVerificationEmailTemplateDoesNotExistException: Boto3ClientError
    EventDestinationAlreadyExistsException: Boto3ClientError
    EventDestinationDoesNotExistException: Boto3ClientError
    FromEmailAddressNotVerifiedException: Boto3ClientError
    InvalidCloudWatchDestinationException: Boto3ClientError
    InvalidConfigurationSetException: Boto3ClientError
    InvalidDeliveryOptionsException: Boto3ClientError
    InvalidFirehoseDestinationException: Boto3ClientError
    InvalidLambdaFunctionException: Boto3ClientError
    InvalidPolicyException: Boto3ClientError
    InvalidRenderingParameterException: Boto3ClientError
    InvalidS3ConfigurationException: Boto3ClientError
    InvalidSNSDestinationException: Boto3ClientError
    InvalidSnsTopicException: Boto3ClientError
    InvalidTemplateException: Boto3ClientError
    InvalidTrackingOptionsException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MailFromDomainNotVerifiedException: Boto3ClientError
    MessageRejected: Boto3ClientError
    MissingRenderingAttributeException: Boto3ClientError
    ProductionAccessNotGrantedException: Boto3ClientError
    RuleDoesNotExistException: Boto3ClientError
    RuleSetDoesNotExistException: Boto3ClientError
    TemplateDoesNotExistException: Boto3ClientError
    TrackingOptionsAlreadyExistsException: Boto3ClientError
    TrackingOptionsDoesNotExistException: Boto3ClientError
