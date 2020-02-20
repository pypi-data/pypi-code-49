import subprocess
import sys
from os import path as p


def git_ls_tree(path="."):
    assert p.isdir(path)
    if p.islink(path):
        rel_link_target = p.relpath(p.realpath(path))
    else:
        rel_link_target = path
    print(path, rel_link_target)

    ls_tree = (
        subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", "HEAD", rel_link_target]
        )
        .decode("utf-8")
        .splitlines()
    )
    for item in ls_tree:
        if p.isfile(item):
            yield p.join(path, p.relpath(item, rel_link_target))
        elif p.islink(item) and p.isdir(item):
            for sub_item in git_ls_tree(item):
                yield p.join(path, p.relpath(sub_item, rel_link_target))
