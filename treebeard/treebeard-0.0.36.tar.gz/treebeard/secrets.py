from typing import Dict, Any
import json
import os

secrets_var = "TREEBEARD_SECRETS"


def get_secrets() -> Dict[str, Any]:
    secrets = os.getenv(secrets_var)
    if secrets is None:
        raise Exception(
            f"Cannot load secrets, {secrets_var} is not set with a json object!"
        )
    try:
        return json.loads(secrets)
    except:
        raise Exception(
            f"Failed to load secrets, is {secrets_var} set to a valid JSON object?"
        )
