#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

from collections import namedtuple

from eth_utils import add_0x_prefix

from ocean_keeper import ContractBase
from ocean_keeper.templates import EscrowAccessSecretStoreTemplate
from ocean_keeper.templates.compute_execution_template import EscrowComputeExecutionTemplate
from ocean_keeper.utils import generate_multi_value_hash

AgreementTemplate = namedtuple(
    'AgreementTemplate',
    ('state', 'owner', 'updated_by', 'block_number_updated', 'condition_types', 'actor_type_ids')
)


class TemplateStoreManager(ContractBase):
    """Class representing the TemplateStoreManager contract."""
    CONTRACT_NAME = 'TemplateStoreManager'
    SERVICE_TO_TEMPLATE_NAME = {
        'access': EscrowAccessSecretStoreTemplate.CONTRACT_NAME,
        'compute': EscrowComputeExecutionTemplate.CONTRACT_NAME
    }

    @staticmethod
    def create_template_id(template_name):
        return generate_multi_value_hash(['string'], [template_name]).hex()

    def get_template_by_name(self, template_name):
        return self.get_template(TemplateStoreManager.create_template_id(template_name))

    def get_template_by_service_type(self, template_type):
        name = self.SERVICE_TO_TEMPLATE_NAME.get(template_type, None)
        if not name:
            return None

        return self.get_template_by_name(name)

    def get_template(self, template_id):
        """
        Get the template for a given template id.

        :param template_id: id of the template, str
        :return:
        """
        template = self.contract_concise.getTemplate(template_id)
        if template and len(template) == 6:
            actor_type_ids = [add_0x_prefix(actor_type_id.hex())
                              for actor_type_id in template[-1]]
            template[-1] = actor_type_ids
            return AgreementTemplate(*template)

        return None

    def get_template_actor_type_ids(self):
        return [add_0x_prefix(actor_type_id.hex())
                for actor_type_id in self.contract_concise.getTemplateActorTypeIds()]

    def get_template_actor_type_id(self, actor_type):
        return add_0x_prefix(self.contract_concise.getTemplateActorTypeId(actor_type).hex())

    def get_template_actor_type_value(self, actor_type_id):
        return self.contract_concise.getTemplateActorTypeValue(actor_type_id)

    def get_template_actor_type_state(self, actor_type_id):
        # 0, 1, or 2 (uninitialized, registered, deregistered
        return self.contract_concise.getTemplateActorTypeState(actor_type_id)

    def propose_template(self, template_id, from_account):
        """Propose a template.

        :param template_id: id of the template, str
        :param from_account: Account
        :return: bool
        """
        tx_hash = self.send_transaction(
            'proposeTemplate',
            (template_id,),
            transact={'from': from_account.address,
                      'passphrase': from_account.password,
                      'account_key': from_account.key}
        )
        return self.is_tx_successful(tx_hash)

    def approve_template(self, template_id, from_account):
        """
        Approve a template.

        :param template_id: id of the template, str
        :param from_account: Account
        :return:
        """
        tx_hash = self.send_transaction(
            'approveTemplate',
            (template_id,),
            transact={'from': from_account.address,
                      'passphrase': from_account.password,
                      'account_key': from_account.key}
        )
        return self.is_tx_successful(tx_hash)

    def revoke_template(self, template_id, from_account):
        """
        Revoke a template.

        :param template_id: id of the template, str
        :param from_account: Account
        :return: bool
        """
        tx_hash = self.send_transaction(
            'revokeTemplate',
            (template_id,),
            transact={'from': from_account.address,
                      'passphrase': from_account.password,
                      'account_key': from_account.key}
        )
        return self.is_tx_successful(tx_hash)

    def is_old_template_approved(self, template_id):
        """
        True if the template is approved.
        Use this for old style templates where template id is the address of a deployed template smart contract

        :param template_id: id of the template, str (contract address)
        :return: bool
        """
        return self.contract_concise.isTemplateApproved(template_id)

    def is_template_approved(self, template_id):
        """
        True if the template is approved.

        :param template_id: id of the template, str
        :return: bool
        """
        return self.contract_concise.isTemplateIdApproved(template_id)

    def get_num_templates(self):
        """
        Return the number of templates on-chain.

        :return: number of templates, int
        """
        return self.contract_concise.getTemplateListSize()
