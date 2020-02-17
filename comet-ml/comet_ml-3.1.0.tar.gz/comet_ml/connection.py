# -*- coding: utf-8 -*-
# *******************************************************
#   ____                     _               _
#  / ___|___  _ __ ___   ___| |_   _ __ ___ | |
# | |   / _ \| '_ ` _ \ / _ \ __| | '_ ` _ \| |
# | |__| (_) | | | | | |  __/ |_ _| | | | | | |
#  \____\___/|_| |_| |_|\___|\__(_)_| |_| |_|_|
#
#  Sign up for free at http://www.comet.ml
#  Copyright (C) 2015-2020 Comet ML INC
#  This file can not be copied and/or distributed without
#  the express permission of Comet ML Inc.
# *******************************************************

from __future__ import print_function

import itertools
import json
import logging
import os
import ssl
import sys
import threading
import time

import comet_ml
import requests
import six
import websocket
from comet_ml import config
from comet_ml._reporting import WS_ON_CLOSE, WS_ON_ERROR, WS_ON_OPEN
from comet_ml.config import (
    DEFAULT_UPLOAD_SIZE_LIMIT,
    get_api_key,
    get_config,
    get_rest_api_key,
)
from comet_ml.exceptions import (
    BackendVersionTooOld,
    CometRestApiException,
    CometRestApiValueError,
    ExperimentAlreadyUploaded,
    InvalidAPIKey,
    InvalidRestAPIKey,
    InvalidWorkspace,
    NotFound,
    PaymentRequired,
    ProjectNameEmpty,
)
from comet_ml.json_encoder import NestedEncoder
from comet_ml.logging_messages import (
    BACKEND_VERSION_CHECK_ERROR,
    INVALID_CONFIG_MINIMAL_BACKEND_VERSION,
    WS_ON_CLOSE_MSG,
    WS_ON_OPEN_MSG,
    WS_SSL_ERROR_MSG,
)
from requests import HTTPError
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from ._typing import Dict, List, Optional, Tuple
from .utils import (
    get_comet_version,
    get_time_monotonic,
    local_timestamp,
    merge_url,
    parse_version_number,
)

if six.PY2:
    from urlparse import urlparse, urlunparse, urljoin
    from urllib import getproxies
else:
    from urllib.parse import urlparse, urlunparse, urljoin
    from urllib.request import getproxies


TIMEOUT = 10

INITIAL_BEAT_DURATION = 10000  # 10 second

LOGGER = logging.getLogger(__name__)


def _comet_version():
    try:
        return comet_ml.__version__
    except NameError:
        return None


def get_retry_strategy():

    # The total backoff sleeping time is computed like that:
    # backoff = 2
    # total = 3
    # s = lambda b, i: b * (2 ** (i - 1))
    # sleep = sum(s(backoff, i) for i in range(1, total + 1))

    return Retry(
        total=3,
        backoff_factor=2,
        method_whitelist=False,
        status_forcelist=[500, 502, 503, 504],
    )  # Will wait up to 24s


def sanitize_url(url):
    # () -> Str
    """ Sanitize an URL, checking that it is a valid URL and ensure it contains a leading slash /
    """
    parts = urlparse(url)
    scheme, netloc, path, params, query, fragment = parts

    # TODO: Raise an exception if params, query and fragment are not empty?

    # Ensure the leading slash
    if path and not path.endswith("/"):
        path = path + "/"
    elif not path and not netloc.endswith("/"):
        netloc = netloc + "/"

    return urlunparse((scheme, netloc, path, params, query, fragment))


def get_root_url(url):
    # () -> Str
    """ Remove the path, params, query and fragment from a given URL
    """
    parts = urlparse(url)
    scheme, netloc, path, params, query, fragment = parts

    return urlunparse((scheme, netloc, "", "", "", ""))


def get_backend_address():
    config = get_config()
    return sanitize_url(config["comet.url_override"])


def get_optimizer_address(config):
    return sanitize_url(config["comet.optimizer_url"])


def get_http_session(backend_address=None, retry_strategy=None):
    session = requests.Session()

    # Setup retry strategy if asked
    if retry_strategy is not None and backend_address is not None:
        session.mount(backend_address, HTTPAdapter(max_retries=retry_strategy))

    # Setup HTTP allow header if configured
    config = get_config()
    allow_header_name = config["comet.allow_header.name"]
    allow_header_value = config["comet.allow_header.value"]

    if allow_header_name and allow_header_value:
        session.headers[allow_header_name] = allow_header_value

    return session


def url_join(base, *parts, **kwargs):
    """ Given a base and url parts (for example [workspace, project, id]) returns a full URL
    """
    # TODO: Enforce base to have a scheme and netloc?
    result = base

    for part in parts[:-1]:
        if not part.endswith("/"):
            raise ValueError("Intermediary part not ending with /")

        result = urljoin(result, part)

    result = urljoin(result, parts[-1])

    if kwargs:
        # merge the url with additional query args:
        result = merge_url(result, kwargs)

    return result


def json_post(url, session, headers, body, timeout):
    response = session.post(
        url=url, data=json.dumps(body), headers=headers, timeout=timeout
    )

    response.raise_for_status()
    return response


def format_messages_for_ws(messages):
    """ Encode a list of messages into JSON
    """
    messages_arr = []
    for message in messages:
        payload = {}
        # make sure connection is actually alive
        if message["stdout"] is not None:
            payload["stdout"] = message
        else:
            payload["log_data"] = message

        messages_arr.append(payload)

    data = json.dumps(messages_arr, cls=NestedEncoder, allow_nan=False)
    LOGGER.debug("ENCODED DATA %r", data)
    return data


def check_api_backend_version(backend_root_url, minimal_backend_version):
    # type: (str, Tuple[int, int, int]) -> None
    version_url = url_join(backend_root_url, "clientlib/isAlive/ver")

    # Get the backend version
    response = requests.get(version_url)
    try:
        response.raise_for_status()
        # Invalid version will raise exception:
        backend_version = parse_version_number(response.json()["version"])
    except Exception:
        LOGGER.warning(BACKEND_VERSION_CHECK_ERROR, version_url, exc_info=True)
        return None

    # Compare versions
    if backend_version < minimal_backend_version:
        raise BackendVersionTooOld(
            version_url, backend_version, minimal_backend_version
        )


class LowLevelHTTPClient(object):
    """ A low-level HTTP client that centralize common code and behavior between the two backends clients, the optimizer and the predictor
    """

    def __init__(
        self, server_address, headers=None, default_retry=True, default_timeout=TIMEOUT
    ):
        self.server_address = server_address

        self.session = get_http_session()
        self.retry_session = get_http_session(
            self.server_address, retry_strategy=get_retry_strategy()
        )

        if headers is None:
            headers = {}

        self.headers = headers
        # Add the common headers
        self.headers["Content-Type"] = "application/json;charset=utf-8"
        self.headers["PYTHON-SDK-VERSION"] = get_comet_version()

        self.default_retry = default_retry
        self.default_timeout = default_timeout

    def close(self):
        self.session.close()
        self.retry_session.close()

    def get(self, url, params=None, headers=None, retry=None, timeout=None):
        if retry is None:
            retry = self.default_retry

        if timeout is None:
            timeout = self.default_timeout

        final_headers = self.headers.copy()
        if headers:
            final_headers.update(headers)

        # Do not logs the headers as they might contains the authentication keys
        LOGGER.debug(
            "GET HTTP Call, url %r, params %r, retry %r, timeout %r",
            url,
            params,
            retry,
            timeout,
        )

        if retry:
            response = self.retry_session.get(
                url, params=params, headers=final_headers, timeout=timeout
            )
        else:
            response = self.session.get(
                url, params=params, headers=final_headers, timeout=timeout
            )

        return response

    def post(
        self,
        url,
        payload,
        headers=None,
        retry=None,
        timeout=None,
        params=None,
        files=None,
    ):
        if retry is None:
            retry = self.default_retry

        if timeout is None:
            timeout = self.default_timeout

        final_headers = self.headers.copy()
        if headers:
            final_headers.update(headers)

        if files is not None:
            del final_headers["Content-Type"]

        # Do not logs the headers as they might contains the authentication keys
        LOGGER.debug(
            "POST HTTP Call, url %r, payload %r, retry %r, timeout %r",
            url,
            payload,
            retry,
            timeout,
        )
        if retry:
            response = self.retry_session.post(
                url,
                json=payload,
                headers=final_headers,
                timeout=timeout,
                files=files,
                params=params,
            )
        else:
            response = self.session.post(
                url,
                json=payload,
                headers=final_headers,
                timeout=timeout,
                files=files,
                params=params,
            )
        LOGGER.debug(
            "POST HTTP Response, url %r, status_code %d, response %r",
            url,
            response.status_code,
            response.content,
        )

        return response


