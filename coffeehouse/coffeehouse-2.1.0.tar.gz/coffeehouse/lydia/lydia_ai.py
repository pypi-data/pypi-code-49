from coffeehouse.exception import CoffeeHouseError
from coffeehouse.lydia.session import Session
from coffeehouse.api import API

import json
import requests


class LydiaAI:

    def __init__(self, coffeehouse_api):
        """
        Public constructor for Lydia

        :type coffeehouse_api: API
        """

        self.api = coffeehouse_api

    def create_session(self, language="en"):
        """
        Creates a new Session with the AI

        :type language: str
        :param language: The language that this session will be based in
        :raises: CoffeeHouseError
        :returns: A ``Session`` object
        :rtype: Session
        """

        request_payload = {
            "access_key": self.api.access_key,
            "target_language": language
        }

        response = requests.post("{0}/v1/lydia/session/create".format(self.api.endpoint), request_payload)
        CoffeeHouseError.raise_for_status(response.status_code, response.text)
        return Session(json.loads(response.text)["payload"], self)

    def get_session(self, session_id):
        """
        Gets an existing session using a Session ID

        :type session_id: int
        :param session_id: The ID of the session to retrieve
        :raises: CoffeeHouseError
        :returns: A ``Session`` object
        :rtype: Session
        """

        request_payload = {
            "access_key": self.api.access_key,
            "session_id": session_id
        }

        response = requests.post("{0}/v1/lydia/session/get".format(self.api.endpoint), request_payload)
        CoffeeHouseError.raise_for_status(response.status_code, response.text)
        return Session(json.loads(response.text)["payload"], self)

    def think_thought(self, session_id, text):
        """
        Processes user input and returns an AI text Response

        :param session_id:
        :type text: str
        :param text: The user input
        :raises: CoffeeHouseError
        :returns: The json payload of the response
        :rtype: str
        """

        request_payload = {
            "access_key": self.api.access_key,
            "session_id": session_id,
            "input": text
        }

        response = requests.post("{0}/v1/lydia/session/think".format(self.api.endpoint),
                                 request_payload)
        CoffeeHouseError.raise_for_status(response.status_code, response.text)
        return json.loads(response.text)["payload"]["output"]
