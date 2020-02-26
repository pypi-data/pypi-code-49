from typing import *
import royalnet
import royalnet.commands as rc
import royalnet.serf.telegram as rt
from royalnet.backpack.tables import Alias
from ..tables import Fiorygi, FiorygiTransaction


class MagickfiorygiCommand(rc.Command):
    name: str = "magickfiorygi"

    description: str = "Crea fiorygi dal nulla."

    syntax: str = "{destinatario} {quantità} {motivo}"

    async def run(self, args: rc.CommandArgs, data: rc.CommandData) -> None:
        author = await data.get_author(error_if_none=True)
        if author.role != "Admin":
            raise rc.UserError("Non hai permessi sufficienti per eseguire questo comando.")

        user_arg = args[0]
        qty_arg = args[1]
        reason_arg = " ".join(args[2:])

        if user_arg is None:
            raise rc.InvalidInputError("Non hai specificato un destinatario!")
        user = await Alias.find_user(self.alchemy, data.session, user_arg)
        if user is None:
            raise rc.InvalidInputError("L'utente specificato non esiste!")

        if qty_arg is None:
            raise rc.InvalidInputError("Non hai specificato una quantità!")
        try:
            qty = int(qty_arg)
        except ValueError:
            raise rc.InvalidInputError("La quantità specificata non è un numero!")
        if qty == 0:
            raise rc.InvalidInputError("La quantità non può essere 0!")

        if reason_arg == "":
            raise rc.InvalidInputError("Non hai specificato un motivo!")

        transaction = self.alchemy.get(FiorygiTransaction)(
            user_id=user.uid,
            change=qty,
            reason=reason_arg
        )
        data.session.add(transaction)
        user.fiorygi.fiorygi += qty
        await data.session_commit()

        if len(user.telegram) > 0:
            user_str = user.telegram[0].mention()
        else:
            user_str = user.username

        if qty > 0:
            msg = f"💰 [b]{user_str}[/b] ha ottenuto [b]{qty}[/b] fioryg{'i' if qty != 1 else ''} per [i]{reason_arg}[/i]!"
        else:
            msg = f"💸 [b]{user_str}[/b] ha perso [b]{-qty}[/b] fioryg{'i' if qty != -1 else ''} per [i]{reason_arg}[/i]."

        client = self.serf.client
        await self.serf.api_call(client.send_message,
                                 chat_id=self.config["Telegram"]["main_group_id"],
                                 text=rt.escape(msg),
                                 parse_mode="HTML",
                                 disable_webpage_preview=True)
