import argparse
import json

from .track import Track


def _get_args():
    parser = argparse.ArgumentParser(description='Take an input file and convert it to MIDI')
    parser.add_argument('infile')
    parser.add_argument(
        '-o',
        '--outfile',
        help='Name of the output file to create',
        default='out.mid',
    )
    parser.add_argument(
        '-m',
        '--mapping',
        help='Name of the mapping file produced by tasmidi-map',
        required=True,
    )
    parser.add_argument(
        '-p',
        '--program',
        type=int,
        default=4,
        help='MIDI program in your soundfont to use. Has no effect if the output is running running in a DAW.'
    )
    return parser.parse_args()


def main():
    args = _get_args()
    config = {}

    with open(args.mapping) as f:
        config.update(json.load(f))

    track = Track(args.outfile, config, args.program)

    with open(args.infile) as infile:
        for line in infile:
            track.handle(line)

    track.save()
