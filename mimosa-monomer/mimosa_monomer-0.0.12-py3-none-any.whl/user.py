import copy
from pprint import pformat
from typing import List

import attr
import typer
from cerberus import Validator
from halo import Halo

from mimosa.models import (
    SiteKeyUser,
    RootUserDoc,
    SiteKeyUserPrivateDoc,
    SiteKeyLocation,
    SiteKeyUserLocation,
)
from mimosa.presets import user_perm_presets, UserPresets
from mimosa.project import choose_project
from mimosa.validators import CustomValidator, validate_list
from . import db, utils

app = typer.Typer()


@app.command("audit-sk-user")
def audit_site_key_user(
    skip_project: bool = typer.Option(
        False, "--skip-project", "-s", help="Use previous project if available."
    ),
    site_key: str = typer.Option(..., prompt=True),
    uid: str = typer.Option(..., prompt=True),
    # include perms
    # include locations
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

        # todo: fetch permissions
        # todo: validate perms
        # todo: fetch locations
        # todo: validate locations

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

            # todo: fetch permissions
            # todo: validate perms
            # todo: fetch locations
            # todo: validate locations

            status = typer.style("passed", fg=typer.colors.GREEN, bold=True)
            typer.echo(f"{styled_site_key} {styled_uid}: {status}")

        except (TypeError, ValueError) as err:
            spinner.fail("Error!")
            status = typer.style("failed", fg=typer.colors.RED, bold=True)
            typer.echo(f"{styled_site_key} {styled_uid}: {status}")
            typer.echo(f"{err}")


@app.command()
def create_site_admin(
    yes: bool = typer.Option(
        False, "--yes", "-y", help="Automatically confirm writes."
    ),
    skip_project: bool = typer.Option(
        False, "--skip-project", "-s", help="Use previous project if available."
    ),
    uid: str = typer.Option(..., prompt=True),
    site_key: str = typer.Option(..., prompt=True),
    company_id: str = None,
):
    choose_project(skip=skip_project)

    # Fetch the exist root user document from Firestore.
    spinner = Halo(text_color="blue")
    spinner.start(f"Fetching root user {uid} data...")
    try:
        root_user_data = db.get_root_user(uid=uid)
        spinner.succeed()
    except db.NotFound as err:
        spinner.fail()
        typer.secho(f"{err}", fg="red", bold=True)
        raise typer.Abort()

    # Validate the root user document.
    spinner.start("Validating data...")
    v = CustomValidator(RootUserDoc.schema)
    v.validate(root_user_data)
    if v.errors != {}:
        spinner.fail()
        typer.secho(f"Errors in root user data. Please fix first.", fg="red", bold=True)
        # print errors to stdout, nicely formatted.
        typer.echo(f"{pformat(v.errors)}")
        raise typer.Abort()
    spinner.succeed()

    # Create an instance of a RootUserDocument after validating data.
    root_user = RootUserDoc(**v.document)

    # copy root user data into site key user doc
    sk_user = parse_root_user_to_sk_user(root_user)

    # todo: add prompt for site key collection instead of checking if site key exists.

    # Create user permissions/private document
    try:
        sk_user_perms = create_user_permissions(
            UserPresets.SITE_ADMIN, site_key=site_key, company_id=company_id
        )
    except db.NotFound as err:
        typer.secho(str(err), bold=True, fg=typer.colors.RED)
        raise typer.Abort()

    # Get site key locations to generate sk_user locations.
    spinner.start("Fetching site key locations...")
    site_locations = db.query_all_site_locations(site_key)
    spinner.succeed()

    spinner.start("Validating site key locations...")
    errors = validate_list(site_locations, CustomValidator, SiteKeyLocation.schema)
    if errors != {}:
        spinner.fail()
        typer.secho(
            f"Errors in site locations. Please fix first.",
            fg=typer.colors.RED,
            bold=True,
        )
        # print errors to stdout, nicely formatted.
        typer.echo(f"{pformat(errors)}")
        raise typer.Abort()
    spinner.succeed()

    # Convert to site user locations
    spinner.start("Parsing to user locations...")
    try:
        site_locations = [SiteKeyLocation(**item) for item in site_locations]
        site_user_locations = utils.site_locations_to_user_locations(
            site_locations, default_value=True
        )
        spinner.succeed()
    except ValueError as err:
        spinner.fail()
        typer.echo(f"{pformat(errors)}")
        raise typer.Abort()

    # Prompt for confirmation and write data to Firestore
    confirm_and_write_site_admin(
        yes=yes,
        site_key=site_key,
        user=sk_user,
        permissions=sk_user_perms,
        locations=site_user_locations,
    )


@app.command("audit-root-user")
def audit_root_user():
    """Audit a single root user"""

    # todo: develop
    print("Hello Root User'")


@app.callback()
def main_callback():
    """ Module for managing root and site key users."""
    pass


def parse_root_user_to_sk_user(doc: RootUserDoc) -> SiteKeyUser:
    """Convert a root user document into a site key user document

    Prompt for necessary additional information.
    """
    sk_user = SiteKeyUser(
        id=doc.id,
        displayName=doc.displayName,
        companyName=doc.companyName,
        jobTitle=doc.jobTitle,
        email=doc.email,
        department=doc.department,
        phone=doc.phone,
    )
    # validate data.
    v = CustomValidator(SiteKeyUser.schema)
    v.validate(attr.asdict(sk_user))
    if v.errors != {}:
        raise ValueError(f"{pformat(v.errors)}")

    return sk_user


def create_user_permissions(
    preset: UserPresets, site_key: str, company_id: str = None
) -> SiteKeyUserPrivateDoc:
    if type(site_key) != str or len(site_key) == 0:
        raise ValueError("Expected site_key to be a non-empty string.")
    if company_id is None:
        company_id = utils.choose_existing_company_id(site_key)

    preset_perms = copy.deepcopy(user_perm_presets[preset])
    preset_perms["companyID"] = company_id

    v = CustomValidator(SiteKeyUserPrivateDoc.schema)
    v.validate(preset_perms)
    if v.errors != {}:
        raise ValueError(f"{pformat(v.errors)}")

    user_private_doc = SiteKeyUserPrivateDoc(**preset_perms)

    return user_private_doc


def confirm_and_write_site_admin(
    yes: bool,
    site_key: str,
    user: SiteKeyUser,
    permissions: SiteKeyUserPrivateDoc,
    locations: List[SiteKeyUserLocation],
) -> None:
    msg_start = typer.style(
        "You are about to write this data for ", fg=typer.colors.YELLOW
    )
    msg_skey = typer.style(site_key, fg="green", bold=True)
    typer.echo(msg_start + msg_skey + ":")
    confirm_text = typer.style(
        "Are you sure?", fg=typer.colors.BRIGHT_YELLOW, bold=True
    )

    # Display data to user
    if not yes:
        typer.secho(
            f"Site Key User Doc for ID: {user.id}", bold=True, fg=typer.colors.MAGENTA,
        )
        typer.echo(f"{pformat(user.to_firestore())}")

        typer.secho("Permissions Doc", bold=True, fg=typer.colors.MAGENTA)
        typer.echo(f"{pformat(permissions.to_firestore())}")

        typer.secho("User Locations", bold=True, fg=typer.colors.MAGENTA)
        typer.echo(f"{pformat(locations)}")

    # Handle auto confirm flag.
    if yes:
        is_confirmed = True
    else:
        is_confirmed = typer.confirm(confirm_text)

    if is_confirmed:
        spinner = Halo(text_color="blue")
        spinner.start(f"Creating site user {user.id}...")
        try:
            db.set_site_key_user(
                site_key=site_key, uid=user.id, updates=user.to_firestore()
            )
            spinner.succeed()

            spinner.start(f"Setting user permissions...")
            db.set_site_key_user_private_data(
                site_key=site_key, uid=user.id, updates=permissions.to_firestore()
            )
            spinner.succeed()

            for loc in locations:
                spinner.start(f"Setting user location {loc.id}...")
                db.set_site_key_user_location(
                    site_key=site_key,
                    uid=user.id,
                    location_id=loc.id,
                    updates=loc.to_firestore(),
                )
                spinner.succeed()

            typer.secho("Update successful!", fg=typer.colors.GREEN, bold=True)

        except Exception as err:
            spinner.fail()
            raise err
    else:
        typer.echo("Exiting. No writes made.")


def main():

    app()


if __name__ == "__main__":
    main()
