# Import python libs
import os


def set_ver(hub):
    """
    Set the version to the <project name>/version.py
    """
    ver = hub.OPT["pop_release"]["ver"]
    name = hub.pop_release.PATHNAME
    ver_str = f'# -*- coding: utf-8 -*-\nversion = "{ver}"\n'
    path = os.path.join(name, "version.py")
    with open(path, "w+") as wfh:
        wfh.write(ver_str)


def set_doc(hub):
    """
    """
    ver = hub.OPT["pop_release"]["ver"]
    name = hub.pop_release.PATHNAME
    lines = []
    paths = [os.path.join("docs", "conf.py"), os.path.join("docs", "source", "conf.py")]
    path = None
    for check in paths:
        if os.path.isfile(check):
            path = check
    if not path:
        print("No docs set up for this project, use Sphinx to set up docs")
        return
    with open(path, "r") as rfh:
        for line in rfh.readlines():
            if line.startswith("ver"):
                lines.append(f'version = "{ver}"')
                continue
            elif line.startswith("release"):
                lines.append(f'release = "{ver}"')
                continue
            else:
                line.append(line)
    with open(path, "w+") as wfh:
        wfh.writelines(lines)
