"""Command line interface module."""

import asyncio

from typing import Any

import click
import tabulate

from midiroute import midiutils


@click.group()
def cli() -> None:
    """MIDI routing and monitoring tool."""
    pass


@cli.command()
@click.option("--input-port", "-i", help="Select the input port.", metavar="PORT_NAME")
@click.option(
    "--output-ports",
    "-o",
    help="Select one or more output ports in a comma separated list.",
    metavar="PORT_NAME",
)
@click.option(
    "--monitor",
    "-m",
    is_flag=True,
    help="Enable monitoring of MIDI activity on the selected ports.",
)
def run(input_port: str, output_ports: Any, monitor: bool) -> None:
    """Run the MIDI router."""
    output_ports = output_ports.split(",")
    asyncio.run(midiutils.stream(input_port, output_ports, monitor))


@cli.command()
def list_ports() -> None:
    """List available input and output ports."""
    inports = midiutils.list_input_port_names()
    outports = midiutils.list_output_port_names()
    print(tabulate.tabulate(list(zip(inports, outports)), headers=["Input", "Output"]))
