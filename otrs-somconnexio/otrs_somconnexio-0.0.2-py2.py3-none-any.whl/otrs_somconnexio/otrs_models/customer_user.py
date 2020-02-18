from otrs_somconnexio.user_management_client.client import UserManagementClient


class CustomerUser:
    def __init__(self, id, client=UserManagementClient):
        self.id = id
        self.client = client

    def change_language(self, lang):
        self.client.set_preference(
            'UserLanguage',
            self.id,
            lang
        )
