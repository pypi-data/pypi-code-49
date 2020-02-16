import os
import sys

from trezorlib.client import TrezorClient
from trezorlib.ui import ClickUI

import colorama

from trezor_file_encryption import EncryptionSession, trezor_encrypt_dir, wait_for_devices, choose_device, \
    trezor_decrypt_dir

help_text = """
Usage: trezorenc COMMAND [OPTIONS]

Options:
  -d DIRECTORY  Specify directory to perform encryption/decryption. Defaults to present directory.

Commands:
  help          Display help message.
  interactive   Run program in interactive mode.
  encrypt       Encrypt directory.
  decrypt       Decrypt directory.
""".strip()


def run():
    args = sys.argv[1:]

    if len(args) == 0 or any(arg in ('help', '--help', '-h') for arg in args):
        print(help_text)
        return 0

    # Poor-man's command line argument parsing
    if len(args) > 1:
        if args[1] == '-d':
            if len(args) > 2:
                directory = args[2]
            else:
                print('Missing directory')
                return 2
        else:
            print(f'Unknown option "{args[1]}"')
            return 1
    else:
        directory = os.getcwd()

    has_access = os.access(directory, os.W_OK | os.X_OK)
    if not has_access:
        print(f'{colorama.Fore.RED}Error: you do not have sufficient permissions for {directory}')
        return

    if args[0] == 'interactive':
        session = EncryptionSession(directory)
        session.run_menu()
        return 0
    elif args[0] == 'encrypt':
        devices = wait_for_devices()
        transport = choose_device(devices)
        c = TrezorClient(transport, ui=ClickUI())
        trezor_encrypt_dir(c, directory)
        return 0
    elif args[0] == 'decrypt':
        print('decrypting')
        devices = wait_for_devices()
        transport = choose_device(devices)
        c = TrezorClient(transport, ui=ClickUI())
        trezor_decrypt_dir(c, directory)
        return 0
    else:
        print(help_text)
        return 0


def main():
    try:
        return run()
    except KeyboardInterrupt:
        print()
        return 1


if __name__ == '__main__':
    main()
