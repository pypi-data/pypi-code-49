import time
from datetime import datetime
from pathlib import Path
from typing import List

import typer

app = typer.Typer()


@app.command()
def create_user(
    name: str,
    age: int = typer.Option(20, min=18, max=70),
    points: float = typer.Option(0, min=0, max=100),
):
    """Test - create a new user"""
    typer.echo(f"name: {name}, age: {age}, points {points:0.2f}")


@app.command()
def check_time(birth: datetime):
    """Testing datetime input"""
    typer.echo(f"Interesting day to be born: {birth}")
    typer.echo(f"Birth hour: {birth.hour}")


@app.command()
def progress_test(name: List[str]):
    """Testing progress bar"""

    with typer.progressbar(name, label="Processing") as progress:
        for item in progress:
            # typer.echo(f"Name is {item}")
            time.sleep(1)


@app.command()
def config_test():
    APP_NAME = "my-super-cli-app"
    app_dir = typer.get_app_dir(APP_NAME)
    config_path: Path = Path(app_dir) / "config.json"
    if not config_path.is_file():
        typer.echo("Config file doesn't exist yet")
    print(app_dir)


@app.command()
def launch_test():
    typer.echo("Opening browser")
    typer.launch("https://typer.tiangolo.com")
