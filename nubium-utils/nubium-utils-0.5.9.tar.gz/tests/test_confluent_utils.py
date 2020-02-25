from unittest import TestCase
from unittest.mock import MagicMock, patch
from nubium_utils.confluent_utils import produce_message


class TestConfluentProducerUtils(TestCase):

    def setUp(self) -> None:
        self.env_patch = patch.dict(
            'os.environ',
            {"DO_METRICS_PUSHING": "False"}
        )
        self.mock_producer = MagicMock()
        self.mock_metrics_manager = MagicMock()
        self.env_patch.start()

    def tearDown(self) -> None:
        self.env_patch.stop()

    def test_produce_message(self):
        test_input = [
            self.mock_producer,
            dict(topic='test_topic',
                 key='blah_key',
                 value={'blah_value': 'blah_value'},
                 headers={'last_updated_by': 'sfdc'}),
            self.mock_metrics_manager,
            [('guid', b'112233'), ('last_updated_by', b'eloqua')]
        ]

        produce_message(*test_input)
        self.mock_producer.produce.assert_called_with(
            **dict(
                topic='test_topic',
                key='blah_key',
                value={'blah_value': 'blah_value'},
                headers={'guid': '112233', 'last_updated_by': 'sfdc'}))
