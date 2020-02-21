from datetime import datetime
from enum import Enum
from pprint import pprint, pformat
from typing import List, Union, Optional, Tuple

import attr
import cutie
import typer
from cerberus import Validator
from halo import Halo

from . import db, utils
from .models import (
    SiteKey,
    CraftDetail,
    DetailDataType,
    craft_type_path_strings,
    CraftTypes,
    TaskStatus,
    TaskTypes,
    task_status_codes,
    TaskDetail,
    task_type_path_strings,
    EventTypes,
    craft_type_codes,
    task_type_codes,
    event_type_codes,
    SiteKeyCompany,
)
from .project import choose_project

app = typer.Typer(help="Manage Stilt Site Keys")
state = {"site_key": ""}


TaskDetailTuple = Tuple[CraftTypes, TaskTypes, str, TaskDetail]


def confirm_and_set_sitekey(yes: bool, site_key: str, updates: dict):
    msg_start = typer.style(
        "You are about to write this data for ", fg=typer.colors.YELLOW
    )
    msg_skey = typer.style(site_key, fg="green", bold=True)
    typer.echo(msg_start + msg_skey + ":")
    pprint(updates)
    confirm_text = typer.style(
        "Are you sure?", fg=typer.colors.BRIGHT_YELLOW, bold=True
    )

    # Handle auto confirm flag.
    if yes:
        is_confirmed = True
    else:
        is_confirmed = typer.confirm(confirm_text)

    if is_confirmed:
        spinner = Halo(text_color="blue")
        spinner.start(f"Creating new {site_key}...")
        try:
            db.set_site_key(site_key=site_key, updates=updates)
            spinner.succeed()
            typer.secho("Update successful!", fg=typer.colors.GREEN, bold=True)
        except Exception as err:
            spinner.fail()
            raise err
    else:
        typer.echo("Exiting. No writes made.")


def confirm_and_set_site_key_company(
    yes: bool, site_key: str, company_id: str, updates: dict
):
    msg_start = typer.style(
        "You are about to write this data for ", fg=typer.colors.YELLOW
    )
    msg_skey = typer.style(site_key, fg="green", bold=True)
    typer.echo(msg_start + msg_skey + ":")
    pprint(f"site_key: {site_key}")
    pprint(f"company_id: {company_id}")
    pprint(updates)
    confirm_text = typer.style(
        "Are you sure?", fg=typer.colors.BRIGHT_YELLOW, bold=True
    )

    # Handle auto confirm flag.
    if yes:
        is_confirmed = True
    else:
        is_confirmed = typer.confirm(confirm_text)

    if is_confirmed:
        spinner = Halo(text_color="blue")
        spinner.start(f"Creating new company {company_id}...")
        try:
            db.set_site_key_company(
                site_key=site_key, site_key_company=company_id, updates=updates
            )
            spinner.succeed()
            typer.secho("Update successful!", fg=typer.colors.GREEN, bold=True)
        except Exception as err:
            spinner.fail()
            raise err
    else:
        typer.echo("Exiting. No writes made.")


def confirm_and_update_sitekey(yes: bool, site_key: str, updates: dict):
    msg_start = typer.style(
        "You are about to write this data for ", fg=typer.colors.YELLOW
    )
    msg_skey = typer.style(site_key, fg="green", bold=True)
    typer.echo(msg_start + msg_skey + ":")
    pprint(updates)
    confirm_text = typer.style(
        "Are you sure?", fg=typer.colors.BRIGHT_YELLOW, bold=True
    )

    # Handle auto confirm flag.
    if yes:
        is_confirmed = True
    else:
        is_confirmed = typer.confirm(confirm_text)

    if is_confirmed:
        spinner = Halo(text_color="blue")
        spinner.start(f"Updating {site_key}...")
        try:
            db.update_site_key(site_key=site_key, updates=updates)
            spinner.succeed()
            typer.secho("Update successful!", fg=typer.colors.GREEN, bold=True)
        except Exception as err:
            spinner.fail()
            raise err
    else:
        typer.echo("Exiting. No writes made.")


