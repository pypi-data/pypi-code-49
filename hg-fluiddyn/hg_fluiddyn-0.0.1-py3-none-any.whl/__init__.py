"""
## Example of configuration for this extension (in ~/.hgrc)

```
[fluiddyn]
root = ~/Dev
maintainer = 1
```

## Writing Mercurial extentions

- https://www.mercurial-scm.org/wiki/WritingExtensions
- https://www.mercurial-scm.org/wiki/MercurialApi

"""

from pathlib2 import Path
import os
import subprocess

from mercurial import registrar
from mercurial import hg
from mercurial import commands
from mercurial import extensions
from mercurial import error

github_base = "git+ssh://git@github.com/fluiddyn/"
heptapod_base = "ssh://hg@foss.heptapod.net/fluiddyn"

cmdtable = {}
command = registrar.command(cmdtable)

testedwith = "4.9.1"
buglink = "https://foss.heptapod.net/fluiddyn/hg-fluiddyn/issues"

all_fluiddyn_packages = [
    "fluiddyn",
    "transonic",
    "fluidfft",
    "fluidsim",
    "fluidlab",
    "fluidimage",
    "fluidsht",
    "fluiddevops",
    "hg-fluiddyn",
    "conda-app",
]


def uisetup(ui):
    global maintainer
    maintainer = ui.configbool(
        b"fluiddyn", b"maintainer", default=False, untrusted=False
    )

    global fluiddyn_packages
    fluiddyn_packages = [
        "fluiddyn",
        "transonic",
        "fluidfft",
        "fluidsim",
        "fluidlab",
        "fluidimage",
        "fluidsht",
    ]

    if maintainer:
        fluiddyn_packages = all_fluiddyn_packages

    tweakdefaults = ui.configbool(b"ui", b"tweakdefaults", untrusted=False)
    if not tweakdefaults:
        ui.warn(
            "Please activate tweakdefaults in your ~/.hgrc:\n\n"
            "[ui]\ntweakdefaults = True\n\n"
        )

    global root
    root = os.path.expanduser(
        ui.config(b"fluiddyn", b"root", default="~/Dev", untrusted=False)
    )


@command(b"fluiddyn-clone-update-default", [], norepo=True)
def fluiddyn_clone_update_default(ui, **opts):
    ui.write("Hello FluidDyn developer!\n")
    for package_name in fluiddyn_packages:
        clone_update_default(ui, package_name)


def clone_update_default(ui, package_name):
    path_repo = Path(root) / package_name
    try:
        repo = hg.repository(ui, str(path_repo))
        # the repository exists, just update
        commands.update(ui, repo, "default")
    except error.RepoError:
        # the repository needs to be cloned
        address = heptapod_base + "/" + package_name
        commands.clone(ui, str(address), dest=str(path_repo))


@command(b"fluiddyn-set-paths", [], norepo=True)
def fluiddyn_set_paths(ui, **opts):
    ui.write("Hello FluidDyn developer!\n")
    for package_name in fluiddyn_packages:
        set_path(ui, package_name)


def set_path(ui, package_name):

    path_repo = Path(root) / package_name
    try:
        repo = hg.repository(ui, str(path_repo))
    except error.RepoError:
        return
    paths = dict(repo.ui.configitems(b"paths", untrusted=False))
    path_default = paths["default"]

    has_to_fix = False

    if "bitbucket.org" in path_default:
        ui.warn(
            "default for {} is still pointing towards Bitbucket.org\n".format(
                package_name
            )
        )
        has_to_fix = True

    if not has_to_fix:
        ui.write("paths {} ok\n".format(package_name))
        return

    nb_paths = len(paths)

    path_hgrc = path_repo / ".hg/hgrc"

    with open(str(path_hgrc), "r") as file:
        lines = file.readlines()

    index_path = -1
    in_paths = False
    for index, line in enumerate(lines):
        if line.strip() == "[paths]":
            index_paths = index
            in_paths = True

        if in_paths and any(line.startswith(key) for key in paths.keys()):
            index_path += 1
            if index_path == nb_paths - 1:
                index_end_paths = index
                break

    lines_new = lines[: index_paths + 1]
    lines_new.append(
        "default = ssh://hg@foss.heptapod.net/fluiddyn/{}\n".format(package_name)
    )

    if maintainer:
        lines_new.append(
            "bitbucket = ssh://hg@bitbucket.org/fluiddyn/{}\n".format(
                package_name
            )
        )

    lines_new += lines[index_end_paths + 1 :]
    text = "".join(lines_new)
    ui.write("Modify .hg/hgrc for package {}\n".format(package_name))

    with open(str(path_hgrc), "w") as file:
        file.write(text)


def check_default_path(repo):
    default = dict(repo.ui.configitems(b"paths", untrusted=False))["default"]
    if "foss.heptapod.net" not in default:
        repo.ui.write("default points to a wrong path")
        return
    return 1


def get_package_name(repo):
    default = dict(repo.ui.configitems(b"paths", untrusted=False))["default"]
    return os.path.split(default)[1]


@command(b"fluiddyn-push-github", [])
def fluiddyn_push_github(ui, repo, **opts):
    if not check_default_path(repo):
        return
    commands.pull(ui, repo)
    commands.update(ui, repo, "default")
    commands.bookmark(ui, repo, "master")
    commands.summary(ui, repo)
    package_name = get_package_name(repo)
    path_github = os.path.join(github_base, package_name)
    commands.push(ui, repo, dest=path_github, bookmark="master")
    commands.bookmark(ui, repo, "master", delete=True)


def extsetup(ui):
    """To check the activated extensions"""

    extensions_to_check = [b"evolve", b"topic", b"rebase"]
    if maintainer:
        extensions_to_check.append(b"hggit")

    for ext in extensions_to_check:
        try:
            extensions.find(ext)
        except KeyError:
            ui.warn(b"extension %s not activated!\n" % ext)


def precommit_hook(ui, repo, **kwargs):
    try:
        subprocess.check_output(["black", "--version"])
    except OSError:
        ui.warn("please install black")
        return 1

    ui.pushbuffer()
    commands.status(ui, repo, no_status=True, added=True, modified=True)
    output = [path for path in ui.popbuffer().split("\n") if path.endswith(".py")]

    if not output:
        return

    return subprocess.call("black -l 82".split() + output)


def reposetup(ui, repo):
    try:
        package_name = get_package_name(repo)
    except KeyError:
        return

    if package_name not in all_fluiddyn_packages:
        return

    ui.setconfig("hooks", "precommit.hgfluiddyn", precommit_hook)
