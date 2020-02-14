import sys
import argparse

from rivm.conversion.input import InputCSV
from rivm.conversion.builder import (
    ResultatenCompact,
    ResultatenUitgebreid,
)


def parse_args(args):
    """
    Parse command arguments required for this script.
    """
    parser = argparse.ArgumentParser(description='Convert Aerius `Resultaten` to Shape') # noqa
    group = parser.add_mutually_exclusive_group(required=True)
    # Input
    group.add_argument("--resultaten-compact", help='Aerius resultaten-compact.csv') # noqa
    group.add_argument('--resultaten-uitgebreid', help='Aerius resultaten-uitgebreid.csv') # noqa
    # Output
    parser.add_argument('--destination', required=True, help="Destination for converted CSV") # noqa
    return parser.parse_args()


def main(argv=sys.argv):
    args = parse_args(argv)

    if args.resultaten_compact:
        input_csv = InputCSV(
            args.resultaten_compact,
            primary_key='calculation_point_id'
        )
        # Resultaten Compact
        result = ResultatenCompact(input_csv).build()
        result.to_file(args.destination, driver='ESRI Shapefile')

    if args.resultaten_uitgebreid:
        input_csv = InputCSV(
            args.resultaten_uitgebreid,
            primary_key='calculation_point_id'
        )
        # Resultaten Uitgebreid
        result = ResultatenUitgebreid(input_csv).build()
        result.to_file(args.destination, driver='ESRI Shapefile')
