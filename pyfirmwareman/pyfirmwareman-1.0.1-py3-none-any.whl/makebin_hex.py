# >>>> DEV MODE #################
import os,sys
# Development Mode
# if pyfcrypt is a global package, then you can remove the following try - except
try:
    import pyfcrypt
    # import pysmtester
except:
    # discover path of the module and add it to the sys.path.
    dev_path = 'X:\\AYEDEK\\Software Projects\\pyfcrypt'
    print("DEV MODE ADDING PATH",dev_path)
    sys.path.append(dev_path)

    # dev_path = 'X:\\AYEDEK\\Software Projects\\pysmtester'
    # print("DEV MODE ADDING PATH",dev_path)
    # sys.path.append(dev_path)

# <<<< DEV MODE #################

# python makebin_hex.py x:\hex_repo\A092\boot\CYBOOTV100-4124PVI-432.hex
# or ->
#python makebin_hex.py x:\hex_repo\A092\boot\CYBOOTV100-4124PVI-432.hex.enc


"""
This script will create encrypted file from the given hex file (generally this is a bootloader file) for use with smtester tester and programmer device
"""
import os
from main import lib


from base64 import b64encode, b64decode
import ctypes
from Cryptodome.Protocol.KDF import PBKDF2
import click
import json
import pathlib


from prompt_toolkit import prompt
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.filters import Condition
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.shortcuts import yes_no_dialog


#import pysmtester.hexdef
import pyfirmwaremandef
from pyfcrypt import fcrypt
from pyfcrypt.fcrypt import decrypt_file

"""
class TARGET_DEVICE():
    def __init__(self):
        self.part_id = pyhexmandef.EnumPartId.PART_ID_PSOC4124
"""




red_style1 = Style.from_dict({
    # User input (default text).
    '':          '#ff0000',
    # Prompt.
    'password': '#ff0000',
    #'at':       '#00aa00',
})


def quit():
    os._exit(0)

def parse_hex(target_device, hex_file_lines) -> bool:
    # Low level implementation, may be used to parse and check different target hex files >
    #sector_start_address = ctypes.c_uint32(0x08002000)
    #byte_count_per_sector = ctypes.c_uint16(1024)
    #flash_memory_size = ctypes.c_uint32(64 * 1024);
    #lib.comp_intelhex_parser_Init(sector_start_address, byte_count_per_sector, flash_memory_size, 0xFF)

    # High level implementation > (For defined parts, necessary information is created automatically with the defined values inside the c dll
    r = lib.comp_intelhex_parser_InitForPart(target_device, pyfirmwaremandef.EnumIntelPurpose.FOR_DIRECT_HEX_PROGRAMMING)
    if r != 1:
        print("comp_intelhex_parser_InitForPart Error, return code:", r)
        return False

    for line in hex_file_lines:
        r = lib.comp_intelhex_parser_ParseRecordLine(ctypes.c_char_p(line.encode('utf-8')))
        if r != 1:
            print("comp_intelhex_parser_ParseRecordLine Error, return code:", r)
            print("line: \r\n", line)
            return False

    return True




bindings = KeyBindings()

"""
try:
    dll_file_path = "capifwb.so"
    lib = ctypes.cdll.LoadLibrary(dll_file_path)
    print(dll_file_path,"dll is loaded successfully")
except Exception as e:
        print("An exception occurred while loading dll", e)
        print("Failed to load dll at:", dll_file_path)
        quit()
"""


def testing(hex_file_lines):

    sector_address = lib.comp_intel_hex_parser_GetSectorAddress(7)
    print(hex(sector_address))
    quit()

    sector_count = lib.comp_intehex_parser_GetSectorCount()
    ctypes_uint16_list = (ctypes.c_uint16 * sector_count)()
    lib.comp_intel_hex_parser_GetSectorList(ctypes.byref(ctypes_uint16_list))
    for i in range(sector_count):
        print(ctypes_uint16_list[i])

    quit()

    parse_out = lib.comp_intelhex_parser_GetParsed(32,7)   #Get only Sector 8 parsed data, 128 byte groups.
    python_string = ctypes.c_char_p(parse_out).value.decode("ascii", errors='ignore')
    print("len", len(python_string))
    print(python_string)
    #print(ctypes.c_char_p(parse_out).value.decode("ascii", errors='ignore'))

    ctypes_sector_data = (ctypes.c_uint8 * 1024)()
    lib.comp_intel_hex_parser_GetSectorData(6, ctypes.byref(ctypes_sector_data))
    print(" ".join("0x{:02x}".format(element) for element in ctypes_sector_data[:]))


    quit()

