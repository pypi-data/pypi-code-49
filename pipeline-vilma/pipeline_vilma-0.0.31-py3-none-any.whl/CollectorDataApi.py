import json
import datetime
import requests
from loguru import logger
from pipelinevilma.Messager import Messager


class CollectorDataApi:
    STATUS_FOR_LABELING = 'labeling-required'
    STATUS_READY_FOR_TRAINING = 'readyForTraining'

    def __init__(self, data_api):
        self.base_url = str(data_api['base_url']) + ":" + str(data_api['port']) + "/"
        self.add_item_endpoint = str(data_api['endpoints']['add_item'])
        self.get_item_endpoint = str(data_api['endpoints']['get_item'])
        self.mark_trained_endpoint = str(data_api['endpoints']['mark_trained'])
        self.count_labeled_endpoint = str(data_api['endpoints']['count_labeled'])
        self.get_training_set_endpoint = str(data_api['endpoints']['get_training_set'])

        logger.info("Checking for enpoints...")
        logger.info(f"base_url: {self.base_url}")
        logger.info(f"add_item_endpoint: {self.add_item_endpoint}")
        logger.info(f"get_item_endpoint: {self.get_item_endpoint}")
        logger.info(f"mark_trained_endpoint: {self.mark_trained_endpoint}")
        logger.info(f"count_labeled_endpoint: {self.count_labeled_endpoint}")
        logger.info(f"get_training_set_endpoint: {self.get_training_set_endpoint}")
        logger.info("Success!")

    def _add_labeling_properties(self, message):
        message['createdAt'] = int(datetime.datetime.utcnow().strftime("%s"))
        message['status'] = CollectorDataApi.STATUS_FOR_LABELING
        return message

    def _insert_on_db(self, message):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        url = self.base_url + self.add_item_endpoint
        logger.debug(f"URL: {url}")
        res = requests.post(url, data=json.dumps(message), headers=headers)

        if not res:
            return False
        return res

    def add_item(self, message):
        # Include API data
        message = self._add_labeling_properties(message)
        api_response = self._insert_on_db(message)

        if not api_response:
            return False

        if api_response.status_code == 200:
            return True

        return False

    def get_item(self, item_id):
        url = self.base_url + self.get_item_endpoint
        url = url.replace("<ID>", item_id)
        res = requests.get(url)
        data = res.json()

        return (data['x']['data'], data['y']['true'])

    def mark_trained(self, item_id, status):
        data = {"status": status}

        url = self.base_url + self.mark_trained_endpoint
        url = url.replace("<ID>", item_id)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        res = requests.put(url, data=json.dumps(data), headers=headers)

    def get_training_data(self):
        url = self.base_url + self.get_training_set_endpoint
        res = requests.get(url)
        data = res.json()

        return data[CollectorDataApi.STATUS_READY_FOR_TRAINING]

    def count_labeled(self):
        url = self.base_url + self.count_labeled_endpoint
        res = requests.get(url)
        data = res.json()

        return data[CollectorDataApi.STATUS_READY_FOR_TRAINING]
