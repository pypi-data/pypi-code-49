from pybbucket.request import get


class BitbucketUser:

    def __init__(self, bitbucket, username):
        self.bitbucket = bitbucket
        self.username = username
        self.REQUEST_USERS = self.bitbucket.api_server_url + "2.0/users/"

    def get_user_details(self):
        return get(url=self.REQUEST_USERS + self.username, headers=self.bitbucket.header_content_type_json,
                   description="Get details for the user with username '{}'".format(self.username),
                   credentials=self.bitbucket.credentials)
