import base64
import os
import sys
import json
import hashlib

import click
import trezorlib
import colorama

from trezorlib.client import TrezorClient
from trezorlib.tools import parse_path
from trezorlib.transport import enumerate_devices
from trezorlib.ui import ClickUI

import trezorlib.misc

from trezor_file_encryption.files import get_all_files, create_storage_dir, encrypt_file, decrypt_file, get_storage_dir

BIP32_PATH_TEXT = "8294'/0"
bip32_path = parse_path(BIP32_PATH_TEXT)


def wait_for_devices():
    dev = enumerate_devices()
    while not len(dev):
        sys.stderr.write("Please connect Trezor to computer and press Enter...")
        input()
        dev = enumerate_devices()

    return dev


def choose_device(all_devices):
    if not len(all_devices):
        raise RuntimeError("No Trezor connected!")

    if len(all_devices) == 1:
        try:
            return all_devices[0]
        except IOError:
            raise RuntimeError("Device is currently in use")

    i = 0
    click.echo("----------------------------")
    click.echo("Available devices:")

    all_ids = []
    remove = []

    for n, d in enumerate(all_devices):
        try:
            client = TrezorClient(d, ui=ClickUI())
        except IOError:
            click.echo("[-] <device is currently in use>")
            continue

        if client.features.device_id not in all_ids:
            all_ids.append(client.features.device_id)  # Prevent duplicates from showing up

            label = client.features.label or '<no label>'
            click.echo("[%d] %s (%s)" % (i, label, client.features.device_id))
            i += 1
        else:
            remove.append(n)
        client.close()

    sorted(remove)
    count = 0
    for val in remove:
        all_devices.pop(val - count)
        count += 1

    click.echo("----------------------------")

    try:
        device_id = int(click.prompt("Please choose device to use"))
        return all_devices[device_id]
    except Exception:
        raise ValueError("Invalid choice, exiting...")


def generate_new_password(client: TrezorClient) -> bytes:
    trezor_entropy = trezorlib.misc.get_entropy(client, 32)
    urandom_entropy = os.urandom(32)
    return hashlib.sha256(trezor_entropy + urandom_entropy).digest()


def encrypt_password(client: TrezorClient, password: bytes, label: str, path):
    path = parse_path(path)
    pwd_encrypted = trezorlib.misc.encrypt_keyvalue(
        client, path, label, password, False, True
    )
    return pwd_encrypted


def decrypt_password(client: TrezorClient, password_encrypted: bytes, label: str, path):
    path = parse_path(path)
    click.echo(f'Decrypting key "{colorama.Fore.GREEN}{label}{colorama.Fore.RESET}"')
    pwd = trezorlib.misc.decrypt_keyvalue(
        client, path, label, password_encrypted, False, True
    )
    return pwd


def create_random_label() -> str:
    return base64.b64encode(hashlib.sha256(os.urandom(32)).digest()).decode()


def dir_is_encrypted(path: str) -> bool:
    directory = get_storage_dir(path)

    dat_path = os.path.join(directory, 'dat.json')
    if not os.path.exists(dat_path):
        return False

    storage_data = json.load(open(dat_path, 'r'))
    try:
        return storage_data['encrypted']
    except KeyError:
        return False


def trezor_encrypt_dir(client: TrezorClient, path: str):
    print(f'{colorama.Style.BRIGHT + colorama.Fore.YELLOW}\nEncrypting contents of {path}\n{colorama.Style.RESET_ALL}')

    storage = create_storage_dir(path)
    dat_path = os.path.join(storage, 'dat.json')
    if os.path.exists(dat_path):
        storage_data = json.load(open(dat_path, 'r'))

        if storage_data['encrypted']:
            proceed = input(colorama.Style.BRIGHT + colorama.Fore.RED +
                            'Warning: files are already encrypted. This will erase your previous encryption key. '
                            'Continue? (y/n) ' + colorama.Style.RESET_ALL)
            if len(proceed) == 0 or proceed.lower()[0] != 'y':
                return
        label = storage_data['label']
        # pwd = decrypt_password(client, bytes.fromhex(storage_data['pwd_encrypted']), storage_data['label'])
    else:
        print('Initializing new storage record')
        label = create_random_label()

    b_path = BIP32_PATH_TEXT
    print('Generating new key with Trezor entropy')
    pwd = generate_new_password(client)
    enc_pwd = encrypt_password(client, pwd, label, b_path)

    storage_data = {
        'bip32_path': b_path,
        'pwd_encrypted': enc_pwd.hex(),
        'label': label,
        'encrypted': False
    }
    json.dump(storage_data, open(dat_path, 'w'))

    all_files = get_all_files(path)
    print(colorama.Style.RESET_ALL)
    proceed = input(f'{colorama.Fore.RED}About to encrypt {len(all_files)} files. Continue? (y/n) ')
    if len(proceed) == 0 or proceed.lower()[0] != 'y':
        return

    for file in all_files:
        print(f'{colorama.Style.BRIGHT} [ ] {file}', end='\r')
        res, msg = encrypt_file(pwd, file)
        if res:
            print(f'{colorama.Fore.GREEN} [✓]{colorama.Fore.RESET} {file}')
        else:
            print(f'{colorama.Fore.RED} [✗]{colorama.Fore.RESET} {file} - {colorama.Fore.RED}{msg}')

    storage_data['encrypted'] = True
    json.dump(storage_data, open(dat_path, 'w'))
    print(colorama.Style.RESET_ALL)


def trezor_decrypt_dir(client: TrezorClient, path: str):
    print(f'{colorama.Style.BRIGHT + colorama.Fore.YELLOW}\nDecrypting contents of {path}\n{colorama.Style.RESET_ALL}')

    storage = create_storage_dir(path)
    dat_path = os.path.join(storage, 'dat.json')
    if not os.path.exists(dat_path):
        print('Storage record has not yet been initialized')
        return

    storage_data = json.load(open(dat_path, 'r'))
    if not storage_data['encrypted']:
        proceed = input(colorama.Style.BRIGHT + colorama.Fore.RED +
                        'Warning: files are not encrypted. '
                        'Continue? (y/n) ' + colorama.Style.RESET_ALL)
        if len(proceed) == 0 or proceed.lower()[0] != 'y':
            return

    pwd = decrypt_password(client, bytes.fromhex(storage_data['pwd_encrypted']), storage_data['label'],
                           storage_data['bip32_path'])

    all_files = get_all_files(path)
    print(colorama.Style.RESET_ALL)
    proceed = input(f'{colorama.Fore.RED}About to decrypt {len(all_files)} files. Continue? (y/n) ')
    if len(proceed) == 0 or proceed.lower()[0] != 'y':
        return

    for file in all_files:
        print(f'{colorama.Style.BRIGHT}{colorama.Fore.RESET} [ ] {file}', end='\r')
        res, msg = decrypt_file(pwd, file)
        if res:
            print(f'{colorama.Fore.GREEN} [✓]{colorama.Fore.RESET} {file}')
        else:
            print(f'{colorama.Fore.RED} [✗]{colorama.Fore.RESET} {file} - {colorama.Fore.RED}{msg}')

    storage_data['encrypted'] = False
    json.dump(storage_data, open(dat_path, 'w'))
    print(colorama.Style.RESET_ALL)