@app.command("audit")
def audit_sitekey(
    site_key: str = typer.Option(..., prompt=True),
    skip_project: bool = typer.Option(
        False, "--skip-project", "-s", help="Use previous project if available."
    ),
):
    """Audit a single site key for data errors."""
    spinner = Halo(text_color="blue")
    choose_project(skip=skip_project)
    styled_site_key = typer.style(site_key, fg=typer.colors.YELLOW, bold=True)
    try:
        spinner.start(f"Fetching {site_key}...")
        data = db.get_site_key(site_key)
        spinner.succeed()

        spinner.start(f"Validating data...")
        v = Validator(SiteKey.schema, require_all=True)
        if v.validate(data) is False:
            raise ValueError(pformat(v.errors))
        spinner.succeed()
        status = typer.style("passed", fg=typer.colors.GREEN, bold=True)
        typer.echo(f"{styled_site_key}: {status}")

    except (ValueError, TypeError, db.NotFound) as err:
        spinner.fail("Error!")
        status = typer.style("failed", fg=typer.colors.RED, bold=True)
        typer.echo(f"{styled_site_key}: {status}")
        typer.echo(f"{err}")


@app.command("audit-all")
def audit_all_sitekeys(
    skip_project: bool = typer.Option(
        False, "--skip-project", "-s", help="Use previous project if available."
    )
):
    """Audit all project site keys for data errors."""
    spinner = Halo(text_color="blue")
    choose_project(skip=skip_project)
    spinner.start("Fetching data...")
    data = db.query_all_site_keys()
    spinner.succeed()

    for item in data:
        site_key = item[0]
        styled_site_key = typer.style(site_key, fg=typer.colors.YELLOW, bold=True)
        site_data = item[1]
        try:
            spinner.start(f"Validating {site_key}...")

            v = Validator(SiteKey.schema, require_all=True)
            if v.validate(site_data) is False:
                raise ValueError(pformat(v.errors))

            status = typer.style("passed", fg=typer.colors.GREEN, bold=True)
            spinner.succeed()
            typer.echo(f"{styled_site_key}: {status}")

        except (ValueError, TypeError) as err:
            spinner.fail()
            status = typer.style("failed", fg=typer.colors.RED, bold=True)
            typer.echo(f"{styled_site_key}: {status}")
            typer.echo(f"{err}")


