import click
from halo import Halo

from .. import convert_to_xlsx, Services


@click.command(context_settings=dict(max_content_width=200))
@click.argument("path", type=click.Path(exists=True))
@click.option("-w", "--workers", default=6, show_default=True, help="amount of workers")
@click.pass_context
def to_xlsx(ctx, path, workers):
    """ Convert invoice to xlsx """
    # Services available
    spinner = Halo(spinner="dots")
    spinner.start()
    Services(ctx)
    spinner.succeed(f"Found dir: {path}\n ")

    endpoints = ctx.obj["config"]["endpoints"]

    # Conversion
    convert_to_xlsx(
        path,
        endpoints["extractor"],
        None if "vat_validation" not in endpoints else endpoints["vat_validation"],
        None if "validation" not in endpoints else endpoints["validation"],
        ctx.obj["token"],
        workers,
    )
    spinner.succeed("Converted invoice(s) to xlsx")
