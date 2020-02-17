import os
from dataverk_vault import api as vault_api


def set_secrets_as_env() -> None:
    secrets = vault_api.read_secrets()
    os.environ.update({**secrets})
