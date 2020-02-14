import sys
import argparse

from rivm.helpers import add_file_affix
from rivm.conversion.input import InputCSV
from rivm.conversion.builder import (
    AeriusRekenpunten,
    AeriusOverdrachtslijnen,
    AeriusWegvakkenSRM1,
    AeriusWegvakkenSRM2,
    AeriusMaatregelen,
    AeriusCorrecties,
)


def parse_args(args):
    """
    Parse command arguments required for this script.
    """
    parser = argparse.ArgumentParser(description='Bi-directional data conversion between NSL-Monitoring and Aerius') # noqa
    group = parser.add_mutually_exclusive_group(required=True)
    # Input
    group.add_argument("--rekenpunten", help='NSL-Monitoring rekenpunten.csv')
    group.add_argument('--wegvakken', help='NSL-Monitoring wegvakken.csv')
    group.add_argument('--maatregelen', help='NSL-Monitoring maatregelen.csv')
    group.add_argument('--correcties', help='NSL-Monitoring correcties.csv')
    # Output
    parser.add_argument('--destination', required=True, help="Destination for converted CSV") # noqa
    return parser.parse_args()


def main(argv=sys.argv):
    args = parse_args(argv)

    if args.rekenpunten:
        input_csv = InputCSV(args.rekenpunten, primary_key='receptorid')
        # Rekenpunten
        result = AeriusRekenpunten(input_csv).build()
        destination_1 = add_file_affix(args.destination, '_1')
        result.to_csv(destination_1, sep=';', index=False)
        # Overdrachtslijnen
        result = AeriusOverdrachtslijnen(input_csv).build()
        destination_2 = add_file_affix(args.destination, '_2')
        result.to_csv(destination_2, sep=';', index=False)

    elif args.wegvakken:
        input_csv = InputCSV(args.wegvakken, primary_key='receptorid')
        # Wegvakken SRM1
        result = AeriusWegvakkenSRM1(input_csv).build()
        destination_1 = add_file_affix(args.destination, '_1')
        result.to_csv(destination_1, sep=';', index=False)
        # Wegvakken SRM2
        result = AeriusWegvakkenSRM2(input_csv).build()
        destination_2 = add_file_affix(args.destination, '_2')
        result.to_csv(destination_2, sep=';', index=False)

    elif args.maatregelen:
        input_csv = InputCSV(args.maatregelen, primary_key='maatr_id')
        # Maatregelen
        result = AeriusMaatregelen(input_csv).build()
        result.to_csv(args.destination, sep=';', index=False)

    elif args.correcties:
        input_csv = InputCSV(args.correcties, primary_key='correctie_id')
        # Correcties
        result = AeriusCorrecties(input_csv).build()
        result.to_csv(args.destination, sep=';', index=False)