@app.command("create")
def create_site_key(
    site_key_id: str = typer.Option(..., prompt=True),
    yes: bool = typer.Option(
        False, "--yes", "-y", help="Automatically confirm writes."
    ),
    skip_project: bool = typer.Option(
        False, "--skip-project", "-s", help="Use previous project if available."
    ),
    name: str = typer.Option(..., prompt=True),
    timezone: str = typer.Option(..., prompt=True),
    managing_company_id: str = typer.Option(
        ..., prompt=True, help="Used to generate the site key company for the plant."
    ),
    valid_craft_types: List[CraftTypes] = typer.Option(None, case_sensitive=False),
    valid_task_types: List[TaskTypes] = typer.Option(None, case_sensitive=False),
    valid_task_status_codes: List[TaskStatus] = typer.Option(
        None, case_sensitive=False
    ),
    valid_event_types: List[EventTypes] = typer.Option(None, case_sensitive=False),
    company_name: Optional[str] = typer.Option(None),
    company_point_of_contact: Optional[str] = typer.Option(None),
    company_logo_photo_url: Optional[str] = typer.Option(None),
    company_members: Optional[List[str]] = typer.Option(None),
):
    """
    Create a new site key. Customizations can be added after creation using
    add-craft-detail and add-task-detail commands.

    Automatically add the first siteKeyCompany based on managing_company_id.
    """

    # Prompt the user for selections.
    if len(valid_craft_types) == 0:
        valid_craft_types = prompt_select_multiple_from_type_enum_with_all(
            title="Select Craft Types ('ALL' will add all craft types):",
            enum=CraftTypes,
        )
    if len(valid_task_types) == 0:
        valid_task_types = prompt_select_multiple_from_type_enum_with_all(
            title="Select Task Types:", enum=TaskTypes,
        )
    if len(valid_task_status_codes) == 0:
        valid_task_status_codes = prompt_select_multiple_from_type_enum_with_all(
            title="Select Task Status Codes:", enum=TaskStatus,
        )
    if len(valid_event_types) == 0:
        valid_event_types = prompt_select_multiple_from_type_enum_with_all(
            title="Select Event Types:", enum=EventTypes,
        )

    # Convert enum lists to integer codes
    valid_craft_types_ints = [craft_type_codes[e] for e in valid_craft_types]
    valid_task_types_ints = [task_type_codes[e] for e in valid_task_types]
    valid_task_status_codes_ints = [
        task_status_codes[e] for e in valid_task_status_codes
    ]
    valid_event_types_ints = [event_type_codes[e] for e in valid_event_types]

    # validate site key data.
    try:
        site_key = SiteKey(
            name=name,
            timezone=timezone,
            managingCompanyID=managing_company_id,
            validCraftTypes=valid_craft_types_ints,
            validTaskTypes=valid_task_types_ints,
            validTaskStatusCodes=valid_task_status_codes_ints,
            validEventTypes=valid_event_types_ints,
            customizations=dict(),
        )
    except (ValueError, TypeError) as err:
        typer.secho(str(err), fg="red")
        raise typer.Abort()

    # Confirm the Firebase project in use.
    choose_project(skip=skip_project)

    # check if site key already exists
    site_key_exists = db.does_site_key_exist(site_key_id)
    if site_key_exists:
        typer.secho(
            f"The site key {site_key_id} already exists!",
            fg=typer.colors.BRIGHT_RED,
            bold=True,
        )
        raise typer.Abort()

    # confirm and set/create new site key
    confirm_and_set_sitekey(
        yes=yes, site_key=site_key_id, updates=site_key.to_firestore()
    )

    if yes:
        create_new_company(
            yes=yes,
            skip_project=skip_project,
            site_key=site_key_id,
            company_id=managing_company_id,
            name=company_name,
            craft_types=valid_craft_types,
            main_point_of_contact=company_point_of_contact,
            logo_photo_url=company_logo_photo_url,
            members=company_members,
        )
    else:
        confirm_text = typer.style(
            "Would you like to create a site key company from the managingCompanyID?",
            fg=typer.colors.CYAN,
        )
        if typer.confirm(confirm_text):
            create_new_company(
                yes=yes,
                skip_project=skip_project,
                site_key=site_key_id,
                company_id=managing_company_id,
                name=company_name,
                craft_types=valid_craft_types,
                main_point_of_contact=company_point_of_contact,
                logo_photo_url=company_logo_photo_url,
                members=company_members,
            )
    typer.secho("Finished.", fg="green")


