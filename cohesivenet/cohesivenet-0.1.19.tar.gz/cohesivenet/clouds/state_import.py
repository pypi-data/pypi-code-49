import json
import subprocess

from cohesivenet import util, CohesiveSDKException


def load_terraform_state(path_to_infra):
    """Load terraform state

    Arguments:
        path_to_infra {str} - full path to infra

    Returns:
        Dict
    """
    raw_result = ""
    try:
        with util.cd(path_to_infra):
            result = subprocess.run(
                ["terraform", "show", "-json"], stdout=subprocess.PIPE
            )
            raw_result = result.stdout.decode("utf-8")
            return json.loads(raw_result.strip())
    except json.decoder.JSONDecodeError:
        raise CohesiveSDKException("Failed to load result: %s" % raw_result)
