#! /usr/bin/env python3

__all__ = ["Base"]

import argparse
import asyncio
import functools
import inspect
import json
import pathlib
import signal
import sys
from typing import Dict, List, Optional, Any, Union, Sequence

import appdirs  # type: ignore
import toml

from . import logging
from .exceptions import InvalidRequest, MethodNotFound
from .json import gen_objects

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Base:
    defaults: Dict[str, Any] = {}
    _kind: str = "base"
    _daemons: List["Base"] = []

    def __init__(
        self, name: str, config: Dict[str, Any], config_filepath: pathlib.Path
    ):
        """Create a yaq daemon.

        Parameters
        ----------
        name: str
            A name for this daemon
        config: dict
            Configuration parameters
        config_filepath: str
            The path for the configuration (not used internally, availble to clients)
        """
        self.name = name
        self.kind = self.__class__._kind
        self.config = config
        self._config_filepath = config_filepath
        self._state_filepath = (
            pathlib.Path(appdirs.user_data_dir("yaqd-state", "yaq"))
            / self.kind
            / f"{self.name}-state.toml"
        )
        logger.info(f"{self.name}: Config File Path = {self._config_filepath}")
        logger.info(f"{self.name}: State File Path = {self._state_filepath}")
        logger.info(f"{self.name}: TCP Port = {config['port']}")
        self._clients: List[str] = []

        self.serial = config.get("serial", None)
        self.make = config.get("make", None)
        self.model = config.get("model", None)

        self._busy_sig = asyncio.Event()
        self._not_busy_sig = asyncio.Event()

        self._loop = asyncio.get_event_loop()

        try:
            self._state_filepath.parent.mkdir(parents=True, exist_ok=True)
            with self._state_filepath.open("rt") as f:
                state = toml.load(f)
        except (toml.TomlDecodeError, FileNotFoundError):
            state = {}

        self._load_state(state)
        self._loop.create_task(self.save_state())

    class Protocol(asyncio.Protocol):
        def __init__(self, daemon, *args, **kwargs):
            self._daemon = daemon
            self._method_list = self._daemon.list_methods()
            asyncio.Protocol.__init__(self, *args, **kwargs)
            self._error_codes = {
                json.JSONDecodeError: {"code": -32700, "message": "Parse error"},
                InvalidRequest: {"code": -32600, "message": "Invalid Request"},
                MethodNotFound: {"code": -32601, "message": "Method not found"},
                TypeError: {"code": -32602, "message": "Invalid params"},
            }

        def connection_lost(self, exc):
            peername = self.transport.get_extra_info("peername")
            logger.info(f"Connection lost from {peername} to {self._daemon.name}")
            self._daemon._connection_lost(peername)

        def connection_made(self, transport):
            """Process an incomming connection."""
            peername = transport.get_extra_info("peername")
            logger.info(f"Connection made from {peername} to {self._daemon.name}")
            self.transport = transport
            self._daemon._connection_made(peername)

        def data_received(self, data):
            """Process an incomming request."""
            logger.debug(f"Data received: {repr(data)}")
            for d in gen_objects(data):
                self.process_single_request(d)

        def process_single_request(self, data):
            logger.debug(f"Process single received: {repr(data)}")
            try:
                request = json.loads(data)
                if isinstance(request, list):
                    if not request:
                        raise InvalidRequest
                    response = list(
                        filter(
                            lambda x: x is not None,
                            [self.run_method(r) for r in request],
                        )
                    )

                else:
                    response = self.run_method(request)
            except InvalidRequest:
                # Handle empty array
                response = {
                    "jsonrpc": "2.0",
                    "error": self._error_codes[InvalidRequest],
                    "id": None,
                }
            except json.JSONDecodeError:
                # Handle invalid JSON
                response = {
                    "jsonrpc": "2.0",
                    "error": self._error_codes[json.JSONDecodeError],
                    "id": None,
                }
            # Notifications do not get responses, empty batch response or None returned
            if response:
                self.transport.write(json.dumps(response).encode())

        def run_method(self, request):
            response = {"jsonrpc": "2.0"}
            # Ignoring "jsonrpc" in request
            # Will need to check if json-rpc v1.0 ever supported
            notification = False
            try:
                if not isinstance(request, dict) or "method" not in request:
                    request = {}
                    raise InvalidRequest
                notification = "id" not in request

                method = request["method"]
                response["id"] = request.get("id")
                params = request.get("params", [])

                if not isinstance(method, str):
                    notification = False
                    raise InvalidRequest
                if method not in self._method_list:
                    raise MethodNotFound(method)
                fun = getattr(self._daemon, method)
                if isinstance(params, list):
                    response["result"] = fun(*params)
                else:
                    response["result"] = fun(**params)
            except BaseException as e:
                logger.error(
                    f"Caught exception in {request.get('method', 'jsonrpc')}: {repr(e)}"
                )
                if type(e) in self._error_codes:
                    response["error"] = self._error_codes[type(e)]
                else:
                    response["error"] = {"code": -1, "message": repr(e)}
            if "error" in response:
                response.pop("result", None)
                try:
                    response["id"] = request.get("id", None)
                except:
                    response["id"] = None
                    return response
            if not notification:
                return response
            # Notifications get no response
            return None

    @classmethod
    def main(cls):
        """Run the event loop."""
        loop = asyncio.get_event_loop()
        if sys.platform.startswith("win"):
            signals = ()
        else:
            signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
        for s in signals:
            loop.add_signal_handler(
                s, lambda s=s: asyncio.create_task(cls.shutdown(s, loop))
            )
        loop.create_task(cls._main())
        try:
            loop.run_forever()
        finally:
            loop.close()

    @classmethod
    async def _main(cls):
        """Parse command line arguments, start event loop tasks."""
        # TODO: break up into more targeted functions
        loop = asyncio.get_running_loop()
        servers = []

        parser = argparse.ArgumentParser()
        parser.add_argument("--config", "-c", default=None, action="store")
        config_filepath = parser.parse_args().config
        if config_filepath is None:
            config_filepath = (
                pathlib.Path(appdirs.user_config_dir("yaqd", "yaq"))
                / cls._kind
                / "config.toml"
            )

        config_filepath = pathlib.Path(config_filepath)

        config_file = toml.load(config_filepath)

        if not config_file.get("enable", True):
            logger.info("Enable set to False, exiting")
            loop.stop()
            return

        for section in config_file:
            if section in ("shared-settings", "enable", "entry"):
                continue

            config = cls.defaults.copy()
            config.update(config_file.get("shared-settings", {}).copy())
            config.update(config_file[section])

            if not config.get("enable", True):
                continue

            daemon = cls(section, config, config_filepath)
            cls._daemons.append(daemon)
            loop.create_task(daemon.update_state())

            # This function is here to namespace `daemon` so it doesn't
            # get overridden for the lambda
            def server(daemon):
                return lambda: cls.Protocol(daemon)

            servers.append(
                await loop.create_server(
                    server(daemon), config.get("host", ""), config.get("port", None)
                )
            )

        await asyncio.wait(list(server.serve_forever() for server in servers))

    @classmethod
    async def shutdown(cls, sig, loop):
        """Gracefully shutdown the asyncio loop.

        Gathers all current tasks, and allows daemons to perform cleanup tasks.

        Adapted from https://www.roguelynn.com/words/asyncio-graceful-shutdowns/
        Original code is licensed under the MIT license, and sublicensed here.
        """
        logger.info(f"Received signal {sig.name}...")
        tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
        logger.info(f"Cancelling {len(tasks)} outstanding tasks")
        [task.cancel() for task in tasks]
        # This is done after cancelling so that shutdown tasks which require the loop
        # are not themselves cancelled.
        [d.close() for d in cls._daemons]
        tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
        await asyncio.gather(*tasks, return_exceptions=True)
        [d._save_state() for d in cls._daemons]
        if hasattr(signal, "SIGHUP") and sig == signal.SIGHUP:
            await cls._main()
        loop.stop()

    def _connection_made(self, peername: str) -> None:
        self._clients.append(peername)
        logger.debug(f"_connection_made {self._clients}")

    def _connection_lost(self, peername: str) -> None:
        self._clients.remove(peername)
        logger.debug(f"_connection_lost {self._clients}")

    def get_lineage(self) -> List[str]:
        """Get list of yaq-daemon inheritance."""
        return [t._kind for t in type(self).mro() if issubclass(t, Base)]

    def _save_state(self) -> None:
        """Write the current state to disk."""
        with open(self._state_filepath, "wt") as f:
            toml.dump(self.get_state(), f)

    async def save_state(self):
        """Schedule writing the current state to disk.

        Note: Current implementation only writes while busy (and once after busy)
        """
        while True:
            while self._busy:
                self._save_state()
                await asyncio.sleep(0.1)
            self._save_state()
            await self._busy_sig.wait()

    def config_filepath(self) -> str:
        """Retrieve the current filepath of the configuration."""
        return str(self._config_filepath.absolute())

    def get_config(self) -> Dict[str, Any]:
        """Retrieve the current configuration, including any defaults."""
        return self.config

    def list_methods(self) -> List[str]:
        """Return a list of all public methods."""
        filt = filter(lambda x: x[0] != "_", dir(self.__class__))
        # Use `isfunction` on the `__class__` to filter out classmethods
        filt = filter(lambda x: inspect.isfunction(getattr(self.__class__, x)), filt)
        filt = filter(lambda x: not asyncio.iscoroutinefunction(getattr(self, x)), filt)
        return list(filt)

    def set_state(self, **kwargs) -> None:
        """Set the daemon state.

        Input may be any portion of the entire state dictionary.
        Key value pairs that are not defined are propagated from the current daemon state.
        If input is not valid, daemon will raise exception.

        Parameters
        ----------
        state: dict
            New state
        """
        full = self.get_state()
        full.update(kwargs)
        self._load_state(full)
        self._save_state()

    def help(self, method: Optional[Union[str, Sequence[str]]] = None):
        """Return useful, human readable information about methods.

        Parameters
        ----------
        method: str or list of str (optional)
            The method or list of methods for which help is requested.
            Default is information on the daemon itself.

        Returns
        -------
        str or list of str: The requested documentation.
        """
        if method is None:
            return self.__doc__
        if isinstance(method, str):
            fun = getattr(self, method)
            return f"{method}{str(inspect.signature(fun))}\n{fun.__doc__}"
        return list(self.help(c) for c in method)

    def id(self) -> Dict[str, Optional[str]]:
        """Dictionary of identifying information for the daemon."""
        return {
            "name": self.name,
            "kind": self.kind,
            "make": self.make,
            "model": self.model,
            "serial": self.serial,
        }

    @property
    def _busy(self) -> bool:
        """Indicates the current 'busy' state for use in internal functions.

        Setting busy can be done with `self._busy = <True|False>`.
        Async tasks can wait for either sense using `await self._[not_]busy_sig.wait()`.
        """
        return self._busy_sig.is_set()

    @_busy.setter
    def _busy(self, value):
        if value:
            self._busy_sig.set()
            self._not_busy_sig.clear()
        else:
            self._not_busy_sig.set()
            self._busy_sig.clear()

    def busy(self) -> bool:
        """Boolean representing if the daemon is busy (state updated) or not."""
        return self._busy

    # The following functions (plus __init__) are what most daemon need to implement

    async def update_state(self):
        """Continually monitor and update the current daemon state."""
        pass

    def get_state(self) -> Dict[str, Any]:
        """Return the current daemon state."""
        return {}

    def _load_state(self, state):
        """Load an initial state from a dictionary (typically read from the state.toml file).

        Must be tolerant of missing fields, including entirely empty initial states.
        Raise an exception if state is invalid.

        Parameters
        ----------
        state: dict
            The saved state to load.
        """
        pass

    def close(self):
        """Perform necessary clean-up and stop running."""
        pass


if __name__ == "__main__":
    Base.main()
