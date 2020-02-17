# Copyright (C) 2019  Neural Concept SA

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ========================================================================
import os
import pprint
import asyncio
import websockets
from functools import wraps
import tabulate
import nest_asyncio
import halo
from time import sleep
import ssl
from requests import HTTPError
from json.decoder import JSONDecodeError

nest_asyncio.apply()


def handle_response(resp):
    try:
        resp.raise_for_status()
    except HTTPError as e:
        code = e.response.status_code
        try:
            payload = e.response.json()
        except JSONDecodeError:
            payload = None
        message = None
        if code == 405:
            message = "Unauthorized. Please check your credentials"
        elif code == 404:
            if payload is not None:
                message = f"{payload.get('message')}. Resource type: {payload.get('object_type')}. Resource id: {payload.get('uuid')}"
            else:
                message = "The resource you requested was not found."
        elif code == 403:
            if payload is not None:
                message = payload.get("message")
            else:
                message = "Not allowed."
        elif code == 400:
            if payload is not None:
                message = f"{payload.pop('message')}"
                for k, v in payload.items():
                    message += f" {k.capitalize()}: {v}"
            else:
                message = "Bad request."
        else:
            message = "The system encountered an unexpected error. Please contact your NCAPI administrator or refer to server logs for more detail."
        raise APIError(message, response=e.response)
    return AttrDict.convert(resp.json())


class APIError(HTTPError):
    def __init__(self, user_msg, response, *args, **kwargs):
        self.user_msg = user_msg
        super().__init__(*args, response=response, **kwargs)

    def _render_traceback_(self):
        return [
            f"{self.__class__.__name__} ({self.response.status_code}):",
            self.user_msg,
        ]

    def __str__(self):
        return (
            f"{self.__class__.__name__} ({self.response.status_code}): {self.user_msg}"
        )


def map_response(method):
    @wraps(method)
    def _wrapper(*args, **kwargs):
        resp = method(*args, **kwargs)
        return handle_response(resp)

    return _wrapper


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

    def __repr__(self):
        return pprint.pformat(dict(self))

    def _repr_html_(self):
        return tabulate.tabulate(self.items(), ["Attribute", "Value"], tablefmt="html")

    @classmethod
    def convert(cls, d):
        if isinstance(d, dict):
            res = d.copy()
            for k, v in res.items():
                res[k] = cls.convert(v)
            res = cls(res)
            return res
        elif isinstance(d, list):
            return list(map(cls.convert, d))
        else:
            return d


def merge_dicts(config_1, config_2=None):
    """merge_dicts
        This function is used for overwriting configuration values by app-configs.yaml
        by merging(and/or overwriting) keys from app_conf recursively.

        Args:
            config_1 (dict): default configuration
            config_2 (dict): application configuration
        Returns:
            merged version of both
    """
    if config_2 is None:
        return config_1

    for key, value in config_2.items():
        if key not in config_1 or not isinstance(value, dict):
            config_1[key] = value
        else:
            merge_dicts(config_1[key], config_2[key])

    return config_1


class ResourceList(list):
    def _repr_html_(self):
        try:
            dicts = []
            for it in self:
                if hasattr(it, "info"):
                    dicts.append(it.info)
                else:
                    dicts.append(it)
            all_keys = []
            for d in dicts:
                all_keys += list(d.keys())
            rows = []
            for d in dicts:
                row = []
                for k in all_keys:
                    if k in d.keys():
                        row.append(d[k])
                    else:
                        row.append("")
                rows.append(row)
            return tabulate.tabulate(rows, headers=all_keys, tablefmt="html")
        except:
            return self.__repr__()


def asyncio_run(coro):
    loop = asyncio.get_event_loop()
    ignore_aiohttp_ssl_eror(loop)
    return loop.run_until_complete(coro)


