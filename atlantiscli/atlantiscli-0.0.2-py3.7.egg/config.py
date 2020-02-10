# -*- coding: utf-8 -*-
import os
from awsvault import Vault

AWS_SECRETS = os.getenv('AWS_SECRETS')
vault = Vault([s.strip() for s in AWS_SECRETS.split(',')] if AWS_SECRETS else [])
ATLANTIS_URL = vault.get("ATLANTIS_URL")
