from argus_cli.plugin import run

from argus_plugins import argus_cli_module
from argus_plugins.api_provider import import_submodules
# Import commands so that they get registered
from argus_plugins import *


def main():
    import_submodules("argus_api.api")
    run(argus_cli_module)


if __name__ == "__main__":
    main()
