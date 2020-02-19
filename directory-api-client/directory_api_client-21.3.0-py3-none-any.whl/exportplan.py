from directory_client_core.authentication import SessionSSOAuthenticator
from directory_api_client.base import AbstractAPIClient


url_exportplan_create = '/exportplan/company-export-plan/'
url_exportplan_update = '/exportplan/company-export-plan/{pk}/'
url_exportplan_detail = '/exportplan/company-export-plan/{pk}/'
url_exportplan_list = '/exportplan/company-export-plan/'


class ExportPlanAPIClient(AbstractAPIClient):
    authenticator = SessionSSOAuthenticator

    def exportplan_update(self, sso_session_id, id, data):
        return self.patch(
            url=url_exportplan_update.format(pk=id), data=data, authenticator=self.authenticator(sso_session_id)
        )

    def exportplan_detail(self, sso_session_id, id):
        return self.get(
            url=url_exportplan_detail.format(pk=id),
            use_fallback_cache=True,
            authenticator=self.authenticator(sso_session_id)
        )

    def exportplan_create(self, sso_session_id, data):
        return self.post(url=url_exportplan_create, data=data, authenticator=self.authenticator(sso_session_id))

    def exportplan_list(self, sso_session_id):
        return self.get(url=url_exportplan_list, authenticator=self.authenticator(sso_session_id))
