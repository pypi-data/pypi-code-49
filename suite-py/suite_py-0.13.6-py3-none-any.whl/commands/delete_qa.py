from __future__ import print_function, unicode_literals
from ..lib.handler.youtrack_handler import YoutrackHandler
from ..lib.handler import git_handler as git
from ..lib.logger import Logger
from ..lib.qainit import qainit_shutdown

import sys

youtrack = YoutrackHandler()
logger = Logger()


def entrypoint(args):
    branch_name = git.current_branch_name()
    youtrack_id = youtrack.get_card_from_name(branch_name)

    logger.info("Spengo il qa se esite...")
    qainit_shutdown(branch_name)

    sys.exit()
