from .proto import notification_hub_pb2 as pb


class MessageType:
    MARKETING = 0
    TRANSACTIONAL = 1
    OTP       = 2


class WaterfallMode:
    AUTO = 0
    OVERRIDE = 1


class Platform:
    Aasaanjobs = 1
    OLXPeople = 2


class ClientPlatform:
    ANDROID = 0
    IOS = 1
    WEB = 2


class Waterfall:
    """
    Initiates Waterfall object
    The priority of the channel in the task
    The time offset in seconds after which the notification should be triggered after the previous channel
    """

    def __init__(self, priority: int = 0, offset_time: int = 0):
        self._waterfall = pb.Waterfall()
        self._waterfall.priority = priority
        self._waterfall.offsetTime = offset_time

    @property
    def proto(self) -> pb.Waterfall:
        return self._waterfall
