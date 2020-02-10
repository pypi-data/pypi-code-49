import click
import json
from datetime import datetime
from .cost_explorer import CostExplorer
from .validator import Validator
from .date_util import DateUtil
from . import constants


@click.command()
@click.option(
    "--debug/--no-debug", default=False, help="enable debug logging. (default: False)"
)
@click.option("--profile", type=str, help="aws profile name.")
@click.option(
    "--granularity",
    "-g",
    type=click.Choice(["DAILY", "MONTHLY"]),
    default="MONTHLY",
    help="granularity. (default: MONTHLY)",
)
@click.option(
    "--point",
    "-p",
    type=int,
    default=constants.DEFAULT_POINT,
    help=f"duration. if granularity is MONTHLY, {constants.DEFAULT_POINT} month ago start. if granularity is DAILY, {constants.DEFAULT_POINT} day ago start. (default: {constants.DEFAULT_POINT})",
)
@click.option(
    "--start",
    callback=Validator.validate_dateformat,
    type=str,
    help=f"range of start day. default is {constants.DEFAULT_POINT} month ago.",
)
@click.option(
    "--end",
    callback=Validator.validate_dateformat,
    type=str,
    default=datetime.today().strftime("%Y-%m-%d"),
    help="range of end day. default is now.",
)
@click.option(
    "--tablefmt",
    "-t",
    type=str,
    default="simple",
    help="tabulate format. (default: simple)",
)
@click.option(
    "--dimensions",
    "-d",
    type=click.Choice(constants.AVAILABLE_DIMENSIONS),
    multiple=True,
    default=["SERVICE"],
    help='group by dimensions. (default: ["SERVICE"])',
)
@click.option(
    "--filter", type=json.loads, help="filter of dimensions. default is no filter."
)
@click.option(
    "--metrics",
    type=click.Choice(constants.AVAILABLE_METRICS),
    default=constants.DEFAULT_METRICS,
    help="metrics. (default: UnblendedCost)",
)
@click.option(
    "--total/--no-total", default=True, help="include total cost. (default: True)"
)
@click.pass_context
def cli(
    ctx, debug, profile, granularity, point, start, end, tablefmt, dimensions, filter, metrics, total
):
    cost_explorer = CostExplorer(
        granularity,
        start or DateUtil.get_start(granularity, point),
        end,
        dimensions=dimensions,
        filter_dimensions=filter,
        metrics=metrics,
        debug=debug,
        profile=profile,
        total=total,
    )
    print(cost_explorer.to_tabulate(tablefmt=tablefmt))


def main():
    cli()
