#!/usr/bin/env python3

"""
Some examples:

xor_key_recovery -f samples/binary_elf_encrypted -p __libc_start_main -n 4
xor_key_recovery -f samples/binary_pe32_encrypted -p "This program cannot be run in DOS" -n 4
"""

import argparse
import sys
from xor_tools import plaintext_bytes
from xor_tools.rolling_key import RollingKey


def calc_template(text, keylength):
    return bytes([text[i] ^ text[i + keylength] for i in range(0, len(text) - keylength)])


def main():
    parser = argparse.ArgumentParser(description='Attempts to find XOR key using a known plaintext')
    parser.add_argument("-f", "--file", help="Input file (encrypted)", type=argparse.FileType('rb'), required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-p", "--plaintext", help="Known plaintext", type=plaintext_bytes)
    group.add_argument("-pf", "--plaintext-file", help="Known plaintext", type=argparse.FileType('rb'))
    parser.add_argument("-n", "--keylength", help="Key length", type=int, required=True)
    parser.add_argument("-o", "--output", help="Output file", type=argparse.FileType('wb'))

    args = parser.parse_args()

    ciphertext = args.file.read()
    plaintext = args.plaintext if args.plaintext else args.plaintext_file.read()
    keylength = args.keylength

    if keylength < 1:
        print('[!] Key lenght must be larger than one.')
        sys.exit(1)

    if len(plaintext) < 2 * keylength:
        print('[!] Plaintext must be at least 2 times longer than expected keylength')
        sys.exit(2)

    plaintext_template = calc_template(plaintext, keylength)
    ciphertext_template = calc_template(ciphertext, keylength)

    try:
        index = ciphertext_template.index(plaintext_template)
    except ValueError:
        print('[-] Plaintext not found in ciphertext with provided keylength')
        sys.exit(3)

    print('[+] Found plaintext at position: {}'.format(index))

    rolling_key = RollingKey(bytes([ciphertext[index + i] ^ plaintext[i] for i in range(0, keylength)]))
    rolling_key = RollingKey(bytes([rolling_key[k] for k in range(-index, -index + keylength)]))
    print('[*] Key found: 0x{}'.format(rolling_key.key.hex()))

    if args.output:
        print('[+] Saving decrypted file to: {}'.format(args.output.name))
        args.output.write(bytes([c ^ k for c, k in zip(ciphertext, rolling_key)]))
        args.output.close()
