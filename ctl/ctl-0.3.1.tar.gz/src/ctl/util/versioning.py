def version_tuple(version):
    """ Returns a tuple from version string """
    return tuple(version.split("."))


def version_string(version):
    """ Returns a string from version tuple or list """
    return ".".join(["{}".format(v) for v in version])


def validate_semantic(version, pad=0):
    if not isinstance(version, (list, tuple)):
        version = version_tuple(version)

    parts = len(version)

    if parts < 1:
        raise ValueError("Semantic version needs to contain at least a major version")
    if parts > 4:
        raise ValueError("Semantic version can not contain more than 4 parts")

    if parts < pad:
        version = tuple(list(version) + [0 for i in range(0, pad - parts)])

    return tuple([int(n) for n in version])


def bump_semantic(version, segment):
    if segment == "major":
        version = list(validate_semantic(version))
        return (version[0] + 1, 0, 0)
    elif segment == "minor":
        version = list(validate_semantic(version, pad=2))
        return (version[0], version[1] + 1, 0)
    elif segment == "patch":
        version = list(validate_semantic(version, pad=3))
        return (version[0], version[1], version[2] + 1)
    elif segment == "dev":
        version = list(validate_semantic(version, pad=4))
        try:
            return (version[0], version[1], version[2], version[3] + 1)
        except IndexError:
            return (version[0], version[1], version[2], 1)