# https://github.com/snakewa/fast/commit/1a947097ba702b97242ba3c349e21bc00d088251
def ignore_aiohttp_ssl_eror(loop):
    """Ignore aiohttp #3535 issue with SSL data after close
     There appears to be an issue on Python 3.7 and aiohttp SSL that throws a
    ssl.SSLError fatal error (ssl.SSLError: [SSL: KRB5_S_INIT] application data
    after close notify (_ssl.c:2609)) after we are already done with the
    connection. See GitHub issue aio-libs/aiohttp#3535
     Given a loop, this sets up a exception handler that ignores this specific
    exception, but passes everything else on to the previous exception handler
    this one replaces.
     """
    import ssl
    import asyncio

    orig_handler = loop.get_exception_handler()

    def ignore_ssl_error(loop, context):
        if context.get('message') == 'SSL error in data received':
            # validate we have the right exception, transport and protocol
            exception = context.get('exception')
            protocol = context.get('protocol')
            if (
                isinstance(exception, ssl.SSLError) and exception.reason == 'KRB5_S_INIT' and
                isinstance(protocol, asyncio.sslproto.SSLProtocol) and
                isinstance(protocol._app_protocol, aiohttp.client_proto.ResponseHandler)
            ):
                if loop.get_debug():
                    asyncio.log.logger.debug('Ignoring aiohttp SSL KRB5_S_INIT error')
                return
        if orig_handler is not None:
            orig_handler(loop, context)
        else:
            loop.default_exception_handler(context)

    loop.set_exception_handler(ignore_ssl_error)


class SyncWebSocket:
    def __init__(self, url, verify_ssl=True, **kwargs):
        ssl_args = {}

        # optional certificate verification (e.g. for self-signed)
        optional_certificate = os.getenv("NCAPI_CERT")
        if verify_ssl and url[:3] == "wss" and optional_certificate:
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            ssl_context.load_verify_locations(optional_certificate)
            ssl_args["ssl"] = ssl_context
        elif not verify_ssl:
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            ssl_args["ssl"] = ssl_context

        async def _connect(url):
            return await websockets.connect(url, **ssl_args, **kwargs)

        self._sock = asyncio_run(_connect(url))

    def send(self, msg):
        return asyncio_run(self._sock.send(msg))

    def recv(self):
        return asyncio_run(self._sock.recv())


def list_files_subdirs(path, ignore_prefs=[".", "__"]):
    res = []
    if not os.path.isdir(path):
        return res
    for entry in os.scandir(path):
        if not any([os.path.basename(entry).startswith(pref) for pref in ignore_prefs]):
            if os.path.isdir(entry):
                res += list_files_subdirs(entry)
            else:
                res.append(entry.path)
    return res


def wait_for_completion(job, jobtype=None, notebook=True):
    info = job.info
    pref = ""
    if "name" in info.keys():
        pref = f"({info['name']}) " + pref
    if jobtype is not None:
        pref = f"{jobtype} " + pref
    if notebook:
        print(
            f"{pref}has been triggered. Please check its status regularly using Job(<client>, {info['name']}).info and wait for completion."
        )
        return
    status = "PENDING"
    spinner = halo.Halo(text=f"{pref}{status}", spinner="dots")
    spinner.start()
    while status in ["PENDING", "RUNNING", "CREATING"]:
        status = job.info["status"]
        spinner.text = f"{pref}{status}"
        sleep(1)
    if status == "FINISHED":
        spinner.succeed("Done!")
        sleep(1)
    else:
        spinner.fail("Error")
        sleep(1)


def delete_dependent_jobs(client, payload):
    async def _delete_dependent_jobs_async(client, payload):
        async def _stop_and_delete(j):
            try:
                j.stop()
            except APIError as e:
                if e.response.status_code == 403:
                    # Job is either complete or errored out. Safe to delete.
                    j.delete()
                    return
                else:
                    raise e
            status = "TO_STOP"
            timeout = 60
            t = 0
            while status not in ["ERROR", "STOPPED", "FINISHED"]:
                status = j.info["status"]
                sleep(1)
                t += 1
                if t == timeout:
                    raise TimeoutError(
                        f"Job {j.info.name} encountered a timeout. Stopping failed"
                    )
            if status == "ERROR":
                raise RuntimeError(
                    f"Job {j.info.name} encountered an error. Stopping failed"
                )
            j.delete()

        matching_jobs = []
        for j in client.jobs:
            info = j.info
            for k in payload.keys():
                if k not in info.keys() or info[k] != payload[k]:
                    continue
                matching_jobs.append(j)
        await asyncio.gather(*tuple(_stop_and_delete(j) for j in matching_jobs))

    return asyncio_run(_delete_dependent_jobs_async(client, payload))
