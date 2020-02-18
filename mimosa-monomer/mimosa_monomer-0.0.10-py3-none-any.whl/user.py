from pprint import pformat

import typer
from cerberus import Validator
from halo import Halo

from mimosa.models import SiteKeyUser
from mimosa.project import choose_project
from . import db

app = typer.Typer()


@app.command("audit-sk-user")
def audit_site_key_user(
    skip_project: bool = typer.Option(
        False, "--skip-project", "-s", help="Use previous project if available."
    ),
    site_key: str = typer.Option(..., prompt=True),
    uid: str = typer.Option(..., prompt=True),
):
    """Audit a single site key user"""
    spinner = Halo(text_color="blue")
    choose_project(skip=skip_project)
    styled_site_key = typer.style(site_key, bold=True)
    styled_uid = typer.style(uid, fg=typer.colors.YELLOW, bold=True)
    try:
        spinner.start(f"Fetching {uid} doc...")
        user_data = db.get_sk_user(site_key, uid)
        spinner.succeed()

        spinner.start(f"Validating data...")
        v = Validator(SiteKeyUser.schema)
        if v.validate(user_data) is False:
            raise ValueError(pformat(v.errors))
        spinner.succeed()
        user = SiteKeyUser(**user_data)

        status = typer.style("passed", fg=typer.colors.GREEN, bold=True)
        typer.echo(f"{styled_site_key} {styled_uid}: {status}")

        return user

    except (TypeError, ValueError, db.NotFound) as err:
        spinner.fail("Error!")
        status = typer.style("failed", fg=typer.colors.RED, bold=True)
        typer.echo(f"{styled_site_key} {styled_uid}: {status}")
        typer.echo(f"{err}")


@app.command("audit-all-sk-users")
def audit_all_site_key_users(
    skip_project: bool = typer.Option(
        False, "--skip-project", "-s", help="Use previous project if available."
    ),
    site_key: str = typer.Option(..., prompt=True),
):
    """Audit all site key users"""
    spinner = Halo(text_color="blue")
    choose_project(skip=skip_project)
    styled_site_key = typer.style(site_key, bold=True)

    spinner.start(f"Fetching data...")
    users = db.query_all_sk_users(site_key)
    spinner.succeed()
    for user in users:
        uid = user[0]
        user_data = user[1]

        styled_uid = typer.style(uid, fg=typer.colors.YELLOW, bold=True)
        try:
            spinner.start(f"Validating data...")
            v = Validator(SiteKeyUser.schema)
            if v.validate(user_data) is False:
                raise ValueError(pformat(v.errors))
            spinner.succeed()

            status = typer.style("passed", fg=typer.colors.GREEN, bold=True)
            typer.echo(f"{styled_site_key} {styled_uid}: {status}")

        except (TypeError, ValueError) as err:
            spinner.fail("Error!")
            status = typer.style("failed", fg=typer.colors.RED, bold=True)
            typer.echo(f"{styled_site_key} {styled_uid}: {status}")
            typer.echo(f"{err}")


@app.command("audit-root-user")
def audit_root_user():
    """Audit a single root user"""

    # todo: develop
    print("Hello Root User'")


@app.callback()
def main_callback():
    """ Module for managing root and site key users."""
    pass


def main():

    app()


if __name__ == "__main__":
    main()
