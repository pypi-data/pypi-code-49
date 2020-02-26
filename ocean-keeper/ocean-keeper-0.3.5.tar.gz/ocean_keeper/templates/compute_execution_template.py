#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0
import logging

from ocean_keeper.templates.template_base import TemplateBase

logger = logging.getLogger('escrowComputeExecutionTemplate')


class EscrowComputeExecutionTemplate(TemplateBase):
    """Class representing the EscrowComputeExecutionTemplate contract."""
    CONTRACT_NAME = 'EscrowComputeExecutionTemplate'

    def get_conditions_order(self):
        return ['', '', '']
