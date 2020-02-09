#  MIT License
#
#  Copyright (c) 2019 Jac. Beekers
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

##
# Informatica Artifact Checks
# @Since: 12-APR-2019
# @Author: Jac. Beekers
# @Version: 20190414.0 - JBE - Initial

import supporting.errorcodes as err
import supporting, logging
from cicd.informatica import infaSettings as settings
from pathlib import Path

logger = logging.getLogger(__name__)


def infaartifactchecks():
    thisproc = "infaartifactchecks"
    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    result = err.OK

    if not settings.infadeploylist:
        supporting.log(logger, err.NO_DEPLOYLIST.level, thisproc, err.NO_DEPLOYLIST.message)
        result = err.NO_DEPLOYLIST
    else:
        deploylistFile = Path(settings.infadeploylist)
        if not deploylistFile.is_file():
            supporting.log(logger, err.DEPLOYLIST_NF.level, thisproc, "deploylist is >" + settings.infadeploylist +"<. " + err.DEPLOYLIST_NF.message)
            result = err.DEPLOYLIST_NF

    supporting.log(logger, logging.DEBUG, thisproc, 'completed with >' + str(result.rc) + "<.")
    return result

def infadeploychecks():
    thisproc = "infadeploychecks"
    supporting.log(logger, logging.DEBUG, thisproc, 'started')

    # for now the checks for deploys and artifacts are the same
    result = infaartifactchecks()

    supporting.log(logger, logging.DEBUG, thisproc, 'completed with >' + str(result.rc) + "<.")
    return result
