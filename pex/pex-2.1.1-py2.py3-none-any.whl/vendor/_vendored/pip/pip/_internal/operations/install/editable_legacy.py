"""Legacy installation process, i.e. `setup.py develop`.
"""
import logging

from pip._internal.utils.logging import indent_log
from pip._internal.utils.setuptools_build import make_setuptools_develop_args
from pip._internal.utils.subprocess import call_subprocess
from pip._internal.utils.typing import MYPY_CHECK_RUNNING

if MYPY_CHECK_RUNNING:
    from typing import List, Optional, Sequence

    from pip._internal.build_env import BuildEnvironment


logger = logging.getLogger(__name__)


def install(
    install_options,  # type: List[str]
    global_options,  # type: Sequence[str]
    prefix,  # type: Optional[str]
    home,  # type: Optional[str]
    use_user_site,  # type: bool
    name,  # type: str
    setup_py_path,  # type: str
    isolated,  # type: bool
    build_env,  # type: BuildEnvironment
    unpacked_source_directory,  # type: str
):
    # type: (...) -> None
    """Install a package in editable mode. Most arguments are pass-through
    to setuptools.
    """
    logger.info('Running setup.py develop for %s', name)

    args = make_setuptools_develop_args(
        setup_py_path,
        global_options=global_options,
        install_options=install_options,
        no_user_config=isolated,
        prefix=prefix,
        home=home,
        use_user_site=use_user_site,
    )

    with indent_log():
        with build_env:
            call_subprocess(
                args,
                cwd=unpacked_source_directory,
            )
