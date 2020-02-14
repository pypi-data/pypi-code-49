from .helpers import read
from collections import namedtuple


LinuxInfo = namedtuple("LinuxInfo", "distro distro_pretty debian_based version version_codename")


def str2dict(ss, delim):
    d = {}
    o = ss.split("\n")

    for line in o:
        try:
            s = line.split(delim)
            # still may have some " characters to remove
            d[s[0]] = s[1].replace('"', '')
        except IndexError:
            # sometimes there is an empty line, so you can't
            # split '' into 2 substrings
            continue
    return d


def linux_info():
    # if un.sysname != 'Linux':
    #     return None

    osr = read('/etc/os-release')
    if osr is None:
        return None

    d = str2dict(osr, "=")
    # d = {}
    # o = osr.split("\n")
    #
    # for line in o:
    #     try:
    #         s = line.split("=")
    #         d[s[0]] = s[1]
    #     except IndexError:
    #         # sometimes there is an empty line, so you can't
    #         # split '' into 2 substrings
    #         continue

    db = True if d["ID_LIKE"] == "debian" else False

    info = LinuxInfo(
        d["ID"],
        d["PRETTY_NAME"],
        db,
        d["VERSION_ID"],
        d["VERSION_CODENAME"]
    )
    return info
