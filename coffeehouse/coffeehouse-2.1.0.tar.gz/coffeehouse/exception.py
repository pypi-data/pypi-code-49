import json


class CoffeeHouseError(Exception):
    """
    Exception raised by API errors.
    The exception message is set to the server's response.

    :param status_code: Status code returned by the server
    :type status_code: int
    :param message: Response content returned by the server
    :type message: string
    """
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content
        try:
            self.message = json.loads(content).get("message", None)
        except json.decoder.JSONDecodeError:
            self.message = "Unknown"
        super().__init__(self.message or content)

    @staticmethod
    def raise_for_status(status_code, message):
        if status_code != 200:
            raise _mapping.get(status_code,
                               CoffeeHouseError)(status_code, message)


class ApiSuspendedError(CoffeeHouseError):
    pass


class InvalidApiKeyError(CoffeeHouseError):
    pass


class AIError(CoffeeHouseError):
    pass


class SessionInvalidError(CoffeeHouseError):
    pass


class SessionNotFoundError(CoffeeHouseError):
    pass


_mapping = {
            400: SessionInvalidError,
            401: InvalidApiKeyError,
            403: ApiSuspendedError,
            404: SessionNotFoundError,
            503: AIError
           }
