#!/usr/bin/python3

from frc1678.limeplotter.loader.networktables import NetworkTablesLoader

import argparse
import sys
import csv
import time

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-N", "--network-server", type=str,
                        help="NetworkTables server address to get data from")

    parser.add_argument("-t", "--sleep-time", default=.01, type=float,
                        help="Time to sleep between polls")


    parser.add_argument("output_file", type=argparse.FileType('w'),
                        nargs='?', default=sys.stdout,
                        help="")

    args = parser.parse_args()
    return args

def main():
    args = parse_args()

    source = NetworkTablesLoader(args.network_server)
    source.open()
    source.setup_table_storage()
    
    table_data = source.variables_available
    default_x = source.get_default_time_column()

    ycolumns = []
    yidents = []

    for table in table_data:
        for column in table_data[table]:
            ycolumns.append(column)
            yidents.append(source.find_column_identifier(column))
            source.setup_table_entry(default_x, yidents[-1])

    csvf = csv.writer(args.output_file)

    while True:
        source.gather_next_datasets()
        df = source.gather(None, yidents, True)

        row = []
        for c in df[:][-1:]:
            row.append(c)
        print(row)
        
        time.sleep(args.sleep_time)
        import pdb ; pdb.set_trace()


if __name__ == "__main__":
    main()
