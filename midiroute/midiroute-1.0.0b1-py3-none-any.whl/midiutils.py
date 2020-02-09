"""MIDI utilities."""

import asyncio
import contextlib
import time

from typing import Any, List

import mido


class MidiPortError(Exception):
    """Base class for MIDI port errors."""


class InvalidPortName(MidiPortError):
    """Unrecognized port name."""


def list_output_port_names() -> List[str]:
    """Print the available MIDI output ports."""
    return sorted(mido.get_output_names())


def list_input_port_names() -> List[str]:
    """Print the available MIDI input ports."""
    return sorted(mido.get_input_names())


def _check_valid_port_name(port_name: str, current_port_names: List[str]) -> None:
    if port_name not in current_port_names:
        str_current_port_names = "\n".join(current_port_names)
        raise InvalidPortName(
            f"Unknown MIDI port '{port_name}'. "
            f"Run the `list-ports` command to get a list of connected ports.\n"
            f"Ports detected:\n{str_current_port_names}"
        )


@contextlib.asynccontextmanager
async def input_port_stream(port_name: str, event_queues: List[asyncio.Queue]) -> Any:
    """Stream messages from the input port with the given name."""
    loop = asyncio.get_event_loop()
    _check_valid_port_name(port_name, mido.get_input_names())

    def callback(msg: mido.Message) -> None:
        msg.time = time.monotonic()
        for event_queue in event_queues:
            loop.call_soon_threadsafe(event_queue.put_nowait, msg)

    try:
        input_port = mido.open_input(port_name, callback=callback)
        yield input_port
    finally:
        input_port.close()


async def output_port_stream(output_port_name: str, event_queue: asyncio.Queue) -> None:
    """Route messages in the event_queue to the midi output port with the given name."""
    _check_valid_port_name(output_port_name, mido.get_output_names())

    async def _send(port: mido.ports.BasePort, msg: mido.Message) -> None:
        """Coroutine to send a mido.Message over a mido.BasePort async."""
        port.send(msg)

    with mido.open_output(output_port_name) as output_port:
        while True:
            msg = await event_queue.get()
            asyncio.create_task(_send(output_port, msg))


async def print_stream(
    input_port_name: str, output_port_names: str, queue: asyncio.Queue
) -> None:
    """Print messages in the queue."""
    # wrapper to schedule prints on the event loop.
    async def _print() -> None:
        """Async print coroutine."""
        print(f"Input:'{input_port_name}' -> Output:'{output_port_names}': {msg}")

    while True:
        msg = await queue.get()
        asyncio.create_task(_print())


async def stream(
    input_port_name: str, output_port_names: List[str], enable_monitor: bool
) -> None:
    """Stream an asynchronous queue of MIDI messages."""
    msg_queue: asyncio.Queue = asyncio.Queue()
    ui_queue: asyncio.Queue = asyncio.Queue()
    output_sinks: Any = []
    async with input_port_stream(input_port_name, [msg_queue, ui_queue]):
        output_sinks = [
            asyncio.create_task(output_port_stream(output_name, msg_queue))
            for output_name in output_port_names
        ]
        if enable_monitor:
            output_sinks.append(
                asyncio.create_task(
                    print_stream(input_port_name, ",".join(output_port_names), ui_queue)
                )
            )
        await msg_queue.join()
        await ui_queue.join()
        asyncio.gather(*output_sinks, return_exceptions=True)
        while True:
            await asyncio.sleep(1)
