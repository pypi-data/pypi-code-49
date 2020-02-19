from pkg_resources import working_set


def _generate_installed_modules():
    for info in working_set:
        yield info.key, info.version


def get_installed_modules():
    return dict(_generate_installed_modules())
