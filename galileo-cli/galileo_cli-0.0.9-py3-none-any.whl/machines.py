import click
import pandas

from galileo_sdk import GalileoSdk
from halo import Halo


def machines_cli(main, galileo: GalileoSdk):
    @main.group()
    def machines():
        """
        Get information about the machines on Galileo or manage your machines.
        """
        pass

    @machines.command()
    @click.argument("index", type=int, required=False)
    @click.option("-m", "--mid", multiple=True, type=str, help="Filter by machine id.")
    @click.option("-u", "--userid", multiple=True, type=str, help="Filter by user id.")
    @click.option("--page", type=int, help="Filter by page number.")
    @click.option(
        "--items", type=int, help="Filter by number of items in the page.",
    )
    @click.option('-n', '--head', type=int, help="Number of items to display.")
    @click.option('-a', '--all', is_flag=True)
    def ls(index, mid, userid, page, items, head, all):
        """
        List all machines on Galileo.
        """
        spinner = Halo("Retrieving machines", spinner="dot")
        spinner.start()
        self = galileo.profiles.self()
        if not all:
            userid += (self["userid"],)

        r = galileo.machines.list_machines(
            mids=list(mid), userids=list(userid), page=page, items=items,
        )

        if not r["machines"]:
            spinner.stop()
            click.echo("No machine matches that query.")
            return

        if isinstance(index, int):
            machines_list = r["machines"][index]
        else:
            machines_list = r["machines"]

        machines_df = pandas.json_normalize(machines_list)
        machines_df = machines_df[
            [
                "name",
                "os",
                "status",
                "mid",
                "userid",
                "arch",
                "cpu",
                "gpu",
                "memory",
                "running_jobs_limit",
            ]
        ]

        spinner.stop()
        if head:
            click.echo(machines_df.head(head))
        else:
            click.echo("(Displaying only first 30 items)\n")
            click.echo(machines_df.head(30))

    @machines.command()
    @click.option(
        "-m",
        "--mid",
        prompt="Machine ID",
        required=True,
        type=str,
        help="Machine's id.",
    )
    def details(mid: str):
        """
        Get details of a single machine based on machine id.
        """
        spinner = Halo("Retrieving machine details", spinner="dot").start()
        r = galileo.machines.get_machines_by_id(mid)
        machines_df = pandas.json_normalize(r)
        machines_df = machines_df[
            [
                "name",
                "os",
                "status",
                "mid",
                "userid",
                "arch",
                "cpu",
                "gpu",
                "memory",
                "running_jobs_limit",
            ]
        ]
        spinner.stop()
        click.echo(machines_df)

    @machines.command()
    @click.option(
        "-m",
        "--mid",
        prompt="Machine ID",
        required=True,
        type=str,
        help="Machine's id.",
    )
    @click.option(
        "-n",
        "--number",
        prompt="Number of concurrent jobs",
        required=True,
        type=int,
        help="The machine's maximum number of concurrent jobs.",
    )
    def update_max_jobs(mid: str, number: int):
        """
        Update the maximum concurrent jobs a machine can run.
        """
        if galileo.machines.update_concurrent_max_jobs(mid, number):
            click.echo(
                f"Successfully updated jobs on machine {mid} with {number} jobs!"
            )
