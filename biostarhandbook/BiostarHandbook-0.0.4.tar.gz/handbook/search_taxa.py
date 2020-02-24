"""
Filters taxonomical information
"""
import csv
import re
import sys

usage = """

"""


def run_filter(blastinfo, lineage, text):

    # Take the regex from command line.
    patt = re.compile(text, re.IGNORECASE)

    # Open stream to lineage.
    stream1 = csv.reader(lineage, delimiter="\t")

    # Filter for more than a single column.
    stream1 = filter(lambda x: len(x) > 1, stream1)

    # Filter for second element matching the pattern.
    stream1 = filter(lambda x: patt.search(x[1]), stream1)

    # The taxids that match the words
    ids1 = map(lambda x: x[0], stream1)

    # Speeds up lookup.
    taxa = set(ids1)

    print (taxa)

    # Open stream to lineage.
    stream2 = csv.reader(blastinfo, delimiter=" ")

    # Filter for more than a single column.
    stream2 = filter(lambda x: len(x) > 2, stream2)

    # Filter for second element matching the pattern.
    stream2 = filter(lambda x: x[1] in taxa, stream2)

    for row in stream2:
        print (" ".join(row))


def main():
    """
    Entry point for the script.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Filters taxonomical information.", usage=usage)

    parser.add_argument("blastinfo", type=argparse.FileType('r'))

    parser.add_argument("lineage", type=argparse.FileType('r'))

    parser.add_argument("pattern", type=str)

    args = parser.parse_args(sys.argv[1:])

    run_filter(blastinfo=args.blastinfo, lineage=args.lineage, text=args.pattern)


if __name__ == '__main__':
    main()