@click.command()
@click.argument('file_name')
def hexformatter_main(file_name):


    file_name = str(file_name).strip()

    f_extensions = pathlib.Path(file_name).suffixes

    enc_psw = ""

    f_formatted_full_path = ""
    hex_file_lines = ""

    # Create lines from given hex file. Decrypt hex file if it is encrypted
    if f_extensions[-1] == ".enc":
        # Encrypted fcrypt file is given

        # Ask password until file is decrypted.
        decrypted_result = None
        while decrypted_result == None:
            enc_psw = fcrypt.prompt_pass(ask_confirmation=False)
            #print(psw)
            decrypted_result = decrypt_file(file_name, enc_psw, output_file=False)
            # if file cannot be decrypted, decrypted_result type will be None

        hex_file = decrypted_result.decode()
        hex_file_lines= hex_file.splitlines()

        # stem.enc
        f_smt_file_name = pathlib.Path(file_name).stem + ".smt.bin"
        f_dir = pathlib.Path(file_name).parent
        f_smt_file =  pathlib.Path(f_dir).joinpath(f_smt_file_name) #f_dir + "\\" + f_smt_file_name


    else:
        # Pure file is given (No encryption)

        f = open(file_name, "r")
        hex_file_lines = f.readlines()
        f.close()

        f_smt_file = file_name + ".smt.bin" # .hex.smt.bin.

    print("File to be created: ", f_smt_file)


    # hex file lines are ready for parsing.
    # Ask for target device
    print_formatted_text(HTML("<lime>(1) 125 kHz 2.Nesil Modül (Yeni) (CY8C412PVI-432)</lime>"))
    print_formatted_text(HTML("<lime>(2) (SM521X) (STM32F100C8T6B 64kb)</lime>"))
    print_formatted_text(HTML("<lime>(3) CY8C27443-24SXI</lime>"))

    selected_device= prompt("Yukarıda belirtilen listeden hedef cihazın numarasını girin:")
    if (int(selected_device) == 1):
        target_device = pyfirmwaremandef.EnumPartId.PART_ID_PSOC4124_16KB
    elif (int(selected_device) == 2):
        target_device = pyfirmwaremandef.EnumPartId.PART_ID_STM32F100
    elif (int(selected_device) == 3):
        target_device = pyfirmwaremandef.EnumPartId.PART_ID_CY8C27443_16KB
    else:
        print("Device is not supported")
        quit()

    status = parse_hex(target_device, hex_file_lines)
    if status == False:
        print("Error parsing hex file")
        quit()

    # testing(hex_file_lines)

    #  Alternative prompt askling yes/no by using click.
    # print_parsed_hex_file_result = click.prompt('Hex dosyasının biçimlenmiş içeriğini görmek ister misiniz?', type=bool, default=True)
    # print(print_parsed_hex_file_result)

    #yes_no = prompt("Hex dosyasının düzenlenmiş içeriğini görmek ister misiniz?", default="Y")
    print_parsed_hex_file_result = click.prompt('"Hex dosyasının biçimlenmiş içeriğini görmek ister misiniz? y/n', type=bool, default=True)

    # print_parsed_hex_file_result = yes_no_dialog(
    #    title='Evet/Hayır Penceresi',
    #    text='Hex dosyasının biçimlenmiş içeriğini görmek ister misiniz?')


    if (print_parsed_hex_file_result):
        # Before creating upgrade file, structured hex file can be investigated
        # first argument is byte grouping
        # second argument for retrieve target sector; -1 for get all parsed sectors and hex file information at the beginning.
        parse_out = lib.comp_intelhex_parser_GetParsed(32,-1)
        #parse_out = lib.comp_intelhex_parser_GetParsed(128,8)   #Get only Sector 8 parsed data, 128 byte groups.
        print(ctypes.c_char_p(parse_out).value.decode("ascii",errors='ignore'))

    continue_creating_formatted_file = click.prompt('İşleme devam edilsin mi? y/n', type=bool, default=True)
    if (continue_creating_formatted_file != True):
        print("İşlem iptal edildi")
        quit()


    if (target_device ==  pyfirmwaremandef.EnumPartId.PART_ID_PSOC4124_16KB):
        smtester_hex_file_header = pyfirmwaremandef.SMTESTER_HEX_FILE_HEADER_PSOC4124()

        # Target Chip
        smtester_hex_file_header.target_chip = target_device
        # Sector Count
        smtester_hex_file_header.sector_count = lib.comp_intehex_parser_GetSectorCount()
        # Sector Size (NoOfBytesPersector)
        smtester_hex_file_header.sector_size = lib.comp_intehex_parser_GetSectorSize()

        # Hex File Checksum
        special_record_data = (ctypes.c_uint8*64)() #Max possible
        special_record_datalength = (ctypes.c_uint16)()
        r = lib.comp_intelhex_parser_GetSpecialRecordData(pyfirmwaremandef.ENUM_SPECIAL_RECORD_ADDRESSES.PSOC4_CHECKSUM_ADDRESS, ctypes.byref(special_record_data), ctypes.byref(special_record_datalength))
        if (r == 0):
            print("PSOC4_CHECKSUM_ADDRESS special record could not be found")
            quit()
        smtester_hex_file_header.hex_checksum = (special_record_data[0] << 8) | (special_record_data[1] & 0xFF)

        # Meta Data - Chip ID
        r = lib.comp_intelhex_parser_GetSpecialRecordData(pyfirmwaremandef.ENUM_SPECIAL_RECORD_ADDRESSES.PSOC4_METADATA, ctypes.byref(special_record_data), ctypes.byref(special_record_datalength))
        if (r == 0):
            print("PSOC4_METADATA special record which includes Silicon ID could not be found.")
            quit()

        # smtester_hex_file_header.hex_silicon_id = (special_record_data[2] << 24) | (special_record_data[3] << 16) | (special_record_data[4] << 8) |  (special_record_data[5] & 0xFF)
        # reverse silicon id ->  04 10 11 93 -> 0x93111004
        smtester_hex_file_header.hex_silicon_id = (special_record_data[5] << 24)
        smtester_hex_file_header.hex_silicon_id |= (special_record_data[4] << 16)
        smtester_hex_file_header.hex_silicon_id |= (special_record_data[3] << 8)
        smtester_hex_file_header.hex_silicon_id |= (special_record_data[2] & 0xFF)
        # print(hex(special_record_data[2]))  04
        # print(hex(special_record_data[3]))  10
        # print(hex(special_record_data[4]))  11
        # print(hex(special_record_data[5]))  93


        # Chip Protection Level
        r = lib.comp_intelhex_parser_GetSpecialRecordData(pyfirmwaremandef.ENUM_SPECIAL_RECORD_ADDRESSES.PSOC4_CHIP_LEVEL_PROTECTION, ctypes.byref(special_record_data), ctypes.byref(special_record_datalength))
        if (r == 0):
            print("PSOC4_CHIP_LEVEL_PROTECTION special record could not be found.")
            quit()

        smtester_hex_file_header.chip_protection_level = special_record_data[0]


        # Flash Protection Rows
        r = lib.comp_intelhex_parser_GetSpecialRecordData(pyfirmwaremandef.ENUM_SPECIAL_RECORD_ADDRESSES.PSOC4_FLASH_PROTECTION_ROWS, ctypes.byref(special_record_data), ctypes.byref(special_record_datalength))
        if (r == 0):
            print("PSOC4_FLASH_PROTECTION_ROWS special record could not be found.")
            quit()

        smtester_hex_file_header.hex_protection_data_length = special_record_datalength.value
        # Alternative Way with bytearray
        # hex_protection_data_ba = bytearray(smtester_hex_file_header.hex_protection_data_length)
        # for i in range(smtester_hex_file_header.hex_protection_data_length):
        #     hex_protection_data_ba[i] = special_record_data[i]

        # Alternative Way
        # for i in range(smtester_hex_file_header.hex_protection_data_length):
        #     smtester_hex_file_header.hex_protection_data[i] = special_record_data[i]

        # Direct binding to special_record_data
        #special_record_data = (ctypes.c_uint8*32)()
        smtester_hex_file_header.hex_protection_data = special_record_data #(ctypes.c_uint8 * 32).from_buffer(special_record_data)
        #smtester_hex_file_header.hex_protection_data = (ctypes.c_uint8 * 16).from_buffer(hex_protection_data_ba)

        # print(" ".join("0x{:02x}".format(element) for element in smtester_hex_file_header.hex_protection_data[:]))
        # print("length:", len(smtester_hex_file_header.hex_protection_data))

        # Here we expect CTYPES STRUCTURE class is converted to bytes properly, with same order that embedded device c compiler can resolve.
        smtester_hex_file_header_ba = bytearray(smtester_hex_file_header)
        if (len(smtester_hex_file_header_ba) != 128):
            print("smtester_hex_file_header_bytes(converted from SMTESTER_HEX_FILE_HEADER structure) supposed to be 128 bytes in length ")
            print("length of smtester_hex_file_header_bytes", len(smtester_hex_file_header_ba))
            print(" ".join("0x{:02x}".format(element) for element in smtester_hex_file_header_ba[:]))
            quit()

        # Print info with the header files
        print("*"*10, "SUMMARY", "*"*10)
        print("Target Device \t\t: {} (0x{:08x})".format(pyfirmwaremandef.EnumPartId(smtester_hex_file_header.target_chip).name, smtester_hex_file_header.target_chip))
        print("Silicon ID \t\t: 0x{:08x}".format(smtester_hex_file_header.hex_silicon_id))
        print("Sector Size\t\t: %d bytes" % smtester_hex_file_header.sector_size)
        print("Sector Count\t\t: %d" % smtester_hex_file_header.sector_count)
        print("Capacity\t\t: {} bytes".format(smtester_hex_file_header.sector_count * smtester_hex_file_header.sector_size))
        print("Chip Level Protection\t: {} (0x{:02x})".format(pyfirmwaremandef.ENUM_CHIP_LEVEL_PROTECTION(smtester_hex_file_header.chip_protection_level).name, smtester_hex_file_header.chip_protection_level))
        print("Protection Data Length\t: %d bytes" % smtester_hex_file_header.hex_protection_data_length)
        print("Protection Data\t\t:",end='')
        print(" ".join("0x{:02x}".format(element) for element in smtester_hex_file_header.hex_protection_data[0:16]))
        print("Unused Data\t\t:",end='')
        print(" ".join("0x{:02x}".format(element) for element in smtester_hex_file_header.hex_protection_data[16:]))
        print("")

        while (1):
            use_enc_psw = False
            if len(enc_psw)>0:
                use_enc_psw = click.prompt('Cihaz anahtarları az önce başarılı bir şekilde girdiğiniz .enc dosyası için kullanılan şifreden mi üretiliyor?', type=bool,default=True)

            if (use_enc_psw == True):
                passsword_for_key_generation = enc_psw
                break
            else:
                pwd_visible = click.prompt('Cihaz anahtaları için şifre istenecek. Şifre görünür olsun mu?', type=bool,
                                           default=True)

                passsword_for_key_generation = click.prompt('Cihaz anahtarlarının yeniden oluşturulması için cihaz şifresini girin (2 parçalı şifre ise tek parçalı olarak bitişik girin)',
                                                            hide_input=not (pwd_visible), confirmation_prompt=True, type=str)
                passsword_for_key_generation = str(passsword_for_key_generation).strip()
                if (len(passsword_for_key_generation) == 1):
                    print("This terminal does not support copy paste short cut. Please enter password by hand")
                else:
                    break

        # print(passsword_for_key_generation)
        #  print("default encode",passsword_for_key_generation.encode())
        # print("utf8 encode",passsword_for_key_generation.encode("utf-8"))
        
        pwd_salt_bytes = pyfirmwaremandef.SmTesterConstants.CONST__DEVICE_KEY_SALT.encode("ascii")
        key_length = 16
        iteration = 1000000
        generated_device_keys = PBKDF2(passsword_for_key_generation, pwd_salt_bytes, key_length, iteration)

        device_xxtea_key = (ctypes.c_uint32 * 4)
        ba = bytearray(generated_device_keys)
        device_xxtea_key_ctypes_u32_array = device_xxtea_key.from_buffer(ba)


        keys_visible = click.prompt('Show generated keys and salt? (If you would like to embed keys to the device)', type=bool, default=False)
        if (keys_visible == True):
            # Word representation
            key_str = " ".join("0x{:08x}".format(element) for element in device_xxtea_key_ctypes_u32_array[:])
            #print(" ".join("0x{:08x}".format(element) for element in device_xxtea_key_ctypes_u32_array[:]))

            click.echo(click.style(f"Generated Key (as word) {key_str}", fg='yellow'))
            click.echo(click.style(f"Generated Key (as byte array) {generated_device_keys.hex()}", fg='yellow'))
            click.echo(click.style(f"Generated Salt byte array {pwd_salt_bytes.hex()} (Salt is required to generate keys from same given password)", fg='yellow'))


        key = device_xxtea_key_ctypes_u32_array

        # Data to be encrypted.
        #encrypted_smtester_hex_file_header = encrypt_as_32_words(smtester_hex_file_header_bytes, key)

        encrypted_smtester_hex_file_header = (ctypes.c_uint32 * 32).from_buffer(smtester_hex_file_header_ba)
        lib.comp_xxtea_encrypt(ctypes.byref(encrypted_smtester_hex_file_header), 32, key)

        # Convert encrypted bytes to binary file.
        binary_file_ba = bytearray()
        binary_file_ba.extend(encrypted_smtester_hex_file_header)

        for i in range(smtester_hex_file_header.sector_count):
            ctypes_sector_data = (ctypes.c_uint8 * smtester_hex_file_header.sector_size)()
            lib.comp_intel_hex_parser_GetSectorData(i, ctypes.byref(ctypes_sector_data))
            #print(" ".join("0x{:02x}".format(element) for element in ctypes_sector_data[:]))

            # Data to be encrypted.
            #n = 32
            # Data to be encrypted.
            n =  int(smtester_hex_file_header.sector_size / 4) #  1024/4 = 256 words (STM32F100) ,  128/4 = 32 Words (PSOC4)

            data_to_be_encrypted = (ctypes.c_uint32 * n).from_buffer(bytearray(ctypes_sector_data))
            # print(" ".join("0x{:08x}".format(element) for element in data_to_be_encrypted[:]))
            lib.comp_xxtea_encrypt(ctypes.byref(data_to_be_encrypted), n, key)
            # data is npw encrypted
            data_encrypted = data_to_be_encrypted
            # print(" ".join("0x{:08x}".format(element) for element in data_to_be_encrypted[:]))

            encrypted_bytes = bytearray(data_encrypted)
            #print(" ".join("0x{:02x}".format(element) for element in encrypted_bytes[:]))


            encrypted_sector_data  = encrypted_bytes #encrypt_as_32_words(ctypes_sector_data, key)
            # print(" ".join("0x{:08x}".format(element) for element in encrypted_sector_data[:]))
            binary_file_ba.extend(encrypted_sector_data)
            #f_smt_lines.append(b64encode(encrypted_sector_data).decode('utf-8'))
            #f_smt_lines.append("\n")


        f = open(f_smt_file, "wb")
        f.write(binary_file_ba)
        f.close()

        print(".smt.bin file for smtester programmer is created successfully. You can use uploading tool to transfer .smt.bin file to the programmer device")

        lib.comp_intelhex_parser_freemem()
        print("dll resources are released")

        """
        # Convert encrypted bytes to binary encoded string.
        # File Header Data
        f_smt_lines = []
        f_smt_lines.append(b64encode(encrypted_smtester_hex_file_header).decode('utf-8'))
        f_smt_lines.append("\n")

        # Get Sector Data
        for i in range(smtester_hex_file_header.sector_count):
            ctypes_sector_data = (ctypes.c_uint8 * smtester_hex_file_header.sector_size)()
            lib.comp_intel_hex_parser_GetSectorData(i, ctypes.byref(ctypes_sector_data))
            #print(" ".join("0x{:02x}".format(element) for element in ctypes_sector_data[:]))

            # Data to be encrypted.
            n = 32
            data_to_be_encrypted = (ctypes.c_uint32 * n).from_buffer(bytearray(ctypes_sector_data))
            # print(" ".join("0x{:08x}".format(element) for element in data_to_be_encrypted[:]))
            lib.comp_xxtea_encrypt(ctypes.byref(data_to_be_encrypted), n, key)
            # data is npw encrypted
            data_encrypted = data_to_be_encrypted
            # print(" ".join("0x{:08x}".format(element) for element in data_to_be_encrypted[:]))

            encrypted_bytes = bytearray(data_encrypted)
            #print(" ".join("0x{:02x}".format(element) for element in encrypted_bytes[:]))


            encrypted_sector_data  = encrypted_bytes #encrypt_as_32_words(ctypes_sector_data, key)
            # print(" ".join("0x{:08x}".format(element) for element in encrypted_sector_data[:]))
            f_smt_lines.append(b64encode(encrypted_sector_data).decode('utf-8'))
            f_smt_lines.append("\n")


        f = open(f_smt_file, "w")
        f.writelines(f_smt_lines)
        f.close()
        """
    elif (target_device == pyfirmwaremandef.EnumPartId.PART_ID_STM32F100):

        smtester_hex_file_header_stm32f100 = pyfirmwaremandef.SMTESTER_HEX_FILE_HEADER_STM32F100()

        smtester_hex_file_header_stm32f100.hex_silicon_id = 0x0420
        # Target Chip
        smtester_hex_file_header_stm32f100.target_chip = target_device
        # Sector Count
        smtester_hex_file_header_stm32f100.sector_count = lib.comp_intehex_parser_GetSectorCount()
        # Sector Size (NoOfBytesPersector)
        smtester_hex_file_header_stm32f100.sector_size = lib.comp_intehex_parser_GetSectorSize()


        # Here we expect CTYPES STRUCTURE class is converted to bytes properly, with same order that embedded device c compiler can resolve.
        smtester_hex_file_header_stm32f100_ba = bytearray(smtester_hex_file_header_stm32f100)
        if (len(smtester_hex_file_header_stm32f100_ba) != 16):
            print("smtester_hex_file_header_bytes(converted from SMTESTER_HEX_FILE_HEADER_STM32F100 structure) supposed to be 16 bytes in length ")
            print("length of smtester_hex_file_header_bytes", len(smtester_hex_file_header_stm32f100_ba))
            print(" ".join("0x{:02x}".format(element) for element in smtester_hex_file_header_stm32f100_ba[:]))
            quit()

        # Print info with the header files
        ctypes_uint16_list = (ctypes.c_uint16 * smtester_hex_file_header_stm32f100.sector_count)()
        lib.comp_intel_hex_parser_GetSectorList(ctypes.byref(ctypes_uint16_list))
        used_sectors = ", ".join("{}".format(element) for element in ctypes_uint16_list[:])
        print(used_sectors)

        print("*"*10, "SUMMARY", "*"*10)
        print("Target Device \t\t: {} (0x{:08x})".format(pyfirmwaremandef.EnumPartId(smtester_hex_file_header_stm32f100.target_chip).name, smtester_hex_file_header_stm32f100.target_chip))
        print("Silicon ID \t\t: 0x{:04x}".format(smtester_hex_file_header_stm32f100.hex_silicon_id))
        print("Sector Size\t\t: %d bytes" % smtester_hex_file_header_stm32f100.sector_size)
        print("Sector Count\t\t: %d" % smtester_hex_file_header_stm32f100.sector_count)
        print("Used Sectors\t\t: {}".format(used_sectors))
        print("Capacity\t\t: {} bytes".format(smtester_hex_file_header_stm32f100.sector_count * smtester_hex_file_header_stm32f100.sector_size))
        print("")


        while (1):
            use_enc_psw = False
            if len(enc_psw)>0:
                use_enc_psw = click.prompt('Cihaz anahtarları az önce başarılı bir şekilde girdiğiniz .enc dosyası için kullanılan şifreden mi üretiliyor?', type=bool,default=True)

            if (use_enc_psw == True):
                passsword_for_key_generation = enc_psw
                break
            else:
                pwd_visible = click.prompt('Cihaz anahtaları için şifre istenecek. Şifre görünür olsun mu?', type=bool,
                                           default=True)

                passsword_for_key_generation = click.prompt('Cihaz anahtarlarının yeniden oluşturulması için cihaz şifresini girin (2 parçalı şifre ise tek parçalı olarak bitişik girin)',
                                                            hide_input=not (pwd_visible), confirmation_prompt=True, type=str)
                passsword_for_key_generation = str(passsword_for_key_generation).strip()
                if (len(passsword_for_key_generation) == 1):
                    print("This terminal does not support copy paste short cut. Please enter password by hand")
                else:
                    break

        #print(passsword_for_key_generation)
        #print("default encode",passsword_for_key_generation.encode())
        #print("utf8 encode",passsword_for_key_generation.encode("utf-8"))

        pwd_salt_bytes = pyfirmwaremandef.SmTesterConstants.CONST__DEVICE_KEY_SALT.encode("ascii")
        key_length = 16
        iteration = 1000000
        generated_device_keys = PBKDF2(passsword_for_key_generation, pwd_salt_bytes, key_length, iteration)

        device_xxtea_key = (ctypes.c_uint32 * 4)
        ba = bytearray(generated_device_keys)
        device_xxtea_key_ctypes_u32_array = device_xxtea_key.from_buffer(ba)

        keys_visible = click.prompt('Show generated keys and salt? (If you would like to embed keys to the device)', type=bool, default=False)
        if (keys_visible == True):
            # Word representation
            key_str = " ".join("0x{:08x}".format(element) for element in device_xxtea_key_ctypes_u32_array[:])
            #print(" ".join("0x{:08x}".format(element) for element in device_xxtea_key_ctypes_u32_array[:]))

            click.echo(click.style(f"Generated Key (as word) {key_str}", fg='yellow'))
            click.echo(click.style(f"Generated Key (as byte array) {generated_device_keys.hex()}", fg='yellow'))
            click.echo(click.style(f"Generated Salt byte array {pwd_salt_bytes.hex()} (Salt is required to generate keys from same given password)", fg='yellow'))


        key = device_xxtea_key_ctypes_u32_array

        # Data to be encrypted.
        #encrypted_smtester_hex_file_header = encrypt_as_32_words(smtester_hex_file_header_bytes, key)

        encrypted_smtester_hex_file_header = (ctypes.c_uint32 * 4).from_buffer(smtester_hex_file_header_stm32f100_ba)
        lib.comp_xxtea_encrypt(ctypes.byref(encrypted_smtester_hex_file_header), 4, key)

        # Convert encrypted bytes to binary file.
        binary_file_ba = bytearray()
        binary_file_ba.extend(encrypted_smtester_hex_file_header)

        for i in range(smtester_hex_file_header_stm32f100.sector_count):
            ctypes_sector_data = (ctypes.c_uint8 * smtester_hex_file_header_stm32f100.sector_size)()
            lib.comp_intel_hex_parser_GetSectorData(i, ctypes.byref(ctypes_sector_data))
            #print(" ".join("0x{:02x}".format(element) for element in ctypes_sector_data[:]))

            # Data to be encrypted.
            n =  int(smtester_hex_file_header_stm32f100.sector_size / 4) #  1024/4 = 256 words (STM32F100) ,  128/4 = 32 Words (PSOC4)
            #print("n words",n)
            data_to_be_encrypted = (ctypes.c_uint32 * n).from_buffer(bytearray(ctypes_sector_data))
            # print(" ".join("0x{:08x}".format(element) for element in data_to_be_encrypted[:]))
            lib.comp_xxtea_encrypt(ctypes.byref(data_to_be_encrypted), n, key)
            # data is npw encrypted
            data_encrypted = data_to_be_encrypted
            # print(" ".join("0x{:08x}".format(element) for element in data_to_be_encrypted[:]))

            encrypted_bytes = bytearray(data_encrypted)
            #print(" ".join("0x{:02x}".format(element) for element in encrypted_bytes[:]))


            encrypted_sector_data  = encrypted_bytes #encrypt_as_32_words(ctypes_sector_data, key)
            # print(" ".join("0x{:08x}".format(element) for element in encrypted_sector_data[:]))

            # sector_address is not encrypted
            actual_sector_no = ctypes.c_uint16()
            sector_address = lib.comp_intel_hex_parser_GetSectorAddress(i,ctypes.byref(actual_sector_no))
            sector_address_ba = sector_address.to_bytes(4, "little")
            binary_file_ba.extend(sector_address_ba)
            binary_file_ba.extend(encrypted_sector_data)
            #f_smt_lines.append(b64encode(encrypted_sector_data).decode('utf-8'))
            #f_smt_lines.append("\n")
            print(i, "Sector {}".format(actual_sector_no.value), hex(sector_address), " {} bytes encrypted".format(len(encrypted_sector_data)))

        f = open(f_smt_file, "wb")
        f.write(binary_file_ba)
        f.close()

        print(".smt.bin file for smtester programmer is created successfully. You can use uploading tool to transfer .smt.bin file to the programmer device")

        lib.comp_intelhex_parser_freemem()
        print("dll resources are released")
    elif (target_device == pyfirmwaremandef.EnumPartId.PART_ID_CY8C27443_16KB):
        smtester_hex_file_header_cy8c27443 = pyfirmwaremandef.SMTESTER_HEX_FILE_HEADER_CY8C27443()

        # Target Chip
        smtester_hex_file_header_cy8c27443.target_chip = target_device
        # Sector Count
        smtester_hex_file_header_cy8c27443.sector_count = lib.comp_intehex_parser_GetSectorCount()
        # Sector Size (NoOfBytesPersector)
        smtester_hex_file_header_cy8c27443.sector_size = lib.comp_intehex_parser_GetSectorSize()

        # Hex File Checksum
        special_record_data = (ctypes.c_uint8*64)() #Max possible
        special_record_datalength = (ctypes.c_uint16)()
        r = lib.comp_intelhex_parser_GetSpecialRecordData(pyfirmwaremandef.ENUM_SPECIAL_RECORD_ADDRESSES.CY8C27443_CHECKSUM_ADDRESS, ctypes.byref(special_record_data), ctypes.byref(special_record_datalength))
        if (r == 0):
            print("PSOC4_CHECKSUM_ADDRESS special record could not be found")
            quit()

        smtester_hex_file_header_cy8c27443.hex_checksum = (special_record_data[0] << 8) | (special_record_data[1] & 0xFF)

        # Flash Protection Rows
        r = lib.comp_intelhex_parser_GetSpecialRecordData(pyfirmwaremandef.ENUM_SPECIAL_RECORD_ADDRESSES.CY8C27443_FLASH_PROTECTION_ROWS, ctypes.byref(special_record_data), ctypes.byref(special_record_datalength))
        if (r == 0):
            print("PSOC4_FLASH_PROTECTION_ROWS special record could not be found.")
            quit()

        smtester_hex_file_header_cy8c27443.flash_security_data_length = special_record_datalength.value
        # Alternative Way with bytearray
        # hex_protection_data_ba = bytearray(smtester_hex_file_header.hex_protection_data_length)
        # for i in range(smtester_hex_file_header.hex_protection_data_length):
        #     hex_protection_data_ba[i] = special_record_data[i]

        # Alternative Way
        # for i in range(smtester_hex_file_header.hex_protection_data_length):
        #     smtester_hex_file_header.hex_protection_data[i] = special_record_data[i]

        # Direct binding to special_record_data
        #special_record_data = (ctypes.c_uint8*32)()
        smtester_hex_file_header_cy8c27443.flash_security_data = special_record_data #(ctypes.c_uint8 * 32).from_buffer(special_record_data)
        #smtester_hex_file_header.hex_protection_data = (ctypes.c_uint8 * 16).from_buffer(hex_protection_data_ba)

        #print(" ".join("0x{:02x}".format(element) for element in smtester_hex_file_header_cy8c27443.flash_security_data[:]))
        #print("length:", len(smtester_hex_file_header_cy8c27443.flash_security_data))
        #print("length:", smtester_hex_file_header_cy8c27443.flash_security_data_length)

        # Here we expect CTYPES STRUCTURE class is converted to bytes properly, with same order that embedded device c compiler can resolve.
        smtester_hex_file_header_ba = bytearray(smtester_hex_file_header_cy8c27443)
        if (len(smtester_hex_file_header_ba) != 128):
            print("smtester_hex_file_header_bytes(converted from SMTESTER_HEX_FILE_HEADER structure) supposed to be 128 bytes in length ")
            print("length of smtester_hex_file_header_bytes", len(smtester_hex_file_header_ba))
            print(" ".join("0x{:02x}".format(element) for element in smtester_hex_file_header_ba[:]))
            quit()

        # Print info with the header files
        print("*"*10, "SUMMARY", "*"*10)
        print("Target Device \t\t\t: {} (0x{:08x})".format(pyfirmwaremandef.EnumPartId(smtester_hex_file_header_cy8c27443.target_chip).name, smtester_hex_file_header_cy8c27443.target_chip))
        print("Silicon ID \t\t\t: 0x{:08x}".format(smtester_hex_file_header_cy8c27443.hex_silicon_id))
        print("Sector Size\t\t\t: %d bytes" % smtester_hex_file_header_cy8c27443.sector_size)
        print("Sector Count\t\t\t: %d" % smtester_hex_file_header_cy8c27443.sector_count)
        print("Capacity\t\t\t: {} bytes".format(smtester_hex_file_header_cy8c27443.sector_count * smtester_hex_file_header_cy8c27443.sector_size))
        print("Flash Protection Data Length\t: %d bytes" % smtester_hex_file_header_cy8c27443.flash_security_data_length)
        print("Flash Protection Data\t\t:",end='')
        print(" ".join("0x{:02x}".format(element) for element in smtester_hex_file_header_cy8c27443.flash_security_data[:]))
        print("")

        while (1):
            use_enc_psw = False
            if len(enc_psw)>0:
                use_enc_psw = click.prompt('Cihaz anahtarları az önce başarılı bir şekilde girdiğiniz .enc dosyası için kullanılan şifreden mi üretiliyor?', type=bool,default=True)

            if (use_enc_psw == True):
                passsword_for_key_generation = enc_psw
                break
            else:
                pwd_visible = click.prompt('Cihaz anahtaları için şifre istenecek. Şifre görünür olsun mu?', type=bool,
                                           default=True)

                passsword_for_key_generation = click.prompt('Cihaz anahtarlarının yeniden oluşturulması için cihaz şifresini girin (2 parçalı şifre ise tek parçalı olarak bitişik girin)',
                                                            hide_input=not (pwd_visible), confirmation_prompt=True, type=str)
                passsword_for_key_generation = str(passsword_for_key_generation).strip()
                if (len(passsword_for_key_generation) == 1):
                    print("This terminal does not support copy paste short cut. Please enter password by hand")
                else:
                    break

        # print(passsword_for_key_generation)
        #  print("default encode",passsword_for_key_generation.encode())
        # print("utf8 encode",passsword_for_key_generation.encode("utf-8"))

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
        #encrypted_smtester_hex_file_header = encrypt_as_32_words(smtester_hex_file_header_bytes, key)

        encrypted_smtester_hex_file_header = (ctypes.c_uint32 * 32).from_buffer(smtester_hex_file_header_ba)
        lib.comp_xxtea_encrypt(ctypes.byref(encrypted_smtester_hex_file_header), 32, key)

        # Convert encrypted bytes to binary file.
        binary_file_ba = bytearray()
        binary_file_ba.extend(encrypted_smtester_hex_file_header)

        for i in range(smtester_hex_file_header_cy8c27443.sector_count):
            ctypes_sector_data = (ctypes.c_uint8 * smtester_hex_file_header_cy8c27443.sector_size)()
            lib.comp_intel_hex_parser_GetSectorData(i, ctypes.byref(ctypes_sector_data))
            # print(" ".join("0x{:02x}".format(element) for element in ctypes_sector_data[:]))

            # Data to be encrypted.
            #n = 32
            n =  int(smtester_hex_file_header_cy8c27443.sector_size / 4) #  64 Bytes / 4 = 16 Words (CY8C27443)   1024/4 = 256 words (STM32F100) ,  128/4 = 32 Words (PSOC4)

            data_to_be_encrypted = (ctypes.c_uint32 * n).from_buffer(bytearray(ctypes_sector_data))
            # print(" ".join("0x{:08x}".format(element) for element in data_to_be_encrypted[:]))
            lib.comp_xxtea_encrypt(ctypes.byref(data_to_be_encrypted), n, key)
            # data is npw encrypted
            data_encrypted = data_to_be_encrypted
            # print(" ".join("0x{:08x}".format(element) for element in data_to_be_encrypted[:]))

            encrypted_bytes = bytearray(data_encrypted)
            #print(" ".join("0x{:02x}".format(element) for element in encrypted_bytes[:]))


            encrypted_sector_data  = encrypted_bytes #encrypt_as_32_words(ctypes_sector_data, key)
            # print(" ".join("0x{:08x}".format(element) for element in encrypted_sector_data[:]))
            binary_file_ba.extend(encrypted_sector_data)
            #f_smt_lines.append(b64encode(encrypted_sector_data).decode('utf-8'))
            #f_smt_lines.append("\n")


        f = open(f_smt_file, "wb")
        f.write(binary_file_ba)
        f.close()

        print("{} for smtester programmer is created successfully. You can use uploading tool to transfer .smt.bin file to the programmer device".format(f_smt_file))

        lib.comp_intelhex_parser_freemem()
        print("dll resources are released")


if __name__ == '__main__':
    hexformatter_main()


