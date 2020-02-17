import uuid

from contribution.models import Payer, Premium


def create_test_premium(policy_id, with_payer=True, custom_props=None):
    payer = create_test_payer() if with_payer else None

    premium = Premium.objects.create(
        **{
            "policy_id": policy_id,
            "payer_id": payer.id if payer else None,
            "amount": 1000,
            "receipt": "Test receipt",
            "pay_date": "2019-01-01",
            "pay_type": Payer.PAYER_TYPE_OTHER,
            "validity_from": "2019-01-01",
            "audit_user_id": -1,
            **(custom_props if custom_props else {})
        }
    )

    return premium


def create_test_payer(payer_type=Payer.PAYER_TYPE_OTHER, custom_props=None):
    payer = Payer.objects.create(
        **{
            "payer_type": payer_type,
            "uuid": uuid.uuid4(),
            "payer_name": "Test Default Payer Name",
            "payer_address": "Test street name 123, CZ9204 City, Country",
            "validity_from": "2019-01-01",
            "audit_user_id": -1,
            **(custom_props if custom_props else {})
        }
    )
    return payer
