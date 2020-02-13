#!/usr/bin/env python3

import argparse
from xor_tools import plaintext_bytes
from xor_tools.rolling_key import RollingKey


def main():
    parser = argparse.ArgumentParser(description='Encrypts a file using a defined XOR key')
    parser.add_argument("-f", "--file", help="Input file", type=argparse.FileType('rb'), required=True)
    parser.add_argument("-o", "--output", help="Output file", type=argparse.FileType('wb'), required=True)
    parser.add_argument("-k", "--key", help="XOR key", type=plaintext_bytes, required=True)

    args = parser.parse_args()

    rk = RollingKey(args.key)
    for c, k in zip(args.file.read(), rk):
        args.output.write(bytes([c ^ k]))
    args.output.close()
