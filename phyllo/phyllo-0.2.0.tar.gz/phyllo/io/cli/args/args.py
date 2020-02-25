"""Print all data received on the serial port."""

# Builtins

import argparse

# Packages


# Parsing

def parse_args(*arg_adders, grouped_args, **parser_kwargs):
    """Parse the command-line args in groups."""
    parser = argparse.ArgumentParser(**parser_kwargs)
    for arg_adder in arg_adders:
        arg_adder(parser)
    for (group_adder, arg_adders) in grouped_args.items():
        group = group_adder(parser)
        for arg_adder in arg_adders:
            arg_adder(group)
    return parser.parse_args()