@app.command("create-company")
def create_new_company(
    yes: bool = typer.Option(
        False, "--yes", "-y", help="Automatically confirm writes."
    ),
    skip_project: bool = typer.Option(
        False, "--skip-project", "-s", help="Use previous project if available."
    ),
    site_key: str = typer.Option(..., prompt=True),
    company_id: str = typer.Option(..., prompt=True),
    name: str = typer.Option(..., prompt=True),
    craft_types: List[CraftTypes] = typer.Option(None, case_sensitive=False),
    main_point_of_contact: Optional[str] = typer.Option("", prompt=True),
    logo_photo_url: Optional[str] = typer.Option("", prompt=True),
    members: List[str] = typer.Option(None),
) -> SiteKeyCompany:

    # Handle prompting for values if function not invoked from the CLI
    if site_key is None:
        site_key = typer.prompt("Enter the site key", type=str)
    if company_id is None:
        company_id = typer.prompt("Enter the company id", type=str)
    if name is None:
        name = typer.prompt("Enter the company name", type=str)
    if main_point_of_contact is None:
        main_point_of_contact = typer.prompt(
            "Main point of contact", default="", type=str
        )
    if logo_photo_url is None:
        logo_photo_url = typer.prompt("Enter a logo photo url", default="", type=str)

    # prompt for craft types
    if len(craft_types) == 0:
        craft_types = prompt_select_multiple_from_type_enum_with_all(
            title="Select Craft Types ('ALL' will add all craft types):",
            enum=CraftTypes,
        )

    # Make sure members is a list
    if members is None:
        members = list()
    else:
        members = list(members)
    # Add members to company in a separate step.

    # Convert potential empty strings to None
    if main_point_of_contact == "":
        main_point_of_contact = None
    if logo_photo_url == "":
        logo_photo_url = None

    # Convert to integer codes.
    craft_types = [e.code for e in craft_types]
    company = SiteKeyCompany(
        name=name,
        craftTypes=craft_types,
        mainPointOfContact=main_point_of_contact,
        logoPhotoURL=logo_photo_url,
        members=members,
    )

    # Validate
    spinner = Halo(text_color="blue")
    spinner.start(f"Validating data...")
    v = Validator(SiteKeyCompany.schema, require_all=True)
    if v.validate(attr.asdict(company)) is False:
        spinner.fail()
        pprint(v.errors)
        typer.Abort()
    spinner.succeed()

    choose_project(skip=skip_project)

    if db.does_doc_exist(f"siteKeys/{site_key}/siteKeyCompanies/{company_id}"):
        typer.secho(
            f"Company doc already exists!", fg=typer.colors.BRIGHT_RED, bold=True
        )
        raise typer.Abort()

    confirm_and_set_site_key_company(
        yes, site_key=site_key, company_id=company_id, updates=company.to_firestore()
    )

    return company


@app.command()
def add_task_detail(
    site_key: str = typer.Option(..., prompt=True),
    yes: bool = typer.Option(
        False, "--yes", "-y", help="Automatically confirm writes."
    ),
    skip_project: bool = typer.Option(
        False, "--skip-project", "-s", help="Use previous project if available."
    ),
    craft_type: CraftTypes = typer.Option(None, case_sensitive=False),
    task_type: TaskTypes = typer.Option(None, case_sensitive=False),
    detail_name: str = typer.Option(
        ...,
        prompt="Enter the detail path name (e.g. legFootAdded)",
        help="Variable name of the detail",
    ),
    data_type: DetailDataType = typer.Option(..., prompt=True, case_sensitive=False),
    title: str = typer.Option(..., prompt=True),
    default_value=typer.Option(
        "",
        prompt=True,
        help="A number, string, bool, or None (in the case of timestamps)",
    ),
    required: bool = typer.Option(..., prompt=True),
    editable: bool = typer.Option(..., prompt=True),
    min_value: Optional[int] = None,
    max_value: Optional[int] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    on_task_status: List[TaskStatus] = typer.Option(None, case_sensitive=False),
) -> None:
    """Add a new or overwrite a dynamic task specific detail."""
    craft_type_list = list(CraftTypes)
    task_type_list = list(TaskTypes)
    task_status_list = list(TaskStatus)

    if craft_type is None:
        typer.secho("Choose the Craft Type:", bold=True)
        selected = cutie.select([e.name for e in craft_type_list])
        craft_type = craft_type_list[selected]
        print("")

    if task_type is None:
        typer.secho("Choose the Task Type:", bold=True)
        selected = cutie.select([e.name for e in task_type_list])
        task_type = task_type_list[selected]
        print("")

    # Typer seems to create an empty tuple for missing List value.
    if len(on_task_status) == 0:
        typer.secho("Choose the Task Statusi:", bold=True)

        selected = cutie.select_multiple(
            [e.name for e in task_status_list], hide_confirm=True
        )
        on_task_status = [task_status_list[index] for index in selected]

    try:
        # Parse the supplied inputs and prompt for any necessary extras.
        task_detail = _parse_add_task_detail(
            craft_type=craft_type,
            task_type=task_type,
            detail_name=detail_name,
            data_type=data_type,
            title=title,
            default_value=default_value,
            required=required,
            editable=editable,
            min_value=min_value,
            max_value=max_value,
            min_length=min_length,
            max_length=max_length,
            on_task_status=on_task_status,
        )

        # Confirm the Firebase project in use.
        choose_project(skip=skip_project)
        # Check to make sure the site key exists.
        utils.check_site_key_exist(site_key)

        # assemble tuple for update parsing.
        task_detail_tuple = _assemble_task_detail(
            craft_type=craft_type,
            task_type=task_type,
            detail_name=detail_name,
            task_detail=task_detail,
        )

        # generate update dictionary.
        updates = build_task_detail_updates([task_detail_tuple])

        # Confirm and update the database
        confirm_and_update_sitekey(yes, site_key, updates)

    except (ValueError, db.NotFound) as err:
        typer.secho(f"{err}", fg="red")
        raise typer.Abort()


