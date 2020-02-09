"""midiroute is a command line tool for routing and monitoring MIDI ports."""

from midiroute import cli


def main() -> int:
    """Main entry point."""
    cli.cli()
    return 0
