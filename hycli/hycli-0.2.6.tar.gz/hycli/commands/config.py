import os.path
from pathlib import Path

import click
import toml

from ..commons.endpoints import default_endpoints


@click.command(context_settings=dict(max_content_width=200))
@click.option("--show", "-s", is_flag=True, help="Print configurations.")
@click.pass_context
def config(ctx, show):
    """
    Store configuration values in a file.
    """
    config_file = ctx.obj["config_file"]

    if show:
        # TODO: print properly structured.
        quit(ctx.obj["config"])

    env = ctx.obj["env"] = click.prompt(
        "Enter endpoint environment",
        type=click.Choice(["localhost", "staging", "production"], case_sensitive=False),
        show_choices=True,
        default=ctx.obj.get("env", ""),
    )

    if env == "production" or env == "staging":
        # Production & staging
        username, password = ask_credentials(ctx, env)
        extractor, vat_validation, validation, token = ask_endpoints(
            *default_endpoints[env].values()
        )
    else:
        # Localhost
        username, password = None, None
        extractor, vat_validation, validation, token = ask_endpoints(
            *default_endpoints[env].values()
        )

    Path(os.path.dirname(config_file)).mkdir(parents=True, exist_ok=True)

    if os.path.exists(config_file):
        open_mode = "r+"
    else:
        open_mode = "w+"

    with open(config_file, open_mode) as cfg:
        data = toml.loads(cfg.read())
        data[env] = {
            "username": username,
            "password": password,
            "endpoints": {
                "extractor": extractor,
                "vat_validation": vat_validation,
                "validation": validation,
                "authentication": token,
            },
        }
        cfg.seek(0)
        cfg.write(toml.dumps(data))


def ask_credentials(ctx, env):
    """ Asks API credentials """
    try:
        default_username = ctx.obj["config"][env].get("username", "")
        default_password = ctx.obj["config"][env].get("password", "")
    except (KeyError, AttributeError):
        default_username = ""
        default_password = ""

    username = click.prompt("API username", default=default_username)
    password = click.prompt("API password", default=default_password)

    return username, password


def ask_endpoints(extractor, vat_validation, validation, *token):
    """ Asks environments endpoints """
    extractor = to_none(
        click.prompt("Extractor endpoint", default=extractor if extractor else "",)
    )
    vat_validation = to_none(
        click.prompt(
            "Vat-validation endpoint (optional)",
            default=vat_validation if vat_validation else "",
        )
    )
    validation = to_none(
        click.prompt(
            "Validation endpoint (optional)", default=validation if validation else "",
        )
    )

    if token[0]:
        token = to_none(click.prompt("Authentication endpoint", default=token[0]))
        return extractor, vat_validation, validation, token
    else:
        return extractor, vat_validation, validation, None


def to_none(s):
    """ Convert empty string to None """
    return None if s == "" else str(s)