@app.command()
def add_craft_detail(
    site_key: str = typer.Option(..., prompt=True),
    yes: bool = typer.Option(
        False, "--yes", "-y", help="Automatically confirm writes."
    ),
    skip_project: bool = typer.Option(
        False, "--skip-project", "-s", help="Use previous project if available."
    ),
    craft_type: CraftTypes = typer.Option(..., prompt=True, case_sensitive=False),
    detail_name: str = typer.Option(
        ...,
        prompt="Enter the detail path name (e.g. legFootAdded)",
        help="Variable name of the detail",
    ),
    data_type: DetailDataType = typer.Option(..., prompt=True, case_sensitive=False),
    title: str = typer.Option(..., prompt=True),
    default_value=typer.Option(
        "",
        prompt=True,
        help="A number, string, bool, or None (in the case of timestamps)",
    ),
    required: bool = typer.Option(..., prompt=True),
    editable: bool = typer.Option(..., prompt=True),
    min_value: Optional[int] = None,
    max_value: Optional[int] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
) -> None:
    """Add a new or overwrite a dynamic craft detail."""
    try:
        # Parse the supplied inputs and prompt for any necessary extras.
        craft_detail = parse_add_craft_detail(
            craft_type=craft_type,
            detail_name=detail_name,
            data_type=data_type,
            title=title,
            default_value=default_value,
            required=required,
            editable=editable,
            min_value=min_value,
            max_value=max_value,
            min_length=min_length,
            max_length=max_length,
        )

        # Confirm the Firebase project in use.
        choose_project(skip=skip_project)
        # Check to make sure the site key exists.
        utils.check_site_key_exist(site_key)

        craft_tuple = assemble_craft_detail(craft_type, detail_name, craft_detail)
        updates = build_craft_detail_updates([craft_tuple])

        confirm_and_update_sitekey(yes, site_key, updates)

    except (ValueError, db.NotFound) as err:
        typer.secho(f"{err}", fg="red")
        typer.Abort()


