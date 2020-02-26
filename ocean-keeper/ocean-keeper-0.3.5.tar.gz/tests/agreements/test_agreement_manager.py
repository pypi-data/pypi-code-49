import uuid

from ocean_keeper import Keeper
from ocean_keeper.web3_provider import Web3Provider
from tests.resources.helper_functions import get_publisher_account, get_consumer_account


def _new_id():
    return '0x' + uuid.uuid4().hex + uuid.uuid4().hex


def test_create_agreement():
    keeper = Keeper.get_instance()
    w3 = Web3Provider.get_web3()
    pub_acc = get_publisher_account()
    cons_acc = get_consumer_account()

    # register did
    did = _new_id()
    keeper.did_registry.register(did, w3.toBytes(0), f'/resolve/asset/{did}', pub_acc)

    # create agreement
    agr_id = _new_id()

    num_agreements = keeper.agreement_manager.get_num_agreements()

    template_mgr = keeper.template_manager
    template_id = template_mgr.create_template_id(template_mgr.SERVICE_TO_TEMPLATE_NAME['access'])
    assert template_mgr.is_template_approved(template_id), '`access` agreement template is not approved.'

    template = keeper.template_manager.get_template(template_id)
    actor_types = [template_mgr.get_template_actor_type_value(_id) for _id in template.actor_type_ids]
    actor_type_map = {'provider': pub_acc.address, 'consumer': cons_acc.address}
    actors = [actor_type_map[actor_type] for actor_type in actor_types]

    access_id = keeper.access_secret_store_condition.generate_id(agr_id, ['bytes32', 'address'], [did, cons_acc.address]).hex()
    lock_id = keeper.lock_reward_condition.generate_id(agr_id, ['address', 'uint256'], [keeper.escrow_reward_condition.address, 100]).hex()
    reward_id = keeper.escrow_reward_condition.generate_id(
        agr_id,
        ['uint256', 'address', 'address', 'bytes32', 'bytes32'],
        [100, pub_acc.address, cons_acc.address, lock_id, access_id]
    ).hex()
    condition_types = template.condition_types
    condition_type_map = {
        keeper.access_secret_store_condition.address: (keeper.access_secret_store_condition, access_id),
        keeper.lock_reward_condition.address: (keeper.lock_reward_condition, lock_id),
        keeper.escrow_reward_condition.address: (keeper.escrow_reward_condition, reward_id)
    }
    ctm = condition_type_map
    condition_ids = [ctm[ct][1] for ct in condition_types]
    keeper.agreement_manager.create_agreement(
        agr_id,
        did,
        template_id,
        condition_ids,
        [0, 0, 0],
        [0, 0, 0],
        actors,
        cons_acc
    )

    # verify AgreementCreated event
    event = keeper.agreement_manager.subscribe_agreement_created(agr_id, 15, None, [], wait=True)
    assert event, f'agreement created event not found.'
    # verify agreement attributes on-chain
    agreement_values = keeper.agreement_manager.get_agreement(agr_id)
    assert agreement_values.template_id == template_id, f'templateId {template_id} does not match'
    assert agreement_values.condition_ids == condition_ids, f''
    assert agreement_values.owner == pub_acc.address

    # verify AgreementActorAdded events
    events = keeper.agreement_manager.get_event_filter_for_agreement_actor(
        cons_acc.address, from_block=agreement_values.block_number_updated).get_all_entries()
    assert events, f'no actor added event for consumer'
    assert events[0].args.actor == cons_acc.address
    # and for the publisher, use the old interface
    events = keeper.agreement_manager.get_event_filter_for_agreement_created(
        pub_acc.address, from_block=agreement_values.block_number_updated).get_all_entries()
    assert events, f'no actor added event for publisher'
    assert events[0].args.actor == pub_acc.address

    assert (num_agreements + 1) == keeper.agreement_manager.get_num_agreements()
    assert keeper.agreement_manager.get_agreement_did_owner(agr_id) == pub_acc.address
    assert keeper.agreement_manager.get_agreement_did_owner(agr_id[:-3] + '012') is None
