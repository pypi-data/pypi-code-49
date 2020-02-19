from clustaar.schemas.v1 import SEND_SIMPLE_CARDS_ACTIONS
from clustaar.schemas.models import OpenURLAction, Button, SimpleCard, SendSimpleCardsAction
import pytest


@pytest.fixture
def button():
    return Button(title="view", action=OpenURLAction(url="http://view.org"))


@pytest.fixture
def card(button):
    return SimpleCard(
        title="Card 1", subtitle="xxx", image_url="http://example.com/logo.png", buttons=[button]
    )


@pytest.fixture
def action(card):
    return SendSimpleCardsAction(cards=[card])


@pytest.fixture
def data(card):
    return {
        "type": "send_simple_cards_action",
        "cards": [
            {
                "type": "simple_card",
                "title": card.title,
                "subtitle": card.subtitle,
                "imageURL": card.image_url,
                "buttons": [
                    {
                        "type": "open_url_button",
                        "title": "view",
                        "action": {"type": "open_url_action", "url": "http://view.org"},
                    }
                ],
            }
        ],
    }


@pytest.fixture
def malicious_data(card):
    return {
        "type": "send_simple_cards_action",
        "cards": [
            {
                "type": "simple_card",
                "title": "<script>void();</script>Card 1",
                "subtitle": card.subtitle,
                "imageURL": card.image_url,
                "buttons": [
                    {
                        "type": "open_url_button",
                        "title": "<script>void();</script>Share",
                        "action": {"type": "open_url_action", "url": "http://view.org"},
                    }
                ],
            }
        ],
    }


class TestDump:
    def test_returns_a_dict(self, action, data, mapper):
        result = SEND_SIMPLE_CARDS_ACTIONS.dump(action, mapper)
        assert result == data


class TestLoad:
    def test_returns_an_action(self, data, mapper):
        action = mapper.load(data, SEND_SIMPLE_CARDS_ACTIONS)
        assert isinstance(action, SendSimpleCardsAction)
        card = action.cards[0]
        assert card.title == "Card 1"
        assert card.subtitle == "xxx"
        assert card.image_url == "http://example.com/logo.png"
        button = card.buttons[0]
        assert button.title == "view"
        assert isinstance(button.action, OpenURLAction)

    def test_returns_an_action_malicious(self, malicious_data, mapper):
        action = mapper.load(malicious_data, SEND_SIMPLE_CARDS_ACTIONS)
        assert isinstance(action, SendSimpleCardsAction)
        card = action.cards[0]
        assert card.title == "&lt;script&gt;void();&lt;/script&gt;Card 1"

        button = card.buttons[0]
        assert button.title == "&lt;script&gt;void();&lt;/script&gt;Share"
        assert isinstance(button.action, OpenURLAction)
