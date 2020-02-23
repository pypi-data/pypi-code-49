"""Entry point for non-CLI calls."""
import os
import sys
import jpl


def main():  # pragma no cover
    """Entrypoint to the `jpl` main command."""

    if sys.path[0] == "" or sys.path[0] == os.getcwd():
        sys.path.pop(0)

    if not sys.argv[-1].endswith(".yml"):
        print("Please enter filepath to .yml")
        sys.exit()
    else:
        jpl.JiggyPlaybookLint(path=sys.argv[-1]).run()


if __name__ == "__main__":  # pragma: no cover
    main()
