"""
Utility functions to transform YAML output.
"""
import sys
import csv
import itertools
from textwrap import wrap
from pprint import pprint

GENBANK, SRA, GFF = 1, 2, 3

usage = """

    reformat.py GENBANK|SRA|GFF
    
Sanity saving data re-formatter.
    
See https://www.biostarhandbook.com for further details.
    
"""
def extract_translation(argv, stream=sys.stdin):
    """
    Extracts the translation attribute of  a GFF file
    """
    if len(argv) < 4:
        sys.exit("**** extraction needs a type and a gene name")
    # Get the
    ftype = argv[2]
    target = argv[3]

    stream = itertools.takewhile(lambda x: not x.startswith(">"), stream)
    stream = filter(lambda x: not x.startswith('#'), stream)
    stream = csv.reader(stream, delimiter="\t")
    stream = filter(lambda x: x[2] == ftype, stream)

    for row in stream:
        elems = row[8].split(";")
        pairs = [elem.split("=") for elem in elems]
        attr = dict(pairs)
        name = attr.get("gene")
        if name == target:
            protein_id = attr.get("protein_id", "None")
            data_id = attr.get("ID", "None").split(".")[0]
            sequence = attr.get("translation", "")
            product = attr.get("product", "None")
            name = f">{protein_id} ID={data_id} gene={target} product={product}"
            print(name)

            text = "\n".join(wrap(sequence, width=80))
            print(text)


def print_genbank():
    """
    Prints GenBank rows from an NCBI YAML output.
    """
    data = parse_yaml()
    rows = data['genbank-sequences']

    # Fix up country and state
    for row in rows:

        # Simplify the needlessly obtuse and verbose column headers.
        row['country'] = row['locality'].get('country', '')
        row['state'] = row['locality'].get('state', '')
        row['region'] = row['gene-region']
        row['date'] = row['collection-date']

        # Replace the accession with refseq id if exists.
        row['accession'] = row.get('refseq-accession', row['accession'])

        # Remove of unused fields
        for key in ('locality', 'gene-region', 'refseq-accession', 'collection-date'):
            row.pop(key, None)

    # Print the Genbank table
    fieldnames = ['accession', 'region', 'date', 'country', 'state']
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, delimiter="\t")
    # writer.writeheader()
    writer.writerows(rows)


def print_sra():
    """
    Prints SRA rows from an NCBI YAML output.
    """
    # Fix up SRA
    data = parse_yaml()
    rows = data['sra-accessions']

    # Print the SRA run table.
    fieldnames = ['sra-run', 'bioproject', 'sra-experiment', 'sra-study', 'sra-sample', 'biosample']
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, delimiter="\t")
    # writer.writeheader()
    writer.writerows(rows)


def parse_yaml(stream=sys.stdin):
    """
    Parses a YAML stream.
    """
    try:
        # Don't make yaml a universal dependency.
        import yaml
    except ImportError as exc:
        print("*** This program requires pyyaml: pip install pyyaml", file=sys.stderr)
        sys.exit(1)

    # Parse the document
    data = yaml.load(stream, Loader=yaml.BaseLoader)

    # Uncomment to understand the structure of the data
    # pprint(data)

    if not data:
        sys.exit("*** error: empty stream")

    return data


def main():
    """
    Entry point for the script.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Reformats bioinformatics data.", usage=usage)

    parser.add_argument("mode", type=str )

    args = parser.parse_args(sys.argv[1:])

    # Valid modes
    modes = dict(
        GENBANK=GENBANK,
        SRA=SRA,
        GFF=GFF,
    )

    # Select the mode
    mode = modes.get(args.mode.upper(), GENBANK)

    if mode == GENBANK:
        print_genbank()
    elif mode == SRA:
        print_sra()
    elif mode == GFF:
        extract_translation(sys.argv)


if __name__ == '__main__':
    main()


