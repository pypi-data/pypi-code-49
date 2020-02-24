import datetime
from typing import *

import discord
import royalnet.commands as rc
import royalnet.serf.discord as rsd
import royalnet.bard.discord as rbd

from ..utils import RoyalQueue


class DiscordPlayEvent(rc.Event):
    name = "discord_play"

    async def run(self,
                  url: str,
                  guild_id: Optional[int] = None,
                  user: Optional[str] = None,
                  force_color: Optional[int] = None,
                  **kwargs) -> dict:
        if not isinstance(self.serf, rsd.DiscordSerf):
            raise rc.UnsupportedError()

        serf: rsd.DiscordSerf = self.serf
        client: discord.Client = self.serf.client

        # TODO: fix this in Royalnet sometime
        candidate_players: List[rsd.VoicePlayer] = []
        for player in serf.voice_players:
            player: rsd.VoicePlayer
            if not player.voice_client.is_connected():
                continue
            if guild_id is not None:
                guild = client.get_guild(guild_id)
                if guild != player.voice_client.guild:
                    continue
            candidate_players.append(player)

        if len(candidate_players) == 0:
            raise rc.UserError("Il bot non è in nessun canale vocale.\n"
                               "Evocalo prima con [c]summon[/c]!")
        elif len(candidate_players) == 1:
            voice_player = candidate_players[0]
        else:
            raise rc.CommandError("Non so in che Server riprodurre questo file...\n"
                               "Invia il comando su Discord, per favore!")

        ytds = await rbd.YtdlDiscord.from_url(url)
        added: List[rbd.YtdlDiscord] = []
        too_long: List[rbd.YtdlDiscord] = []
        if isinstance(voice_player.playing, RoyalQueue):
            for index, ytd in enumerate(ytds):
                if ytd.info.duration >= datetime.timedelta(seconds=self.config["Play"]["max_song_duration"]):
                    too_long.append(ytd)
                    continue
                await ytd.convert_to_pcm()
                added.append(ytd)
                voice_player.playing.contents.append(ytd)
            if not voice_player.voice_client.is_playing():
                await voice_player.start()
        else:
            raise rc.CommandError(f"Non so come aggiungere musica a [c]{voice_player.playing.__class__.__qualname__}[/c]!")

        main_channel: discord.TextChannel = client.get_channel(self.config["Discord"]["main_channel_id"])

        if len(added) > 0:
            if user:
                await main_channel.send(rsd.escape(f"▶️ {user} ha aggiunto {len(added)} file alla coda:"))
            else:
                await main_channel.send(rsd.escape(f"▶️ Aggiunt{'o' if len(added) == 1 else 'i'} {len(added)} file alla"
                                                   f" coda:"))
        for ytd in added:
            embed: discord.Embed = ytd.embed()
            if force_color:
                embed._colour = discord.Colour(force_color)
            await main_channel.send(embed=embed)

        if len(too_long) > 0:
            if user:
                await main_channel.send(rsd.escape(
                    f"⚠ {len(too_long)} file non {'è' if len(too_long) == 1 else 'sono'}"
                    f" stat{'o' if len(too_long) == 1 else 'i'} scaricat{'o' if len(too_long) == 1 else 'i'}"
                    f" perchè durava{'' if len(too_long) == 1 else 'no'}"
                    f" più di [c]{self.config['Play']['max_song_duration']}[/c] secondi."
                ))

        if len(added) + len(too_long) == 0:
            raise

        return {
            "added": [{
                "title": ytd.info.title,
            } for ytd in added],
            "too_long": [{
                "title": ytd.info.title,
            } for ytd in too_long]
        }
