"""
Iterates over a BAM file and prints reads that match a genotype at a location.

Works for matches and mistmatching bases only.
"""
import csv
import os
import sys

try:
    import pysam
except ImportError as exc:
    print("*** This program requires pysam: pip install pysam", file=sys.stderr)
    sys.exit(1)

def group_matches(fname, chrom, pos, metadata="metadata.txt"):
    if os.path.isfile(metadata):
        lines = csv.reader(open(metadata, 'rt'), delimiter="\t")
        pairs = [(p[0], p[2:]) for p in lines]
        store = dict(pairs)
    else:
        store = dict()

    # The position is zero based.
    pos = pos - 1
    bam = pysam.AlignmentFile(fname, 'rb')

    group = dict()
    for column in bam.pileup(chrom):
        if column.pos == pos:
            for read in column.pileups:
                name = read.alignment.query_name
                base = read.alignment.query_sequence[read.query_position]
                group.setdefault(base, []).append(name)

    for base, values in group.items():
        for name in values:
            name = name.split(".")[0]
            fields = store.get(name, [])
            meta = "\t".join(fields)
            data = [name, base, meta]
            print("\t".join(data))


def main():
    """
    Entry point for the script.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Reformats various data")

    parser.add_argument("bam", type=str, )
    parser.add_argument("chrom", type=str, )
    parser.add_argument("pos", type=int, )

    args = parser.parse_args(sys.argv[1:])

    group_matches(fname=args.bam, chrom=args.chrom, pos=args.pos)


if __name__ == '__main__':
    main()
