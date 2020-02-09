from abc import ABC, abstractmethod
import requests
import json
import urllib
import base64
import copy

class UpdateClient(ABC):
    """Serves as a baseclass for all the api-clients.
    Also provides a way to transform response returned by API to labelsync format and vice-versa.
    """

    def __init__(self, owner, repo, token, url, session):
        self.owner = owner
        self.repo = repo
        self.token = token
        self.url = url
        self.session = session

    @abstractmethod
    def ping_repo(self):
        """Call a GET or HEAD on the repository. Successful ping must return 200.

            :return: requests.Response object

        """
        pass

    @abstractmethod
    def read_labels(self):
        """Return list of all the labels present. If paging is supported, this method must use it to combine all the pages to one list.

            :return: list of labels as returned by the service
        """
        pass

    @abstractmethod
    def add_label(self, label):
        """Add new label to repository.

            :param label: label in service format
            :return: requests.Response object
        """
        pass

    @abstractmethod
    def delete_label(self, label):
        """Delete label from repository.

            :param label string: label id defined by service
            :return: requests.Response object

        """
        pass

    @abstractmethod
    def update_label(self, label):
        """Update label in repository.

            :param label: label in service format
            :return: requests.Response object
        """
        pass

    @abstractmethod
    def map_to_create(self, label):
        """Turn labelsync representation to service representation.

            :param label: label in labelsync format
            :return: label in service format
        """
        pass

    @abstractmethod
    def map_to_update(self, label):
        """Turn labelsync representation to service representation suited for update.

            :param label: label in labelsync format
            :return: label in service format for update
        """
        pass

    @abstractmethod
    def map_from_response(self, label):
        """Turn service format to labelsync format.

            :param label: label in service format
            :return: label in labelsync format
        """
        pass


class GithubClient(UpdateClient):
    """Http client for connecting to github. It's method implement github api.
    """
    def __init__(self, owner, repo, token, url, session):
        super().__init__(owner, repo, token, url, session)
        self.service = 'github'
        self.session.headers.update({"Authorization": f"token {self.token}"})

    def read_labels(self):
        result = []
        response = self.session.get(f"{self.url}/repos/{self.owner}/{self.repo}/labels")
        response.raise_for_status()
        while True:
            labels = response.json()
            for label in labels:
                result.append(label)
            if "next" not in response.links:
                break
            response = self.session.get(response.links["next"]["url"])
            response.raise_for_status()
        return result

    def add_label(self, label):
        return self.session.post(f"{self.url}/repos/{self.owner}/{self.repo}/labels", json=label)

    def update_label(self, label, id):
        return self.session.patch(f"{self.url}/repos/{self.owner}/{self.repo}/labels/{urllib.parse.quote(id, safe='')}", json=label)

    def delete_label(self, id):
        return self.session.delete(f"{self.url}/repos/{self.owner}/{self.repo}/labels/{urllib.parse.quote(id, safe='')}")

    def ping_repo(self):
        return self.session.head(f"{self.url}/repos/{self.owner}/{self.repo}")

    def map_to_create(self, label):
        return label

    def map_to_update(self, label):
        return {"new_name": label["name"], "color": label["color"], "description": label["description"]}

    def map_from_response(self, label):
        return {"name": label["name"], "color": label["color"], "description": label["description"]}

class GithubMasterClient(GithubClient):

    def __init__(self, owner, repo, token, url, secret, session):
        super().__init__(owner, repo, token, url, session)
        self.secret = secret

    def get_file(self, filename):
        response = self.session.get(f"{self.url}/repos/{self.owner}/{self.repo}/contents/{filename}")
        response.raise_for_status()
        return response

    def create_repo(self):

        repo = {"name": self.repo, "description": "Master repository for labelsync."}
        response = self.session.post(f"{self.url}/user/repos", json=repo)
        response.raise_for_status()
        return response

    def update_file(self, filename, contents, sha, commit_message):
        transfer_object = {
            "message": commit_message,
            "content": contents,
            "sha": sha
        }

        response = self.session.put(f"{self.url}/repos/{self.owner}/{self.repo}/contents/{filename}", json=transfer_object)
        response.raise_for_status()
        return response

    def upload_file(self, filename, contents, commit_message):

        transfer_object = {
            "message": commit_message,
            "content": contents,
        }

        response = self.session.put(f"{self.url}/repos/{self.owner}/{self.repo}/contents/{filename}", json=transfer_object)
        response.raise_for_status()
        return response

    def set_webhook(self, url, secret=None):
        config = {
            "url": url,
            "content_type": "json",
        }
        if secret is not None:
            config["secret"] = secret
        payload = {
            "config": config
        }
        response = self.session.post(f"{self.url}/repos/{self.owner}/{self.repo}/hooks", json=payload)
        response.raise_for_status()
        return response

    def map_content_to_string(self, raw_file_response):
        return base64.b64decode(raw_file_response.json()['content']).decode()

class GitlabClient(UpdateClient):

    def __init__(self, owner, repo, token, url, session):
        super().__init__(owner, repo, token, url, session)
        self.session.headers.update({"Private-Token": f"{self.token}"})
        self.reposlug = urllib.parse.quote(f"{self.owner}/{self.repo}", safe='')
        self.service = 'gitlab'

    def read_labels(self):
        result = []
        response = self.session.get(f"{self.url}/api/v4/projects/{self.reposlug}/labels")
        while True:
            labels = response.json()
            for label in labels:
                result.append(label)
            if "next" not in response.links:
                break
            response = self.session.get(response.links["next"]["url"])
        return result

    def add_label(self, label):
        return self.session.post(f"{self.url}/api/v4/projects/{self.reposlug}/labels", json=label)

    def update_label(self, label, id):
        return self.session.put(f"{self.url}/api/v4/projects/{self.reposlug}/labels/?name={urllib.parse.quote(id, safe='')}", json=label)

    def delete_label(self, id):
        return self.session.delete(f"{self.url}/api/v4/projects/{self.reposlug}/labels?name={urllib.parse.quote(id, safe='')}")

    def ping_repo(self):
        return self.session.head(f"{self.url}/api/v4/projects/{self.reposlug}")

    def map_to_create(self, label):
        label_to = copy.deepcopy(label)
        label_to["color"] = '#' + label["color"]
        return label_to

    def map_to_update(self, label):
        return {"new_name": label["name"], "color": "#" + label["color"], "description": label["description"]}

    def map_from_response(self, label):
        return {"name": label["name"], "color": label["color"].split('#')[1], "description": label["description"]}
