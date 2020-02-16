from colorama import init, Fore, Style

from trezorlib.client import TrezorClient
from trezorlib.ui import ClickUI

from trezor_file_encryption.trezor import wait_for_devices, choose_device, trezor_decrypt_dir, trezor_encrypt_dir

init()
orange = (255, 165, 0)


def print_header(text):
    lines = text.split('\n')
    longest = 0
    for line in lines:
        if len(line) > longest:
            longest = len(line)
    top = '╔' + '═' * (longest + 2) + '╗\n'
    bottom = '╚' + '═' * (longest + 2) + '╝'
    middle = ''.join(['║ ' + line + ' ' * (longest - len(line)) + ' ║\n' for line in lines])

    return top + middle + bottom


class EncryptionSession:
    def __init__(self, base_directory):
        self.base_directory = base_directory
        self.client = None

    def set_client(self):
        if self.client is not None:
            return

        devices = wait_for_devices()
        transport = choose_device(devices)
        self.client = TrezorClient(transport, ui=ClickUI())

    def run_menu(self):
        print(Fore.YELLOW + print_header(f'Directory Encryption Tool\n{self.base_directory}'))
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 'Select:\n0. Quit\n1. Encrypt\n2. Decrypt\n> ' + Style.RESET_ALL,
              end='')
        num = -1
        while not (0 <= num <= 2):
            try:
                num = int(input())
            except ValueError:
                num = -1

            if not (0 <= num <= 2):
                print(Fore.RED + 'Invalid selection' + Style.RESET_ALL)
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + '> ' + Style.RESET_ALL, end='')

        if num == 0:
            print('Bye')
            return

        self.set_client()

        if num == 1:
            trezor_encrypt_dir(self.client, self.base_directory)
        elif num == 2:
            trezor_decrypt_dir(self.client, self.base_directory)
