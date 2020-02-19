from sixgill.sixgill_request_classes.sixgill_headers_request import SixgillHeadersRequest


class SixgillFeedRequest(SixgillHeadersRequest):
    end_point = None
    method = 'GET'

    def __init__(self, channel_id: str, access_token: str, limit: int, feed_steam: str):
        super(SixgillFeedRequest, self).__init__(channel_id, access_token)
        self.end_point = f'{feed_steam}/ioc'
        self.request.params['limit'] = limit
