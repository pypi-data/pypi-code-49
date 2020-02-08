from datetime import datetime
from pprint import pprint
from typing import List, Union, Optional, Tuple, Any, TypeVar

import cutie
import typer
from halo import Halo

from .project import choose_project
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
)

app = typer.Typer(help="Manage Stilt Site Keys")
state = {"site_key": ""}


TaskDetailTuple = Tuple[CraftTypes, TaskTypes, str, TaskDetail]


def _confirm_and_update_sitekey(yes: bool, site_key: str, updates: dict):
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
        check_sitekey(**data)
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
            check_sitekey(**site_data)
            status = typer.style("passed", fg=typer.colors.GREEN, bold=True)
            spinner.succeed()
            typer.echo(f"{styled_site_key}: {status}")
        except (ValueError, TypeError) as err:
            spinner.fail()
            status = typer.style("failed", fg=typer.colors.RED, bold=True)
            typer.echo(f"{styled_site_key}: {status}")
            typer.echo(f"{err}")


@app.command("create")
def create_site_key():
    """Not yet implemented."""
    pass


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
        _confirm_and_update_sitekey(yes, site_key, updates)

    except (ValueError, db.NotFound) as err:
        typer.secho(f"{err}", fg="red")
        typer.Abort()


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

        _confirm_and_update_sitekey(yes, site_key, updates)

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
            data_type=data_type,
            title=title,
            default_value=default_value,
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
            data_type=data_type,
            title=title,
            default_value=default_value,
            required=required,
            editable=editable,
            min_value=min_value,
            max_value=max_value,
        )
        return craft_detail
    elif data_type == DetailDataType.string:

        if min_length is None:
            min_length = utils.prompt("Please enter the min length", data_type=int)
        if max_length is None:
            max_length = utils.prompt("Please enter the max length", data_type=int)
        craft_detail = CraftDetail.from_raw_data(
            data_type=data_type,
            title=title,
            default_value=default_value,
            required=required,
            editable=editable,
            min_length=min_length,
            max_length=max_length,
        )
        return craft_detail
    elif data_type == DetailDataType.timestamp:
        # noinspection PyNoneFunctionAssignment
        default_value = utils.convert_string_to_none(default_value)
        craft_detail = CraftDetail.from_raw_data(
            data_type=data_type,
            title=title,
            default_value=default_value,
            required=required,
            editable=editable,
            min_length=min_length,
            max_length=max_length,
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
            data_type=data_type,
            title=title,
            default_value=default_value,
            required=required,
            editable=editable,
            on_task_status=on_task_status,
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
            data_type=data_type,
            title=title,
            default_value=default_value,
            required=required,
            editable=editable,
            min_value=min_value,
            max_value=max_value,
            on_task_status=on_task_status,
        )
        return task_detail
    elif data_type == DetailDataType.string:
        if min_length is None:
            min_length = utils.prompt("Please enter the min length", data_type=int)
        if max_length is None:
            max_length = utils.prompt("Please enter the max length", data_type=int)
        task_detail = TaskDetail.from_raw_data(
            data_type=data_type,
            title=title,
            default_value=default_value,
            required=required,
            editable=editable,
            min_length=min_length,
            max_length=max_length,
            on_task_status=on_task_status,
        )
        return task_detail
    elif data_type == DetailDataType.timestamp:
        # noinspection PyNoneFunctionAssignment
        default_value = utils.convert_string_to_none(default_value)
        task_detail = TaskDetail.from_raw_data(
            data_type=data_type,
            title=title,
            default_value=default_value,
            required=required,
            editable=editable,
            min_length=min_length,
            max_length=max_length,
            on_task_status=on_task_status,
        )
        return task_detail
    else:
        raise ValueError(f"Unexpected data type for {data_type}")
    pass


def check_sitekey(
    name: str,
    timezone: str,
    managingCompanyID: str,
    validCraftTypes: List[int],
    validTaskTypes: List[int],
    validTaskStatusCodes: List[int],
    validEventTypes: List[int],
    customizations: dict,
) -> SiteKey:
    # Validates when initialized
    site_key: SiteKey = SiteKey(**locals())

    return site_key


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