class RestServerConnection(object):
    """
    A static class that handles the connection with the server.
    """

    def __init__(self, api_key, experiment_id, server_address):
        self.api_key = api_key
        self.experiment_id = experiment_id

        # Set once get_run_id is called
        self.run_id = None
        self.project_id = None

        self.server_address = server_address

        self.session = get_http_session()
        self.retry_session = get_http_session(
            self.server_address, retry_strategy=get_retry_strategy()
        )

    def close(self):
        self.session.close()
        self.retry_session.close()

    def heartbeat(self):
        """ Inform the backend that we are still alive
        """
        LOGGER.debug("Doing an heartbeat")
        return self.update_experiment_status(self.run_id, self.project_id, True)

    def update_experiment_status(self, run_id, project_id, is_alive, offline=False):
        endpoint_url = self.server_address + "status-report/update"
        headers = {"Content-Type": "application/json;charset=utf-8"}

        payload = {
            "apiKey": self.api_key,
            "runId": run_id,
            "experimentKey": self.experiment_id,
            "projectId": project_id,
            "is_alive": is_alive,
            "local_timestamp": local_timestamp(),
            "offline": offline,
        }

        LOGGER.debug("Experiment status update with payload: %s", payload)

        r = self.session.post(
            url=endpoint_url, data=json.dumps(payload), headers=headers, timeout=TIMEOUT
        )

        if r.status_code != 200:
            raise ValueError(r.content)

        data = r.json()
        LOGGER.debug("Update experiment status response payload: %r", data)
        beat_duration = data.get("is_alive_beat_duration_millis")

        if beat_duration is None:
            raise ValueError("Missing heart-beat duration")

        gpu_monitor_interval = data.get("gpu_monitor_interval_millis")

        if gpu_monitor_interval is None:
            raise ValueError("Missing gpu-monitor interval")

        # Default the backend response until it responds:
        cpu_monitor_interval = data.get("cpu_monitor_interval_millis", 68 * 1000)

        if cpu_monitor_interval is None:
            raise ValueError("Missing cpu-monitor interval")

        pending_rpcs = data.get("pending_rpcs", False)

        return_data = {
            "gpu_monitor_interval": gpu_monitor_interval,
            "cpu_monitor_interval": cpu_monitor_interval,
        }

        return beat_duration, return_data, pending_rpcs

    def get_run_id(self, project_name, workspace, offline=False):
        """
        Gets a new run id from the server.
        :param api_key: user's API key
        :return: run_id - String
        """
        endpoint_url = get_run_id_url(self.server_address)
        headers = {"Content-Type": "application/json;charset=utf-8"}

        # We used to pass the team name as second parameter then we migrated
        # to workspaces. We keep using the same payload field as compatibility
        # is ensured by the backend and old SDK version will still uses it
        # anyway
        payload = {
            "apiKey": self.api_key,
            "local_timestamp": local_timestamp(),
            "experimentKey": self.experiment_id,
            "offline": offline,
            "projectName": project_name,
            "teamName": workspace,
            "libVersion": _comet_version(),
        }

        LOGGER.debug("Get run id URL: %s", endpoint_url)
        r = self.retry_session.post(
            url=endpoint_url, data=json.dumps(payload), headers=headers, timeout=TIMEOUT
        )

        if r.status_code != 200:
            if r.status_code == 400:
                # Check if the api key was invalid
                data = r.json()  # Raise a ValueError if failing
                code = data.get("sdk_error_code")
                if code == 90212:
                    raise InvalidAPIKey(self.api_key)

                elif code == 90219:
                    raise InvalidWorkspace(workspace)

                elif code == 98219:
                    raise ProjectNameEmpty()

                elif code == 90999:
                    raise ExperimentAlreadyUploaded(self.experiment_id)

            raise ValueError(r.content)

        res_body = json.loads(r.content.decode("utf-8"))

        LOGGER.debug("New run response body: %s", res_body)

        return self._parse_run_id_res_body(res_body)

    def get_old_run_id(self, previous_experiment):
        """
        Gets a run id from an existing experiment.
        :param api_key: user's API key
        :return: run_id - String
        """
        endpoint_url = self.server_address + "logger/get/run"
        headers = {"Content-Type": "application/json;charset=utf-8"}

        payload = {
            "apiKey": self.api_key,
            "local_timestamp": local_timestamp(),
            "previousExperiment": previous_experiment,
            "libVersion": _comet_version(),
        }
        LOGGER.debug("Get old run id URL: %s", endpoint_url)
        r = self.retry_session.post(
            url=endpoint_url, data=json.dumps(payload), headers=headers, timeout=TIMEOUT
        )

        if r.status_code != 200:
            if r.status_code == 400:
                # Check if the api key was invalid
                data = r.json()  # Raise a ValueError if failing
                if data.get("sdk_error_code") == 90212:
                    raise InvalidAPIKey(self.api_key)

            raise ValueError(r.content)

        res_body = json.loads(r.content.decode("utf-8"))

        LOGGER.debug("Old run response body: %s", res_body)

        return self._parse_run_id_res_body(res_body)

    def copy_run(self, previous_experiment, copy_step):
        """
        Gets a run id from an existing experiment.
        :param api_key: user's API key
        :return: run_id - String
        """
        endpoint_url = copy_experiment_url(self.server_address)
        headers = {"Content-Type": "application/json;charset=utf-8"}

        payload = {
            "apiKey": self.api_key,
            "copiedExperimentKey": previous_experiment,
            "newExperimentKey": self.experiment_id,
            "stepToCopyTo": copy_step,
            "localTimestamp": local_timestamp(),
            "libVersion": _comet_version(),
        }
        LOGGER.debug("Copy run URL: %s", endpoint_url)
        r = self.retry_session.post(
            url=endpoint_url, data=json.dumps(payload), headers=headers, timeout=TIMEOUT
        )

        if r.status_code != 200:
            if r.status_code == 400:
                # Check if the api key was invalid
                data = r.json()  # Raise a ValueError if failing
                if data.get("sdk_error_code") == 90212:
                    raise InvalidAPIKey(self.api_key)

            raise ValueError(r.content)

        res_body = json.loads(r.content.decode("utf-8"))

        LOGGER.debug("Copy run response body: %s", res_body)

        return self._parse_run_id_res_body(res_body)

    def _parse_run_id_res_body(self, res_body):
        run_id_server = res_body["runId"]
        ws_server = res_body["ws_url"]

        project_id = res_body.get("project_id", None)

        is_github = bool(res_body.get("githubEnabled", False))

        focus_link = res_body.get("focusUrl", None)

        upload_limit = res_body.get("upload_file_size_limit_in_mb", None)

        last_offset = res_body.get("lastOffset", 0)

        if not (isinstance(upload_limit, int) and upload_limit > 0):
            upload_limit = DEFAULT_UPLOAD_SIZE_LIMIT
        else:
            # The limit is given in Mb, convert it back in bytes
            upload_limit = upload_limit * 1024 * 1024

        res_msg = res_body.get("msg")
        if res_msg:
            LOGGER.info(res_msg)

        # Parse feature toggles
        feature_toggles = {}
        LOGGER.debug("Raw feature toggles %r", res_body.get("featureToggles", []))
        for toggle in res_body.get("featureToggles", []):
            try:
                feature_toggles[toggle["name"]] = bool(toggle["enabled"])
            except (KeyError, TypeError):
                LOGGER.debug("Invalid feature toggle: %s", toggle, exc_info=True)
        LOGGER.debug("Parsed feature toggles %r", feature_toggles)

        # Parse URL prefixes
        web_asset_url = res_body.get("cometWebAssetUrl", None)
        web_image_url = res_body.get("cometWebImageUrl", None)
        api_asset_url = res_body.get("cometRestApiAssetUrl", None)
        api_image_url = res_body.get("cometRestApiImageUrl", None)

        # Save run_id and project_id around
        self.run_id = run_id_server
        self.project_id = project_id

        return (
            run_id_server,
            ws_server,
            project_id,
            is_github,
            focus_link,
            upload_limit,
            feature_toggles,
            last_offset,
            web_asset_url,
            web_image_url,
            api_asset_url,
            api_image_url,
        )

    def report(self, event_name=None, err_msg=None):
        try:
            if event_name is not None:
                endpoint_url = notify_url(self.server_address)
                headers = {"Content-Type": "application/json;charset=utf-8"}
                # Automatically add the sdk_ prefix to the event name
                real_event_name = "sdk_{}".format(event_name)

                payload = {
                    "event_name": real_event_name,
                    "api_key": self.api_key,
                    "run_id": self.run_id,
                    "experiment_key": self.experiment_id,
                    "project_id": self.project_id,
                    "err_msg": err_msg,
                    "timestamp": local_timestamp(),
                }

                LOGGER.debug("Report notify URL: %s", endpoint_url)

                json_post(endpoint_url, self.session, headers, payload, TIMEOUT / 2)

        except Exception:
            LOGGER.debug("Error reporting %s", event_name, exc_info=True)
            pass

    def offline_experiment_start_end_time(self, run_id, start_time, stop_time):
        endpoint_url = offline_experiment_times_url(self.server_address)
        headers = {"Content-Type": "application/json;charset=utf-8"}

        payload = {
            "apiKey": self.api_key,
            "runId": run_id,
            "experimentKey": self.experiment_id,
            "startTimestamp": start_time,
            "endTimestamp": stop_time,
        }

        LOGGER.debug(
            "Offline experiment start time and end time update with payload: %s",
            payload,
        )

        r = self.session.post(
            url=endpoint_url, data=json.dumps(payload), headers=headers, timeout=TIMEOUT
        )

        if r.status_code != 200:
            raise ValueError(r.content)

        return None

    def add_tags(self, added_tags):
        endpoint_url = add_tags_url(self.server_address)
        headers = {"Content-Type": "application/json;charset=utf-8"}

        payload = {
            "apiKey": self.api_key,
            "experimentKey": self.experiment_id,
            "addedTags": added_tags,
        }

        LOGGER.debug("Add tags with payload: %s", payload)

        r = self.session.post(
            url=endpoint_url, data=json.dumps(payload), headers=headers, timeout=TIMEOUT
        )

        if r.status_code != 200:
            raise ValueError(r.content)

        return None

    def get_upload_url(self, upload_type):
        return get_upload_url(self.server_address, upload_type)

    def get_pending_rpcs(self):
        endpoint_url = pending_rpcs_url(self.server_address)
        headers = {"Content-Type": "application/json;charset=utf-8"}

        payload = {"apiKey": self.api_key, "experimentKey": self.experiment_id}

        LOGGER.debug("Get pending RPCS with payload: %s", payload)

        r = self.session.get(
            url=endpoint_url, params=payload, headers=headers, timeout=TIMEOUT
        )

        if r.status_code != 200:
            raise ValueError(r.content)

        res_body = json.loads(r.content.decode("utf-8"))

        return res_body

    def register_rpc(self, function_definition):
        endpoint_url = register_rpc_url(self.server_address)
        headers = {"Content-Type": "application/json;charset=utf-8"}

        payload = {"apiKey": self.api_key, "experimentKey": self.experiment_id}
        # We might replace this payload.update by defining the exact
        # parameters once the payload body has been stabilized
        payload.update(function_definition)

        LOGGER.debug("Register RPC with payload: %s", payload)

        r = json_post(endpoint_url, self.session, headers, payload, TIMEOUT)

        if r.status_code != 200:
            raise ValueError(r.content)

        return None

    def send_rpc_result(self, callId, result, start_time, end_time):
        endpoint_url = rpc_result_url(self.server_address)
        headers = {"Content-Type": "application/json;charset=utf-8"}

        error = result.get("error", "")
        error_stacktrace = result.get("traceback", "")
        result = result.get("result", "")

        payload = {
            "apiKey": self.api_key,
            "experimentKey": self.experiment_id,
            "callId": callId,
            "result": result,
            "errorMessage": error,
            "errorStackTrace": error_stacktrace,
            "startTimeMs": start_time,
            "endTimeMs": end_time,
        }

        LOGGER.debug("Sending RPC result with payload: %s", payload)

        r = json_post(endpoint_url, self.session, headers, payload, TIMEOUT)

        if r.status_code != 200:
            raise ValueError(r.content)

        return None

    def send_new_symlink(self, project_name):
        endpoint_url = new_symlink_url(self.server_address)

        payload = {
            "apiKey": self.api_key,
            "experimentKey": self.experiment_id,
            "projectName": project_name,
        }

        headers = {"Content-Type": "application/json;charset=utf-8"}

        LOGGER.debug("new symlink: %s", payload)

        r = self.session.get(
            url=endpoint_url, params=payload, headers=headers, timeout=TIMEOUT
        )

        if r.status_code != 200:
            raise ValueError(r.content)

    def send_notification(
        self, title, status, experiment_name, experiment_link, notification_map
    ):
        endpoint_url = notification_url(self.server_address)

        payload = {
            "api_key": self.api_key,
            "title": title,
            "status": status,
            "experiment_key": self.experiment_id,
            "experiment_name": experiment_name,
            "experiment_link": experiment_link,
            "additional_data": notification_map,
        }

        headers = {"Content-Type": "application/json;charset=utf-8"}

        LOGGER.debug("Notification: %s", payload)

        try:
            r = json_post(endpoint_url, self.session, headers, payload, TIMEOUT)

            if r.status_code != 200 and r.status_code != 204:
                raise ValueError(r.content)

        except HTTPError as e:
            # for backwards and forwards compatibility, this endpoint was introduced backend v1.1.103
            if e.response.status_code != 404:
                raise


