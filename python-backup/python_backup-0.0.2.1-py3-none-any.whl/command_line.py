#!/usr/bin/env python
import backup
import sys


def main():
    try:
        backup.main(sys.argv[1:])

    except backup.BackupException as ex:
        print(ex)
        sys.exit(1)

    except Exception:
        from traceback import format_exc
        msg = "Error encountered:\n" + format_exc().strip()
        print(msg)
        sys.exit(1)
