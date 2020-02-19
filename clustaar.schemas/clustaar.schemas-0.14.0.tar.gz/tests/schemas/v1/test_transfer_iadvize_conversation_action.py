from clustaar.schemas.v1 import TRANSFER_IADVIZE_CONVERSATION_ACTION
from clustaar.schemas.models import TransferIAdvizeConversationAction, IAdvizeDistributionRule
import pytest


@pytest.fixture
def action():

    return TransferIAdvizeConversationAction(
        failed_transfer_message="sorry",
        distribution_rule=IAdvizeDistributionRule(id="234", label="Human"),
    )


@pytest.fixture
def data():
    return {
        "type": "transfer_iadvize_conversation_action",
        "failed_transfer_message": "sorry",
        "distribution_rule": {"id": "234", "label": "Human"},
    }


class TestDump(object):
    def test_returns_a_dict(self, action, data, mapper):
        result = TRANSFER_IADVIZE_CONVERSATION_ACTION.dump(action, mapper)
        assert result == data


class TestLoad(object):
    def test_returns_an_action(self, data, mapper):
        action = mapper.load(data, TRANSFER_IADVIZE_CONVERSATION_ACTION)
        assert isinstance(action, TransferIAdvizeConversationAction)