def parse_add_craft_detail(
    craft_type: CraftTypes,
    detail_name: str,
    data_type: DetailDataType,
    title: str,
    default_value: Union[str, bool, int, float, datetime],
    required: bool,
    editable: bool,
    min_value: Union[int, float, None] = None,
    max_value: Union[int, float, None] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
) -> CraftDetail:
    """Call user prompts if necessary data was left out."""
    if data_type == DetailDataType.boolean:
        # Convert the string value from the command line to a boolean.
        default_value = utils.convert_string_to_bool(default_value)
        craft_detail = CraftDetail.from_raw_data(
            type=data_type,
            title=title,
            defaultValue=default_value,
            required=required,
            editable=editable,
        )
        return craft_detail
    elif data_type == DetailDataType.number:
        # Convert string from CLI to float.
        default_value = float(default_value)
        if min_value is None:
            min_value = utils.prompt("Please enter the min value", data_type=float)
        if max_value is None:
            max_value = utils.prompt("Please enter the max value", data_type=float)
        craft_detail = CraftDetail.from_raw_data(
            type=data_type,
            title=title,
            defaultValue=default_value,
            required=required,
            editable=editable,
            minValue=min_value,
            maxValue=max_value,
        )
        return craft_detail
    elif data_type == DetailDataType.string:

        if min_length is None:
            min_length = utils.prompt("Please enter the min length", data_type=int)
        if max_length is None:
            max_length = utils.prompt("Please enter the max length", data_type=int)
        craft_detail = CraftDetail.from_raw_data(
            type=data_type,
            title=title,
            defaultValue=default_value,
            required=required,
            editable=editable,
            minLength=min_length,
            maxLength=max_length,
        )
        return craft_detail
    elif data_type == DetailDataType.timestamp:
        # noinspection PyNoneFunctionAssignment
        default_value = utils.convert_string_to_none(default_value)
        craft_detail = CraftDetail.from_raw_data(
            type=data_type,
            title=title,
            defaultValue=default_value,
            required=required,
            editable=editable,
            minLength=min_length,
            maxLength=max_length,
        )
        return craft_detail
    else:
        raise ValueError(f"Unexpected data type for {data_type}")


def _parse_add_task_detail(
    craft_type: CraftTypes,
    task_type: TaskTypes,
    detail_name: str,
    data_type: DetailDataType,
    title: str,
    default_value: Union[str, bool, int, float, datetime],
    required: bool,
    editable: bool,
    min_value: Union[int, float, None] = None,
    max_value: Union[int, float, None] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    on_task_status: List[TaskStatus] = None,
):
    # Lookup integer codes for enum TaskStatus
    if on_task_status is not None:
        on_task_status = [task_status_codes[e] for e in on_task_status]
    """Call user prompts to fill in missing data if necessary."""
    if data_type == DetailDataType.boolean:
        # Convert the string value from the command line to a boolean.
        default_value = utils.convert_string_to_bool(default_value)
        task_detail = TaskDetail.from_raw_data(
            type=data_type,
            title=title,
            defaultValue=default_value,
            required=required,
            editable=editable,
            onTaskStatus=on_task_status,
        )
        return task_detail
    elif data_type == DetailDataType.number:
        # Convert string from CLI to float.
        default_value = float(default_value)
        if min_value is None:
            min_value = utils.prompt("Please enter the min value", data_type=float)
        if max_value is None:
            max_value = utils.prompt("Please enter the max value", data_type=float)
        task_detail = TaskDetail.from_raw_data(
            type=data_type,
            title=title,
            defaultValue=default_value,
            required=required,
            editable=editable,
            minValue=min_value,
            maxValue=max_value,
            onTaskStatus=on_task_status,
        )
        return task_detail
    elif data_type == DetailDataType.string:
        if min_length is None:
            min_length = utils.prompt("Please enter the min length", data_type=int)
        if max_length is None:
            max_length = utils.prompt("Please enter the max length", data_type=int)
        task_detail = TaskDetail.from_raw_data(
            type=data_type,
            title=title,
            defaultValue=default_value,
            required=required,
            editable=editable,
            minLength=min_length,
            maxLength=max_length,
            onTaskStatus=on_task_status,
        )
        return task_detail
    elif data_type == DetailDataType.timestamp:
        # noinspection PyNoneFunctionAssignment
        default_value = utils.convert_string_to_none(default_value)
        task_detail = TaskDetail.from_raw_data(
            type=data_type,
            title=title,
            defaultValue=default_value,
            required=required,
            editable=editable,
            minLength=min_length,
            maxLength=max_length,
            onTaskStatus=on_task_status,
        )
        return task_detail
    else:
        raise ValueError(f"Unexpected data type for {data_type}")
    pass


