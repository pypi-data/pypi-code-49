#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

import logging

from ocean_keeper.templates.template_base import TemplateBase

logger = logging.getLogger('escrowAccessSecretStoreTemplate')


class EscrowAccessSecretStoreTemplate(TemplateBase):
    """Class representing the EscrowAccessSecretStoreTemplate contract."""
    CONTRACT_NAME = 'EscrowAccessSecretStoreTemplate'

    def get_conditions_order(self):
        return ['', '', '']
