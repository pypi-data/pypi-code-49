from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.trackers import DialogueStateTracker
from rasa_core.constants import FALLBACK_SCORE
from rasa_core.actions.action import ACTION_LISTEN_NAME
from rasa_core.domain import Domain
from typing import List, Text
import logging

logger = logging.getLogger(__name__)


from rasa_core.events import (
    UserUttered, ActionExecuted,
    Event, SlotSet, Restarted, ActionReverted, UserUtteranceReverted,
    BotUttered, Form)

class FormFallbackPolicy(FallbackPolicy):
    """Policy which predicts fallback actions.

    A fallback can be triggered by a low confidence score on a
    NLU prediction or by a low confidence score on an action
    prediction. """

    def should_fallback(self,
                        nlu_confidence: float,
                        last_action_name: Text) -> bool:
        """It should predict fallback action only if
        a. predicted NLU confidence is lower than ``nlu_threshold`` &&
        b. last action is NOT fallback action
        """
        return (nlu_confidence < self.nlu_threshold and
                last_action_name != self.fallback_action_name)

    def get_confidence(self, events):
        active_form = None
        for event in events:
            if isinstance(event, UserUttered):
                if active_form not in ('authentication_form', 'feedback_form'):
                    form_latest_message = event
            elif isinstance(event, Form):
                active_form = event.name

        nlu_data = form_latest_message.parse_data
        return nlu_data["intent"].get("confidence", 1.0)


    def predict_action_probabilities(self,
                                     tracker: DialogueStateTracker,
                                     domain: Domain) -> List[float]:
        """Predicts a fallback action if NLU confidence is low
            or no other policy has a high-confidence prediction"""

        end_states = ['utter_transfer', 'utter_ok_else', 'utter_bye']

        if tracker.latest_action_name == self.fallback_action_name:
            result = [0.0] * domain.num_actions
            if tracker.get_slot('errors') > 2:
                idx = domain.index_for_action('utter_transfer')
                result[idx] = 1.3
            else:
                idx = domain.index_for_action(ACTION_LISTEN_NAME)
                result[idx] = 1.3
                return result

        if tracker.latest_action_name in end_states:
            result = self.fallback_scores(domain, self.core_threshold)
            return result

        nlu_confidence = self.get_confidence(tracker.applied_events())
        if self.should_fallback(nlu_confidence, tracker.latest_action_name):
            result = self.fallback_scores(domain, 1.1)
            return result

        # NLU confidence threshold is met, so
        # predict fallback action with confidence `core_threshold`
        # if this is the highest confidence in the ensemble,
        # the fallback action will be executed.
        result = self.fallback_scores(domain, self.core_threshold)
        return result
