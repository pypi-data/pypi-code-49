"""This file houses the primary entrypoint, and main business logic of ahd.

Module Variables
----------------

usage (str):
    Used by docopt to setup argument parsing;
    Defines the actual command line interface.

CONFIG_FILE_PATH(str):
    The path to the configuration file.

CURRENT_PATH(str):
    Used to keep track of users current directory
    to cd back into it after script execution.


Documentation
-------------
Docs website: https://ahd.readthedocs.io
"""

# Standard lib dependencies
import os                             # Used primarily to validate paths
import sys                            # Used to check length of input arguments
import glob                           # Used to preprocess wildcard paths
import logging                        # Used to log valueable logging info
import webbrowser                     # Used to auto-launch the documentation link
import subprocess                     # Used to run the dispatched commands
from configparser import ConfigParser # Used to serialize and de-serialize config files


# Internal dependencies
from .autocomplete import command, generate_bash_autocomplete

# Third-party dependencies
import colored                        # Used to colour terminal output
from docopt import docopt             # Used to parse arguments and setup POSIX compliant usage info


usage = """Add-hoc dispatcher
    Create ad-hoc commands to be dispatched within their own namespace.

    Usage: 
        ahd list [-l]
        ahd [-h] [-v] [-d]
        ahd docs [-a] [-o]
        ahd config [-e] [-i CONFIG_FILE_PATH]
        ahd register <name> [<command>] [<paths>]
        ahd <name> [<command>] [<paths>]

    Options:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    -l, --long            Shows all commands in configuration with paths and commands
    -a, --api             shows the local API docs
    -o, --offline         shows the local User docs instead of live ones
    -e, --export          exports the configuration file
    -i CONFIG_FILE_PATH, --import CONFIG_FILE_PATH 
                        imports the configuration file
    """

command_list =  [ # Used for autocompletion generation
    command("docs", ["-a", "--api", "-o", "--offline"]),
    command("register", []),
    command("config", ["-e", "--export", "-i", "--import"])
]


config = ConfigParser() # Global configuration parser

# The default (and currently only) path to the configuration file
CONFIG_FILE_PATH = f"{os.path.dirname(__file__)}{os.sep}.ahdconfig"


CURRENT_PATH = os.curdir # Keeps track of current directory to return to after executing commands

def main():
    """The primary entrypoint for the ahd script.
    
    All primary business logic is within this function."""

    # Setup arguments for parsing
    arguments = docopt(usage, version="ahd V 0.4.0")

    if len(sys.argv) == 1:
        print("\n", usage)
        exit()

    if os.path.exists(CONFIG_FILE_PATH): # If the file already exists
        config.read(CONFIG_FILE_PATH) # Read it

    else: # If a file does not exist create one
        with open(CONFIG_FILE_PATH, "w") as config_file:
                config.write(config_file)
    
    # Begin argument parsing

    if arguments["list"]:
        list_commands(arguments["--long"])

    # ========= Docs argument parsing =========
    if arguments["docs"]:
        docs(arguments["--api"], arguments["--offline"])

    # ========= config argument parsing =========
    if arguments["config"]:
        configure(arguments["--export"], arguments["--import"])
            
    # ========= preprocessing commands and paths =========
    if not arguments["<paths>"]:
        logging.debug("No paths argument registered setting to \'\'")
        arguments["<paths>"] = ""
    else:
        arguments["<paths>"] = _preprocess_paths(arguments["<paths>"])
    
    if not arguments["<command>"]:
        logging.debug("No command argument registered setting to \'\'")
        arguments["<command>"] = ""
    
    if "." == arguments["<command>"]: # If <command> is . set to specified value
        logging.debug(f". command registered, setting to {config[arguments['<name>']]['command']}")
        arguments["<command>"] = config[arguments["<name>"]]["command"]

    # ========= register argument parsing =========
    if arguments["register"]:
        register(arguments["<name>"], arguments["<command>"], arguments["<paths>"] )

    # ========= User command argument parsing =========
    
    if arguments['<name>']:
        if not arguments['<paths>'] and not arguments['<command>']:
            dispatch(arguments['<name>'])

        else:
            if arguments['<paths>'] and not arguments['<command>']: 
                # Process inputted paths
                arguments['<paths>'] = _preprocess_paths(arguments['<paths>'])
                arguments['<paths>'] = _postprocess_paths(arguments['<paths>'])
                dispatch(arguments['<name>'], paths = arguments['<paths>'])

            if arguments['<command>'] and not arguments['<paths>']:
                dispatch(arguments['<name>'], command = arguments['<command>'])

            else:
                # Process inputted paths
                arguments['<paths>'] = _preprocess_paths(arguments['<paths>'])
                arguments['<paths>'] = _postprocess_paths(arguments['<paths>'])
                dispatch(arguments['<name>'], paths = arguments['<paths>'], command = arguments['<command>'])
    
