import pytest
from clustaar.schemas.models import CustomerSatisfactionCallbackAction, StepTarget
from tests.utils import MAPPER
from lupin.errors import InvalidDocument


@pytest.fixture
def callback():
    return CustomerSatisfactionCallbackAction(
        kind="positive", target=StepTarget(step_id="a1" * 12, name="a step")
    )


@pytest.fixture
def data():
    return {
        "type": "customer_satisfaction_callback_action",
        "kind": "positive",
        "target": {"type": "step", "id": "a1" * 12, "name": "a step"},
    }


class TestDump:
    def test_returns_a_dict(self, data, callback):
        result = MAPPER.dump(callback, "customer_satisfaction_callback_action")
        assert result == data


class TestLoad:
    def test_returns_an_object(self, data):
        result = MAPPER.load(data, "customer_satisfaction_callback_action")
        assert isinstance(result, CustomerSatisfactionCallbackAction)
        assert result.kind == "positive"
        assert isinstance(result.target, StepTarget)
        assert result.target.step_id == "a1" * 12


class TestValidate:
    def test_render_error_if_invalid(self, data):
        data["kind"] = "toto"

        with pytest.raises(InvalidDocument):
            MAPPER.validate(data, "customer_satisfaction_callback_action")

    def test_doesnt_raise_if_valid(self, data):
        MAPPER.validate(data, "customer_satisfaction_callback_action")