class Reporting(object):
    @staticmethod
    def report(
        event_name=None,
        api_key=None,
        run_id=None,
        experiment_key=None,
        project_id=None,
        err_msg=None,
        is_alive=None,
    ):

        try:
            if event_name is not None:
                server_address = get_backend_address()
                endpoint_url = notify_url(server_address)
                headers = {"Content-Type": "application/json;charset=utf-8"}
                # Automatically add the sdk_ prefix to the event name
                real_event_name = "sdk_{}".format(event_name)

                payload = {
                    "event_name": real_event_name,
                    "api_key": api_key,
                    "run_id": run_id,
                    "experiment_key": experiment_key,
                    "project_id": project_id,
                    "err_msg": err_msg,
                    "timestamp": local_timestamp(),
                }

                json_post(
                    endpoint_url, get_http_session(), headers, payload, TIMEOUT / 2
                )

        except Exception:
            LOGGER.debug("Failing to report %s", event_name, exc_info=True)


class WebSocketConnection(threading.Thread):
    """
    Handles the ongoing connection to the server via Web Sockets.
    """

    def __init__(self, ws_server_address, connection):
        threading.Thread.__init__(self)
        self.daemon = True
        self.name = "WebSocketConnection(%s)" % (ws_server_address)
        self.closed = False

        if config.DEBUG:
            websocket.enableTrace(True)

        self.address = ws_server_address

        self.config = get_config()

        self.allow_header_name = self.config["comet.allow_header.name"]
        self.allow_header_value = self.config["comet.allow_header.value"]

        LOGGER.debug("Creating a new WSConnection with url: %s", ws_server_address)

        self.ws = self.connect_ws(self.address)

        self.connection = connection

        self.last_error = None

    def is_connected(self):
        return getattr(self.ws.sock, "connected", False)

    def connect_ws(self, ws_server_address):
        header = []

        if self.allow_header_name and self.allow_header_value:
            header.append("%s: %s" % (self.allow_header_name, self.allow_header_value))

        ws = websocket.WebSocketApp(
            ws_server_address,
            header=header,
            on_message=lambda *args, **kwargs: self.on_message(*args, **kwargs),
            on_error=lambda *args, **kwargs: self.on_error(*args, **kwargs),
            on_close=lambda *args, **kwargs: self.on_close(*args, **kwargs),
        )
        ws.on_open = lambda *args, **kwargs: self.on_open(*args, **kwargs)
        return ws

    def run(self):
        while self.closed is False:
            try:
                self._loop()
            except Exception:
                LOGGER.debug("Run forever error", exc_info=True)
                # Avoid hammering the backend
                time.sleep(0.5)
        LOGGER.debug("WebSocketConnection has ended")

    def _loop(self):
        # Pass the default ping_timeout to avoid issues with websocket-client
        # >= 0.50.0
        http_proxy_host, http_proxy_port, http_proxy_auth, proxy_type = get_http_proxy()
        self.ws.run_forever(
            ping_timeout=10,
            http_proxy_host=http_proxy_host,
            http_proxy_port=http_proxy_port,
            http_proxy_auth=http_proxy_auth,
            proxy_type=proxy_type,
        )
        LOGGER.debug("Run forever has ended")

    def send(self, data, retry=5):
        """ Encode the messages into JSON and send them on the websocket
        connection
        """
        for i in range(retry):
            success = self._send(data)
            if success:
                return
            else:
                LOGGER.debug("Retry WS sending!")

        LOGGER.debug("Message %r failed to be sent", data)

    def close(self):
        LOGGER.debug("Closing %r", self)
        self.closed = True
        self.ws.close()

    def wait_for_finish(self, timeout=10):
        self.join(timeout)
        if self.is_alive():
            msg = "Websocket connection didn't closed properly after %d seconds"
            LOGGER.debug(msg, timeout)
            return False
        else:
            LOGGER.debug("Websocket connection correctly closed")
            return True

    def _send(self, data):
        if self.ws.sock:
            self.ws.send(data)
            LOGGER.debug("Sending data done, %r", data)
            return True

        else:
            LOGGER.debug("WS not ready for connection")
            self.wait_for_connection()
            return False

    def wait_for_connection(self, num_of_tries=20):
        """
        waits for the server connection
        Args:
            num_of_tries: number of times to try connecting before giving up

        Returns: True if succeeded to connect.

        """
        if not self.is_connected():
            counter = 0

            while not self.is_connected() and counter < num_of_tries:
                time.sleep(0.5)
                counter += 1

            if not self.is_connected():
                self.close()

                if self.last_error is not None:
                    # Process potential sources of errors
                    if isinstance(self.last_error[1], ssl.SSLError):
                        LOGGER.error(
                            WS_SSL_ERROR_MSG,
                            exc_info=self.last_error,
                            extra={"show_traceback": True},
                        )

                raise ValueError("Could not connect to server after multiple tries.")

        return True

    def on_open(self, ws):
        LOGGER.debug(WS_ON_OPEN_MSG)

        self.connection.report(event_name=WS_ON_OPEN, err_msg=WS_ON_OPEN_MSG)

    def on_message(self, ws, message):
        if message not in ("got msg", "ok"):
            LOGGER.debug("WS msg: %s", message)

    def on_error(self, ws, error):
        error_type_str = type(error).__name__
        ignores = [
            "WebSocketBadStatusException",
            "error",
            "WebSocketConnectionClosedException",
            "ConnectionRefusedError",
            "BrokenPipeError",
        ]

        self.connection.report(event_name=WS_ON_ERROR, err_msg=repr(error))

        # Ignore some errors for auto-reconnecting
        if error_type_str in ignores:
            LOGGER.debug("Ignore WS error: %r", error, exc_info=True)
            return

        LOGGER.debug("WS on error: %r", error, exc_info=True)

        # Save error
        self.last_error = sys.exc_info()

    def on_close(self, *args, **kwargs):
        LOGGER.debug(WS_ON_CLOSE_MSG)

        # Report only abnormal WS closing
        if not self.closed:
            self.connection.report(event_name=WS_ON_CLOSE, err_msg=WS_ON_CLOSE_MSG)


def notify_url(server_address):
    return server_address + "notify/event"


def visualization_upload_url():
    """ Return the URL to upload visualizations
    """
    return "visualizations/upload"


def asset_upload_url():
    return "asset/upload"


def get_git_patch_upload_endpoint():
    return "git-patch/upload"


def log_url(server_address):
    return server_address + "log/add"


def offline_experiment_times_url(server_address):
    return server_address + "status-report/offline-metadata"


def pending_rpcs_url(server_address):
    return server_address + "rpc/get-pending-rpcs"


def add_tags_url(server_address):
    return server_address + "tags/add-tags-to-experiment"


def register_rpc_url(server_address):
    return server_address + "rpc/register-rpc"


def rpc_result_url(server_address):
    return server_address + "rpc/save-rpc-result"


def new_symlink_url(server_address):
    return server_address + "symlink/new"


def get_run_id_url(server_address):
    return server_address + "logger/add/run"


def copy_experiment_url(server_address):
    return server_address + "logger/copy-steps-from-experiment"


def notification_url(server_address):
    return server_address + "notification/experiment"


UPLOAD_TYPE_URL_MAP = {
    "asset": asset_upload_url(),
    "visualization": visualization_upload_url(),
    "git-patch": get_git_patch_upload_endpoint(),
    "audio": asset_upload_url(),
    "histogram2d": asset_upload_url(),
    "histogram3d": asset_upload_url(),
    "confusion-matrix": asset_upload_url(),
    "text-sample": asset_upload_url(),
    "model-element": asset_upload_url(),
}


def get_upload_url(server_address, upload_type):
    return server_address + UPLOAD_TYPE_URL_MAP[upload_type]