def list_commands(verbose = False) -> None:
    """Lists commands currently in config

    Parameters
    ----------
    verbose: (bool)
        When specified will print both the command name and
        associated commands + paths
    
    """
    configuration = ConfigParser()
    if os.path.exists(CONFIG_FILE_PATH): # If the file already exists
        configuration.read(CONFIG_FILE_PATH) # Read it
        for count, command in enumerate(configuration):
            if count > 0:
                if verbose:
                    print("\n\n============================================\n\n")
                    print(f"{colored.fg(6)}{command}\n")
                    print(f"{colored.fg(100)}\tCommand = {configuration[command]['command']}")
                    print(f"\tPaths = {configuration[command]['paths']}{colored.fg(15)}")
                else:
                    print(f"\n{colored.fg(6)}{command}{colored.fg(15)}")

    else: # If a file does not exist create one
        print(f"{colored.fg(1)}No commands found")
    print() # reset terminal text to white
    exit()


def docs(api:bool = False, offline:bool = False) -> None:
    """Processes incoming arguments when the docs command is invoked

    Parameters
    ----------
    api: (bool)
        When specified, shows API docs as opposed to user docs.

    offline: (bool)
        When specified will build local copy of docs instead of going to website

    Notes
    -----
    - By Default user documentation is selected
    - By default the online documentation is selected
    """
    if not api and not offline:
        webbrowser.open_new("https://ahd.readthedocs.io")
        exit()
    else:
        if offline and not api:
            # TODO Implement build local user docs.
            print("Not yet implemented")

        elif api:
            if not offline:
                webbrowser.open_new("https://kieranwood.ca/ahd")
                exit()
            else:
                # TODO Implement build local user docs.
                print("Not yet implemented")

def configure(export:bool = False, import_config:bool = False) -> None:
    """Handles all the exporing and importing of configurations

    Parameters
    ----------
    export: (bool)
        When specified, shows API docs as opposed to user docs.

    import_config: (bool|str)
        False if no path, otherwise a string representation of path to config file.

    Notes
    -----
    - If neither export or import_config are specified, then usage is printed.
    """

    if not export and not import_config:
            print(usage)
            exit()
    if export:
        with open(f"{os.path.abspath(os.curdir)}{os.sep}.ahdconfig", "w") as config_file:
            config.write(config_file)

    if import_config:

        new_config_path = import_config
        new_config = ConfigParser()
        
        new_config.read(new_config_path)
        try:
            os.remove(CONFIG_FILE_PATH)
            print(f"Importing {os.path.abspath(new_config_path)} to {CONFIG_FILE_PATH}")
            with open(CONFIG_FILE_PATH, "w") as config_file:
                new_config.write(config_file)
        except PermissionError:
            print(f"{colored.fg(1)} Unable to import configuration file, are you sudo?")
            print(f"{colored.fg(15)}\tTry running: sudo ahd config -i \"{arguments['--import']}\" ")

def register(name, commands, paths):
    """Handles registering of custom commands, and autocompletion generation.

    Parameters
    ----------
    name: (str)
        The name used to call the commands.

    commands: (str)
        The set of commands to execute.
    
    paths: (str)
        A string representation of the paths to execute the command with.

    Notes
    -----
    - When passing paths to this function make sure they are preprocessed.
    """
    logging.info(f"Registering command {name} with \nCommand: {commands} \nPaths: {paths}")
    if not name or not paths:
        print(usage)
        exit()
    config[name] = {
        "command": commands,
        "paths": paths,
    }

    try:
        logging.info(f"Begin writing config file to {CONFIG_FILE_PATH}")
        with open(CONFIG_FILE_PATH, "w") as config_file:
            config.write(config_file)
    except PermissionError:
            print(f"{colored.fg(1)}Unable to register command are you sudo?")
            print(f"{colored.fg(15)}\tTry running: sudo ahd register {name} \"{commands}\" \"{paths}\" ")

    if not os.name == "nt": # Generate bash autocomplete
        for index, custom_command in enumerate(config):
            if not index == 0: # for some reason the first thing in config object is garbage
                command_list.append(command(custom_command, []))

        autocomplete_file_text = generate_bash_autocomplete(command_list)
        try:
            with open("/etc/bash_completion.d/ahd.sh", "w") as autocomplete_file:
                autocomplete_file.write(autocomplete_file_text)
            print("Bash autocompletion file written to /etc/bash_completion.d/ahd.sh \nPlease restart shell for autocomplete to update")
        except PermissionError:
            print(f"{colored.fg(1)}Unable to write bash autocompletion file are you sudo?")

    # Since executing commands requires changing directories, make sure to return after
    os.chdir(CURRENT_PATH)
    exit()

