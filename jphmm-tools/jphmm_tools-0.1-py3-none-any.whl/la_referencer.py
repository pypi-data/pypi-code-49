import re
from collections import defaultdict

from Bio import SeqIO
from Bio.Alphabet import generic_dna

from jphmm_tools import VERSION


def get_subtype(name):
    """
    Extracts the subtype information from the sequence name,
    in subtype.whatever format (x.whatever for unknown subtypes.

    :param name: sequence name
    :type name: str
    :return: list of subtypes
    :rtype: list(str)
    """
    st = re.findall(r'^[^.]+[\._]', name)[0]
    st = st[:-1]
    if st == 'x':
        return []
    return ['CRF_{}'.format(_) if _[0].isdigit() else _ for _ in re.findall(r'[\d]{2}|A\d|F\d|[ABCDEFGHJKUO]', st)]


def reformat_reference(la_alignment, jphmm_ref_alignment):
    """
    Reformats a Los Alamos (https://www.hiv.lanl.gov/content/sequence/HIV/mainpage.html) alignment file
    with sequences name as subtype.whatever (x.whatever for unknown subtypes)
    into a reference file suitable for jpHMM (http://jphmm.gobics.de).

    :param la_alignment: path to the Los Alamos alignment file in fasta format.
    :type la_alignment: str
    :param jphmm_ref_alignment: path where the reference file suitable for jpHMM will be saved.
    :type jphmm_ref_alignment: str
    """
    subtype2rec = defaultdict(list)
    for rec in SeqIO.parse(la_alignment, 'fasta', alphabet=generic_dna):
        sts = get_subtype(rec.id)
        if len(sts) == 1:
            print(sts)
            subtype2rec[sts[0]].append(rec)
    with open(jphmm_ref_alignment, 'w') as f:
        for subtype in sorted(subtype2rec.keys()):
            f.write('>>{}\n'.format(subtype))
            for rec in subtype2rec[subtype]:
                f.write('>{}\n{}\n'.format(rec.id, rec.seq))


def main():
    """
    Entry point, calling :py:func:`jphmm_tools.la_referencer.reformat_reference` with command-line arguments.

    :return: void
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="Reformats a Los Alamos (https://www.hiv.lanl.gov/content/sequence/HIV/mainpage.html) alignment file"
                    "into a reference file suitable for jpHMM (http://jphmm.gobics.de).",
        prog='jphmm_ref')

    parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=VERSION))

    parser.add_argument('--la_alignment', required=True, type=str,
                        help='Path to the Los Alamos alignment file in fasta format, '
                             'with sequences name as subtype.whatever (x.whatever for unknown subtypes).')
    parser.add_argument('--jphmm_ref_alignment', required=True, type=str,
                        help='Path where the reference file suitable for jpHMM will be saved.')

    params = parser.parse_args()

    reformat_reference(**vars(params))


if '__main__' == __name__:
    main()
