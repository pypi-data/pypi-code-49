import click

from pathlib import Path
from tubex import mp3


class Logger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        click.echo(msg)


class Config:
    def __init__(self):
        self.outdir = None
        self.opts = {
            "logger": Logger(),
            "restrictfilenames": True,
            "ignoreerrors": True,
        }


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option("--outdir")
@click.option("--username")
@click.option("--password")
@pass_config
def cli(config, outdir, username, password):
    if outdir is None:
        outdir = Path.cwd() / "tubex_out"
    config.outdir = str(Path(outdir))
    click.echo(f"Output directory: {config.outdir}")
    if username:
        config.opts["username"] = username
    if password:
        config.opts["password"] = password


@cli.command()
@click.option("--album", default="tubex", required=False)
@click.option("--artist", default="tubex", required=False)
@click.argument("url")
@pass_config
def download_mp3(config, url, album, artist):
    config.opts.update(
        {
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "outtmpl": f"{config.outdir}/%(title)s.%(ext)s",
        }
    )
    click.echo(f"Downloading mp3 from {url}")
    mp3.download(opts=config.opts, album=album, artist=artist, tube_url=url)
    exit(0)


@cli.command()
@click.argument("url")
@pass_config
def download_oreilly(config, url):
    import youtube_dl

    config.opts.update(
        {
            "format": "best[tbr<=1000]/worst[[height>=720]]/best[[height<720]]",
            "outtmpl": f"{config.outdir}/%(playlist_title)s/%(playlist_index)s-%(title)s.%(ext)s",
        }
    )
    with youtube_dl.YoutubeDL(config.opts) as ydl:
        click.echo("Downloading...")
        ydl.download([url])
        exit(0)
