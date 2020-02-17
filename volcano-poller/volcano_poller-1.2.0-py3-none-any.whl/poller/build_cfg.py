BUILD_ON = False
tags = []


def enable_build() -> None:
    global BUILD_ON     # pylint: disable=global-statement
    BUILD_ON = True


def build_tag(branch: (str, None), long_name: str, vt: str) -> None:
    assert branch is None or isinstance(branch, str), branch
    assert isinstance(long_name, str), long_name
    assert isinstance(vt, str), vt

    if BUILD_ON:
        if branch:
            full_name = branch + '.' + long_name
        else:
            full_name = long_name

        tags.append((full_name, vt))


def flush_build() -> None:
    assert BUILD_ON
    """
    print('<?xml version="1.0" encoding="UTF-8"?>')
    print('<doc>')
    for name, vt in tags:
        print('  <Tag name="{}" type="{}" />'.format(name, vt))
    print('</doc>')
    """
    for name, vt in tags:
        print('tag {} {}'.format(name, vt))
