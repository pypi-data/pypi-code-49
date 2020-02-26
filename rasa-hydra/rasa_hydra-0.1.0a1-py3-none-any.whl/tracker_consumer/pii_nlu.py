from os import environ

from rasa.core.interpreter import NaturalLanguageInterpreter
from rasa.core.utils import AvailableEndpoints

_endpoints = AvailableEndpoints.read_endpoints("rasa-app-data/{}".format(environ['ENDPOINTS_FILE']))


class PiiNlu:
    """
    Remove PII using the nlu
    Currently disabled
    """
    def __init__(self):
        # self.pii_nlu = NaturalLanguageInterpreter.create("default/pii", _endpoints.nlu)
        self.actions = []
        self.pii_intents = [
            "username",
            "password",
            "phone",
            "address",
            "zipcode",
            "name",
            "CCN",
        ]

    def set_actions(self, actions):
        """
        Set the list of actions so far in history
        """
        self.actions = actions

    # def _remove_pii(self, message):
    #     """
    #     Removes pii using the NLU component
    #     """
    #     if message[0] == "/":
    #         return message
    #
    #     output = self.pii_nlu.parse(message)
    #     if output["intent"]["name"] == "pii":
    #         if not output["entities"]:
    #             message = "[pii]"
    #         else:
    #             replacements = {}
    #             for entity in output["entities"]:
    #                 replacements[message[entity["start"] : entity["end"]]] = entity[
    #                     "entity"
    #                 ]
    #                 if entity["confidence"] < 0.5:
    #                     return "[pii]"
    #             for key in replacements:
    #                 pii_cover = "[{0}]".format(replacements[key])
    #                 message = message.replace(key, pii_cover)
    #     return message

    def should_clean(self):
        """
        Checks if the last active state was an authentication state
        If so, the information should be redacted
        """
        if len(self.actions) > 1:
            while self.actions[-1] in ['action_handle_error', 'action_asr_fallback']:
                self.actions.pop()

            return self.actions[-1].startswith(environ["AUTHENTICATION_STATE"])
        return False

    def clean_message(self, message):
        """
        Cleans message, checks if we're in an authentication state
        if so, clean the input

        If we need to remove some pii from the middle of a statement
        and we dont have the state, then we can use _remove_pii.
        This checks for information that looks like PII information,
        and plucks it out. Hopefully replacing it with the type of info removed.
        """
        if self.should_clean():
            return "{authentication}"

        # return self._remove_pii(message)
        return message