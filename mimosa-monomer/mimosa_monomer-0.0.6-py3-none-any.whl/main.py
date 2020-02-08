import sys
import time
from enum import Enum

import cutie
import typer
from halo import Halo

from . import sitekey

app = typer.Typer(no_args_is_help=True, help="The Awesome Stilt Admin CLI")
state = {"verbose": False}

app.add_typer(sitekey.app, name="sitekey")

existing_usernames = ["rick", "morty"]


class NeuralNetwork(Enum):
    simple = "simple"
    conv = "conv"
    lstm = "lstm"


@app.command(help="What's this?")
def neural(
    network: NeuralNetwork = typer.Option(
        NeuralNetwork.simple.value, case_sensitive=False
    ),
):
    spinner = Halo(text_color="yellow")
    spinner.start(f"Training a neural network of type: {network.value}")
    time.sleep(10)
    spinner.succeed()
    typer.secho("Was it worth it?", fg=typer.colors.BRIGHT_CYAN, bold=True)


@app.command(help="Awww yeah!")
def happy_birthday():
    while True:
        text = typer.style("Kat, is it your birthday?", bold=True)
        answer = cutie.prompt_yes_or_no(text)
        if answer is True:
            typer.secho(
                "Aww yeah, let's set this up!", fg=typer.colors.MAGENTA, bold=True
            )
            break
        else:
            typer.echo("Nope! Try again.")

    typer.secho("Which of these is true? Kat is...:", bold=True)
    print()
    options = [
        "Awesome",
        "Smart",
        "Attractive",
        "Funny",
        "Kind",
    ]
    cutie.select_multiple(options, minimal_count=5)

    pause = lambda: time.sleep(0.2)
    one = "🔥🚲💏🔥🚲💏🔥🚲💏🔥🚲💏🔥🚲💏"
    two = "🎉🎂🍦🎉🎂🍦🎉🎂🍦🎉🎂🍦🎉🎂🍦"
    three = "😀💌💯🌲😀💌💯🌲😀💌💯🌲😀💌💯"
    i = 0
    while i < 20:
        print(one, end="")
        pause()
        sys.stdout.write("\033[2K\033[1G")
        print(two, end="\r")
        pause()
        sys.stdout.write("\033[2K\033[1G")
        print(three, end="\r")
        pause()
        sys.stdout.write("\033[2K\033[1G")
        i += 1

    typer.secho("HAPPY BIRTHDAY KAT! <3", fg=typer.colors.GREEN, bold=True)


@app.command()
def delete(
    force: bool = typer.Option(
        False,
        "--force",
        prompt="Are you sure you want to delete ALL the things?",
        help="Force deletion without confirmation",
    ),
):
    """A Test to delete all the things."""
    if force:
        typer.secho("EVERYTHING IS BEING DELETED", fg="red", bold=True)
    else:
        typer.secho("Ok, whew. That was close.", fg="bright_blue")


@app.callback()
def main_callback(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Not yet implemented."),
):
    if verbose:
        typer.echo("Verbose output enabled.")
        state["verbose"] = True


def main():
    app()


if __name__ == "__main__":
    main()
