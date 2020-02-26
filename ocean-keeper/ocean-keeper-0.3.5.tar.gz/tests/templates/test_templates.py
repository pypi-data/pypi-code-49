#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0
from ocean_keeper import Keeper
from ocean_keeper.templates.template_manager import TemplateStoreManager
from tests.resources.tiers import e2e_test


@e2e_test
def test_template():
    template_store_manager = TemplateStoreManager('TemplateStoreManager')
    assert template_store_manager.get_num_templates() == 2


@e2e_test
def test_default_templates():
    keeper = Keeper.get_instance()

    tm = keeper.template_manager
    access_template_name = tm.SERVICE_TO_TEMPLATE_NAME['access']
    compute_template_name = tm.SERVICE_TO_TEMPLATE_NAME['compute']
    access_id = tm.create_template_id(access_template_name)
    compute_id = tm.create_template_id(compute_template_name)
    # ids = [access_id, compute_id]
    assert tm.is_template_approved(access_id)
    assert tm.is_template_approved(compute_id)

    actor_ids = tm.get_template_actor_type_ids()
    for _id in actor_ids:
        type_value = tm.get_template_actor_type_value(_id)
        assert _id == tm.get_template_actor_type_id(type_value)
        assert 0 <= tm.get_template_actor_type_state(_id) <= 2

    template_values = tm.get_template(access_id)
    assert len(template_values.actor_type_ids) == 2
    assert tm.get_template_actor_type_value(template_values.actor_type_ids[0]) == 'provider'
    assert tm.get_template_actor_type_value(template_values.actor_type_ids[1]) == 'consumer'

    assert template_values.condition_types[0] == keeper.lock_reward_condition.address
    assert template_values.condition_types[1] == keeper.access_secret_store_condition.address
    assert template_values.condition_types[2] == keeper.escrow_reward_condition.address

    template_values = tm.get_template(compute_id)
    assert tm.get_template_actor_type_value(template_values.actor_type_ids[0]) == 'provider'
    assert tm.get_template_actor_type_value(template_values.actor_type_ids[1]) == 'consumer'

    assert template_values.condition_types[0] == keeper.lock_reward_condition.address
    assert template_values.condition_types[1] == keeper.compute_execution_condition.address
    assert template_values.condition_types[2] == keeper.escrow_reward_condition.address
