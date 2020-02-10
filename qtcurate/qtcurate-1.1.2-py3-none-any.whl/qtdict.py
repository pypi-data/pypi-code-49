from qtcurate.config import BASE_URL
import requests
import json
import os.path
from typing import Dict, List
from qtcurate.exceptions import QtArgumentError, QtDictError, QtConnectionError, QtRestApiError

dic_entries = "entries"
dic_name = "name" 


class QtDict:
    def __init__(self, api_key):
        self.session = requests.Session()
        self.headers = {"X-API-Key": api_key}
        self.temp_dict = dict()
        self.temp_dict[dic_entries] = []
        self.temp_dict[dic_name] = None
        self.url = BASE_URL + "dictionaries/"

    def name(self, name: str) -> None:
        """Create a new name for dictionary"""

        if isinstance(name, str):
            self.temp_dict[dic_name] = name
        else:
            raise QtArgumentError("Argument type error: String is expected as name")

    def entries(self, entry: Dict) -> None:
        """Create dictionary data"""

        if not isinstance(entry, Dict):
            raise QtArgumentError("Argument type error: QtDict is expected as entry")
        elif len(entry) != 2:
            raise QtArgumentError("Argument error: QtDict must have 2 element where keys are 'key' and 'value'."
                                  "Example {'key': 'some key', 'value': 'some value'} ")
        elif "key" not in entry.keys() or "value" not in entry.keys():
            raise QtArgumentError("Argument error: QtDict must have 2 element where keys are 'key' and 'value'."
                                  "Example {'key': 'some key', 'value': 'some value'} ")
        else:
            self.temp_dict[dic_entries].append(entry)

    def clear(self) -> None:
        """Remove all temporary data"""

        self.temp_dict[dic_entries] = []
        self.temp_dict[dic_name] = None

    def add_entry(self, key, value) -> None:
        """Create dictionary data"""

        if not isinstance(key, (str, int, float)):
            raise QtArgumentError("Argument type error: String, integer or float are expected as key")
        elif not isinstance(value, (str, int, float)):
            raise QtArgumentError("Argument type error: String, integer or float is expected as value")
        self.temp_dict[dic_entries].append({'key': key, 'value': value})

    def list(self) -> List:
        """List all dictionaries"""

        try:
            res = self.session.get(self.url, headers=self.headers)
        except requests.exceptions.RequestException as e:
            raise QtConnectionError(f"Connection error: {e}")
        if res.status_code not in [200, 201, 202]:
            raise QtRestApiError(f"HTTP error: Full authentication is required to access this resource. "
                                 f"HTTP status code: {res.status_code}. Server message: {res.json()}")
        return res.json()

    def fetch(self, index: str) -> Dict:
        """Fetch dictionary by ID"""

        if not isinstance(index, str):
            raise QtArgumentError("Argument type error: String is expected as index")
        try:
            res = self.session.get(self.url + index, headers=self.headers)
        except requests.exceptions.RequestException as e:
            raise QtConnectionError(f"Connection error: {e}")
        if res.status_code not in [200, 201, 202]:
            raise QtRestApiError(f"HTTP error: Full authentication is required to access this resource. "
                                 f"HTTP status code: {res.status_code}. Server message: {res.json()}")
        return res.json()

    def delete(self, index: str) -> bool:
        """Delete existing dictionary"""

        if not isinstance(index, str):
            raise QtArgumentError("Argument type error: String is expected as index")
        try:
            res = self.session.delete(self.url + index, headers=self.headers)
        except requests.exceptions.RequestException as e:
            raise QtConnectionError(f"Connection error: {e}")
        if res.status_code not in [200, 201, 202, 204]:
            raise QtRestApiError(f"HTTP error: Full authentication is required to access this resource. "
                                 f"HTTP status code: {res.status_code}. Server message: {res.json()}")
        return res.ok

    def create(self) -> Dict:
        """Create dictionary data"""

        if self.temp_dict[dic_name] is None:
            raise QtDictError("QtDict error: Please add name using name function")
        if len(self.temp_dict[dic_entries]) == 0:
            raise QtDictError("QtDict error: Please add dictionary using add_entry function")
        data = {'name': self.temp_dict[dic_name], 'entries': self.temp_dict[dic_entries]}
        self.headers['Content-Type'] = 'application/json'
        try:
            res = self.session.post(self.url, headers=self.headers, data=json.dumps(data))
        except requests.exceptions.RequestException as e:
            raise QtConnectionError(f"Connection error: {e}")
        if res.status_code not in [200, 201, 202]:
            raise QtRestApiError(f"HTTP error: Full authentication is required to access this resource. "
                                 f"HTTP status code: {res.status_code}. Server message: {res.json()}")
        return res.json()

    def update(self, index: str) -> bool:
        """Update existing dictionary"""

        if not isinstance(index, str):
            raise QtArgumentError("Argument type error: String is expected as index")
        if self.temp_dict[dic_name] is None:
            raise QtDictError("QtDict error: Please add name using name function")
        if len(self.temp_dict[dic_entries]) == 0:
            raise QtDictError("QtDict error: Please add dictionary using add_entry function")
        data = {'name': self.temp_dict[dic_name], 'entries': self.temp_dict[dic_entries]}
        try:
            res = self.session.put(self.url + index, headers=self.headers, data=json.dumps(data))
        except requests.exceptions.RequestException as e:
            raise QtConnectionError(f"Connection error: {e}")
        if res.status_code not in [200, 201, 202]:
            raise QtRestApiError(f"HTTP error: Full authentication is required to access this resource. "
                                 f"HTTP status code: {res.status_code}. Server message: {res.json()}")
        return res.ok

    def upload(self, file: str, name: str) -> Dict:
        """Upload dictionary data from TSV files"""

        if not isinstance(file, str):
            raise QtArgumentError("Argument type error: String is expected as file")
        if not isinstance(name, str):
            raise QtArgumentError("Argument type error: String is expected as name")
        extension = os.path.splitext(file)[1].lower()
        if extension != ".tsv":
            raise QtArgumentError("Argument type error: TSV file expected")
        if not os.path.exists(file):
            raise QtArgumentError(f"Argument error: File {file} does not exist")
        files = {
            'name': (None, name),
            'file': open(file, 'rb')
        }
        try:
            res = self.session.post(self.url + "upload", headers=self.headers, files=files)
        except requests.exceptions.RequestException as e:
            raise QtConnectionError(f"Connection error: {e}")
        if res.status_code not in [200, 201, 202]:
            raise QtRestApiError(f"HTTP error: Full authentication is required to access this resource. "
                                 f"HTTP status code: {res.status_code}. Server message: {res.json()}")
        return res.json()

    def __repr__(self):
        return str({'name': self.temp_dict[dic_name], 'entries': self.temp_dict[dic_entries]})
