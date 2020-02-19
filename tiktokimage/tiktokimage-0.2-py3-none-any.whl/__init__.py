# -*- coding: utf-8 -*-

import argparse
from tiktokimage.convert import process


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", help='path of image to add effect', dest='input_path')
    parser.add_argument('--output_path', help='path of output image', dest='output_path')
    args = parser.parse_args()

    if args.input_path is None:
        parser.error('Please specify or --input_path')

    out = args.output_path if args.output_path is not None else 'out.jpeg'
    process(args.input_path, out)
