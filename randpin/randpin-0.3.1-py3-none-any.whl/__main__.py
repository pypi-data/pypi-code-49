import os
import pathlib
import random
import subprocess
import sys

import click
import pinboard


def get_config_path():
    configdir = pathlib.Path(click.get_app_dir('randpin'))
    configdir.mkdir(parents=True, exist_ok=True)

    return configdir / 'apikey.txt'


@click.command()
@click.option('--save/--no-save', default=False,
              help="Save API key to the config file")
@click.argument('apikey', nargs=-1)
@click.pass_context
def cli(ctx, save, apikey):

    if apikey:
        apikey = apikey[0]
    else:
        apikey = None

    if apikey is None:
        apikey = os.environ.get('RANDPIN_APIKEY')

    if apikey is None:

        configpath = get_config_path()

        if not configpath.exists():
            raise click.ClickException("Couldn't find the API key")

        with configpath.open('r') as f:
            apikey = f.read().strip()

        if not apikey:
            raise click.ClickException("Wasn't able to load API key. Try saving again.")

    if save:
        with get_config_path().open('w') as f:
            print(apikey, file=f)

    pb = pinboard.Pinboard(apikey)

    unread = [b for b in pb.posts.all() if b.toread]
    random_unread = random.choice(unread)

    click.echo("Opening: {}".format(random_unread.url))
    returncode = click.launch(random_unread.url)

    ctx.exit(returncode)


def main():
    cli()


if __name__ == '__main__':
    main()