def get_http_proxy():
    http_proxy_host = None
    http_proxy_port = None
    http_proxy_auth = None
    proxy_type = None
    proxies = getproxies()
    http_proxy = proxies.get("https")
    if http_proxy is not None:
        http_proxy_obj = urlparse(http_proxy)
        proxy_type = http_proxy_obj.scheme
        if http_proxy_obj.port is not None:
            http_proxy_port = int(http_proxy_obj.port)
        http_proxy_host = http_proxy_obj.hostname
        if http_proxy_obj.username or http_proxy_obj.password:
            http_proxy_auth = (http_proxy_obj.username, http_proxy_obj.password)
        LOGGER.debug("Using HTTPS_PROXY: %s:%s" % (http_proxy_host, http_proxy_port))
        if http_proxy_host is None:
            raise ValueError("Invalid https proxy format `%s`" % http_proxy)
    return http_proxy_host, http_proxy_port, http_proxy_auth, proxy_type


class OptimizerAPI(object):
    """
    API for talking to Optimizer Server.
    """

    def __init__(self, api_key=None, version=None, persistent=True):
        """
        """

        self._config = get_config()
        self.DEFAULT_VERSION = "v1"
        self.URLS = {"v1": {"SERVER": get_optimizer_address(self._config), "REST": "/"}}
        self._session = None if not persistent else get_http_session()
        self._version = version if version is not None else self.DEFAULT_VERSION
        self._api_key = get_api_key(api_key, self._config)

    def get_url(self, version=None):
        """
        Returns the URL for this version of the API.
        """
        version = version if version is not None else self._version
        return self.URLS[version]["SERVER"] + self.URLS[version]["REST"]

    def get_url_server(self, version=None):
        """
        Returns the URL server for this version of the API.
        """
        version = version if version is not None else self._version
        return self.URLS[version]["SERVER"]

    def get_url_end_point(self, end_point, version=None):
        """
        Return the URL + end point.
        """
        return self.get_url(version) + end_point

    def get_request(self, end_point, params, return_type="json"):
        """
        Given an end point and a dictionary of params,
        return the results.
        """
        from . import __version__

        url = self.get_url_end_point(end_point)
        LOGGER.debug("API.get_request: url = %s, params = %s", url, params)
        headers = {"X-API-KEY": self._api_key, "PYTHON-SDK-VERSION": __version__}
        if self._session is not None:
            response = self._session.get(url, params=params, headers=headers)
        else:
            response = requests.get(url, params=params, headers=headers)
        raise_exception = None
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as exception:
            if exception.response.status_code == 401:
                raise_exception = ValueError("Invalid COMET_API_KEY")
            else:
                raise
        if raise_exception:
            raise raise_exception
        ### Return data based on return_type:
        if return_type == "json":
            return response.json()
        elif return_type == "binary":
            return response.content
        elif return_type == "text":
            return response.text
        elif return_type == "response":
            return response

    def post_request(self, end_point, json=None, **kwargs):
        """
        Given an end point and a dictionary of json,
        post the json, and return the results.
        """
        from . import __version__

        url = self.get_url_end_point(end_point)
        if json is None:
            json = {}
        LOGGER.debug("API.post_request: url = %s, json = %s", url, json)
        headers = {
            "PYTHON-SDK-VERSION": __version__,
            "X-API-KEY": self._api_key,
            "Content-Type": "application/json",
        }
        if "files" in kwargs:
            del headers["Content-Type"]
        if self._session is not None:
            response = self._session.post(url, headers=headers, json=json, **kwargs)
        else:
            response = requests.post(url, headers=headers, json=json, **kwargs)
        raise_exception = None
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as exception:
            if exception.response.status_code == 401:
                raise_exception = ValueError("Invalid COMET_API_KEY")
            else:
                raise
        if raise_exception:
            raise raise_exception
        return response.json()

    def get_version(self):
        """
        Return the default version of the API.
        """
        return self._version

    def optimizer_next(self, id):
        """
        Get the next set of parameters to evaluate.
        """
        ## /next?id=ID
        params = {"id": id}
        results = self.get_request("next", params=params)
        if results["code"] == 200:
            return results["parameters"]
        else:
            return None

    def optimizer_spec(self, algorithm_name):
        """
        Get the full spec for a optimizer by name.
        """
        if algorithm_name is not None:
            params = {"algorithmName": algorithm_name}
        else:
            raise ValueError("Optimizer must have an algorithm name")

        results = self.get_request("spec", params=params)
        if "code" in results:
            raise ValueError(results["message"])
        return results

    def optimizer_status(self, id=None):
        """
        Get the status of optimizer instance or
        search.
        """
        ## /status
        ## /status?id=ID
        if id is not None:
            params = {"id": id}
        else:
            params = {}
        results = self.get_request("status", params=params)
        return results

    def optimizer_algorithms(self):
        """
        Get a list of algorithms.
        """
        ## /algorithms
        results = self.get_request("algorithms", {})
        return results

    def optimizer_update(self, id, pid, trial, status=None, score=None, epoch=None):
        """
        Post the status of a search.
        """
        ## /update {"pid": PID, "trial": TRIAL,
        ##          "status": STATUS, "score": SCORE, "epoch": EPOCH}
        json = {
            "id": id,
            "pid": pid,
            "trial": trial,
            "status": status,
            "score": score,
            "epoch": epoch,
        }
        results = self.post_request("update", json=json)
        return results

    def optimizer_insert(self, id, p):
        """
        Insert a completed parameter package.
        """
        ## /insert {"pid": PID, "trial": TRIAL,
        ##          "status": STATUS, "score": SCORE, "epoch": EPOCH}
        json = {
            "id": id,
            "pid": p["pid"],
            "trial": p["trial"],
            "status": p["status"],
            "score": p["score"],
            "epoch": p["epoch"],
            "parameters": p["parameters"],
            "tries": p["tries"],
            "startTime": p["startTime"],
            "endTime": p["endTime"],
            "lastUpdateTime": p["lastUpdateTime"],
            "count": p["count"],
        }
        results = self.post_request("insert", json=json)
        return results


def get_rest_api_client(
    version,
    server_address=None,
    headers=None,
    rest_api_key=None,
    comet_api_key=None,
    use_cache=False,
):
    # (str, Optional[Dict[str, Any]]) -> RestApiClient
    if server_address is None:
        server_address = get_config("comet.url_override")
    server_url = get_root_url(server_address)

    low_level_api = LowLevelHTTPClient(server_url, headers)

    if use_cache:
        return RestApiClientWithCache(
            server_url=server_url,
            version=version,
            low_level_api_client=low_level_api,
            rest_api_key=rest_api_key,
            comet_api_key=comet_api_key,
        )
    else:
        return RestApiClient(
            server_url=server_url,
            version=version,
            low_level_api_client=low_level_api,
            rest_api_key=rest_api_key,
            comet_api_key=comet_api_key,
        )


class BaseApiClient(object):
    """ A base api client to centralize how we build urls and treat exceptions """

    REST_API_KEY_HEADER = "Authorization"
    COMET_API_KEY_HEADER = "Comet-Sdk-Api"

    def __init__(
        self, server_url, base_url, low_level_api_client, rest_api_key, comet_api_key
    ):
        # type: (str, List[str], LowLevelHTTPClient, Optional[str], Optional[str]) -> None
        self.server_url = server_url
        self.base_url = url_join(server_url, *base_url)
        self.low_level_api_client = low_level_api_client
        self.rest_api_key = rest_api_key
        self.comet_api_key = comet_api_key

    def get(self, url, params, headers=None):
        response = self.low_level_api_client.get(url, params=params, headers=headers)

        if response.status_code != 200:
            if response.status_code == 401:
                raise InvalidRestAPIKey(self.rest_api_key)  # probably
            elif response.status_code == 404:
                raise NotFound("GET", response)
            else:
                raise CometRestApiException("GET", response)

        return response

    def get_from_endpoint(self, endpoint, params, return_type="json"):
        url = url_join(self.base_url, endpoint)
        response = self.get(url, params)

        ### Return data based on return_type:
        if return_type == "json":
            content_type = response.headers["content-type"]
            # octet-stream is a GZIPPED stream:
            if content_type in ["application/json", "application/octet-stream"]:
                retval = response.json()
            else:
                raise CometRestApiValueError("GET", "data is not json", response)
        elif return_type == "binary":
            retval = response.content
        elif return_type == "text":
            retval = response.text
        elif return_type == "response":
            retval = response
        else:
            raise CometRestApiValueError(
                "GET",
                "invalid return_type %r: should be 'json', 'binary', or 'text'"
                % return_type,
                response,
            )

        return retval

    def post(self, url, payload, headers, files=None, params=None):
        response = self.low_level_api_client.post(
            url, payload=payload, headers=headers, files=files, params=params
        )

        if response.status_code != 200:
            if response.status_code == 402:
                raise PaymentRequired("POST", response)
            else:
                raise CometRestApiException("POST", response)

        return response

    def post_from_endpoint(self, endpoint, payload, **kwargs):
        url = url_join(self.base_url, endpoint)
        return self.post(url, payload, **kwargs)


