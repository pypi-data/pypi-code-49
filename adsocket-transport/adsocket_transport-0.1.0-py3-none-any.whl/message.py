import json

__all__ = [
    'Message'
]


class Message:

    channel = None
    channel_id = None
    type = None
    data = None
    kwargs = None
    request_id = None
    _response_data = None

    def __init__(self, type, channel, channel_id=None, data=None):
        self.type = type
        self.data = data or {}
        self.channel = channel
        if channel_id:
            self.channel = "{}:{}".format(self.channel, channel_id)

    def to_json(self):
        data = {
            'type': self.type,
            'data': self._response_data or self.data
        }
        if self.channel:
            data['channel'] = self.channel
        if self.channel_id:
            data['channel_id'] = self.channel_id

        return json.dumps(data)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        return iter(self.data)
