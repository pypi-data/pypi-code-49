from sixgill.sixgill_request_classes.sixgill_headers_request import SixgillHeadersRequest


class SixgillFeedDigestedRequest(SixgillHeadersRequest):
    end_point = None
    method = 'POST'

    def __init__(self, channel_id: str, access_token: str, feed_steam: str):
        super(SixgillFeedDigestedRequest, self).__init__(channel_id, access_token)
        self.end_point = f'{feed_steam}/ioc/ack'

