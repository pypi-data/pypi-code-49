from sixgill.sixgill_request_classes.sixgill_headers_request import SixgillHeadersRequest


class SixgillAlertsRequest(SixgillHeadersRequest):
    end_point = 'alerts/feed/alerts'
    method = 'GET'

    def __init__(self, channel_id: str, access_token: str, include_delivered_items: bool, bulk_size: int, skip: int,
                 sort_by: str, sort_order: str, is_read: str, severity: str, threat_level: str, threat_type: str):
        super(SixgillAlertsRequest, self).__init__(channel_id, access_token)

        self.request.params['include_delivered_items'] = include_delivered_items
        self.request.params['limit'] = bulk_size
        self.request.params['skip'] = skip
        self.request.params['sort_by'] = sort_by
        self.request.params['sort_order'] = sort_order
        self.request.params['is_read'] = is_read
        self.request.params['severity'] = severity
        self.request.params['threat_level'] = threat_level
        self.request.params['threat_type'] = threat_type

