import asyncclick as click

from bord.config import init_config
from bord.bord import Bord


@click.command()
@click.argument("config_path")
async def bord(config_path: str):
    config = init_config(config_path)
    await Bord(config).start()


def main():
    bord(_anyio_backend="asyncio")


if __name__ == "__main__":
    main()
