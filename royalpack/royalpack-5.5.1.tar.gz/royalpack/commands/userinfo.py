from typing import *
from royalnet.commands import *
from royalnet.utils import *
from royalnet.backpack.tables import User, Alias
from sqlalchemy import func


class UserinfoCommand(Command):
    name: str = "userinfo"

    aliases = ["uinfo", "ui", "useri"]

    description: str = "Visualizza informazioni su un utente."

    syntax = "[username]"

    async def run(self, args: CommandArgs, data: CommandData) -> None:
        username = args.optional(0)
        if username is None:
            user: User = await data.get_author(error_if_none=True)
        else:
            found: Optional[User] = await asyncify(Alias.find_by_alias, self.alchemy, data.session, username)
            if not found:
                raise InvalidInputError("Utente non trovato.")
            else:
                user = found

        r = [
            f"ℹ️ [b]{user.username}[/b]",
            f"{user.role}",
            "",
        ]

        # Bios are a bit too long
        # if user.bio:
        #     r.append(f"{user.bio}")

        for account in user.telegram:
            r.append(f"{account}")

        for account in user.discord:
            r.append(f"{account}")

        for account in user.steam:
            r.append(f"{account}")
            if account.dota is not None:
                r.append(f"{account.dota}")

        for account in user.leagueoflegends:
            r.append(f"{account}")

        r.append("")

        r.append(f"Ha creato [b]{len(user.diario_created)}[/b] righe di diario, e vi compare in"
                 f" [b]{len(user.diario_quoted)}[/b] righe.")

        r.append("")

        if user.trivia_score:
            r.append(f"Ha [b]{user.trivia_score.score:.0f}[/b] punti trivia, avendo risposto correttamente a"
                     f" [b]{user.trivia_score.correct_answers}[/b] domande su"
                     f" [b]{user.trivia_score.total_answers}[/b].")
            r.append("")

        if user.fiorygi:
            r.append(f"Ha [b]{user.fiorygi}[/b].")
            r.append("")

        await data.reply("\n".join(r))
