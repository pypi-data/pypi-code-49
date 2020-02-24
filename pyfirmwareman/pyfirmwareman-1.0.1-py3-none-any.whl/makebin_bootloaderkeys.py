# Converts A092.json.enc file to the A092.smt.bin file
# Decrypts enc file with fcrypt and create bin file and encrypt it with smtester device keys(xxtea)

# >>>> DEV MODE #################
import sys
# Development Mode
# if pyfcrypt is a global package, then you can remove the following try - except
try:
    import pyfcrypt
except:
    # discover path of the module and add it to the sys.path.

    dev_path = 'X:\\AYEDEK\\Software Projects\\pyfcrypt'
    print("DEV MODE ADDING PATH",dev_path)
    sys.path.append(dev_path)

# <<<< DEV MODE #################

import os
import json
import pathlib

import click
import ctypes
from Cryptodome.Protocol.KDF import PBKDF2


from main import lib
import pyfirmwaremandef
from pyfcrypt import fcrypt
from pyfcrypt.fcrypt import decrypt_file

from pyfirmwaremandef import SMTESTER_BOOTLOADER_KEYS

# python makebin_bootloaderkeys.py x:\hex_repo\A092\config\A092.json.enc


def quit():
    os._exit(0)

@click.command()
@click.argument('masterkeys_json_enc_file_path')
def make_bin_appmasterkeys(masterkeys_json_enc_file_path):

    f_dir = pathlib.Path(masterkeys_json_enc_file_path).parent
    f_extensions = pathlib.Path(masterkeys_json_enc_file_path).suffixes
    f_ext = "".join(f_extensions)
    if (f_ext != ".json.enc"):
        click.echo(click.style(f"Expected .json.enc file", fg='red'))
        #print_formatted_text(HTML("<ansired>Expected .hex.smt file</ansired>"))
        return False

    # Remove all extensions
    f_name_wo_extension = masterkeys_json_enc_file_path
    for i in range(len(f_extensions)):
        f_name_wo_extension = pathlib.Path(f_name_wo_extension).stem

    # Add extensions
    # f_ext = "".join(f_extensions)
    # pure_f_name = f_name_wo_extension + f_ext

    smt_bin_file_path = str(f_dir) + "\\" + f_name_wo_extension + ".smt.bin"


    #Check if ile exist
    if not os.path.exists(masterkeys_json_enc_file_path):
        # click.echo(click.style(f"File not found", fg='red'))
        click.echo(click.style(f"File not found {masterkeys_json_enc_file_path}", fg='bright_red'))
        # print_formatted_text(HTML("<ansired>File not found</ansired>"))
        return

    enc_psw = ""
    decrypted_result = None
    while decrypted_result == None:
        enc_psw = fcrypt.prompt_pass(ask_confirmation=False)
        #print(psw)
        decrypted_result = decrypt_file(masterkeys_json_enc_file_path, enc_psw, output_file=False)
        # if file cannot be decrypted, decrypted_result type will be None

    # Decryption success
    json_result = json.loads(decrypted_result)

    smtester_bootloaderkeys =  pyfirmwaremandef.SMTESTER_BOOTLOADER_KEYS()
    for i in range(4):
        smtester_bootloaderkeys.masterkeys[i] = int(json_result["MasterKeys"][f"key%s" % str(i + 1)], 16)
        smtester_bootloaderkeys.statickeys[i] = int(json_result["StaticKeys"][f"key%s" % str(i + 1)], 16)
        smtester_bootloaderkeys.firstimekeys[i] = int(json_result["FirstTimeKeys"][f"key%s" % str(i + 1)], 16)

    while (1):
        use_enc_psw = False
        if len(enc_psw) > 0:
            use_enc_psw = click.prompt(
                'Cihaz anahtarları az önce başarılı bir şekilde girdiğiniz .enc dosyası için kullanılan şifreden mi üretiliyor?',
                type=bool, default=True)

        if (use_enc_psw == True):
            passsword_for_key_generation = enc_psw
            break
        else:
            pwd_visible = click.prompt('Cihaz anahtaları için şifre istenecek. Şifre görünür olsun mu?', type=bool,
                                       default=False)

            passsword_for_key_generation = click.prompt(
                'Cihaz anahtarlarının yeniden oluşturulması için cihaz şifresini girin (2 parçalı şifre ise tek parçalı olarak bitişik girin)',
                hide_input=not (pwd_visible), confirmation_prompt=True, type=str)
            passsword_for_key_generation = str(passsword_for_key_generation).strip()
            if (len(passsword_for_key_generation) == 1):
                print("This terminal does not support copy paste short cut. Please enter password by hand")
            else:
                break


    pwd_salt_bytes = pyfirmwaremandef.SmTesterConstants.CONST__DEVICE_KEY_SALT.encode("ascii")
    key_length = 16
    iteration = 1000000
    generated_device_keys = PBKDF2(passsword_for_key_generation, pwd_salt_bytes, key_length, iteration)

    device_xxtea_key = (ctypes.c_uint32 * 4)
    ba = bytearray(generated_device_keys)
    device_xxtea_key_ctypes_u32_array = device_xxtea_key.from_buffer(ba)

    keys_visible = click.prompt('Show generated keys and salt? (If you would like to embed keys to the device)',
                                type=bool, default=False)
    if (keys_visible == True):
        # Word representation
        key_str = " ".join("0x{:08x}".format(element) for element in device_xxtea_key_ctypes_u32_array[:])
        # print(" ".join("0x{:08x}".format(element) for element in device_xxtea_key_ctypes_u32_array[:]))

        click.echo(click.style(f"Generated Key (as word) {key_str}", fg='yellow'))
        click.echo(click.style(f"Generated Key (as byte array) {generated_device_keys.hex()}", fg='yellow'))
        click.echo(click.style(
            f"Generated Salt byte array {pwd_salt_bytes.hex()} (Salt is required to generate keys from same given password)",
            fg='yellow'))

    key = device_xxtea_key_ctypes_u32_array

    # Data to be encrypted.
    data_to_be_encrypted = (ctypes.c_uint32 * 12).from_buffer(bytearray(smtester_bootloaderkeys))
    # print(" ".join("0x{:08x}".format(element) for element in data_to_be_encrypted[:]))
    lib.comp_xxtea_encrypt(ctypes.byref(data_to_be_encrypted), 12, key)
    # data is npw encrypted
    data_encrypted = data_to_be_encrypted
    # print(" ".join("0x{:08x}".format(element) for element in data_to_be_encrypted[:]))

    encrypted_bytes = bytearray(data_encrypted)
    print(" ".join("0x{:02x}".format(element) for element in encrypted_bytes[:]))


    f = open(smt_bin_file_path, "wb")
    f.write(encrypted_bytes)
    f.close()


if __name__ == '__main__':
    make_bin_appmasterkeys()


