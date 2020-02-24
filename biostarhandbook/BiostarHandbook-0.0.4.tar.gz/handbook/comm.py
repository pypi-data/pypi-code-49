"""
A better version of the 'comm' command line tool.

Usage:

    comm.py A B

Selects columns from two files A and B and prints a three column output where:

1. the first column lists elements unique to A,
2. the second column lists elements unique to B,
3. the third column lists elements in both files.

Comments and empty lines are ignored.

Additional parameters may be used to

1. Select different columns from files.
2. Change the column delimiter.
3. Print only column 1, 2 or 3 of the output.

"""
import sys
import csv
import argparse
import itertools

FILL_VALUE = ''


def process(file1, file2, delimiter, colidx, args=None):
    """
    Processes the files and prints the output
    """

    def parse(stream):
        """
        A generator in a clojure to processes each stream.
        Returns the value of a column at the column index.
        """
        # Skip comment lines
        stream = filter(lambda x: not x.startswith('#'), stream)

        # Ignore empty lines.
        stream = filter(lambda x: x.strip(), stream)

        # Format the stream.
        stream = csv.reader(stream, delimiter=delimiter)

        # Generate empty values on missing columns.
        for row in stream:
            try:
                yield (row[colidx], None)
            except IndexError as exc:
                yield ('', None)

    # Make dictionaries to maintain original item order.
    store1 = dict(parse(file1))
    store2 = dict(parse(file2))

    # Generate the various groupings.
    union = [key for key in store1.keys() if key in store2]
    only1 = [key for key in store1.keys() if key not in store2]
    only2 = [key for key in store2.keys() if key not in store1]

    # Select output based on flags.
    if args.flag1:
        output = only1
    elif args.flag2:
        output = only2
    elif args.common:
        output = union
    else:
        output = itertools.zip_longest(only1, only2, union, fillvalue=FILL_VALUE)
        output = map(lambda x: "\t".join(x), output)

    # Print the output
    for line in output:
        print(line)


def main():
    """
    Entry point for the script.
    """
    parser = argparse.ArgumentParser(description='Finds common data in CSV/TAB delimited files')

    parser.add_argument('-c', action="store", dest="column", metavar="N", type=int,
                        help="column to process (%(default)s)", default=1)

    parser.add_argument('-t', action="store_true", dest="usetab", default=False,
                        help="tab delimited columns (default is comma)")

    parser.add_argument('-1', action="store_true", dest="flag1", default=False,
                        help="elements unique to file A (A-B)")
    parser.add_argument('-2', action="store_true", dest="flag2", default=False,
                        help="elements unique to file B (B-A)")
    parser.add_argument('-3', action="store_true", dest="common", default=False,
                        help="common elements in file (A and B)")

    parser.add_argument("file1", type=argparse.FileType('r'))
    parser.add_argument("file2", type=argparse.FileType('r'))

    if len(sys.argv) == 1:
        sys.argv.append("-h")

    args = parser.parse_args(sys.argv[1:])

    delimiter = "\t" if args.usetab else ","

    colidx = args.column - 1

    process(file1=args.file1, file2=args.file2, delimiter=delimiter, colidx=colidx, args=args)


if __name__ == '__main__':
    main()
