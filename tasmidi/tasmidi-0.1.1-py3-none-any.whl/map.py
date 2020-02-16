import argparse
import json

from .notes import generate_scale

def _get_args():
    parser = argparse.ArgumentParser(
        description='Take a LibTAS input file and generate a mapping for it',
    )
    parser.add_argument('input_file', help='LibTAS input file (usually named inputs)')
    parser.add_argument(
        '-m',
        '--minor',
        help='Change to a minor scale',
        action='store_true',
    )
    parser.add_argument(
        '-t',
        '--transpose',
        help='Transpose key a number of half steps',
        type=int,
        default=0,
    )
    parser.add_argument(
        '-i',
        '--interpolate',
        help='Interpolate the scale degrees for harmony',
        action='store_true',
    )
    parser.add_argument(
        '-f',
        '--fps',
        help='FPS of the TAS',
        type=int,
        default=60
    )
    return parser.parse_args()


def interpolate_scale(input_scale):
    scale = input_scale.copy()

    for idx in range(len(scale)):
        if idx % 2 == 0 and idx > 1:
            scale[idx], scale[idx - 1] = scale[idx - 1], scale[idx]

    return scale


def main():
    args = _get_args()

    inputs = set()
    counts = {}

    with open(args.input_file) as f:
        for line in f:
            inputs_on_frame = [i for i in line.split('|')[1].split(':') if i != '']

            for input_str in inputs_on_frame:
                inputs.add(input_str)
                counts[input_str] = counts.get(input_str, 0) + 1

    inputs = sorted(inputs, key=lambda x: counts[x], reverse=True)
    scale = generate_scale(transpose=args.transpose, minor=args.minor)[:len(inputs)]

    if args.interpolate:
        scale = interpolate_scale(scale)

    print(json.dumps({
        'validInputs': inputs,
        'midiNotes': scale,
        'fps': args.fps,
    }))
