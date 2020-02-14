"""Validate BIDS data structure.

Call validate_bids() to run the bids-validator on BIDS formatted
data.  This will log the results and report errors and warnings.
If you want more control, call call_validate_bids() instead which
will return an error code and the complete bids validator output
as a dictionary.

Install the command-line version of the BIDS Validator into container by adding
this to Dockerfile, e.g.:

    .. code-block:: console

        RUN npm install -g bids-validator@1.3.8

Example:
    .. code-block:: python

        from pathlib import Path
        import flywheel

        bids_path = Path(context.work_dir)/'bids'

        # download BIDS data...

        # validate
        err_code = validate_bids(bids_path)

        if err_code > 0:
            log.exception('Error in BIDS download and validation.')
            # do not bother processing BIDS data

        else:
            # process BIDS data...

    See validate_bids() below for an example of calling call_validate_bids().
"""

import subprocess as sp
from pathlib import Path
import logging
import json
import pprint


log = logging.getLogger(__name__)


def call_validate_bids(bids_path, out_path):
    """Call command-line version of the bids validator.

    Use this function if you want to parse the bids output yourself.
    Otherwise, call validate_bids() below and it will add a description
    of the results to the log.

    Args:
        bids_path (str): path to top directory of BIDS data.
        out_path (pathlib path): full path and name of json formatted output
            file that will be produced when BIDS validation is run.  If you
            want the gear to return this file, write it to the output/
            directory.  If you want to process this file inside the gear
            and don't want to save it (like validate_bids() does below),
            write it into the work/ directory.

    Returns:

        tuple: Two values:

            * err_code (int): zero if no error.

            * bids_output (dict): The results of bids validation.

            `bids_output` contains a summary of the bids data present
            and a list of errors and warnings (if any).
    """

    log.debug('Running BIDS Validator')

    command = ['bids-validator', '--verbose', '--json', str(bids_path)]
    msg = 'Command: ' + ' '.join(command)
    log.info(msg)

    with open(out_path, "w") as f:
        result = sp.run(command, stdout=f, stderr=sp.PIPE,
                        universal_newlines=True, check=True)

    msg = command[0] + ' return code: ' + str(result.returncode)
    log.info(msg)

    if result.stderr:
        log.error(result.stderr)

    with open(out_path) as jfp:
        bids_output = json.load(jfp)

    return result.returncode, bids_output


def validate_bids(bids_path):
    """Run BIDS Validator on provided bids_path.

    This calls the bids validator and then prints a summary of files
    that are valid, and then lists errors and warnings.  It returns
    non-zero if there was an error.

    Args:
        bids_path (str): path to top directory of BIDS data.

    Returns:
        int: err_code
            0 if no error, 1 if there was a KeyError (some strange thing
            happend), or 2 if there were any BIDS errors detected.
    """

    num_bids_errors = -1  # impossible value

    out_path = Path(bids_path) / '..' / 'validator.output.json'

    err_code, bids_output = call_validate_bids(bids_path, out_path)

    try:
        # show summary of valid BIDS stuff
        msg = 'bids-validator results:\n\nValid BIDS files summary:\n' + \
              pprint.pformat(bids_output['summary'], indent=8) + '\n'
        log.info(msg)

        num_bids_errors = len(bids_output['issues']['errors'])

        # show all errors
        for err in bids_output['issues']['errors']:
            err_msg = err['reason'] + '\n'
            for ff in err['files']:
                if ff["file"]:
                    err_msg += '      ' + ff["file"]["relativePath"] + '\n'
            log.error(err_msg)

        # show all warnings
        for warn in bids_output['issues']['warnings']:
            warn_msg = warn['reason'] + '\n'
            for ff in warn['files']:
                if ff["file"]:
                    warn_msg += '      ' + ff["file"]["relativePath"] + '\n'
            log.warning(warn_msg)

    except TypeError as ter:
        msg = 'KeyError: bids-validator result missing ' + str(repr(ter))
        log.critical(msg)
        err_code = 1

    if num_bids_errors < 0:
        log.debug('BIDS validation could not run.')

    elif num_bids_errors > 0:
        err_code = 2
        log.debug('%d BIDS validation error(s) were detected.', num_bids_errors)

    else:
        log.debug('No BIDS errors detected.')

    return err_code
