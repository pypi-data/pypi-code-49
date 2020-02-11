from typing import *
from royalnet.constellation.api import *
import logging


log = logging.getLogger(__name__)


class ApiDiscordPlayStar(ApiStar):
    path = "/api/discord/play/v1"

    async def api(self, data: ApiData) -> dict:
        url = data["url"]
        user = data.get("user")
        guild_id_str = data.get("guild_id")
        if guild_id_str:
            try:
                guild_id: Optional[int] = int(guild_id_str)
            except (ValueError, TypeError):
                raise InvalidParameterError("'guild_id' is not a valid int.")
        log.info(f"Received request to play {url} on guild_id {guild_id} via web")
        response = await self.interface.call_herald_event("discord", "discord_play",
                                                          url=url,
                                                          guild_id=guild_id,
                                                          user=user)
        return response