def assemble_craft_detail(
    craft_type: CraftTypes, detail_name: str, craft_detail: CraftDetail
) -> Tuple[CraftTypes, str, CraftDetail]:
    """
    Check if craft type and detail name are correct data types and return a
    craft tuple
    """
    if isinstance(craft_type, CraftTypes) is False:
        raise ValueError("Expect craft_type to be in CraftTypes enum.")
    if isinstance(detail_name, str) is False:
        raise ValueError("Expected detail_name to be a string.")

    return craft_type, detail_name, craft_detail


def _assemble_task_detail(
    craft_type: CraftTypes,
    task_type: TaskTypes,
    detail_name: str,
    task_detail: TaskDetail,
) -> Tuple[CraftTypes, TaskTypes, str, TaskDetail]:
    """
    Check if craft type, task type, and detail name are correct data types and return
    a task detail tuple.
    """
    if isinstance(craft_type, CraftTypes) is False:
        raise ValueError("Expect craft_type to be in CraftTypes enum.")
    if isinstance(task_type, TaskTypes) is False:
        raise ValueError("Expect task_type to be in TaskTypes enum.")
    if isinstance(detail_name, str) is False:
        raise ValueError("Expected detail_name to be a string.")

    return craft_type, task_type, detail_name, task_detail


def prompt_select_multiple_craft_types() -> List[CraftTypes]:
    """
    Prompt the user to select from a list of available craft types. Return a list
    of the selected craft type enums.
    """
    craft_types = list(CraftTypes)
    craft_types_strings = [e.value for e in craft_types]
    # insert ALL options
    craft_types_strings.insert(0, "ALL")
    typer.secho(
        "Select Craft Types ('ALL' will add all craft types):", fg=typer.colors.MAGENTA
    )
    selected_indexes = cutie.select_multiple(craft_types_strings, hide_confirm=True)
    if 0 in selected_indexes:
        return craft_types
    select_craft_types = [craft_types[index - 1] for index in selected_indexes]
    return select_craft_types


def prompt_select_multiple_from_type_enum_with_all(
    title: str, enum: Enum
) -> List[Enum]:
    """
    Prompt the user to select from a list of available types in an enum. Return a list
    of the selected enums. Needs to be an enum with string values.
    """
    enum_list = list(enum)
    enum_strings = [e.value for e in enum_list]

    # insert ALL options
    enum_strings.insert(0, "ALL")
    typer.secho(title, fg=typer.colors.CYAN)
    selected_indexes = cutie.select_multiple(enum_strings, hide_confirm=True)
    if 0 in selected_indexes:
        return enum_list
    selected_enums = [enum_list[index - 1] for index in selected_indexes]
    return selected_enums


def build_craft_detail_updates(
    data_list: List[Tuple[CraftTypes, str, CraftDetail]]
) -> dict:
    """
    Parse a list of craft detail tuples and return a single dictionary formatted
    for Firestore.
    """
    updates = dict()
    for item in data_list:
        craft_type, detail_name, detail_data = item
        craft_type_path = craft_type_path_strings[craft_type]
        updates[
            f"customizations.craftDetails.{craft_type_path}.{detail_name}"
        ] = detail_data.to_firestore()
    return updates


def build_task_detail_updates(data_list: List[TaskDetailTuple]) -> dict:
    """
    Parse a list of task detail tuples and return a single dictionary formatted
    for Firestore.
    """
    updates = dict()
    for item in data_list:
        craft_type, task_type, detail_name, detail_data = item
        craft_type_path = craft_type_path_strings[craft_type]
        task_type_path = task_type_path_strings[task_type]
        updates[
            f"customizations.taskSpecificDetails.{craft_type_path}.{task_type_path}.{detail_name}"
        ] = detail_data.to_firestore()
    return updates


def main():
    app()


if __name__ == "__main__":
    main()
