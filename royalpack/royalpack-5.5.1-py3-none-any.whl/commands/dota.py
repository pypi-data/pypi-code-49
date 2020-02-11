import asyncio
import logging
import sentry_sdk
import aiohttp
from typing import *
from royalnet.commands import *
from royalnet.utils import *
from royalnet.serf.telegram.escape import escape as tg_escape
from ..tables import Steam, Dota
from ..utils import DotaRank

log = logging.getLogger(__name__)


class DotaCommand(Command):
    name: str = "dota"

    aliases = ["dota2", "doto", "doto2"]

    description: str = "Visualizza le tue statistiche di Dota!"

    syntax: str = ""

    def __init__(self, interface: CommandInterface):
        super().__init__(interface)
        if self.interface.name == "telegram":
            self.loop.create_task(self._updater(900))

    async def _send(self, message):
        client = self.serf.client
        await self.serf.api_call(client.send_message,
                                 chat_id=self.config["Telegram"]["main_group_id"],
                                 text=tg_escape(message),
                                 parse_mode="HTML",
                                 disable_webpage_preview=True)

    @staticmethod
    def _display(dota: Dota) -> str:
        string = f"ℹ️ [b]{dota.steam.persona_name}[/b]\n"

        if dota.rank:
            string += f"{dota.rank}\n"

        string += f"\n" \
                  f"Wins: [b]{dota.wins}[/b]\n" \
                  f"Losses: [b]{dota.losses}[/b]\n" \
                  f"\n"

        return string

    async def _notify(self,
                      obj: Dota,
                      attribute_name: str,
                      old_value: Any,
                      new_value: Any):
        if attribute_name == "wins":
            if old_value is None:
                message = f"↔️ Account {obj} connesso a {obj.steam.user}!"
                await self._send(message)
        elif attribute_name == "rank":
            old_rank: Optional[DotaRank] = old_value
            new_rank: Optional[DotaRank] = new_value
            if new_rank > old_rank:
                message = f"📈 [b]{obj.steam.user}[/b] è salito a [b]{new_value}[/b] su Dota 2! Congratulazioni!"
            elif new_rank < old_rank:
                message = f"📉 [b]{obj.steam.user}[/b] è sceso a [b]{new_value}[/b] su Dota 2."
            else:
                return
            await self._send(message)

    @staticmethod
    async def _change(obj: Dota,
                      attribute_name: str,
                      new_value: Any,
                      callback: Callable[[Dota, str, Any, Any], Awaitable[None]]):
        old_value = obj.__getattribute__(attribute_name)
        if old_value != new_value:
            await callback(obj, attribute_name, old_value, new_value)
        obj.__setattr__(attribute_name, new_value)

    async def _update(self, steam: Steam, db_session):
        log.info(f"Updating: {steam}")
        log.debug(f"Getting player data from OpenDota...")
        async with aiohttp.ClientSession() as session:
            # Get profile data
            async with session.get(f"https://api.opendota.com/api/players/{steam.steamid.as_32}/") as response:
                if response.status != 200:
                    raise ExternalError(f"OpenDota / returned {response.status}!")
                p = await response.json()
                # No such user
                if "profile" not in p:
                    log.debug(f"Not found: {steam}")
                    return
            # Get win/loss data
            async with session.get(f"https://api.opendota.com/api/players/{steam.steamid.as_32}/wl") as response:
                if response.status != 200:
                    raise ExternalError(f"OpenDota /wl returned {response.status}!")
                wl = await response.json()
                # No such user
                if wl["win"] == 0 and wl["lose"] == 0:
                    log.debug(f"Not found: {steam}")
                    return
        # Find the Dota record, if it exists
        dota: Dota = steam.dota
        if dota is None:
            dota = self.alchemy.get(Dota)(steam=steam)
            db_session.add(dota)
            db_session.flush()
        await self._change(dota, "wins", wl["win"], self._notify)
        await self._change(dota, "losses", wl["lose"], self._notify)
        if p["rank_tier"]:
            await self._change(dota, "rank", DotaRank(rank_tier=p["rank_tier"]), self._notify)
        else:
            await self._change(dota, "rank", None, self._notify)

    async def _updater(self, period: int):
        log.info(f"Started updater with {period}s period")
        while True:
            log.info(f"Updating...")
            session = self.alchemy.Session()
            log.info("")
            steams = session.query(self.alchemy.get(Steam)).all()
            for steam in steams:
                try:
                    await self._update(steam, session)
                except Exception as e:
                    sentry_sdk.capture_exception(e)
                    log.error(f"Error while updating {steam.user.username}: {e}")
                await asyncio.sleep(1)
            await asyncify(session.commit)
            session.close()
            log.info(f"Sleeping for {period}s")
            await asyncio.sleep(period)

    async def run(self, args: CommandArgs, data: CommandData) -> None:
        author = await data.get_author(error_if_none=True)

        found_something = False

        message = ""
        for steam in author.steam:
            await self._update(steam, data.session)
            if steam.dota is None:
                continue
            found_something = True
            message += self._display(steam.dota)
            message += "\n"
        if not found_something:
            raise UserError("Nessun account di Dota 2 trovato.")
        await data.reply(message)
