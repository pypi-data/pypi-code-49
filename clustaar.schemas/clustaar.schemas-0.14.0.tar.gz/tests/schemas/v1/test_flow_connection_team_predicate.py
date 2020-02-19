from clustaar.schemas.v1 import FLOW_CONNECTION_TEAM_PREDICATE
from clustaar.schemas.models import ConnectionTeamPredicate, IsOnlineCondition
import pytest


@pytest.fixture
def data():
    return {"type": "connection_team_predicate", "condition": {"type": "is_online"}}


@pytest.fixture
def predicate():
    return ConnectionTeamPredicate(condition=IsOnlineCondition())


class TestLoad(object):
    def test_returns_a_predicate(self, data, mapper):
        result = mapper.load(data, FLOW_CONNECTION_TEAM_PREDICATE)
        assert isinstance(result, ConnectionTeamPredicate)
        assert isinstance(result.condition, IsOnlineCondition)


class TestDump(object):
    def test_returns_a_dict(self, data, mapper, predicate):
        result = mapper.dump(predicate, FLOW_CONNECTION_TEAM_PREDICATE)
        assert result == data
