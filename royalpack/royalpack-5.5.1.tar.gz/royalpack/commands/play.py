import discord
import asyncio as aio
from typing import *
from royalnet.commands import *
from royalnet.backpack.tables import User, Discord


class PlayCommand(Command):
    name: str = "play"

    aliases = ["p"]

    description: str = "Aggiunge un url alla coda della chat vocale."

    syntax = "{url}"

    async def get_url(self, args: CommandArgs):
        url = args.joined(require_at_least=1)
        if not (url.startswith("http://") or url.startswith("https://")):
            raise InvalidInputError(f"L'URL specificato non inizia con il nome di un protocollo supportato"
                                    f" ([c]http://[/c] o [c]https://[/c]).")
        return url

    def get_embed_color(self) -> Optional[int]:
        return None

    async def run(self, args: CommandArgs, data: CommandData) -> None:
        if self.interface.name == "discord":
            message: discord.Message = data.message
            guild: discord.Guild = message.guild
            if guild is None:
                guild_id = None
            else:
                guild_id: Optional[int] = guild.id
        else:
            guild_id = None

        user: User = await data.get_author()
        user_str = None

        if user is not None:
            try:
                user_discord: Discord = user.discord[0]
            except (AttributeError, IndexError):
                user_str = str(user)
            else:
                user_str = str(f"<@{user_discord.discord_id}>")

        play_task: aio.Task = self.loop.create_task(
            self.interface.call_herald_event("discord", "discord_play",
                                             url=await self.get_url(args),
                                             guild_id=guild_id,
                                             user=user_str,
                                             force_color=self.get_embed_color())
        )

        await data.reply("⌛ Attendi un attimo...")

        await play_task
