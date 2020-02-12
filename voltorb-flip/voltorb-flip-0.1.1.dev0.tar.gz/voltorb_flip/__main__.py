import click


@click.group()
def cli():
    pass


@cli.command()
def new():
    pass


if __name__ == "__main__":
    # pylint: disable=E1120
    cli()
