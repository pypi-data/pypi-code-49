import html
import requests


class Importer:

    def __init__(self, session: requests.Session):
        self.session = session
        self.hostname = self.session.headers.get('origin')

    def force_pickup(self) -> requests.Response:
        """
        Trigger a force pickup.

        Parameters
        ----------
        verbose : bool
            When True, the
        """
        url = f"https://{self.hostname}/manage/service/import?cmd=pickup"
        response = self.session.get(url, stream=True, hooks={'response': print_response})
        response.raise_for_status()
        return response

    def force_import(self) -> requests.Response:
        """
        Trigger a force import.
        """
        url = f"http://{self.hostname}/manage/import/load?cmd=process"
        response = self.session.get(url, stream=True, hooks={'response': print_response})
        response.raise_for_status()
        return response

def print_response(response: requests.Response):
    for line in response.iter_lines(decode_unicode=True):
        if line:
            print(html.unescape(line).replace('<br />', '\n'))
