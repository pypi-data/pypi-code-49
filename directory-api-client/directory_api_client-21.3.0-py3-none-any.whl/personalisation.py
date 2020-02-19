from directory_client_core.authentication import SessionSSOAuthenticator
from directory_api_client.base import AbstractAPIClient


url_user_location_create = '/personalisation/user-location/'


class PersonalisationAPIClient(AbstractAPIClient):
    authenticator = SessionSSOAuthenticator

    def user_location_create(self, sso_session_id, data):
        return self.post(url=url_user_location_create, data=data, authenticator=self.authenticator(sso_session_id))
