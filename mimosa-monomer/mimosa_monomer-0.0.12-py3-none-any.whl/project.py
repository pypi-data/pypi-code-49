import json
import time
from pathlib import Path
from tkinter import filedialog

from firebase_admin import credentials, initialize_app, get_app, App
from halo import Halo
from termcolor import colored


def choose_project(skip: bool = False):
    save_path = Path("~/.mimosa/last_project.json").expanduser()
    save_path.parent.mkdir(parents=True, exist_ok=True)
    # todo: fetch available site keys and prompt user
    # todo: prompt for data (craftType, variable name, data type, title,
    #  editable, validation parameters, default value, required)
    # todo: display data and confirm write
    # todo: update database
    # todo: prompt to add another entry?
    if save_path.is_file() is True:
        with save_path.open("r") as f:
            service_key_path: Path = Path(json.load(f).get("service_key"))
        with service_key_path.open() as f:
            service_key_data = json.load(f)
        while True:
            colored_project_title = colored(
                service_key_data.get("project_id"), "yellow", attrs=["bold"]
            )
            if skip:
                print(f"Using previous project: {colored_project_title}")
                break
            response = input(
                f"Do you want to continue using project {colored_project_title}? (y/n): "
            )
            if response.lower() == "n":
                service_key_path = Path(
                    filedialog.askopenfilename(
                        filetypes=(("JSON", "*.json"),),
                        title="Select service account key",
                    )
                )
                with service_key_path.open() as f:
                    service_key_data = json.load(f)
                break
            elif response.lower() == "y":
                break
            else:
                print(colored("Invalid input. Try again.", "red", attrs=["bold"]))
                continue

    else:
        service_key_path = Path(
            filedialog.askopenfilename(
                filetypes=(("JSON", "*.json"),), title="Select service account key"
            )
        )
        with service_key_path.open() as f:
            service_key_data = json.load(f)
    if service_key_path.is_file() is not True:
        raise FileNotFoundError(f"File not found at: {service_key_path}")
    with save_path.open("w") as f:
        json.dump({"service_key": str(service_key_path)}, f, indent=4)
    app = init_firebase(str(service_key_path))
    spinner = Halo(text="Getting coffee...", spinner="dots", text_color="blue")
    spinner.start()
    time.sleep(1)
    spinner.succeed("Coffee acquired!")
    # text = colored("Success!", "green", attrs=["underline", "bold"])
    # print(text)


def init_firebase(key_path: str) -> App:
    """
    Initialize and return the App object for the Firebase project.
    :param app_name:
    :param key_path:
    :return:
    """
    spinner = Halo(text_color="blue")
    spinner.start("Initializing Firebase app.")
    cred = credentials.Certificate(key_path)
    try:
        app = initialize_app(cred)
    except ValueError:
        app = get_app()
    spinner.succeed()
    return app
