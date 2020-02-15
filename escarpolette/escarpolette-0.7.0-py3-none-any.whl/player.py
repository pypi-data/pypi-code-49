import asyncio
import json
import logging
from enum import Enum
from subprocess import Popen
from typing import Any, Dict, Optional, Tuple

from pydantic import BaseModel, ValidationError
from pydantic.fields import Field

from escarpolette.models import Playlist
from escarpolette.settings import Config


logger = logging.getLogger(__name__)


class MpvEvent(BaseModel):
    name: str = Field(..., alias="event")


class MpvResponse(BaseModel):
    data: Any
    error: str
    request_id: int


class State(str, Enum):
    PLAYING = "PLAYING"
    PAUSED = "PAUSED"
    STOPPED = "STOPPED"


class PlayerCommandError(ValueError):
    pass


class Player:
    """Control mpv using IPC."""

    _command_id = 0
    _mpv_ipc_socket = "/tmp/mpv-socket"
    _mpv: Optional[Popen] = None
    _mpv_reader: asyncio.StreamReader
    _mpv_writer: asyncio.StreamWriter
    _state = State.STOPPED

    async def init_app(self, config: Config) -> None:
        self._mpv_ipc_socket = config.MPV_IPC_SOCKET or self._mpv_ipc_socket
        self._mpv = Popen(
            [
                "mpv",
                "--idle",
                "--no-terminal",
                f"--input-ipc-server={self._mpv_ipc_socket}",
            ]
        )

        # Let MPV starts
        await asyncio.sleep(2)

        loop = asyncio.get_event_loop()
        loop.create_task(self._listen_events())
        self._mpv_reader, self._mpv_writer = await self._get_mpv_connection()

    def shutdown(self) -> None:
        if self._mpv_writer is not None:
            self._mpv_writer.close()

        if self._mpv is not None:
            # TODO: find why MPV does not respond to a SIGTERM signal
            self._mpv.kill()

    async def add_item(self, url: str) -> None:
        """Add a new item to the playlist.

        If the player was stopped, play the music.
        """
        if self._state == State.STOPPED:
            await self._send_command("loadfile", url, "append-play")
            self._state = State.PLAYING
        else:
            await self._send_command("loadfile", url, "append")

    async def get_current_item_title(self) -> Optional[str]:
        """Get the current playing item's title."""
        response = await self._send_command("get_property", "metadata")
        if not response:
            return None

        return response.data["title"]

    async def get_current_item_position(self) -> Optional[int]:
        response = await self._send_command("get_property", "playback-time")
        if not response:
            return None

        return response.data

    def get_state(self) -> State:
        return self._state

    async def play(self) -> None:
        """Play the current playlist."""
        if self._state == State.PLAYING:
            return
        elif self._state == State.STOPPED:
            raise PlayerCommandError("The player is stopped. Add an item to play it.")
        else:
            await self._send_command("cycle", "pause")

        return None

    async def pause(self) -> None:
        """Pause the current playlist."""
        if self._state == State.PAUSED:
            return
        elif self._state == State.STOPPED:
            raise PlayerCommandError("The player is stopped.")

        await self._send_command("cycle", "pause")
        return None

    def _get_command_id(self) -> int:
        self._command_id += 1
        return self._command_id

    async def _get_mpv_connection(
        self,
    ) -> Tuple[asyncio.StreamReader, asyncio.StreamWriter]:
        logger.info("Connecting to MVP on %s", self._mpv_ipc_socket)
        reader, writer = await asyncio.open_unix_connection(self._mpv_ipc_socket)
        logger.info("Connected to MVP")
        return reader, writer

    @staticmethod
    async def _get_mpv_message(reader: asyncio.StreamReader) -> Optional[Dict]:
        data = await reader.readuntil(b"\n")
        logger.debug("Received data from MVP: %s", data)
        try:
            message = json.loads(data)
        except json.JSONDecodeError as e:
            logger.debug("Cannot decode MVP data: %s", e)
            return None

        logger.debug("Received MVP message %s", message)
        return message

    async def _listen_events(self):
        """Listen for events from MVP.

        Open a connection to MVP, listen for events and update the playlist
        accordingly.
        """
        reader, _ = await self._get_mpv_connection()

        while True:
            message = await self._get_mpv_message(reader)

            try:
                event = MpvEvent(**message)
            except ValidationError as e:
                logger.debug("Received unknown message from MPV: %s", e)
                continue

            if event.name == "end-file":
                logger.info("Track ended")
                Playlist.item_ended()
            elif event.name == "idle":
                logger.info("Player stopped")
                self._state = State.STOPPED
            elif event.name == "pause":
                logger.info("Player paused")
                self._state = State.PAUSED
            elif event.name == "start-file":
                logger.info("Player playing")
                self._state = State.PLAYING
            elif event.name == "unpause":
                logger.info("Player playing")
                self._state = State.PLAYING
            else:
                logger.debug("Unknown MPV event %s", event.name)

    async def _send_command(self, *command: str) -> Optional[MpvResponse]:
        """Send a command to MPV and return the response."""
        command_id = self._get_command_id()
        msg = {"command": command, "request_id": command_id}
        logger.debug("Sending MPV command %s", msg)

        data = json.dumps(msg).encode("utf8") + b"\n"
        self._mpv_writer.write(data)
        await self._mpv_writer.drain()

        return await self._read_response(command_id)

    async def _read_response(self, command_id: int) -> Optional[MpvResponse]:
        while True:
            message = await self._get_mpv_message(self._mpv_reader)
            if not message:
                return None

            if "event" in message:
                logger.debug("Skipping event")
                continue

            try:
                response = MpvResponse(**message)
            except ValidationError:
                logger.warning("Received unknown message from MPV: %s", message)
                continue

            if response.request_id == command_id:
                return response


_current_player = Player()


def get_player():
    return _current_player
