"""Keeper agreements sub-module."""
#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0
import logging
from collections import namedtuple

from eth_utils import add_0x_prefix
from web3.contract import ContractEvent
from web3.exceptions import MismatchedABI

from ocean_keeper import ContractBase
from ocean_keeper.event_filter import EventFilter
from ocean_keeper.web3_provider import Web3Provider

logger = logging.getLogger(__name__)


AgreementValues = namedtuple(
    'AgreementValues',
    ('did', 'owner', 'template_id', 'condition_ids', 'updated_by', 'block_number_updated')
)


class AgreementStoreManager(ContractBase):
    """Class representing the AgreementStoreManager contract."""
    CONTRACT_NAME = 'AgreementStoreManager'
    AGREEMENT_CREATED_EVENT = 'AgreementCreated'
    AGREEMENT_ACTOR_ADDED_EVENT = 'AgreementActorAdded'

    agreement_actor_added_event_abi = {
        "abi": [{
          "anonymous": False,
          "inputs": [
            {
              "indexed": True,
              "name": "agreementId",
              "type": "bytes32"
            },
            {
              "indexed": True,
              "name": "actor",
              "type": "address"
            }
          ],
          "name": "AgreementActorAdded",
          "type": "event"
    }]}

    def create_agreement(
            self,
            agreement_id,
            did,
            template_id,
            condition_ids,
            time_locks,
            time_outs,
            actors,
            account
    ):
        """
        Create a new agreement.
        The agreement will create conditions of conditionType with conditionId.
        Only "approved" templates can access this function.
        :param agreement_id:id of the agreement, hex str
        :param did: DID of the asset. The DID must be registered beforehand, bytes32
        :param template_id: hex str of bytes32 that is the id of an approved agreement template
        :param condition_ids: is a list of bytes32 content-addressed Condition IDs, bytes32
        :param time_locks: is a list of uint time lock values associated to each Condition, int
        :param time_outs: is a list of uint time out values associated to each Condition, int
        :param actors: list of ethereum addresses of each of the actors in this agreement. The
            order of actors should match the order defined in the template
        :return: bool
        """
        tx_hash = self.send_transaction(
            'createAgreement',
            (agreement_id,
             did,
             template_id,
             condition_ids,
             time_locks,
             time_outs,
             actors),
            transact={'from': account.address,
                      'passphrase': account.password,
                      'account_key': account.key},
        )
        return self.is_tx_successful(tx_hash)

    def get_agreement(self, agreement_id):
        """
        Retrieve the agreement for a agreement_id.

        :param agreement_id: id of the agreement, hex str
        :return: the agreement attributes.
        """
        agreement = self.contract_concise.getAgreement(agreement_id)
        if agreement and len(agreement) == 6:
            agreement = AgreementValues(*agreement)
            did = add_0x_prefix(agreement.did.hex())
            cond_ids = [add_0x_prefix(_id.hex()) for _id in agreement.condition_ids]

            return AgreementValues(
                did,
                agreement.owner,
                add_0x_prefix(agreement.template_id.hex()),
                cond_ids,
                agreement.updated_by,
                agreement.block_number_updated
            )

        return None

    def get_agreement_did_owner(self, agreement_id):
        """Get the DID owner for this agreement with _id.

        :param agreement_id: id of the agreement, hex str
        :return: the DID owner associated with agreement.did from the DID registry.
        """
        return self.contract_concise.getAgreementDIDOwner(agreement_id)

    def get_num_agreements(self):
        """Return the size of the Agreements list.

        :return: the length of the agreement list, int
        """
        return self.contract_concise.getAgreementListSize()

    def subscribe_agreement_created(self, agreement_id, timeout, callback, args, wait=False,
                                    from_block='latest', to_block='latest'):
        """
        Subscribe to an AgreementCreated event matching the given `agreement_id`.

        :param agreement_id: hex str -- id of the agreement
        :param timeout: int -- time in seconds to wait for the event
        :param callback: function callback when the
        :param args:
        :param wait: bool -- if true block the listener until the event is fetched,
            else return immediately and process the event in the background
        :param from_block: int or None -- the block number to start searching for matching events
        :param to_block: int or None -- the block number to end searching for matching events
        :return: event (dict) if blocking is True and an event is received, otherwise returns None

        """
        logger.debug(
            f'Subscribing {self.AGREEMENT_CREATED_EVENT} event '
            f'with agreement id {agreement_id}.'
        )
        return self.subscribe_to_event(
            self.AGREEMENT_CREATED_EVENT,
            timeout,
            {'agreementId': Web3Provider.get_web3().toBytes(hexstr=agreement_id)},
            callback=callback,
            args=args,
            wait=wait,
            from_block=from_block,
            to_block=to_block
        )

    def _get_contract_agreement_actor_added_event(self):
        try:
            event = getattr(self.events, self.AGREEMENT_ACTOR_ADDED_EVENT, None)
        except MismatchedABI:
            event = None

        if not event:
            event = ContractEvent.factory(
                self.AGREEMENT_ACTOR_ADDED_EVENT,
                web3=Web3Provider.get_web3(),
                contract_abi=self.agreement_actor_added_event_abi['abi'],
                address=self.address,
                event_name=self.AGREEMENT_ACTOR_ADDED_EVENT)

        return event

    def get_event_filter_for_agreement_created(self, provider_address=None, from_block='latest',
                                               to_block='latest'):
        return self.get_event_filter_for_agreement_actor(provider_address, from_block, to_block)

    def get_event_filter_for_agreement_actor(self, actor_address, from_block='latest', to_block='latest'):
        """
        :param actor_address: hex str ethereum address of actor
        :param from_block: int or None
        :param to_block: int or None
        :return:
        """

        _filter = {}
        if actor_address:
            assert isinstance(actor_address, str)
            _filter['actor'] = actor_address

        event_filter = EventFilter(
            self.AGREEMENT_ACTOR_ADDED_EVENT,
            self._get_contract_agreement_actor_added_event(),
            _filter,
            from_block=from_block,
            to_block=to_block
        )
        event_filter.set_poll_interval(0.5)
        return event_filter
