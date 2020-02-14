import os
import site
import textwrap
import sys


REGISTRATION_CODE = textwrap.dedent(
    """
    try:
        import colossal
    except ImportError:
        pass
    else:
        colossal.register()
    """
)


def get_site_packages():
    for path in sys.path:
        if path.endswith("site-packages"):
            return path
    return site.getusersitepackages()


def main():
    with open(os.path.join(get_site_packages(), 'colossal.pth'), 'w') as f:
        f.write(f"import sys; exec({REGISTRATION_CODE!r})\n")