def dispatch(name, command = False, paths = False):
    """Controls the dispatching of custom functions"""
    if "register" == name:
                print(usage)
                exit()
    logging.info(f"Beggining execution of {name}")

    try: # Accessing stored information on the command
        config[name]

    except KeyError: # TODO Find a way to suggest a similar command
        print(f"{colored.fg(1)}Command not found in configuration validate spelling is correct.")
        exit()
    
    if not command or command == ".":
        command = config[name]['command']
    
    if not paths:
        paths = _postprocess_paths(config[name]['paths'])

    if len(paths) > 1:
        for current_path in paths:
            if os.name == "nt":
                current_path = current_path.replace("/", f"{os.sep}")
                current_path = current_path.replace("~", os.getenv('USERPROFILE'))
            print(f"Running: cd {current_path} && {command} ".replace("\'",""))
            subprocess.Popen(f"cd {current_path} && {command} ".replace("\'",""), shell=True)

    else: # if only a single path is specified instead of a 'list' of them
        print(f"Running: cd {paths[0]} && {command} ".replace("\'",""))
        subprocess.Popen(f"cd {paths[0]} && {command} ".replace("\'",""), shell=True)
    pass

def _preprocess_paths(paths:str) -> str:
    """Preprocesses paths from input and splits + formats them
    into a useable list for later parsing.
    
    Example
    -------
    ```
    paths = '~/Desktop/Development/Canadian Coding/SSB, C:\\Users\\Kieran\\Desktop\\Development\\*, ~\\Desktop\\Development\\Personal\\noter, .'
    
    paths = _preprocess_paths(paths)

    print(paths) # Prints: '~/Desktop/Development/Canadian Coding/SSB,~/Desktop/Development/*,~/Desktop/Development/Personal/noter,.'
    ```
    """
    logging.info(f"Beginning path preprocessing on {paths}")
    result = paths.split(",")
    for index, directory in enumerate(result):
        directory = directory.strip()
        logging.debug(f"Directory: {directory}")
        if directory.startswith(".") and (len(directory) > 1):
            directory = os.path.abspath(directory)
        if not "~" in directory:
            if os.name == "nt":
                directory = directory.replace(os.getenv('USERPROFILE'),"~")

            else:
                directory = directory.replace(os.getenv('HOME'),"~")
            directory = directory.replace("\\", "/")
            result[index] = directory
        else:
            directory = directory.replace("\\", "/")
            result[index] = directory

    logging.debug(f"Result: {result}")
    result = ",".join(result)

    return result

def _postprocess_paths(paths:str) -> list:
    """Postprocesses existing paths to be used by dispatcher.

    This means things like expanding wildcards, and processing correct path seperators.
    
    Example
    -------
    ```
    paths = 'C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding\\SSB, C:\\Users\\Kieran\\Desktop\\Development\\Canadian Coding\\website, ~/Desktop/Development/Personal/noter, C:\\Users\\Kieran\\Desktop\\Development\\*'
    
    paths = _preprocess_paths(paths)

    print(_postprocess_paths(paths)) 
    # Prints: ['C:/Users/Kieran/Desktop/Development/Canadian Coding/SSB', ' C:/Users/Kieran/Desktop/Development/Canadian Coding/website', ' C:/Users/Kieran/Desktop/Development/Personal/noter', 'C:/Users/Kieran/Desktop/Development/Canadian Coding', 'C:/Users/Kieran/Desktop/Development/Personal', 'C:/Users/Kieran/Desktop/Development/pystall', 'C:/Users/Kieran/Desktop/Development/python-package-template', 'C:/Users/Kieran/Desktop/Development/Work']
    ```
    """
    logging.info(f"Beginning path postprocessing on {paths}")

    paths = paths.split(",")
    result = []
    for directory in paths:
        directory = directory.strip()

        if os.name == "nt":
            directory = directory.replace("/", "\\")

        if directory.startswith("."):
            try:
                if directory[1] == "/" or directory[1] == "\\":
                    directory = f"{os.curdir}{directory[1::]}"
            except IndexError:
                directory = os.path.abspath(".")

        if "~" in directory:
            if os.name == "nt":
                directory = directory.replace("~",f"{os.getenv('USERPROFILE')}")
            else:
                directory = directory.replace("~", f"{os.getenv('HOME')}")
        
        if "*" in directory:

            wildcard_paths = glob.glob(directory.strip())

            for wildcard_directory in wildcard_paths:
                wildcard_directory = wildcard_directory.replace("\\", "/")
                result.append(wildcard_directory)
        else:
            result.append(directory)

    logging.debug(f"Result: {result}")
    return result


if __name__ == "__main__":
    main()
