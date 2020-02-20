import pandas
import click

from galileo_sdk import GalileoSdk


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
    def ls(index, id, username, partialname, wallet, publickey, page, items):
        """
        List of all the profiles.
        """
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
            click.echo("No user matches that query.")
            return

        if isinstance(index, int):
            users_list = r["users"][index]
        else:
            users_list = r["users"]

        users_df = pandas.json_normalize(users_list)
        users_df = users_df[["username", "userid", "mids"]]
        click.echo(users_df)

    @profiles.command()
    def invites():
        """
        Gives a list of all your station invites.
        """
        print(
            pandas.json_normalize(galileo.profiles.list_station_invites()["stations"])
        )
