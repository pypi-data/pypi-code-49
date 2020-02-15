import os
import subprocess
import sys


def find_files(dirname):
    dirname = dirname or "."
    if os.path.isdir(os.path.join(dirname, ".git")):
        for path in subprocess.check_output(
            ["git", "ls-files", "--cached", "--recurse-submodules"],
            cwd=dirname,
        ).decode(sys.getfilesystemencoding()).splitlines():
            yield os.path.normcase(path)


if __name__ == "__main__":
    dirname = sys.argv[1] if len(sys.argv) > 1 else "."
    for path in find_files(dirname):
        print(path)
