from ._version import __version__
from inscribe.errors import InscribeAPIException
from inscribe.pusher import PusherFactory
from requests import HTTPError
import datetime
import inscribe.config as inscribe_config
import json
import logging
import os
import requests
import urllib
import threading
import atexit

try:
    ENVIRONMENT = os.environ['INSCRIBE_PYTHON_ENV']
except KeyError:
    ENVIRONMENT = 'production'

logger = logging.getLogger("inscribe-api")
config = inscribe_config.config
MS_IN_SECOND = 1000
SECONDS_IN_AN_HOUR = 3600
TIMEOUT_MS = MS_IN_SECOND * SECONDS_IN_AN_HOUR
CHECK_QUEUE_INTERVAL = 10
DEFAULT_API_VERSION = 2
CONFIG = config[ENVIRONMENT]['api']


class Client(object):
    def __init__(self, api_key: str, user_id: str, timeout: int = TIMEOUT_MS,
                 check_queue_interval: int = CHECK_QUEUE_INTERVAL, version: int = None,
                 async_enabled: bool = False, host: str = CONFIG['url']):
        logger.info("Instantiate API class")

        self._version = version or DEFAULT_API_VERSION
        self.session = requests.Session()
        self.api_key = api_key
        self.domain_url = host
        self.user_id = user_id
        self.pusher_enabled = async_enabled

        if self.pusher_enabled is True:
            self.channel = PusherFactory(
                api_key=self.api_key,
                base_url=self.base_url,
                pusher_key=CONFIG['pusher_key'],
                user_id=self.user_id
            ).get_pusher_channel()
            self.queue = []
            self.check_queue_interval = check_queue_interval
            self._check_queue()
            atexit.register(self.stop_queue_check)

        self.timeout = timeout
        self.token = None

    def create_customer(self, name: str) -> dict:
        """
        Creates a customer object.

        :param name: A unique name for the customer
        """
        url = "/customers"
        payload = {"name": name}
        return self._post(url, json=payload)
    
    def get_customer(self, customer_id: str) -> dict:
        """
        Retrieves the details of an existing customer. Supply the unique customer ID from either a 
        customer creation request or the customer list, and Inscribe will return the corresponding 
        customer information. 

        :param id: Unique identifier for the object
        """
        url = f"/customers/{customer_id}"
        return self._get(url)

    def update_customer(self, customer_id: str, name: str, notes: str = None, approved: bool = None) -> dict:
        """
        Updates the specific customer by setting the values of the parameters passed. Any parameters 
        not provided will be left unchanged.

        :param customer_id: Unique identifier for the object
        :param name: A unique name for the customer
        :param notes: Any additional notes about this customer that you would like to keep a record of.
        :param approved: Has the value true if you have identified the customer as fraudulent, false is legitimate, 
                         and null if unknown. The default is null. 
        """
        url = f"/customers/{customer_id}"
        payload = {"name": name}
        if notes is not None:
            payload["notes"] = notes
        if approved is not None:
            payload["approved"] = approved
        return self._put(url, json=payload)
    
    def delete_customer(self, customer_id: str) -> dict:
        """
        Permanently deletes a customer and all documents associated with this customer. It cannot be undone. 
        """
        url = f"/customers/{customer_id}"
        return self._delete(url)


    def get_customers(self, page_number: int = 1, limit_per_page: int = None, search_query: str = None,
         is_approved: bool = None, order_by: str = None, start_date: str = None, end_date: str = None, creator_uuid: str = None) -> dict:
        """
        Returns a paginated list of your customers based on optional query parameters. If the customer search query parameter is used, 
        the list is sorted by relevance, otherwise the customers are returned sorted by creation date, with the most recently created 
        customers appearing first.

        :param page_number: A indicator of which page of the customer list to return (Default: 1)
        :param limit_per_page: A limit on the number of customers to be returned. The limit can range between 1 and 100, and the default is 10.
        :param search_query: A search query for a customer name. Having this query set will override any orderBy by the relevance of the search term.
        :param is_approved: Whether or not the customer has been indicated by you be approved or rejected by you. 
        :param order_by: Following options:
                            created_at - customers are returned sorted by ascending creation date
                            -created_at  - customers are returned sorted by descending creation date
        :param start_data and end_date: The date filter allows you to filter customer by date intervals. The value can take any date format supported by the {TODO}.
                             The filter includes everything from the start date up to but not including the end date.
        :param creator_uuid: Returns only customers owned by this user UUID. This user must be in your organization and you must have access to their customers. 

        """
        url = f"/customers?page={page_number}"
        if limit_per_page is not None:
            url = url + f"&limit={limit_per_page}"
        if search_query is not None:
            url = url + f"&search={search_query}"
        if is_approved is not None:
            url = url + f"&approved={is_approved}"
        if order_by is not None:
            url = url + f"&order={order_by}"
        if start_date is not None:
            url = url + f"&startDate={start_date}"
        if end_date is not None:
            url = url + f"&endDate={end_date}"
        if creator_uuid is not None:
            url = url + f"&creator={creator_uuid}"
        return self._get(url)

    def upload_document(self, customer_id: str, document: object,
                        success_callback: object = None, error_callback: object = None):
        url = f"/customers/{customer_id}/documents"
        filename = os.path.basename(document.name)
        upload_response = self._post(url, files=((filename, document),))

        if self.pusher_enabled and (success_callback is not None) and (error_callback is not None):
            return self._manage_upload_document_response(
                upload_response,
                success_callback=success_callback,
                error_callback=error_callback
            )
        else:
            return upload_response

    def retrieve_document_results(self, customer_id: str, document_id: str) -> dict:
        """
        Retrieves the results of an existing document. Supply the unique customer ID from either a customer creation request or the customer list,
        the unique document ID from either a document upload request or document list of the customer, and Inscribe will return the corresponding 
        document results if it has finished processing. 

        :param customer_id: id of the customer you want to retrieve document results.
        :param document_id: id of the document you want to retrieve results.
        """

        url = f"/customers/{customer_id}/documents/{document_id}"
        return self._get(url)

    def delete_document(self, customer_id: str, document_id: str) -> dict:
        """
        Delete document. This cannot be undone

        :param customer_id: id of customer you want to delete a document from.
        :param document_id: id of document to be deleted.
        """
        url = f"/customers/{customer_id}/documents/{document_id}"
        return self._delete(url)

    def get_all_documents(self, customer_id: str):
        """
        Get all documents for a customer.

        :param customer_id: id of customer you want to get all documents from.
        """
        url = f"/customers/{customer_id}/documents/"
        return self._get(url)
      
    def add_webhook(self, webhook_url: str):
        """
        Add webhook

        :param webhook_url: the URL that will receive document_processed events.
        """
        url = f"/webhooks/"
        payload = dict(url=webhook_url)
        return self._post(url, payload=payload)
        
    def get_all_webhooks(self):
        """
        List of all webhooks

        """
        url = f"/webhooks/"
        payload = dict(url=url)
        return self._get(url)

    def get_webhook(self, webhook_id: str):
        """
        List of all webhooks

        :param webhook_id: the ID of the webhook to retrieve.

        """
        url = f"/webhooks/{webhook_id}"
        return self._get(url)

    def delete_webhook(self, webhook_id : str) -> dict:
        """
        Delete webhook. This cannot be undone

        :param webhook_id: id of the webhook to delete.
        """
        url = f"/webhooks/{webhook_id}/"
        return self._delete(url)

    def update_webhook(self, webhook_id : str, webhook_url : str) -> dict:
        """
        Update webhook.

        :param webhook_id: id of the webhook to update.
        :param webhook_url: the URL that will receive document_processed events.

        """
        url = f"/webhooks/{webhook_id}/"
        payload = dict(url=webhook_url)
        return self._put(url, payload=payload)

    @property
    def headers(self):
        return {'Authorization': self.api_key}

    @property
    def version(self):
        return "v%s" % self._version

    @property
    def base_url(self):
        return f"{self.domain_url}/api/{self.version}"

    def _manage_upload_document_response(
            self, response: dict, success_callback: object, error_callback: object):
        if 'data' in response:
            for document in response['data']:
                document_id = document.get('id')
                bind_name = f"document-processed-{document_id}"
                self._add_binding_to_queue(bind_name, document_id, error_callback)
                self.channel.bind(
                    bind_name,
                    lambda data: self._process_pusher_message(
                        data=data,
                        bind_name=bind_name,
                        success_callback=success_callback,
                        error_callback=error_callback
                    )
                )
        else: 
            error_callback(
                    InscribeAPIException(
                        'Could not parse output from upload document response. Please try again.'
                    )
                )

                

    def _process_pusher_message(
            self, data: dict, bind_name: str,
            success_callback: object, error_callback: object):
        json_data = json.loads(data)
        self._find_and_remove_from_queue(bind_name)
        success_callback(self.retrieve_document_results(json_data["customer_id"], json_data["document_id"]))

    def _check_queue(self):
        for index, binding in enumerate(self.queue):
            currentTimestamp = datetime.datetime.now().timestamp()
            if ((currentTimestamp - binding['started_at']) >= self.timeout):
                self._remove_from_queue(binding['bind_name'], index)
                binding['error_callback'](
                    InscribeAPIException(f"Document ({binding['document_id']}) timed out, please try again.")
                )

        self.queue_check = threading.Timer(self.check_queue_interval, self._check_queue)
        self.queue_check.daemon = True
        self.queue_check.start()

    def stop_queue_check(self):
        self.queue_check.cancel()

    def _find_and_remove_from_queue(self, bind_name: str):
        for index, binding in enumerate(self.queue):
            if binding['bind_name'] == bind_name:
                self._remove_from_queue(bind_name, index)

    def _remove_from_queue(self, bind_name: str, index: int):
        self.channel.unbind(bind_name)
        self.queue.pop(index)

    def _add_binding_to_queue(self, bind_name: str, documentId: int, error_callback: object):
        self.queue.append({
            'bind_name': bind_name,
            'document_id': documentId,
            'error_callback': error_callback,
            'started_at': datetime.datetime.now().timestamp()
        })

    def _get_http_method(self, method_name):
        http_method_mapping = {
            "GET": self.session.get,
            "POST": self.session.post,
            "DELETE": self.session.delete,
            "PUT": self.session.put,
            "PATCH": self.session.patch,
            "HEAD": self.session.head
        }

        try:
            return http_method_mapping[method_name]
        except KeyError:
            raise InscribeAPIException("HTTP method '%s' is invalid!" % method_name)

    def _get(self, url, **kwargs):
        return self._request("GET", url, **kwargs)

    def _post(self, url, **kwargs):
        return self._request("POST", url, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request("DELETE", url, **kwargs)

    def _put(self, url, **kwargs):
        return self._request("PUT", url, **kwargs)

    def _patch(self, url, **kwargs):
        return self._request("PATCH", url, **kwargs)

    def _head(self, url, **kwargs):
        return self._request("HEAD", url, **kwargs)

    def _request(self, method, url, **kwargs):

        http_method = self._get_http_method(method)

        url = self.base_url + url
        logger.info("HTTP %s request. : %s " % (method, url))

        response = http_method(url, headers=self.headers, **kwargs)
        logger.info("Response: %s" % response.text)
        try:
            response.raise_for_status()
        except HTTPError as e:
            logger.info(str(e))
            try:
                response_json = response.json()
            except:
                raise InscribeAPIException(f"{str(e)}\nError occurred during sending a request to {url}")
            raise InscribeAPIException(f"Error occurred during API call: {response_json['message']}")  

        try:
            response_json = response.json()
        except:            
            if response.status_code == 204:
                return response.text
            raise InscribeAPIException("Couldn't get a valid JSON from response")
            
        return response_json

    def __del__(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
