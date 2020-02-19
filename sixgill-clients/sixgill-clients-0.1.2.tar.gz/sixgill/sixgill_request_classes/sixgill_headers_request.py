from sixgill.sixgill_request_classes.sixgill_base_post_auth_request import SixgillBasePostAuthRequest


class SixgillHeadersRequest(SixgillBasePostAuthRequest):

    def __init__(self, channel_id: str, access_token: str):
        super(SixgillHeadersRequest, self).__init__(access_token)

        self.request.headers['X-Channel-Id'] = channel_id
