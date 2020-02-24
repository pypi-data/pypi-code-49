from typing import *
from royalnet.commands import *
from royalnet.utils import *
from ..tables.steam import Steam
import steam
import datetime


class SteampoweredCommand(Command):
    name: str = "steampowered"

    description: str = "Connetti il tuo account di Steam!"

    syntax: str = "{profile_url}"

    def __init__(self, interface: CommandInterface):
        super().__init__(interface)
        if "Steam" not in self.config or "web_api_key" not in self.config["Steam"]:
            raise ConfigurationError("[c]Steam.web_api_key[/c] config option is missing!")
        self._api = steam.WebAPI(self.config["Steam"]["web_api_key"])

    def _display(self, account: Steam):
        string = f"ℹ️ [b]{account.persona_name}[/b]\n" \
                 f"{account.profile_url}\n" \
                 f"\n" \
                 f"SteamID: [c]{account.steamid.as_32}[/c]\n" \
                 f"SteamID2: [c]{account.steamid.as_steam2}[/c]\n" \
                 f"SteamID3: [c]{account.steamid.as_steam3}[/c]\n" \
                 f"SteamID64: [c]{account.steamid.as_64}[/c]\n" \
                 f"\n" \
                 f"Created on: [b]{account.account_creation_date}[/b]\n"
        return string

    async def _update(self, account: Steam):
        response = await asyncify(self._api.ISteamUser.GetPlayerSummaries_v2, steamids=account._steamid)
        r = response["response"]["players"][0]
        account.persona_name = r["personaname"]
        account.profile_url = r["profileurl"]
        account.avatar = r["avatar"]
        account.primary_clan_id = r["primaryclanid"]
        account.account_creation_date = datetime.datetime.fromtimestamp(r["timecreated"])

    async def run(self, args: CommandArgs, data: CommandData) -> None:
        author = await data.get_author()
        if len(args) > 0:
            url = args.joined()
            steamid64 = await asyncify(steam.steamid.steam64_from_url, url)
            response = await asyncify(self._api.ISteamUser.GetPlayerSummaries_v2, steamids=steamid64)
            r = response["response"]["players"][0]
            steam_account = self.alchemy.get(Steam)(
                user=author,
                _steamid=int(steamid64),
                persona_name=r["personaname"],
                profile_url=r["profileurl"],
                avatar=r["avatarfull"],
                primary_clan_id=r["primaryclanid"],
                account_creation_date=datetime.datetime.fromtimestamp(r["timecreated"])
            )
            data.session.add(steam_account)
            await data.session_commit()
            await data.reply(f"↔️ Account {steam_account} connesso a {author}!")
        else:
            # Update and display the Steam info for the current account
            if len(author.steam) == 0:
                raise UserError("Nessun account di Steam trovato.")
            message = ""
            for account in author.steam:
                await self._update(account)
                message += self._display(account)
                message += "\n"
            await data.session_commit()
            await data.reply(message)
