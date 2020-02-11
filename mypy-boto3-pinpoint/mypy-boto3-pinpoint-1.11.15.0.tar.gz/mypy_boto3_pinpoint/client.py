"""
Main interface for pinpoint service client

Usage::

    import boto3
    from mypy_boto3.pinpoint import PinpointClient

    session = boto3.Session()

    client: PinpointClient = boto3.client("pinpoint")
    session_client: PinpointClient = session.client("pinpoint")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_pinpoint.client as client_scope
else:
    client_scope = object
from mypy_boto3_pinpoint.type_defs import (
    ClientCreateAppCreateApplicationRequestTypeDef,
    ClientCreateAppResponseTypeDef,
    ClientCreateCampaignResponseTypeDef,
    ClientCreateCampaignWriteCampaignRequestTypeDef,
    ClientCreateEmailTemplateEmailTemplateRequestTypeDef,
    ClientCreateEmailTemplateResponseTypeDef,
    ClientCreateExportJobExportJobRequestTypeDef,
    ClientCreateExportJobResponseTypeDef,
    ClientCreateImportJobImportJobRequestTypeDef,
    ClientCreateImportJobResponseTypeDef,
    ClientCreateJourneyResponseTypeDef,
    ClientCreateJourneyWriteJourneyRequestTypeDef,
    ClientCreatePushTemplatePushNotificationTemplateRequestTypeDef,
    ClientCreatePushTemplateResponseTypeDef,
    ClientCreateSegmentResponseTypeDef,
    ClientCreateSegmentWriteSegmentRequestTypeDef,
    ClientCreateSmsTemplateResponseTypeDef,
    ClientCreateSmsTemplateSMSTemplateRequestTypeDef,
    ClientCreateVoiceTemplateResponseTypeDef,
    ClientCreateVoiceTemplateVoiceTemplateRequestTypeDef,
    ClientDeleteAdmChannelResponseTypeDef,
    ClientDeleteApnsChannelResponseTypeDef,
    ClientDeleteApnsSandboxChannelResponseTypeDef,
    ClientDeleteApnsVoipChannelResponseTypeDef,
    ClientDeleteApnsVoipSandboxChannelResponseTypeDef,
    ClientDeleteAppResponseTypeDef,
    ClientDeleteBaiduChannelResponseTypeDef,
    ClientDeleteCampaignResponseTypeDef,
    ClientDeleteEmailChannelResponseTypeDef,
    ClientDeleteEmailTemplateResponseTypeDef,
    ClientDeleteEndpointResponseTypeDef,
    ClientDeleteEventStreamResponseTypeDef,
    ClientDeleteGcmChannelResponseTypeDef,
    ClientDeleteJourneyResponseTypeDef,
    ClientDeletePushTemplateResponseTypeDef,
    ClientDeleteSegmentResponseTypeDef,
    ClientDeleteSmsChannelResponseTypeDef,
    ClientDeleteSmsTemplateResponseTypeDef,
    ClientDeleteUserEndpointsResponseTypeDef,
    ClientDeleteVoiceChannelResponseTypeDef,
    ClientDeleteVoiceTemplateResponseTypeDef,
    ClientGetAdmChannelResponseTypeDef,
    ClientGetApnsChannelResponseTypeDef,
    ClientGetApnsSandboxChannelResponseTypeDef,
    ClientGetApnsVoipChannelResponseTypeDef,
    ClientGetApnsVoipSandboxChannelResponseTypeDef,
    ClientGetAppResponseTypeDef,
    ClientGetApplicationDateRangeKpiResponseTypeDef,
    ClientGetApplicationSettingsResponseTypeDef,
    ClientGetAppsResponseTypeDef,
    ClientGetBaiduChannelResponseTypeDef,
    ClientGetCampaignActivitiesResponseTypeDef,
    ClientGetCampaignDateRangeKpiResponseTypeDef,
    ClientGetCampaignResponseTypeDef,
    ClientGetCampaignVersionResponseTypeDef,
    ClientGetCampaignVersionsResponseTypeDef,
    ClientGetCampaignsResponseTypeDef,
    ClientGetChannelsResponseTypeDef,
    ClientGetEmailChannelResponseTypeDef,
    ClientGetEmailTemplateResponseTypeDef,
    ClientGetEndpointResponseTypeDef,
    ClientGetEventStreamResponseTypeDef,
    ClientGetExportJobResponseTypeDef,
    ClientGetExportJobsResponseTypeDef,
    ClientGetGcmChannelResponseTypeDef,
    ClientGetImportJobResponseTypeDef,
    ClientGetImportJobsResponseTypeDef,
    ClientGetJourneyDateRangeKpiResponseTypeDef,
    ClientGetJourneyExecutionActivityMetricsResponseTypeDef,
    ClientGetJourneyExecutionMetricsResponseTypeDef,
    ClientGetJourneyResponseTypeDef,
    ClientGetPushTemplateResponseTypeDef,
    ClientGetSegmentExportJobsResponseTypeDef,
    ClientGetSegmentImportJobsResponseTypeDef,
    ClientGetSegmentResponseTypeDef,
    ClientGetSegmentVersionResponseTypeDef,
    ClientGetSegmentVersionsResponseTypeDef,
    ClientGetSegmentsResponseTypeDef,
    ClientGetSmsChannelResponseTypeDef,
    ClientGetSmsTemplateResponseTypeDef,
    ClientGetUserEndpointsResponseTypeDef,
    ClientGetVoiceChannelResponseTypeDef,
    ClientGetVoiceTemplateResponseTypeDef,
    ClientListJourneysResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTemplateVersionsResponseTypeDef,
    ClientListTemplatesResponseTypeDef,
    ClientPhoneNumberValidateNumberValidateRequestTypeDef,
    ClientPhoneNumberValidateResponseTypeDef,
    ClientPutEventStreamResponseTypeDef,
    ClientPutEventStreamWriteEventStreamTypeDef,
    ClientPutEventsEventsRequestTypeDef,
    ClientPutEventsResponseTypeDef,
    ClientRemoveAttributesResponseTypeDef,
    ClientRemoveAttributesUpdateAttributesRequestTypeDef,
    ClientSendMessagesMessageRequestTypeDef,
    ClientSendMessagesResponseTypeDef,
    ClientSendUsersMessagesResponseTypeDef,
    ClientSendUsersMessagesSendUsersMessageRequestTypeDef,
    ClientTagResourceTagsModelTypeDef,
    ClientUpdateAdmChannelADMChannelRequestTypeDef,
    ClientUpdateAdmChannelResponseTypeDef,
    ClientUpdateApnsChannelAPNSChannelRequestTypeDef,
    ClientUpdateApnsChannelResponseTypeDef,
    ClientUpdateApnsSandboxChannelAPNSSandboxChannelRequestTypeDef,
    ClientUpdateApnsSandboxChannelResponseTypeDef,
    ClientUpdateApnsVoipChannelAPNSVoipChannelRequestTypeDef,
    ClientUpdateApnsVoipChannelResponseTypeDef,
    ClientUpdateApnsVoipSandboxChannelAPNSVoipSandboxChannelRequestTypeDef,
    ClientUpdateApnsVoipSandboxChannelResponseTypeDef,
    ClientUpdateApplicationSettingsResponseTypeDef,
    ClientUpdateApplicationSettingsWriteApplicationSettingsRequestTypeDef,
    ClientUpdateBaiduChannelBaiduChannelRequestTypeDef,
    ClientUpdateBaiduChannelResponseTypeDef,
    ClientUpdateCampaignResponseTypeDef,
    ClientUpdateCampaignWriteCampaignRequestTypeDef,
    ClientUpdateEmailChannelEmailChannelRequestTypeDef,
    ClientUpdateEmailChannelResponseTypeDef,
    ClientUpdateEmailTemplateEmailTemplateRequestTypeDef,
    ClientUpdateEmailTemplateResponseTypeDef,
    ClientUpdateEndpointEndpointRequestTypeDef,
    ClientUpdateEndpointResponseTypeDef,
    ClientUpdateEndpointsBatchEndpointBatchRequestTypeDef,
    ClientUpdateEndpointsBatchResponseTypeDef,
    ClientUpdateGcmChannelGCMChannelRequestTypeDef,
    ClientUpdateGcmChannelResponseTypeDef,
    ClientUpdateJourneyResponseTypeDef,
    ClientUpdateJourneyStateJourneyStateRequestTypeDef,
    ClientUpdateJourneyStateResponseTypeDef,
    ClientUpdateJourneyWriteJourneyRequestTypeDef,
    ClientUpdatePushTemplatePushNotificationTemplateRequestTypeDef,
    ClientUpdatePushTemplateResponseTypeDef,
    ClientUpdateSegmentResponseTypeDef,
    ClientUpdateSegmentWriteSegmentRequestTypeDef,
    ClientUpdateSmsChannelResponseTypeDef,
    ClientUpdateSmsChannelSMSChannelRequestTypeDef,
    ClientUpdateSmsTemplateResponseTypeDef,
    ClientUpdateSmsTemplateSMSTemplateRequestTypeDef,
    ClientUpdateTemplateActiveVersionResponseTypeDef,
    ClientUpdateTemplateActiveVersionTemplateActiveVersionRequestTypeDef,
    ClientUpdateVoiceChannelResponseTypeDef,
    ClientUpdateVoiceChannelVoiceChannelRequestTypeDef,
    ClientUpdateVoiceTemplateResponseTypeDef,
    ClientUpdateVoiceTemplateVoiceTemplateRequestTypeDef,
)


__all__ = ("PinpointClient",)


class PinpointClient:
    """
    [Pinpoint.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.can_paginate)
        """

    def create_app(
        self, CreateApplicationRequest: ClientCreateAppCreateApplicationRequestTypeDef
    ) -> ClientCreateAppResponseTypeDef:
        """
        [Client.create_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.create_app)
        """

    def create_campaign(
        self,
        ApplicationId: str,
        WriteCampaignRequest: ClientCreateCampaignWriteCampaignRequestTypeDef,
    ) -> ClientCreateCampaignResponseTypeDef:
        """
        [Client.create_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.create_campaign)
        """

    def create_email_template(
        self,
        EmailTemplateRequest: ClientCreateEmailTemplateEmailTemplateRequestTypeDef,
        TemplateName: str,
    ) -> ClientCreateEmailTemplateResponseTypeDef:
        """
        [Client.create_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.create_email_template)
        """

    def create_export_job(
        self, ApplicationId: str, ExportJobRequest: ClientCreateExportJobExportJobRequestTypeDef
    ) -> ClientCreateExportJobResponseTypeDef:
        """
        [Client.create_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.create_export_job)
        """

    def create_import_job(
        self, ApplicationId: str, ImportJobRequest: ClientCreateImportJobImportJobRequestTypeDef
    ) -> ClientCreateImportJobResponseTypeDef:
        """
        [Client.create_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.create_import_job)
        """

    def create_journey(
        self, ApplicationId: str, WriteJourneyRequest: ClientCreateJourneyWriteJourneyRequestTypeDef
    ) -> ClientCreateJourneyResponseTypeDef:
        """
        [Client.create_journey documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.create_journey)
        """

    def create_push_template(
        self,
        PushNotificationTemplateRequest: ClientCreatePushTemplatePushNotificationTemplateRequestTypeDef,
        TemplateName: str,
    ) -> ClientCreatePushTemplateResponseTypeDef:
        """
        [Client.create_push_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.create_push_template)
        """

    def create_segment(
        self, ApplicationId: str, WriteSegmentRequest: ClientCreateSegmentWriteSegmentRequestTypeDef
    ) -> ClientCreateSegmentResponseTypeDef:
        """
        [Client.create_segment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.create_segment)
        """

    def create_sms_template(
        self,
        SMSTemplateRequest: ClientCreateSmsTemplateSMSTemplateRequestTypeDef,
        TemplateName: str,
    ) -> ClientCreateSmsTemplateResponseTypeDef:
        """
        [Client.create_sms_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.create_sms_template)
        """

    def create_voice_template(
        self,
        TemplateName: str,
        VoiceTemplateRequest: ClientCreateVoiceTemplateVoiceTemplateRequestTypeDef,
    ) -> ClientCreateVoiceTemplateResponseTypeDef:
        """
        [Client.create_voice_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.create_voice_template)
        """

    def delete_adm_channel(self, ApplicationId: str) -> ClientDeleteAdmChannelResponseTypeDef:
        """
        [Client.delete_adm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_adm_channel)
        """

    def delete_apns_channel(self, ApplicationId: str) -> ClientDeleteApnsChannelResponseTypeDef:
        """
        [Client.delete_apns_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_channel)
        """

    def delete_apns_sandbox_channel(
        self, ApplicationId: str
    ) -> ClientDeleteApnsSandboxChannelResponseTypeDef:
        """
        [Client.delete_apns_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_sandbox_channel)
        """

    def delete_apns_voip_channel(
        self, ApplicationId: str
    ) -> ClientDeleteApnsVoipChannelResponseTypeDef:
        """
        [Client.delete_apns_voip_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_voip_channel)
        """

    def delete_apns_voip_sandbox_channel(
        self, ApplicationId: str
    ) -> ClientDeleteApnsVoipSandboxChannelResponseTypeDef:
        """
        [Client.delete_apns_voip_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_voip_sandbox_channel)
        """

    def delete_app(self, ApplicationId: str) -> ClientDeleteAppResponseTypeDef:
        """
        [Client.delete_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_app)
        """

    def delete_baidu_channel(self, ApplicationId: str) -> ClientDeleteBaiduChannelResponseTypeDef:
        """
        [Client.delete_baidu_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_baidu_channel)
        """

    def delete_campaign(
        self, ApplicationId: str, CampaignId: str
    ) -> ClientDeleteCampaignResponseTypeDef:
        """
        [Client.delete_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_campaign)
        """

    def delete_email_channel(self, ApplicationId: str) -> ClientDeleteEmailChannelResponseTypeDef:
        """
        [Client.delete_email_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_email_channel)
        """

    def delete_email_template(
        self, TemplateName: str, Version: str = None
    ) -> ClientDeleteEmailTemplateResponseTypeDef:
        """
        [Client.delete_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_email_template)
        """

    def delete_endpoint(
        self, ApplicationId: str, EndpointId: str
    ) -> ClientDeleteEndpointResponseTypeDef:
        """
        [Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_endpoint)
        """

    def delete_event_stream(self, ApplicationId: str) -> ClientDeleteEventStreamResponseTypeDef:
        """
        [Client.delete_event_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_event_stream)
        """

    def delete_gcm_channel(self, ApplicationId: str) -> ClientDeleteGcmChannelResponseTypeDef:
        """
        [Client.delete_gcm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_gcm_channel)
        """

    def delete_journey(
        self, ApplicationId: str, JourneyId: str
    ) -> ClientDeleteJourneyResponseTypeDef:
        """
        [Client.delete_journey documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_journey)
        """

    def delete_push_template(
        self, TemplateName: str, Version: str = None
    ) -> ClientDeletePushTemplateResponseTypeDef:
        """
        [Client.delete_push_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_push_template)
        """

    def delete_segment(
        self, ApplicationId: str, SegmentId: str
    ) -> ClientDeleteSegmentResponseTypeDef:
        """
        [Client.delete_segment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_segment)
        """

    def delete_sms_channel(self, ApplicationId: str) -> ClientDeleteSmsChannelResponseTypeDef:
        """
        [Client.delete_sms_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_sms_channel)
        """

    def delete_sms_template(
        self, TemplateName: str, Version: str = None
    ) -> ClientDeleteSmsTemplateResponseTypeDef:
        """
        [Client.delete_sms_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_sms_template)
        """

    def delete_user_endpoints(
        self, ApplicationId: str, UserId: str
    ) -> ClientDeleteUserEndpointsResponseTypeDef:
        """
        [Client.delete_user_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_user_endpoints)
        """

    def delete_voice_channel(self, ApplicationId: str) -> ClientDeleteVoiceChannelResponseTypeDef:
        """
        [Client.delete_voice_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_voice_channel)
        """

    def delete_voice_template(
        self, TemplateName: str, Version: str = None
    ) -> ClientDeleteVoiceTemplateResponseTypeDef:
        """
        [Client.delete_voice_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.delete_voice_template)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.generate_presigned_url)
        """

    def get_adm_channel(self, ApplicationId: str) -> ClientGetAdmChannelResponseTypeDef:
        """
        [Client.get_adm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_adm_channel)
        """

    def get_apns_channel(self, ApplicationId: str) -> ClientGetApnsChannelResponseTypeDef:
        """
        [Client.get_apns_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_apns_channel)
        """

    def get_apns_sandbox_channel(
        self, ApplicationId: str
    ) -> ClientGetApnsSandboxChannelResponseTypeDef:
        """
        [Client.get_apns_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_apns_sandbox_channel)
        """

    def get_apns_voip_channel(self, ApplicationId: str) -> ClientGetApnsVoipChannelResponseTypeDef:
        """
        [Client.get_apns_voip_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_apns_voip_channel)
        """

    def get_apns_voip_sandbox_channel(
        self, ApplicationId: str
    ) -> ClientGetApnsVoipSandboxChannelResponseTypeDef:
        """
        [Client.get_apns_voip_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_apns_voip_sandbox_channel)
        """

    def get_app(self, ApplicationId: str) -> ClientGetAppResponseTypeDef:
        """
        [Client.get_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_app)
        """

    def get_application_date_range_kpi(
        self,
        ApplicationId: str,
        KpiName: str,
        EndTime: datetime = None,
        NextToken: str = None,
        PageSize: str = None,
        StartTime: datetime = None,
    ) -> ClientGetApplicationDateRangeKpiResponseTypeDef:
        """
        [Client.get_application_date_range_kpi documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_application_date_range_kpi)
        """

    def get_application_settings(
        self, ApplicationId: str
    ) -> ClientGetApplicationSettingsResponseTypeDef:
        """
        [Client.get_application_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_application_settings)
        """

    def get_apps(self, PageSize: str = None, Token: str = None) -> ClientGetAppsResponseTypeDef:
        """
        [Client.get_apps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_apps)
        """

    def get_baidu_channel(self, ApplicationId: str) -> ClientGetBaiduChannelResponseTypeDef:
        """
        [Client.get_baidu_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_baidu_channel)
        """

    def get_campaign(self, ApplicationId: str, CampaignId: str) -> ClientGetCampaignResponseTypeDef:
        """
        [Client.get_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_campaign)
        """

    def get_campaign_activities(
        self, ApplicationId: str, CampaignId: str, PageSize: str = None, Token: str = None
    ) -> ClientGetCampaignActivitiesResponseTypeDef:
        """
        [Client.get_campaign_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_activities)
        """

    def get_campaign_date_range_kpi(
        self,
        ApplicationId: str,
        CampaignId: str,
        KpiName: str,
        EndTime: datetime = None,
        NextToken: str = None,
        PageSize: str = None,
        StartTime: datetime = None,
    ) -> ClientGetCampaignDateRangeKpiResponseTypeDef:
        """
        [Client.get_campaign_date_range_kpi documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_date_range_kpi)
        """

    def get_campaign_version(
        self, ApplicationId: str, CampaignId: str, Version: str
    ) -> ClientGetCampaignVersionResponseTypeDef:
        """
        [Client.get_campaign_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_version)
        """

    def get_campaign_versions(
        self, ApplicationId: str, CampaignId: str, PageSize: str = None, Token: str = None
    ) -> ClientGetCampaignVersionsResponseTypeDef:
        """
        [Client.get_campaign_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_versions)
        """

    def get_campaigns(
        self, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> ClientGetCampaignsResponseTypeDef:
        """
        [Client.get_campaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_campaigns)
        """

    def get_channels(self, ApplicationId: str) -> ClientGetChannelsResponseTypeDef:
        """
        [Client.get_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_channels)
        """

    def get_email_channel(self, ApplicationId: str) -> ClientGetEmailChannelResponseTypeDef:
        """
        [Client.get_email_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_email_channel)
        """

    def get_email_template(
        self, TemplateName: str, Version: str = None
    ) -> ClientGetEmailTemplateResponseTypeDef:
        """
        [Client.get_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_email_template)
        """

    def get_endpoint(self, ApplicationId: str, EndpointId: str) -> ClientGetEndpointResponseTypeDef:
        """
        [Client.get_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_endpoint)
        """

    def get_event_stream(self, ApplicationId: str) -> ClientGetEventStreamResponseTypeDef:
        """
        [Client.get_event_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_event_stream)
        """

    def get_export_job(self, ApplicationId: str, JobId: str) -> ClientGetExportJobResponseTypeDef:
        """
        [Client.get_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_export_job)
        """

    def get_export_jobs(
        self, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> ClientGetExportJobsResponseTypeDef:
        """
        [Client.get_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_export_jobs)
        """

    def get_gcm_channel(self, ApplicationId: str) -> ClientGetGcmChannelResponseTypeDef:
        """
        [Client.get_gcm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_gcm_channel)
        """

    def get_import_job(self, ApplicationId: str, JobId: str) -> ClientGetImportJobResponseTypeDef:
        """
        [Client.get_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_import_job)
        """

    def get_import_jobs(
        self, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> ClientGetImportJobsResponseTypeDef:
        """
        [Client.get_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_import_jobs)
        """

    def get_journey(self, ApplicationId: str, JourneyId: str) -> ClientGetJourneyResponseTypeDef:
        """
        [Client.get_journey documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_journey)
        """

    def get_journey_date_range_kpi(
        self,
        ApplicationId: str,
        JourneyId: str,
        KpiName: str,
        EndTime: datetime = None,
        NextToken: str = None,
        PageSize: str = None,
        StartTime: datetime = None,
    ) -> ClientGetJourneyDateRangeKpiResponseTypeDef:
        """
        [Client.get_journey_date_range_kpi documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_journey_date_range_kpi)
        """

    def get_journey_execution_activity_metrics(
        self,
        ApplicationId: str,
        JourneyActivityId: str,
        JourneyId: str,
        NextToken: str = None,
        PageSize: str = None,
    ) -> ClientGetJourneyExecutionActivityMetricsResponseTypeDef:
        """
        [Client.get_journey_execution_activity_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_journey_execution_activity_metrics)
        """

    def get_journey_execution_metrics(
        self, ApplicationId: str, JourneyId: str, NextToken: str = None, PageSize: str = None
    ) -> ClientGetJourneyExecutionMetricsResponseTypeDef:
        """
        [Client.get_journey_execution_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_journey_execution_metrics)
        """

    def get_push_template(
        self, TemplateName: str, Version: str = None
    ) -> ClientGetPushTemplateResponseTypeDef:
        """
        [Client.get_push_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_push_template)
        """

    def get_segment(self, ApplicationId: str, SegmentId: str) -> ClientGetSegmentResponseTypeDef:
        """
        [Client.get_segment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_segment)
        """

    def get_segment_export_jobs(
        self, ApplicationId: str, SegmentId: str, PageSize: str = None, Token: str = None
    ) -> ClientGetSegmentExportJobsResponseTypeDef:
        """
        [Client.get_segment_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_segment_export_jobs)
        """

    def get_segment_import_jobs(
        self, ApplicationId: str, SegmentId: str, PageSize: str = None, Token: str = None
    ) -> ClientGetSegmentImportJobsResponseTypeDef:
        """
        [Client.get_segment_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_segment_import_jobs)
        """

    def get_segment_version(
        self, ApplicationId: str, SegmentId: str, Version: str
    ) -> ClientGetSegmentVersionResponseTypeDef:
        """
        [Client.get_segment_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_segment_version)
        """

    def get_segment_versions(
        self, ApplicationId: str, SegmentId: str, PageSize: str = None, Token: str = None
    ) -> ClientGetSegmentVersionsResponseTypeDef:
        """
        [Client.get_segment_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_segment_versions)
        """

    def get_segments(
        self, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> ClientGetSegmentsResponseTypeDef:
        """
        [Client.get_segments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_segments)
        """

    def get_sms_channel(self, ApplicationId: str) -> ClientGetSmsChannelResponseTypeDef:
        """
        [Client.get_sms_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_sms_channel)
        """

    def get_sms_template(
        self, TemplateName: str, Version: str = None
    ) -> ClientGetSmsTemplateResponseTypeDef:
        """
        [Client.get_sms_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_sms_template)
        """

    def get_user_endpoints(
        self, ApplicationId: str, UserId: str
    ) -> ClientGetUserEndpointsResponseTypeDef:
        """
        [Client.get_user_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_user_endpoints)
        """

    def get_voice_channel(self, ApplicationId: str) -> ClientGetVoiceChannelResponseTypeDef:
        """
        [Client.get_voice_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_voice_channel)
        """

    def get_voice_template(
        self, TemplateName: str, Version: str = None
    ) -> ClientGetVoiceTemplateResponseTypeDef:
        """
        [Client.get_voice_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.get_voice_template)
        """

    def list_journeys(
        self, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> ClientListJourneysResponseTypeDef:
        """
        [Client.list_journeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.list_journeys)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.list_tags_for_resource)
        """

    def list_template_versions(
        self, TemplateName: str, TemplateType: str, NextToken: str = None, PageSize: str = None
    ) -> ClientListTemplateVersionsResponseTypeDef:
        """
        [Client.list_template_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.list_template_versions)
        """

    def list_templates(
        self,
        NextToken: str = None,
        PageSize: str = None,
        Prefix: str = None,
        TemplateType: str = None,
    ) -> ClientListTemplatesResponseTypeDef:
        """
        [Client.list_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.list_templates)
        """

    def phone_number_validate(
        self, NumberValidateRequest: ClientPhoneNumberValidateNumberValidateRequestTypeDef
    ) -> ClientPhoneNumberValidateResponseTypeDef:
        """
        [Client.phone_number_validate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.phone_number_validate)
        """

    def put_event_stream(
        self, ApplicationId: str, WriteEventStream: ClientPutEventStreamWriteEventStreamTypeDef
    ) -> ClientPutEventStreamResponseTypeDef:
        """
        [Client.put_event_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.put_event_stream)
        """

    def put_events(
        self, ApplicationId: str, EventsRequest: ClientPutEventsEventsRequestTypeDef
    ) -> ClientPutEventsResponseTypeDef:
        """
        [Client.put_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.put_events)
        """

    def remove_attributes(
        self,
        ApplicationId: str,
        AttributeType: str,
        UpdateAttributesRequest: ClientRemoveAttributesUpdateAttributesRequestTypeDef,
    ) -> ClientRemoveAttributesResponseTypeDef:
        """
        [Client.remove_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.remove_attributes)
        """

    def send_messages(
        self, ApplicationId: str, MessageRequest: ClientSendMessagesMessageRequestTypeDef
    ) -> ClientSendMessagesResponseTypeDef:
        """
        [Client.send_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.send_messages)
        """

    def send_users_messages(
        self,
        ApplicationId: str,
        SendUsersMessageRequest: ClientSendUsersMessagesSendUsersMessageRequestTypeDef,
    ) -> ClientSendUsersMessagesResponseTypeDef:
        """
        [Client.send_users_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.send_users_messages)
        """

    def tag_resource(self, ResourceArn: str, TagsModel: ClientTagResourceTagsModelTypeDef) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.untag_resource)
        """

    def update_adm_channel(
        self, ADMChannelRequest: ClientUpdateAdmChannelADMChannelRequestTypeDef, ApplicationId: str
    ) -> ClientUpdateAdmChannelResponseTypeDef:
        """
        [Client.update_adm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_adm_channel)
        """

    def update_apns_channel(
        self,
        APNSChannelRequest: ClientUpdateApnsChannelAPNSChannelRequestTypeDef,
        ApplicationId: str,
    ) -> ClientUpdateApnsChannelResponseTypeDef:
        """
        [Client.update_apns_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_apns_channel)
        """

    def update_apns_sandbox_channel(
        self,
        APNSSandboxChannelRequest: ClientUpdateApnsSandboxChannelAPNSSandboxChannelRequestTypeDef,
        ApplicationId: str,
    ) -> ClientUpdateApnsSandboxChannelResponseTypeDef:
        """
        [Client.update_apns_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_apns_sandbox_channel)
        """

    def update_apns_voip_channel(
        self,
        APNSVoipChannelRequest: ClientUpdateApnsVoipChannelAPNSVoipChannelRequestTypeDef,
        ApplicationId: str,
    ) -> ClientUpdateApnsVoipChannelResponseTypeDef:
        """
        [Client.update_apns_voip_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_apns_voip_channel)
        """

    def update_apns_voip_sandbox_channel(
        self,
        APNSVoipSandboxChannelRequest: ClientUpdateApnsVoipSandboxChannelAPNSVoipSandboxChannelRequestTypeDef,
        ApplicationId: str,
    ) -> ClientUpdateApnsVoipSandboxChannelResponseTypeDef:
        """
        [Client.update_apns_voip_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_apns_voip_sandbox_channel)
        """

    def update_application_settings(
        self,
        ApplicationId: str,
        WriteApplicationSettingsRequest: ClientUpdateApplicationSettingsWriteApplicationSettingsRequestTypeDef,
    ) -> ClientUpdateApplicationSettingsResponseTypeDef:
        """
        [Client.update_application_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_application_settings)
        """

    def update_baidu_channel(
        self,
        ApplicationId: str,
        BaiduChannelRequest: ClientUpdateBaiduChannelBaiduChannelRequestTypeDef,
    ) -> ClientUpdateBaiduChannelResponseTypeDef:
        """
        [Client.update_baidu_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_baidu_channel)
        """

    def update_campaign(
        self,
        ApplicationId: str,
        CampaignId: str,
        WriteCampaignRequest: ClientUpdateCampaignWriteCampaignRequestTypeDef,
    ) -> ClientUpdateCampaignResponseTypeDef:
        """
        [Client.update_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_campaign)
        """

    def update_email_channel(
        self,
        ApplicationId: str,
        EmailChannelRequest: ClientUpdateEmailChannelEmailChannelRequestTypeDef,
    ) -> ClientUpdateEmailChannelResponseTypeDef:
        """
        [Client.update_email_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_email_channel)
        """

    def update_email_template(
        self,
        EmailTemplateRequest: ClientUpdateEmailTemplateEmailTemplateRequestTypeDef,
        TemplateName: str,
        CreateNewVersion: bool = None,
        Version: str = None,
    ) -> ClientUpdateEmailTemplateResponseTypeDef:
        """
        [Client.update_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_email_template)
        """

    def update_endpoint(
        self,
        ApplicationId: str,
        EndpointId: str,
        EndpointRequest: ClientUpdateEndpointEndpointRequestTypeDef,
    ) -> ClientUpdateEndpointResponseTypeDef:
        """
        [Client.update_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_endpoint)
        """

    def update_endpoints_batch(
        self,
        ApplicationId: str,
        EndpointBatchRequest: ClientUpdateEndpointsBatchEndpointBatchRequestTypeDef,
    ) -> ClientUpdateEndpointsBatchResponseTypeDef:
        """
        [Client.update_endpoints_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_endpoints_batch)
        """

    def update_gcm_channel(
        self, ApplicationId: str, GCMChannelRequest: ClientUpdateGcmChannelGCMChannelRequestTypeDef
    ) -> ClientUpdateGcmChannelResponseTypeDef:
        """
        [Client.update_gcm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_gcm_channel)
        """

    def update_journey(
        self,
        ApplicationId: str,
        JourneyId: str,
        WriteJourneyRequest: ClientUpdateJourneyWriteJourneyRequestTypeDef,
    ) -> ClientUpdateJourneyResponseTypeDef:
        """
        [Client.update_journey documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_journey)
        """

    def update_journey_state(
        self,
        ApplicationId: str,
        JourneyId: str,
        JourneyStateRequest: ClientUpdateJourneyStateJourneyStateRequestTypeDef,
    ) -> ClientUpdateJourneyStateResponseTypeDef:
        """
        [Client.update_journey_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_journey_state)
        """

    def update_push_template(
        self,
        PushNotificationTemplateRequest: ClientUpdatePushTemplatePushNotificationTemplateRequestTypeDef,
        TemplateName: str,
        CreateNewVersion: bool = None,
        Version: str = None,
    ) -> ClientUpdatePushTemplateResponseTypeDef:
        """
        [Client.update_push_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_push_template)
        """

    def update_segment(
        self,
        ApplicationId: str,
        SegmentId: str,
        WriteSegmentRequest: ClientUpdateSegmentWriteSegmentRequestTypeDef,
    ) -> ClientUpdateSegmentResponseTypeDef:
        """
        [Client.update_segment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_segment)
        """

    def update_sms_channel(
        self, ApplicationId: str, SMSChannelRequest: ClientUpdateSmsChannelSMSChannelRequestTypeDef
    ) -> ClientUpdateSmsChannelResponseTypeDef:
        """
        [Client.update_sms_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_sms_channel)
        """

    def update_sms_template(
        self,
        SMSTemplateRequest: ClientUpdateSmsTemplateSMSTemplateRequestTypeDef,
        TemplateName: str,
        CreateNewVersion: bool = None,
        Version: str = None,
    ) -> ClientUpdateSmsTemplateResponseTypeDef:
        """
        [Client.update_sms_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_sms_template)
        """

    def update_template_active_version(
        self,
        TemplateActiveVersionRequest: ClientUpdateTemplateActiveVersionTemplateActiveVersionRequestTypeDef,
        TemplateName: str,
        TemplateType: str,
    ) -> ClientUpdateTemplateActiveVersionResponseTypeDef:
        """
        [Client.update_template_active_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_template_active_version)
        """

    def update_voice_channel(
        self,
        ApplicationId: str,
        VoiceChannelRequest: ClientUpdateVoiceChannelVoiceChannelRequestTypeDef,
    ) -> ClientUpdateVoiceChannelResponseTypeDef:
        """
        [Client.update_voice_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_voice_channel)
        """

    def update_voice_template(
        self,
        TemplateName: str,
        VoiceTemplateRequest: ClientUpdateVoiceTemplateVoiceTemplateRequestTypeDef,
        CreateNewVersion: bool = None,
        Version: str = None,
    ) -> ClientUpdateVoiceTemplateResponseTypeDef:
        """
        [Client.update_voice_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/pinpoint.html#Pinpoint.Client.update_voice_template)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    MethodNotAllowedException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
