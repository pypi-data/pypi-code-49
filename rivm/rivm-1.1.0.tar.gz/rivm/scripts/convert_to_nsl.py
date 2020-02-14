import sys
import argparse

from rivm.conversion.input import InputCSV, InputBundle
from rivm.conversion.builder import (
    NSLMonitoringRekenpunten,
    NSLMonitoringWegvakken,
)


def parse_args(args):
    """
    Parse command arguments required for this script.
    """
    parser = argparse.ArgumentParser(description='Bi-directional data conversion between NSL-Monitoring and Aerius') # noqa
    # Input
    group = parser.add_argument_group('Rekenpunten')
    group.add_argument("--rekenpunten", help="Aerius rekenpunten.csv")
    group.add_argument("--overdrachtslijnen", help="Aerius overdrachtslijnen.csv") # noqa

    group = parser.add_argument_group('Wegvakken')
    group.add_argument("--wegvakken_srm1", help="Aerius wegvakken_srm1.csv")
    group.add_argument("--wegvakken_srm2", help="Aerius wegvakken_srm2.csv")
    # Output
    parser.add_argument('--destination', required=True, help="Destination for converted CSV") # noqa
    return parser.parse_args()


def main(argv=sys.argv):
    args = parse_args(argv)

    if args.rekenpunten and args.overdrachtslijnen:
        input_bundle = InputBundle(
            InputCSV(args.rekenpunten, primary_key='calculation_point_id'),
            InputCSV(args.overdrachtslijnen, primary_key='calculation_point_id'), # noqa
        )
        # Rekenpunten
        result = NSLMonitoringRekenpunten(input_bundle).build()
        result.to_csv(args.destination, sep=';', index=False)

    if args.wegvakken_srm1 and args.wegvakken_srm2:
        input_bundle = InputBundle(
            InputCSV(args.wegvakken_srm1, primary_key='srm1_road_id'),
            InputCSV(args.wegvakken_srm2, primary_key='srm2_road_id'),
        )
        # Wegvakken
        result = NSLMonitoringWegvakken(input_bundle).build()
        result.to_csv(args.destination, sep=';', index=False)
