"""
Trace module
"""

import asyncio
import json
import logging
import os
import socket
import ssl
from typing import Callable
import aiohttp
import requests
from requests import Session
from tqdm import tqdm

from superwise.config import Config
from superwise.exceptions.superwise_exceptions import SuperwiseDataError
from superwise.validations.superwise_validator import *


class Trace:

    def __init__(self, session: Session, token: str,host: str):
        self._logger = logging.getLogger('superwise')
        self._session = session
        self._token = token
        self._host = host
        self._uri = f"https://{host}" + "/v1/trace/task/{task_id}/"

    def prediction_emit(self, data, task_id: int, version_id: int):
        """
        send trace prediction single record(single mode)
        :param version_id:
        :param _retry: private parameter, which retries
        :param data: data of user
        :param task_id:
        :return: status_code, exception
        """
        url = str(self._uri.format(task_id=task_id) + 'prediction/emit')
        body = dict(record=data, version_id=version_id)
        validator = valid_trace_prediction_emit
        return self._prediction_helper_func(url=url, body=body, validator=validator, chunk_size=-1, is_label=False)

    def prediction_batch(self, data, task_id: int, version_id: int, chunk_size: int = 10):
        """
        send trace prediction records(batch mode)
        :param chunk_size:
        :param version_id:
        :param _retry:
        :param data: data of user
        :param task_id:
        :return: status_code, exception
        """
        url = str(self._uri.format(task_id=task_id) + 'prediction/batch')
        body = dict(records=data, version_id=version_id)
        validator = valid_trace_prediction_batch
        return self._prediction_helper_func(url=url, body=body, validator=validator, chunk_size=chunk_size,
                                            is_label=False)

    def prediction_file(self, file_url: str, version_id: int, task_id: int):
        """
        send trace batch request with path to file in s3.
        :param version_id:
        :param file_url:
        :param task_id:
        :param _retry:
        :return: status code from the request
        """
        url = str(self._uri.format(task_id=task_id) + 'prediction/file')
        body = dict(file_url=file_url, version_id=version_id)
        validator = valid_trace_prediction_file
        return self._prediction_helper_func(url=url, body=body, validator=validator, chunk_size=-1, is_label=False)

    def label_emit(self, data, task_id: int):
        """
        send trace label prediction single record(single mode)
        :param version_id:
        :param _retry: private parameter, which retries
        :param data: data of user
        :param task_id:
        :return: status_code, exception
        """
        url = str(self._uri.format(task_id=task_id) + 'label/emit')
        validator = valid_trace_label_emit
        return self._prediction_helper_func(url=url, body=data, validator=validator, chunk_size=-1, is_label=True)

    def label_batch(self, data, task_id: int, chunk_size: int = 10):
        """
        send trace label prediction records(batch mode)
        :param chunk_size:
        :param version_id:
        :param _retry:
        :param data: data of user
        :param task_id:
        :return: status_code, exception
        """
        url = str(self._uri.format(task_id=task_id) + 'label/batch')
        body = dict(records=data)
        validator = valid_trace_label_batch
        return self._prediction_helper_func(url=url, body=body, validator=validator, chunk_size=chunk_size,
                                            is_label=True)

    def label_file(self, file_url: str, task_id: int):
        """
        send trace batch request with path to file in s3.
        :param version_id:
        :param file_url:
        :param task_id:
        :param _retry:
        :return: status code from the request
        """
        url = str(self._uri.format(task_id=task_id) + 'label/file')
        body = dict(file_url=file_url)
        validator = valid_trace_label_file
        return self._prediction_helper_func(url=url, body=body, validator=validator, chunk_size=-1, is_label=True)

    def _prediction_helper_func(self, url: str, body: dict, validator: Callable, chunk_size: int, is_label: bool):
        """
        Centralize function to send post request to the server
        :param url: end point URI
        :param body: request body
        :param validator: validate the body structure
        :param _retry: amount of times try to send post
        :return: Error or Response Code of the request
        """
        header = {'Content-Type': 'application/json',
                  'Authorization': self._session.headers.get('Authorization')}
        self._logger.info(f" send {url} request")
        if validator(data=body):
            if chunk_size == -1:
                res = self._session.post(url=url, data=json.dumps(body), headers=header)
                self._logger.info(
                    f"request {url}  return with status code {res.status_code}")
                return res.status_code
            else:
                chunks = []
                for i in range(0, len(body["records"]), chunk_size):
                    if not is_label:
                        chunks.append({"records": body["records"][i:i + chunk_size], "version_id": body["version_id"]})
                    else:
                        chunks.append({"records": body["records"][i:i + chunk_size]})
                loop = asyncio.get_event_loop()
                status_codes, text_res = loop.run_until_complete(
                    self._main_task(chunks=chunks, url=url, headers=header))
                if len(status_codes) != 1:
                    raise SuperwiseDataError(f"problem send multiple chunks with status codes {status_codes}")
                text_res = json.loads(text_res.pop())['failed_to_load']
                if len(text_res) == 0:
                    self._logger.info(
                        f"request {url}  return with status code {status_codes}, all records were accepted")
                else:
                    self._logger.info(
                        f"request {url}  return with status code {status_codes}, records were not accepted: {text_res}")
                return status_codes
        self._logger.info(f"request {url}  with wrong data format")
        raise SuperwiseDataError("data don't in the right format")

    async def _main_task(self, chunks, url, headers):
        """
        task manager for the multiple post request (request for each chunk).
        :param chunks:
        :param url:
        :param :
        :return: set of status codes of all requests
        """
        status_codes = []
        responses = []
        connector = aiohttp.TCPConnector(family=socket.AF_INET)
        async with aiohttp.ClientSession(connector=connector) as session:
            for chunk in tqdm(chunks):
                status, text = await self._fetch_task(session=session, url=url, headers=headers, chunk=chunk)
                status_codes.append(status)
                responses.append(text)
        return set(status_codes), set(responses)

    async def _fetch_task(self, session, url, headers, chunk):
        """
        send each request to trace service and return 2 arrays- status codes array and results array.
        :param session:
        :param url:
        :param headers:
        :param chunk:
        :return:
        """
        async with session.post(url=url, data=json.dumps(chunk), headers=headers) as response:
            status_code = response.status
            res = await response.text()
        return status_code, res