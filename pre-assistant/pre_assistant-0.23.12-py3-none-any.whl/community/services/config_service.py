from typing import Text, Tuple, Dict, List

from rasax.community import config


def get_runtime_config_and_errors(
    credentials_path: Text = config.credentials_path,
    endpoints_path: Text = config.endpoints_path,
) -> Tuple[Dict[Text, Text], List]:
    """Returns dictionary of runtime configs and possible errors.

    Runtime configs are read from `credentials_path` and `endpoints_path` (by
    default these are `/app/credentials.yml` and `/app/endpoints.yml`).
    Returns a dictionary with keys `credentials` and `endpoints`, containing the
    respective configs as yaml strings.
    """

    runtime_config = {}
    errors = []

    for key, filename in [
        ("credentials", credentials_path),
        ("endpoints", endpoints_path),
    ]:
        try:
            with open(filename) as f:
                runtime_config[key] = f.read()
        except OSError as e:
            errors.append(e)

    return runtime_config, errors
