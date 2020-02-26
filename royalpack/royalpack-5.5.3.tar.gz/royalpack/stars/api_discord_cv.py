from royalnet.constellation.api import *


class ApiDiscordCvStar(ApiStar):
    path = "/api/discord/cv/v1"

    async def api(self, data: ApiData) -> dict:
        response = await self.interface.call_herald_event("discord", "discord_cv")
        return response
