from .rg_utils import Util


class BaseRequest:

    def __init__(self, request_data: dict):
        self.game_id = Util.get_string_from_dict(request_data, "game_id")
        self.device_id = Util.get_string_from_dict(request_data, "device_id")
        self.player_id = Util.get_string_from_dict(request_data, "player_id")

        self.event_id = Util.get_string_from_dict(request_data, "event_id")

        self.game_version = Util.get_string_from_dict(request_data, "game_version")

        if self.game_id:
            self.game_id = self.game_id.lower()

