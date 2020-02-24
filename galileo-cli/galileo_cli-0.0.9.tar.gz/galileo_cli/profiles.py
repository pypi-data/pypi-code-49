import pandas
import click

from galileo_sdk import GalileoSdk
from halo import Halo


def profiles_cli(main, galileo: GalileoSdk):
    @main.group()
    def profiles():
        """
        View other Galileo profiles or your own.
        """

    @profiles.command()
    def self():
        """
        Details of your Galileo profile.
        """
        print(pandas.json_normalize(galileo.profiles.self()))

    @profiles.command()
    @click.argument("index", type=int, required=False)
    @click.option(
        "-i",
        "--id",
        type=str,
        multiple=True,
        help="Filter by userids, can provide multiple options.",
    )
    @click.option(
        "-u",
        "--username",
        type=str,
        multiple=True,
        help="Filter by usernames, can provide multiple options.",
    )
    @click.option(
        "-p",
        "--partialname",
        type=str,
        multiple=True,
        help="Filter by partial usernames, can provide multiple options.",
    )
    @click.option(
        "-w",
        "--wallet",
        type=str,
        multiple=True,
        help="Filter by wallet address, can provide multiple options.",
    )
    @click.option(
        "-k",
        "--publickey",
        type=str,
        multiple=True,
        help="Filter by public key, can provide multiple options.",
    )
    @click.option("--page", type=int, help="Filter by page number.")
    @click.option(
        "--items", type=int, help="Filter by number of items in the page.",
    )
    @click.option('-n', '--head', type=int, help="Number of items to display.")
    def ls(index, id, username, partialname, wallet, publickey, page, items, head):
        """
        List of all the profiles.
        """
        spinner = Halo("Retrieving machines", spinner="dot").start()
        r = galileo.profiles.list_users(
            userids=list(id),
            usernames=list(username),
            partial_usernames=list(partialname),
            wallets=list(wallet),
            public_keys=list(publickey),
            page=page,
            items=items,
        )

        if not r["users"]:
            spinner.stop()
            click.echo("No user matches that query.")
            return

        if isinstance(index, int):
            users_list = r["users"][index]
        else:
            users_list = r["users"]

        users_df = pandas.json_normalize(users_list)
        users_df = users_df[["username", "userid", "mids"]]

        spinner.stop()
        if head:
            click.echo(users_df.head(head))
        else:
            click.echo("(Displaying only first 30 items)\n")
            click.echo(users_df.head(30))

    @profiles.command()
    def invites():
        """
        Gives a list of all your station invites.
        """
        print(
            pandas.json_normalize(galileo.profiles.list_station_invites()["stations"])
        )