class RestApiClient(BaseApiClient):

    """ This API Client is meant to discuss to the REST API and handle, params and payload formatting,
    input validation if necessary, creating the url and parsing the output. All the HTTP
    communication is handled by the low-level HTTP client.

    Inputs must be JSON-encodable, any conversion must be done by the caller.

    One method equals one endpoint and one call"""

    def __init__(
        self,
        server_url,
        version,
        low_level_api_client,
        rest_api_key=None,
        comet_api_key=None,
    ):
        # type: (str, str, LowLevelHTTPClient, Optional[str], Optional[str]) -> None
        if rest_api_key is None and comet_api_key is None:
            raise ValueError("Either rest_api_key or comet_api_key must be given")

        elif rest_api_key is not None and comet_api_key is not None:
            raise ValueError(
                "You can either pass rest_api_key or comet_api_key, not both"
            )

        config_minimal_backend_version = get_config(
            "comet.rest_v2_minimal_backend_version"
        )
        minimal_backend_version = None
        try:
            # Invalid version will raise exception:
            minimal_backend_version = parse_version_number(
                config_minimal_backend_version
            )
        except Exception:
            LOGGER.warning(
                INVALID_CONFIG_MINIMAL_BACKEND_VERSION, config_minimal_backend_version
            )

        if minimal_backend_version:
            check_api_backend_version(server_url, minimal_backend_version)

        super(RestApiClient, self).__init__(
            server_url,
            ["api/rest/", version + "/"],
            low_level_api_client,
            rest_api_key,
            comet_api_key,
        )

    def reset(self):
        pass

    def get(self, url, params):
        headers = {}

        if self.comet_api_key is not None:
            raise ValueError("You cannot do GET requests with a comet api key")
        elif self.rest_api_key is not None:
            headers[self.REST_API_KEY_HEADER] = self.rest_api_key

        return super(RestApiClient, self).get(url, params=params, headers=headers)

    def post(self, url, payload, files=None, params=None):
        headers = {}

        if self.comet_api_key is not None:
            headers[self.COMET_API_KEY_HEADER] = self.comet_api_key
        elif self.rest_api_key is not None:
            headers[self.REST_API_KEY_HEADER] = self.rest_api_key

        return super(RestApiClient, self).post(
            url, payload=payload, headers=headers, files=files, params=params
        )

    # Read Experiment methods:

    def get_account_details(self):
        """
        Example: {'userName': 'USERNAME', 'defaultWorkspaceName': 'WORKSPACE'}
        """
        payload = {}
        response = self.get_from_endpoint("account-details", payload)
        return response

    def get_experiment_os_packages(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["osPackages"]
        else:
            return None

    def get_experiment_user(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["user"]
        else:
            return None

    def get_experiment_installed_packages(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["installedPackages"]
        else:
            return None

    def get_experiment_command(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["command"]
        else:
            return None

    def get_experiment_executable(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["executable"]
        else:
            return None

    def get_experiment_hostname(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["hostname"]
        else:
            return None

    def get_experiment_gpu_static_info(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["gpuStaticInfoList"]
        else:
            return None

    def get_experiment_additional_system_info(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["logAdditionalSystemInfoList"]
        else:
            return None

    def get_experiment_ip(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["ip"]
        else:
            return None

    def get_experiment_max_memory(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            # FIXME: always None
            return response["maxTotalMemory"]
        else:
            return None

    def get_experiment_network_interface_ips(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["networkInterfaceIps"]
        else:
            return None

    def get_experiment_os(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["os"]
        else:
            return None

    def get_experiment_os_type(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["osType"]
        else:
            return None

    def get_experiment_pid(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["pid"]
        else:
            return None

    def get_experiment_python_version(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["pythonVersion"]
        else:
            return None

    def get_experiment_python_version_verbose(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["pythonVersionVerbose"]
        else:
            return None

    def get_experiment_total_memory(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["totalRam"]
        else:
            return None

    def get_experiment_system_info(self, experiment_key):
        """
        Deprecated.
        """
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response["logAdditionalSystemInfoList"]
        else:
            return None

    def get_experiment_system_metric_names(self, experiment_key):
        """
        """
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("experiment/system-details", payload)
        if response:
            return response.get("systemMetricNames", [])
        else:
            return []

    def get_experiment_model_graph(self, experiment_key):
        """
        Get the associated graph/model description for this
        experiment.
        """
        params = {"experimentKey": experiment_key}
        return self.get_from_endpoint("experiment/graph", params)

    def get_experiment_tags(self, experiment_key):
        """
        Get the associated tags for this experiment.
        """
        params = {"experimentKey": experiment_key}
        return self.get_from_endpoint("experiment/tags", params)

    def get_experiment_parameters_summaries(self, experiment_key):
        params = {"experimentKey": experiment_key}
        return self.get_from_endpoint("experiment/parameters", params)

    def get_experiment_metrics_summaries(self, experiment_key):
        params = {"experimentKey": experiment_key}
        return self.get_from_endpoint("experiment/metrics/summary", params)

    def get_experiment_metric(self, experiment_key, metric):
        params = {"experimentKey": experiment_key, "metricName": metric}
        return self.get_from_endpoint("experiment/metrics/get-metric", params)

    def get_experiment_multi_metrics(
        self, experiment_keys, metrics, independent=True, full=True
    ):
        payload = {
            "targetedExperiments": experiment_keys,
            "metrics": metrics,
            "independentMetrics": independent,
            "fetchFull": full,
        }
        return self.post_from_endpoint("experiments/multi-metric-chart", payload)

    def get_experiment_asset_list(self, experiment_key, asset_type=None):
        """
        Get a list of assets associated with the experiment.
        """
        params = {"experimentKey": experiment_key}
        if asset_type is not None:
            params["type"] = asset_type
        results = self.get_from_endpoint("experiment/asset/list", params)
        if results:
            return results["assets"]

    def get_experiment_asset(self, experiment_key, asset_id, return_type="binary"):
        params = {"experimentKey": experiment_key, "assetId": asset_id}
        return self.get_from_endpoint(
            "experiment/asset/get-asset", params, return_type=return_type
        )

    def get_experiment_others_summaries(self, experiment_key):
        params = {"experimentKey": experiment_key}
        return self.get_from_endpoint("experiment/log-other", params)

    def get_experiment_system_details(self, experiment_key):
        """
        Return the dictionary of system details.
        """
        params = {"experimentKey": experiment_key}
        return self.get_from_endpoint("experiment/system-details", params)

    def get_experiment_html(self, experiment_key):
        """
        Get the HTML associated with the experiment.
        """
        params = {"experimentKey": experiment_key}
        return self.get_from_endpoint("experiment/html", params=params)

    def get_experiment_code(self, experiment_key):
        """
        Get the associated source code for this experiment.
        """
        params = {"experimentKey": experiment_key}
        return self.get_from_endpoint("experiment/code", params)

    def get_experiment_output(self, experiment_key):
        """
        Get the associated standard output for this experiment.
        """
        params = {"experimentKey": experiment_key}
        return self.get_from_endpoint("experiment/output", params)

    def get_experiment_metadata(self, experiment_key):
        """
        Returns the JSON metadata for an experiment

        Returns:

        ```python
        {
         "experimentKey": "someExperimentKey",
         "experimentName": "someExperimentName",
         "optimizationId": "someOptimizationId",
         "projectId": "someProjectId",
         "projectName": "someProjectName",
         "workspaceName": "someWorkspaceName",
         "durationMillis": someDurationMillis,
         "startTimeMillis": someStartTimeMillis,
         "endTimeMillis": someEndTimeMillis
        }
        ```
        """
        params = {"experimentKey": experiment_key}
        results = self.get_from_endpoint("experiment/metadata", params)
        return results

    def get_experiment_git_patch(self, experiment_key):
        """
        Get the git-patch associated with this experiment.
        """
        params = {"experimentKey": experiment_key}
        results = self.get_from_endpoint("experiment/git/patch", params, "binary")
        # NOTE: returns either a binary JSON message or a binary git patch
        if results.startswith(b'{"msg"'):
            return None  # JSON indicates no patch
        else:
            return results

    def get_experiment_git_metadata(self, experiment_key):
        """
        Get the git-metadata associated with this experiment.
        """
        params = {"experimentKey": experiment_key}
        return self.get_from_endpoint("experiment/git/metadata", params)

    def get_experiments_metadata(self, workspace, project_name):
        """
        Return the names of the projects in a workspace.
        """
        payload = {"workspaceName": workspace, "projectName": project_name}
        results = self.get_from_endpoint("projects", payload)
        return results

    # Other methods:

    def get_workspaces(self):
        """
        Get workspace names.
        """
        return self.get_from_endpoint("workspaces", {})

    def get_project_experiments(self, workspace, project_name):
        """
        Return the metadata JSONs of the experiments in a project.
        """
        payload = {"workspaceName": workspace, "projectName": project_name}
        results = self.get_from_endpoint("experiments", payload)
        # Returns list of experiment dicts
        return results

    def get_project_notes_by_id(self, project_id):
        """
        Return the notes of a project.
        """
        payload = {"projectId": project_id}
        results = self.get_from_endpoint("project/notes", payload)
        if results and "notes" in results:
            return results["notes"]

    def get_project_jsons(self, workspace):
        """
        Return the JSONs of the projects in a workspace.
        """
        payload = {"workspaceName": workspace}
        return self.get_from_endpoint("projects", payload)

    def get_projects(self, workspace):
        """
        Get project names in a workspace.
        """
        payload = {"workspaceName": workspace}
        results = self.get_from_endpoint("projects", payload)
        if results and "projects" in results:
            projects = [
                project_json["projectName"] for project_json in results["projects"]
            ]
            return projects

    def get_project(self, workspace=None, project_name=None, project_id=None):
        """
        Get project details.
        """
        if project_id is not None:
            payload = {"projectId": project_id}
        else:
            payload = {"workspaceName": workspace, "projectName": project_name}
        results = self.get_from_endpoint("project", payload)
        return results

    def get_project_by_id(self, project_id):
        """
        Get project details.
        """
        payload = {"projectId": project_id}
        results = self.get_from_endpoint("project", payload)
        return results

    def get_project_json(self, workspace, project_name):
        """
        Get Project metadata JSON.
        """
        payload = {"workspaceName": workspace}
        results = self.get_from_endpoint("projects", payload)
        if results and "projects" in results:
            projects = [
                project_json
                for project_json in results["projects"]
                if project_json["projectName"] == project_name
            ]
            if len(projects) > 0:
                # Get the first if more than one
                return projects[0]
            # else, return None

    def query_project(self, workspace, project_name, predicates, archived=False):
        """
        Given a workspace, project_name, and predicates, return matching experiments.
        """
        payload = {
            "workspaceName": workspace,
            "projectName": project_name,
            "predicates": predicates,
            "archived": archived,
        }
        return self.post_from_endpoint("project/query", payload)

    def get_project_columns(self, workspace, project_name):
        """
        Given a workspace and project_name return the column names, types, etc.
        """
        payload = {"workspaceName": workspace, "projectName": project_name}
        return self.get_from_endpoint("project/column-names", payload)

    # Write methods:

    def update_project(
        self,
        workspace,
        project_name,
        new_project_name=None,
        description=None,
        public=None,
    ):
        """
        Update the metadata of a project by project_name
        and workspace.

        Args:
            workspace: name of workspace
            project_name: name of project
            new_project_name: new name of project (optional)
            description: new description of project (optional)
            public: new setting of visibility (optional)
        """
        payload = {}
        if project_name is None or workspace is None:
            raise ValueError("update_project requires workspace and project_name")
        payload["projectName"] = project_name
        payload["workspaceName"] = workspace
        if new_project_name is not None:
            payload["newProjectName"] = new_project_name
        if description is not None:
            payload["newProjectDescription"] = description
        if public is not None:
            payload["isPublic"] = public
        response = self.post_from_endpoint("write/project/update", payload)
        return response

    def update_project_by_id(
        self, project_id, new_project_name=None, description=None, public=None
    ):
        """
        Update the metdata of a project by project_id.

        Args:
            project_id: project id
            new_project_name: new name of project (optional)
            description: new description of project (optional)
            public: new setting of visibility (optional)
        """
        if project_id is None:
            raise ValueError("update_project_by_id requires project_id")
        payload = {}
        payload["projectId"] = project_id
        if new_project_name is not None:
            payload["newProjectName"] = new_project_name
        if description is not None:
            payload["newProjectDescription"] = description
        if public is not None:
            payload["isPublic"] = public
        response = self.post_from_endpoint("write/project/update", payload)
        return response

    def add_experiment_gpu_metrics(self, experiment_key, gpu_metrics):
        """
        Add an instance of GPU metrics.

        Args:
            experiment_key: an experiment id
            gpu_metrics: a list of dicts with keys:
                * gpuId: required, Int identifier
                * freeMemory: required, Long
                * usedMemory: required, Long
                * gpuUtilization: required, Int percentage utilization
                * totalMemory: required, Long
        """
        payload = {"experimentKey": experiment_key, "gpus": gpu_metrics}
        response = self.post_from_endpoint("write/experiment/gpu-metrics", payload)
        return response

    def add_experiment_cpu_metrics(
        self,
        experiment_key,
        cpu_metrics,
        context=None,
        step=None,
        epoch=None,
        timestamp=None,
    ):
        """
        Add an instance of CPU metrics.

        Args:
            experiment_key: an experiment id
            cpu_metrics: a list of integer percentages, ordered by cpu
            context: optional, a run context
            step: optional, the current step
            epoch: optional, the current epoch
            timestamp: optional": current time, in milliseconds since the Epoch
        """
        payload = {
            "experimentKey": experiment_key,
            "cpuPercentUtilization": cpu_metrics,
        }
        if context is not None:
            payload["context"] = context
        if step is not None:
            payload["step"] = step
        if epoch is not None:
            payload["epoch"] = epoch
        if timestamp is not None:
            payload["timestamp"] = timestamp
        response = self.post_from_endpoint("write/experiment/cpu-metrics", payload)
        return response

    def add_experiment_ram_metrics(
        self,
        experiment_key,
        total_ram,
        used_ram,
        context=None,
        step=None,
        epoch=None,
        timestamp=None,
    ):
        """
        Add an instance of RAM metrics.

        Args:
            experiment_key: an experiment id
            total_ram: required, total RAM available
            used_ram: required,  RAM used
            context: optional, the run context
            step: optional, the current step
            epoch: optional, the current epoch
            timestamp: optional, the current timestamp
        """
        payload = {
            "experimentKey": experiment_key,
            "totalRam": total_ram,
            "usedRam": used_ram,
        }
        if context is not None:
            payload["context"] = context
        if step is not None:
            payload["step"] = step
        if epoch is not None:
            payload["epoch"] = epoch
        if timestamp is not None:
            payload["timestamp"] = timestamp
        response = self.post_from_endpoint("write/experiment/ram-metrics", payload)
        return response

    def add_experiment_load_metrics(
        self,
        experiment_key,
        load_avg,
        context=None,
        step=None,
        epoch=None,
        timestamp=None,
    ):
        """
        Add an instance of system load metrics.

        Args:
            experiment_key: an experiment id
            load_avg: required, the load average
            context: optional, the run context
            step: optional, the current step
            epoch: optional, the current epoch
            timestamp: optional, the current timestamp
        """
        payload = {"experimentKey": experiment_key, "loadAverage": load_avg}
        if context is not None:
            payload["context"] = context
        if step is not None:
            payload["step"] = step
        if epoch is not None:
            payload["epoch"] = epoch
        if timestamp is not None:
            payload["timestamp"] = timestamp
        response = self.post_from_endpoint("write/experiment/load-metrics", payload)
        return response

    def set_experiment_git_metadata(
        self, experiment_key, user, root, branch, parent, origin
    ):
        """
        """
        payload = {
            "experimentKey": experiment_key,
            "user": user,
            "root": root,
            "branch": branch,
            "parent": parent,
            "origin": origin,
        }
        response = self.post_from_endpoint("write/experiment/git/metadata", payload)
        return response

    def set_experiment_git_patch(self, experiment_key, contents):
        """
        """
        params = {"experimentKey": experiment_key}
        files = {"file": ("filename", contents)}
        response = self.post_from_endpoint(
            "write/experiment/git/patch", {}, files=files, params=params
        )
        return response

    def set_experiment_code(self, experiment_key, code):
        payload = {"experimentKey": experiment_key, "code": code}
        response = self.post_from_endpoint("write/experiment/code", payload)
        return response

    def set_experiment_model_graph(self, experiment_key, graph):
        payload = {"experimentKey": experiment_key, "graph": graph}
        response = self.post_from_endpoint("write/experiment/graph", payload)
        return response

    def set_experiment_os_packages(self, experiment_key, os_packages):
        payload = {"experimentKey": experiment_key, "osPackages": os_packages}
        response = self.post_from_endpoint("write/experiment/system-details", payload)
        return response

    def set_experiment_user(self, experiment_key, user):
        payload = {"experimentKey": experiment_key, "user": user}
        response = self.post_from_endpoint("write/experiment/system-details", payload)
        return response

    def set_experiment_installed_packages(self, experiment_key, installed_packages):
        payload = {
            "experimentKey": experiment_key,
            "installedPackages": installed_packages,
        }
        response = self.post_from_endpoint("write/experiment/system-details", payload)
        return response

    def set_experiment_command(self, experiment_key, command):
        payload = {"experimentKey": experiment_key, "command": command}
        response = self.post_from_endpoint("write/experiment/system-details", payload)
        return response

    def set_experiment_gpu_static_info(self, experiment_key, gpu_static_info):
        payload = {
            "experimentKey": experiment_key,
            "gpuStaticInfoList": gpu_static_info,
        }
        response = self.post_from_endpoint("write/experiment/system-details", payload)
        return response

    def set_experiment_executable(self, experiment_key, executable):
        payload = {"experimentKey": experiment_key, "executable": executable}
        response = self.post_from_endpoint("write/experiment/system-details", payload)
        return response

    def set_experiment_hostname(self, experiment_key, hostname):
        payload = {"experimentKey": experiment_key, "hostname": hostname}
        response = self.post_from_endpoint("write/experiment/system-details", payload)
        return response

    def set_experiment_ip(self, experiment_key, ip):
        payload = {"experimentKey": experiment_key, "ip": ip}
        response = self.post_from_endpoint("write/experiment/system-details", payload)
        return response

    def log_experiment_system_info(self, experiment_key, system_info):
        if not isinstance(system_info, list):
            raise ValueError("system_info must be a list of {key:..., value:...} dicts")
        for si in system_info:
            if "key" not in si or "value" not in si:
                raise ValueError(
                    "system_info must be a list of {key:..., value:...} dicts"
                )

        payload = {
            "experimentKey": experiment_key,
            "logAdditionalSystemInfoList": system_info,
        }
        response = self.post_from_endpoint("write/experiment/system-details", payload)
        return response

    def set_experiment_network_interface_ips(
        self, experiment_key, network_interface_ips
    ):
        payload = {
            "experimentKey": experiment_key,
            "networkInterfaceIps": network_interface_ips,
        }
        response = self.post_from_endpoint("write/experiment/system-details", payload)
        return response

    def set_experiment_os(self, experiment_key, os):
        payload = {"experimentKey": experiment_key, "os": os}
        response = self.post_from_endpoint("write/experiment/system-details", payload)
        return response

    def set_experiment_os_type(self, experiment_key, os_type):
        payload = {"experimentKey": experiment_key, "osType": os_type}
        response = self.post_from_endpoint("write/experiment/system-details", payload)
        return response

    def set_experiment_pid(self, experiment_key, pid):
        payload = {"experimentKey": experiment_key, "pid": pid}
        response = self.post_from_endpoint("write/experiment/system-details", payload)
        return response

    def set_experiment_python_version(self, experiment_key, python_version):
        payload = {"experimentKey": experiment_key, "pythonVersion": python_version}
        response = self.post_from_endpoint("write/experiment/system-details", payload)
        return response

    def set_experiment_python_version_verbose(
        self, experiment_key, python_version_verbose
    ):
        payload = {
            "experimentKey": experiment_key,
            "pythonVersionVerbose": python_version_verbose,
        }
        response = self.post_from_endpoint("write/experiment/system-details", payload)
        return response

    def update_experiment_status(self, experiment_key):
        payload = {"experimentKey": experiment_key}
        response = self.get_from_endpoint("write/experiment/set-status", payload)
        return response

    def set_experiment_start_end(self, experiment_key, start_time, end_time):
        """
        Set the start/end time of an experiment.

        Note: times are in milliseconds.
        """
        payload = {
            "experimentKey": experiment_key,
            "startTimeMillis": start_time,
            "endTimeMillis": end_time,
        }
        response = self.post_from_endpoint(
            "write/experiment/set-start-end-time", payload
        )
        return response

    def set_project_notes_by_id(self, project_id, notes):
        """
        Set the notes of a project.
        """
        payload = {"projectId": project_id, "notes": notes}
        results = self.post_from_endpoint("write/project/notes", payload)
        if results:
            return results.json()

    def log_experiment_output(
        self, experiment_key, lines, context=None, stderr=False, timestamp=None
    ):
        """
        Log an output line.

        Args:
            experiment_key: str, the experiment id
            lines: list of str, the lines to log
            context: str, the context of the output
            stderr: bool, if True, then output is stderr
            timestamp: int, time in seconds, since epoch
        """
        if timestamp is None:
            timestamp = get_time_monotonic()
        stdout_lines = [
            {
                "stderr": stderr,
                "output": line + "\n",
                "localTimestamp": int(timestamp * 1000),
                "offset": offset,
            }
            for (offset, line) in enumerate(lines.split("\n"))
        ]
        payload = {
            "experimentKey": experiment_key,
            "runContext": context,
            "outputLines": stdout_lines,
        }
        response = self.post_from_endpoint("write/experiment/output", payload)
        return response

    def log_experiment_other(self, experiment_key, key, value, timestamp=None):
        """
        Set an other key/value pair for an experiment.

        Args:
            experiment_key: str, the experiment id
            key: str, the name of the other value
            value: any, the value of the other key
            timestamp: int, time in seconds, since epoch
        """
        payload = {"experimentKey": experiment_key, "key": key, "value": value}
        if timestamp is not None:
            payload["timestamp"] = int(timestamp * 1000)
        response = self.post_from_endpoint("write/experiment/log-other", payload)
        return response

    def log_experiment_parameter(
        self, experiment_key, parameter, value, step=None, timestamp=None
    ):
        """
        Set a parameter name/value pair for an experiment.

        Args:
            experiment_key: str, the experiment id
            parameter: str, the name of the parameter
            value: any, the value of the parameter
            step: int, the step number at time of logging
            timestamp: int, time in seconds, since epoch
        """
        payload = {
            "experimentKey": experiment_key,
            "parameterName": parameter,
            "parameterValue": value,
        }
        if step is not None:
            payload["step"] = step
        if timestamp is not None:
            payload["timestamp"] = int(timestamp * 1000)
        response = self.post_from_endpoint("write/experiment/parameter", payload)
        return response

    def log_experiment_metric(
        self,
        experiment_key,
        metric,
        value,
        step=None,
        epoch=None,
        timestamp=None,
        context=None,
    ):
        """
        Set a metric name/value pair for an experiment.
        """
        payload = {
            "experimentKey": experiment_key,
            "metricName": metric,
            "metricValue": value,
        }
        if epoch is not None:
            payload["epoch"] = epoch
        if context is not None:
            payload["context"] = context
        if step is not None:
            payload["step"] = step
        if timestamp is not None:
            payload["timestamp"] = int(timestamp * 1000)
        response = self.post_from_endpoint("write/experiment/metric", payload)
        return response

    def log_experiment_html(
        self, experiment_key, html, overwrite=False, timestamp=None
    ):
        """
        Set, or append onto, an experiment's HTML.

        Args:
            experiment_key: str, the experiment id
            html: str, the html string to log
            overwrite: bool, if, true overwrite previously-logged html
            timestamp: int, time in seconds, since epoch
        """
        if timestamp is None:
            timestamp = local_timestamp()
        payload = {
            "experimentKey": experiment_key,
            "html": html,
            "override": overwrite,
            "timestamp": int(timestamp * 1000),
        }
        response = self.post_from_endpoint("write/experiment/html", payload)
        return response

    def add_experiment_tags(self, experiment_key, tags):
        """
        Append onto an experiment's list of tags.
        """
        payload = {"experimentKey": experiment_key, "addedTags": tags}
        response = self.post_from_endpoint("write/experiment/tags", payload)
        return response

    def log_experiment_asset(
        self,
        experiment_key,
        filename,
        step=None,
        overwrite=None,
        context=None,
        ftype=None,
        metadata=None,
        extension=None,
    ):
        """
        Upload an asset to an experiment.
        """
        with open(filename, "rb") as fp:
            params = {"experimentKey": experiment_key, "fileName": filename}
            files = {"file": (filename, fp)}
            if step is not None:
                params["step"] = step
            if overwrite is not None:
                params["overwrite"] = overwrite
            if context is not None:
                params["context"] = context
            if ftype is not None:
                params["type"] = ftype
            if metadata is not None:
                params["metadata"] = metadata
            if extension is not None:
                params["extension"] = extension
            else:
                ext = os.path.splitext(filename)[1]
                if ext:
                    params["extension"] = ext

            response = self.post_from_endpoint(
                "write/experiment/upload-asset", {}, params=params, files=files
            )
            return response

    def log_experiment_image(
        self,
        experiment_key,
        filename,
        image_name=None,
        step=None,
        overwrite=None,
        context=None,
    ):
        """
        Upload an image asset to an experiment.
        """
        _, filename_extension = os.path.splitext(filename)
        with open(filename, "rb") as fp:
            params = {
                "experimentKey": experiment_key,
                "type": "image",
                "extension": filename_extension,
            }
            files = {"file": (filename, fp)}
            if image_name is not None:
                params["fileName"] = image_name
            if step is not None:
                params["step"] = step
            if overwrite is not None:
                params["overwrite"] = overwrite
            if context is not None:
                params["context"] = context
            response = self.post_from_endpoint(
                "write/experiment/upload-asset", {}, params=params, files=files
            )
            return response

    def stop_experiment(self, experiment_key):
        """
        Stop a running experiment.
        """
        payload = {"experimentKey": experiment_key}
        return self.get_from_endpoint("write/experiment/stop", payload)

    # Create, Delete, and Archive methods:

    def delete_experiment(self, experiment_key):
        """
        Delete one experiment.
        """
        payload = {"experimentKey": experiment_key}
        return self.get_from_endpoint("write/experiment/delete", payload)

    def delete_project(
        self,
        workspace=None,
        project_name=None,
        project_id=None,
        delete_experiments=False,
    ):
        """
        Delete a project.
        """
        if project_id is not None:
            payload = {
                "projectId": project_id,
                "deleteAllExperiments": delete_experiments,
            }
        else:
            payload = {
                "workspaceName": workspace,
                "projectName": project_name,
                "deleteAllExperiments": delete_experiments,
            }
        return self.post_from_endpoint("write/project/delete", payload)

    def restore_experiment(self, experiment_key):
        """
        Restore one experiment.
        """
        payload = {"experimentKey": experiment_key}
        return self.get_from_endpoint("write/experiment/restore", payload)

    def delete_experiments(self, experiment_keys):
        """
        Delete list of experiments.
        """
        return [self.delete_experiment(key) for key in experiment_keys]

    def archive_experiment(self, experiment_key):
        """
        Archive one experiment.
        """
        payload = {"experimentKey": experiment_key}
        return self.get_from_endpoint("write/experiment/archive", payload)

    def archive_experiments(self, experiment_keys):
        """
        Archive list of experiments.
        """
        return [self.archive_experiment(key) for key in experiment_keys]

    def create_project(
        self, workspace, project_name, project_description=None, public=False
    ):
        """
        Create a project.
        """
        payload = {
            "workspaceName": workspace,
            "projectName": project_name,
            "projectDescription": project_description,
            "isPublic": public,
        }
        response = self.post_from_endpoint("write/project/create", payload)
        return response.json()

    def create_experiment(self, workspace, project_name, experiment_name=None):
        """
        Create an experiment and return its associated APIExperiment.
        """
        payload = {"workspaceName": workspace, "projectName": project_name}
        if experiment_name is not None:
            payload["experimentName"] = experiment_name
        return self.post_from_endpoint("write/experiment/create", payload)

    def create_experiment_symlink(self, experiment_key, project_name):
        """
        Create a copy of this experiment in another project
        in the workspace.
        """
        payload = {"experimentKey": experiment_key, "projectName": project_name}
        return self.get_from_endpoint("write/project/symlink", payload)

    # General methods:

    def close(self):
        self.low_level_api_client.close()

    def do_not_cache(self, *items):
        """
        Add these items from the do-not-cache list. Ignored
        as this class does not have cache.
        """
        pass

    def do_cache(self, *items):
        """
        Remove these items from the do-not-cache list. Raises
        Exception as this class does not have cache.
        """
        raise Exception("this implementation does not have cache")


class RestApiClientWithCache(RestApiClient):
    """
    Same as RestApiClient, except with optional cache.

    When you post_from_endpoint(write_endpoint) you clear the
    associated read_endpoints.

    When you get_from_endpoint(read_endpoint) you attempt to
    read from cache and save to cache unless in the NOCACHE.

    If you read from a read_endpoint that is not listed, then
    a debug message is shown.
    """

    # map of write endpoints to read endpoints
    # POST-ENDPOINT: [(GET-ENDPOINT, [GET-ARGS]), ...]
    ENDPOINTS = {
        "write/project/symlink": [],  # Nothing to do
        "write/experiment/set-status": [],  # Nothing to do
        "write/experiment/set-start-end-time": [
            ("experiment/metadata", ["experimentKey"])
        ],
        "write/experiment/system-details": [
            ("experiment/system-details", ["experimentKey"])
        ],
        "write/experiment/code": [("experiment/code", ["experimentKey"])],
        "write/experiment/graph": [("experiment/graph", ["experimentKey"])],
        "write/experiment/output": [("experiment/output", ["experimentKey"])],
        "write/experiment/log-other": [("experiment/log-other", ["experimentKey"])],
        "write/experiment/parameter": [("experiment/parameters", ["experimentKey"])],
        "write/experiment/metric": [
            ("experiment/metrics/get-metric", ["experimentKey"]),
            ("experiment/metrics/summary", ["experimentKey"]),
        ],
        "write/experiment/html": [("experiment/html", ["experimentKey"])],
        "write/experiment/tags": [("experiment/tags", ["experimentKey"])],
        "write/experiment/upload-asset": [
            ("experiment/asset/list", ["experimentKey"]),  # not usually cached
            (
                "experiment/asset/get-asset",
                ["experimentKey", "assetId"],
            ),  # not usually cached
        ],
        "write/experiment/git/metadata": [
            ("experiment/git/metadata", ["experimentKey"])
        ],
        "write/experiment/git/patch": [("experiment/git/patch", ["experimentKey"])],
        "write/experiment/cpu-metrics": [
            ("experiment/system-details", ["experimentKey"])
        ],
        "write/experiment/gpu-metrics": [
            ("experiment/system-details", ["experimentKey"])
        ],
        "write/experiment/load-metrics": [
            ("experiment/system-details", ["experimentKey"])
        ],
        "write/experiment/ram-metrics": [
            ("experiment/system-details", ["experimentKey"])
        ],
        "write/project/notes": [("project/notes", ["projectId"])],
        # Only read that is really a POST:
        "experiments/multi-metric-chart": [],  # Nothing to do
    }  # type: Dict[str, List[Tuple[str, List[str]]]]

    # Don't use cache on these GET endpoints:
    NOCACHE_ENDPOINTS = set(
        [
            "write/experiment/delete",  # GET
            "write/experiment/archive",  # GET
            "write/experiment/restore",  # GET
            "write/experiment/set-status",  # GET
            "write/project/symlink",  # GET
            "projects",  # GET
            "project/column-names",  # GET
            "experiments",  # GET
            "experiment/metadata",  # GET
            "experiment/asset/get-asset",  # GET
            "experiment/asset/list",  # GET
        ]
    )

    # Some read endpoints have additional payload key/values to clear:
    EXTRA_PAYLOAD = {
        "experiment/asset/list": {
            "type": ["all", "histogram_combined_3d", "image", "audio", "video"]
        }
    }

    def __init__(self, *args, **kwargs):
        super(RestApiClientWithCache, self).__init__(*args, **kwargs)
        self.use_cache = True
        self.cache = {}
        self.READ_ENDPOINTS = list(
            itertools.chain.from_iterable(
                [[ep for (ep, items) in self.ENDPOINTS[key]] for key in self.ENDPOINTS]
            )
        )

    # Cache methods:

    def do_not_cache(self, *items):
        """
        Add these items from the do-not-cache list.
        """
        for item in items:
            self.NOCACHE_ENDPOINTS.add(item)

    def do_cache(self, *items):
        """
        Remove these items from the do-not-cache list.
        """
        for item in items:
            if item in self.NOCACHE_ENDPOINTS:
                self.NOCACHE_ENDPOINTS.remove(item)

    def cacheable(self, read_endpoint):
        return read_endpoint not in self.NOCACHE_ENDPOINTS

    def get_hash(self, kwargs):
        key = hash(json.dumps(kwargs, sort_keys=True, default=str))
        return key

    def cache_get(self, **kwargs):
        # Look up in cache
        key = self.get_hash(kwargs)
        if key in self.cache:
            hit = True
            value = self.cache[key]
        else:
            hit = False
            value = None
        return hit, value

    def cache_put(self, value, **kwargs):
        # Put in cache
        if not self.check_read_endpoint(kwargs["endpoint"]):
            LOGGER.debug(
                "this endpoint cannot be cleared from cache: %r", kwargs["endpoint"]
            )
        key = self.get_hash(kwargs)
        LOGGER.debug("cache_put: %s, key: %s", kwargs, key)
        self.cache[key] = value

    def cache_clear_return_types(self, **kwargs):
        # Remove all return_types from cache for this endpoint/params:
        for return_type in ["json", "binary", "text"]:
            kwargs["return_type"] = return_type
            key = self.get_hash(kwargs)
            LOGGER.debug("attempting cache_clear: %s, key: %s", kwargs, key)
            if key in self.cache:
                LOGGER.debug("cache_clear: CLEARED!")
                del self.cache[key]

    def cache_clear(self, **kwargs):
        extra = self.EXTRA_PAYLOAD.get(kwargs["endpoint"])
        if extra:
            # First, without extras:
            self.cache_clear_return_types(**kwargs)
            # If more than one extra, we have to do all combinations:
            for key in extra:
                for value in extra[key]:
                    kwargs["payload"][key] = value
                    self.cache_clear_return_types(**kwargs)
        else:
            self.cache_clear_return_types(**kwargs)

    def get_read_endpoints(self, write_endpoint):
        """
        Return the mapping from a write endpoint to a list
        of tuples of (read-endpoint, [payload keys]) to
        clear the associated read endpoint caches.
        """
        return self.ENDPOINTS.get(write_endpoint, None)

    def check_read_endpoint(self, read_endpoint):
        """
        Check to see if the read_endpoint is in the
        list of known ones, or if it is not cached.
        If it is neither, then there is no way to
        clear it.
        """
        return (read_endpoint in self.READ_ENDPOINTS) or not self.cacheable(
            read_endpoint
        )

    # Overridden methods:

    def reset(self):
        self.cache.clear()

    def cache_clear_read_endpoints(self, endpoint, payload):
        # Clear read cache:
        endpoints = self.get_read_endpoints(endpoint)
        if endpoints:
            for read_endpoint, keys in endpoints:
                # Build read payload:
                read_payload = {}
                for key in keys:
                    if key in payload:
                        read_payload[key] = payload[key]
                self.cache_clear(endpoint=read_endpoint, payload=read_payload)

    def post_from_endpoint(self, endpoint, payload, **kwargs):
        """
        Wrapper that clears the cache after posting.
        """
        response = super(RestApiClientWithCache, self).post_from_endpoint(
            endpoint, payload, **kwargs
        )
        self.cache_clear_read_endpoints(endpoint, payload)
        if "params" in kwargs:
            self.cache_clear_read_endpoints(endpoint, kwargs["params"])
        return response

    def get_from_endpoint(self, endpoint, params, return_type="json"):
        """
        Wrapper around RestApiClient.get_from_endpoint() that adds cache.

        """
        if self.use_cache and self.cacheable(endpoint):
            hit, result = self.cache_get(
                endpoint=endpoint, payload=params, return_type=return_type
            )
            if hit:
                # LOGGER.debug(
                #     "RestApiClientWithCache, hit: endpoint = %s, params = %s, return_type = %s",
                #     endpoint,
                #     params,
                #     return_type,
                # )
                return result

        # LOGGER.debug(
        #     "RestApiClientWithCache, miss: endpoint = %s, params = %s, return_type = %s",
        #     endpoint,
        #     params,
        #     return_type,
        # )
        retval = super(RestApiClientWithCache, self).get_from_endpoint(
            endpoint, params, return_type
        )

        if self.use_cache and self.cacheable(endpoint) and retval is not None:
            self.cache_put(
                retval, endpoint=endpoint, payload=params, return_type=return_type
            )

        return retval


def get_optimizer_api_client(
    api_key, server_address=None, headers=None, rest_api_key=None
):
    # (str, Optional[Dict[str, Any]]) -> RestApiClient
    config = get_config()
    if server_address is None:
        server_address = config["comet.url_override"]
    server_url = get_root_url(server_address)

    low_level_api = LowLevelHTTPClient(server_url, headers)

    rest_api_key = get_rest_api_key(rest_api_key, config)

    return OptimizerApiClient(api_key, server_url, low_level_api, rest_api_key)


class OptimizerApiClient(BaseApiClient):

    """ This API Client is meant to discuss to the Optimizer backend (www.comet.ml/clientlib/optimizer/) and handle, params and payload formatting,
    input validation if necessary, creating the url and parsing the output. All
    the HTTP communication is handled by the low-level HTTP client.

    Inputs must be JSON-encodable, any conversion must be done by the caller.

    One method equals one endpoint and one call"""

    def __init__(self, api_key, server_url, low_level_api_client, rest_api_key):
        # type: (str, str, LowLevelHTTPClient, str) -> None
        super(OptimizerApiClient, self).__init__(
            server_url, ["clientlib/"], low_level_api_client, rest_api_key, api_key
        )

    def get(self, url, params):
        from . import __version__

        headers = {
            self.REST_API_KEY_HEADER: self.rest_api_key,
            "PYTHON-SDK-VERSION": __version__,
        }

        return super(OptimizerApiClient, self).get(url, params=params, headers=headers)

    # Read endpoints

    def get_optimizer_best(
        self, experiment_key, optimizer_id, metric_name="loss", maximum=False
    ):
        """
        Get the best metric_name value (minimum by default).

        Args:
            experiment_key: An experiment key in the set
                experiments run by the optimizer.
            optimizer_id: The ID of the Optimizer.
            metric_name: str, default "loss". The metric
                being optimized.
            maximum: bool, default False. If True, return
                the largest value.
        """
        params = {
            "experimentKey": experiment_key,
            "apiKey": self.comet_api_key,
            "optimizationId": optimizer_id,
            "metricName": metric_name,
            "withMaxValue": maximum,
        }
        results = self.get_from_endpoint("optimizer/get-best-experiment", params)
        return results


def get_comet_api_client(server_address=None, headers=None):
    # (Optional[Dict[str, Any]]) -> CometApiClient
    config = get_config()
    if server_address is None:
        server_address = config["comet.url_override"]
    server_url = get_root_url(server_address)

    low_level_api = LowLevelHTTPClient(server_url, headers)

    return CometApiClient(server_url, low_level_api)


class CometApiClient(BaseApiClient):
    """
    Inputs must be JSON-encodable, any conversion must be done by the caller.

    One method equals one endpoint and one call
    """

    def __init__(self, server_url, low_level_api_client):
        # type: (str, LowLevelHTTPClient) -> None
        super(CometApiClient, self).__init__(
            server_url, ["api/auth/"], low_level_api_client, None, None
        )

    def get(self, url, params, headers=None):
        # Overrides to suppress exceptions on errors
        response = self.low_level_api_client.get(url, params=params, headers=headers)
        return response

    def post(self, url, payload, files=None, params=None):
        # CometApiClient-level headers to be injected
        headers = {}
        return super(CometApiClient, self).post(
            url, payload=payload, headers=headers, files=files, params=params
        )

    def check_email(self, email, reason):
        # type: (str, str) -> int
        """
        Check if the given email is associated with a user.

        Args:
            email: str, the email of the user
            reason: str, the reason for the check

        Returns: a status code

        * 200: ok, existing user
        * 204: unknown user
        """
        payload = {"email": email, "reason": reason}
        response = self.get_from_endpoint("users", payload, return_type="response")
        return response.status_code

    def create_user(self, email, username, signup_source):
        # type: (str, str, str) -> dict
        """
        Creates a temporary user token for the email/username.

        Args:
            email: str, an email address
            username: str, a proper Comet username
            signup_source: str, description of signup source

        Returns: dict (if successful), a JSON response as follows.
            Otherwise, a CometRestApiException with reason for
            failure.

        ```json
        {
         'cometUserName': 'new-usernane',
         'token': 'MXZRU1WXsEJAzeFn0I235423549',
         'apiKey': 'X6Wr0uKXZwOLnPFpNvV39874857'
        }
        ```
        """
        payload = {"email": email, "userName": username, "signupSource": signup_source}
        response = self.post_from_endpoint("users", payload)
        return response.json()
