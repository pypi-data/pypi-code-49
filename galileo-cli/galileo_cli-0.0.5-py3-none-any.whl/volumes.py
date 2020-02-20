from galileo_sdk import GalileoSdk
import pandas
import click


def volumes_cli(main, galileo: GalileoSdk):
    @main.group()
    def volumes():
        """
        Complete station actions to start your running your first project.
        :return:
        """
        pass

    @volumes.command()
    @click.option(
        "-s",
        "--sid",
        type=str,
        required=True,
        prompt="Station ID",
        help="Filter by station id, can provide multiple options.",
    )
    def ls(sid):
        """
        List volumes.
        """
        r = galileo.stations.list_stations(stationids=[sid])

        if not r["stations"]:
            click.echo("No station matches that query.")
            return

        volumes_list = r["stations"][0]["volumes"]

        volumes_df = pandas.json_normalize(volumes_list)
        volumes_df = volumes_df[
            ["volumeid", "stationid", "name", "host_paths", "access"]
        ]
        click.echo(volumes_df)
