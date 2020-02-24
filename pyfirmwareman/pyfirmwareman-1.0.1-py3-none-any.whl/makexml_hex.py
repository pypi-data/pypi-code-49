# Creates upgrade xml file from given hex file. Script version of SBoot Manager .NET Software
# Firmware versions, and desciptions must be organized in a different software
# This script only create xml file for given firmware version and parameters. It does not keep versions organized.
# It is prone to create wrong firmware version files as there is no organization, or check mechanism.
import ctypes
import json
import pathlib
import datetime

from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text, HTML

from shared import bindings
from helper_configini import prompt_and_update_config_option
from pyfirmwaremandef import CONST__CONFIG_SECTION_NAME_PARAMS, ENUM_APPLICATION
from main import lib
import pyfirmwaremandef
import pyfcrypt
from pyfcrypt import fcrypt
from enum import IntEnum

class EnumTarget(IntEnum):
    TARGET_FOR_ALL = 1,
    TARGET_FOR_DEVICE_FAMILY = 2,
    TARGET_FOR_DEVICE_ID = 3,



class STRUCT_TARGET_DEVICE_INFO(ctypes.Structure):
    def __init__(self):
        self.deviceFamily = 0
        self.manufacturerID = 0
        self.serialNumber = 0
        self.partID = 0
        self.isFirstTime = 0
        self.target = EnumTarget.TARGET_FOR_ALL

    _fields_ = [("deviceFamily",ctypes.c_uint32),
                ("manufacturerID",ctypes.c_uint32),
                ("serialNumber", ctypes.c_uint32),
                ("partID", ctypes.c_uint32),
                ("isFirstTime",ctypes.c_uint8),
                ("target",ctypes.c_uint)]


class STRUCT_FIRMWARE_INFO(ctypes.Structure):
    def __init__(self):
        self.caption = "".encode("ascii") # bytes(0)
        self.version = 0
        self.revision = 0
        self.build = 0
        self.releaseType = pyfirmwaremandef.EnumFirmwareReleaseType.BETA
        self.dateYear = 0
        self.dateMonth = 0
        self.dateDay = 0
        # self.configId = 0

    _fields_ = [("caption",ctypes.c_char*24), #("caption",c_char_p),
                ("version",ctypes.c_uint8),
                ("revision", ctypes.c_uint8),
                ("build", ctypes.c_uint8),
                ("releaseType",ctypes.c_uint8),
                ("dateYear",ctypes.c_uint16),
                ("dateMonth",ctypes.c_uint8),
                ("dateDay",ctypes.c_uint8),
                #("configId",c_uint8),
                ]


def menu():

    while (1):
        print_formatted_text(HTML("<lime>(1) A011 SM5210 Mifare (STM32F100)</lime>"))
        print_formatted_text(HTML("<lime>(2) A092 125 kHz 2nd Gen (CY8C4124)</lime>"))
        print_formatted_text(HTML("<lime>(0) Exit</lime>"))

        selected_device = prompt("Seçiminiz:", key_bindings=bindings)

        if (int(selected_device) == 0):
            quit()
        elif (int(selected_device) == 1):
            makexml_for_SM5210()
            quit()
        elif (int(selected_device) == 2):
            makexml_for_4124()
            quit()



def makexml_for_SM5210():

    #target_chip_part_id = pyfirmwaremandef.EnumPartId.PART_ID_STM32F100
    application_str = ENUM_APPLICATION.A011.name

    targetDeviceInfo = STRUCT_TARGET_DEVICE_INFO()
    targetDeviceInfo.deviceFamily = 0xA0115210                                          # 0 #0xA0115210
    targetDeviceInfo.manufacturerID = 0                                                 # Will be override by smtester programmer
    targetDeviceInfo.serialNumber = 0                                                   # Will be override by smtester programmer
    targetDeviceInfo.partID = pyfirmwaremandef.EnumPartId.PART_ID_STM32F100.value       # 0x00000103;  # STM32F100/103
    targetDeviceInfo.target = EnumTarget.TARGET_FOR_ALL                                 # TARGET_FOR_DEVICE_FAMILY #TARGET_FOR_ALL # TARGET_FOR_DEVICE_FAMILY # .TARGET_FOR_DEVICE_ID
    targetDeviceInfo.isFirstTime = 0                                                    # if it is firstime; target will be changed to TARGET_FOR_DEVICE_ID internally on C api.

    checksum_excluded_sectors = {30, 31}

    makexml(application_str=application_str,targetDeviceInfo=targetDeviceInfo,checksum_excluded_sectors=checksum_excluded_sectors)

def makexml_for_4124():

    #target_chip_part_id = pyfirmwaremandef.EnumPartId.PART_ID_PSOC4124_16KB
    application_str = ENUM_APPLICATION.A092.name

    targetDeviceInfo = STRUCT_TARGET_DEVICE_INFO()
    targetDeviceInfo.deviceFamily = 0xA0920000                                          # 0 #0xA0920000
    targetDeviceInfo.manufacturerID = 0                                                 # Will be override by smtester programmer
    targetDeviceInfo.serialNumber = 0                                                   # Will be override by smtester programmer
    targetDeviceInfo.partID = pyfirmwaremandef.EnumPartId.PART_ID_PSOC4124_16KB.value       # 0x00000103;  # STM32F100/103
    targetDeviceInfo.target = EnumTarget.TARGET_FOR_ALL                                 # TARGET_FOR_DEVICE_FAMILY #TARGET_FOR_ALL # TARGET_FOR_DEVICE_FAMILY # .TARGET_FOR_DEVICE_ID
    targetDeviceInfo.isFirstTime = 0                                                    # if it is firstime; target will be changed to TARGET_FOR_DEVICE_ID internally on C api.

    checksum_excluded_sectors = {127}

    makexml(application_str=application_str,targetDeviceInfo=targetDeviceInfo,checksum_excluded_sectors=checksum_excluded_sectors)


def makexml(application_str,targetDeviceInfo,checksum_excluded_sectors):
    purpose = pyfirmwaremandef.EnumIntelPurpose.FOR_UPGRADE.value
    hex_file_path = prompt_and_update_config_option(CONST__CONFIG_SECTION_NAME_PARAMS, "{}_HEX_FILE".format(application_str),
                                                    "Hex dosyasının yolunu belirtiniz (*.hex):", default_val=".hex")


    # hex_file_parent_folder = pathlib.Path(hex_file_path).parent
    # print(parent_folder)

    if (hex_file_path == ""):
        print("Dosya seçilmedi")
        return

    try:
        f = open(hex_file_path,"r")
        hex_file_lines = f.readlines()
        f.close()
    except FileNotFoundError:
        print('Dosya bulunamadı', hex_file_path)
        return
    except Exception as e:
        print("Sistem hatası (Exception)", e)
        return

    # Low level implementation, may be used to parse and check different target hex files >
    # sector_start_address = ctypes.c_uint32(0x08002000)
    # byte_count_per_sector = ctypes.c_uint16(1024)
    # flash_memory_size = ctypes.c_uint32(64 * 1024);
    # lib.comp_intelhex_parser_Init(sector_start_address, byte_count_per_sector, flash_memory_size, 0xFF)

    # High level implementation > (For defined parts, necessary information is created automatically with the defined values
    r = lib.comp_intelhex_parser_InitForPart(targetDeviceInfo.partID, purpose)
    if r != 1:
        print("DLL API Error (comp_intelhex_parser_InitForPart), return code:", r)
        quit()

    for line in hex_file_lines:
        r = lib.comp_intelhex_parser_ParseRecordLine(ctypes.c_char_p(line.encode('utf-8')))
        if r != 1:
            print("DLL API Error (comp_intelhex_parser_ParseRecordLine), return code:", r)
            break

    # Before creating upgrade file, structured hex file can be investigated
    # first argument is byte grouping
    # second argument for retrieve target sector; -1 for get all parsed sectors and hex file information at the beginning.
    parse_out = lib.comp_intelhex_parser_GetParsed(64,-1)
    # parse_out = lib.comp_intelhex_parser_GetParsed(128,8)   #Get only Sector 8 parsed data, 128 byte groups.
    print(ctypes.c_char_p(parse_out).value.decode("ascii",errors='ignore'))

    # Get Empty sectors (sectors with full of zeros, and exclude them when creating script file)
    # This operation is optional. There is no problem to include empty sectors in the upgrade file.
    sector_count = lib.comp_intehex_parser_GetSectorCount()
    ctypes_empty_sector_count = (ctypes.c_uint16)()
    ctypes_uint16_empty_sector_list = (ctypes.c_uint16 * sector_count)()
    lib.comp_intel_hex_parser_GetEmptySectorList(ctypes.byref(ctypes_uint16_empty_sector_list),ctypes.byref(ctypes_empty_sector_count))

    excluded_sectors_list = [] # {} #{124,125,126}  # 30,31}
    empty_sector_count = ctypes_empty_sector_count.value
    for i in range(empty_sector_count):
        excluded_sectors_list.append(ctypes_uint16_empty_sector_list[i])

    #empty_sectors = ", ".join("{}".format(element) for element in excluded_sectors_list[:])
    #print(empty_sectors)

    # preserve config sectors (do not write these blocks to preserve existing data)>
    c_excluded_sectors = (ctypes.c_uint16 * len(excluded_sectors_list))(*excluded_sectors_list)

    # excluded_sectors = {} #{124,125,126}  # 30,31}
    # c_excluded_sectors = (ctypes.c_uint16 * len(excluded_sectors))(*excluded_sectors)


    # Wait for input here. We can check parsed hex file
    r =  input("Continue y/n ?") or "y"
    if r == "n":
        lib.comp_intelhex_parser_freemem()
        quit()

    # Instead of sending parsed sectors manually for upgrade operation;
    # we transfer already parsed sectors to internal C buffers to proceed with the upgrade
    lib.comp_fwb_storage_LoadSectorsFromIntelParser_x86_64()


    #Ask for application keys
    # r"X:\hex_repo\masterkeys\A011.json.enc"
    enc_app_keys_file_path = prompt_and_update_config_option(CONST__CONFIG_SECTION_NAME_PARAMS, "{}_APP_KEYS_FILE".format(application_str),
                                                    "Application Keys için dosya yolunu belirtiniz (*.json.enc):", default_val=".json.enc")

    while(1):
        psw = fcrypt.prompt_pass(ask_confirmation=False)
        #print(psw)
        #psw = "test"
        decrypted_result = fcrypt.decrypt_file(f_encrypted_full_path=enc_app_keys_file_path,password=psw, output_file=False)
        if not decrypted_result == None:
            break

    json_result = json.loads(decrypted_result)
    keyMaster = (ctypes.c_uint32 * 4)()
    keyStatic = (ctypes.c_uint32 * 4)()
    keyFirstTime = (ctypes.c_uint32 * 4)()

    for i in range(4):
        keyMaster[i] = int(json_result["MasterKeys"][f"key%s" % str(i + 1)], 16)
        keyStatic[i] = int(json_result["StaticKeys"][f"key%s" % str(i + 1)], 16)
        keyFirstTime[i] = int(json_result["FirstTimeKeys"][f"key%s" % str(i + 1)], 16)

    # print(" ".join("0x{:08x}".format(element) for element in keyMaster[:]))
    # print(" ".join("0x{:08x}".format(element) for element in keyStatic[:]))
    # print(" ".join("0x{:08x}".format(element) for element in keyFirstTime[:]))

    # Ask for Firmware Information
    firmwareInfo = STRUCT_FIRMWARE_INFO()

    firmware_caption = prompt_and_update_config_option(CONST__CONFIG_SECTION_NAME_PARAMS, "{}_FIRMWARE_CAPTION".format(application_str),
                                                    "Firmware Caption:(stdMifare, stdProxB):", default_val="")


    firmwareInfo.caption = firmware_caption.encode('ascii')
    #firmwareInfo.caption = "UM 1.3R".encode('ascii')  # ctypes.c_char_p("TEST".encode('ascii'))

    firmware_version = prompt_and_update_config_option(CONST__CONFIG_SECTION_NAME_PARAMS, "{}_FIRMWARE_VERSION".format(application_str),
                                                    "Version No:", default_val="1")
    firmwareInfo.version = int(firmware_version)

    firmware_revision = prompt_and_update_config_option(CONST__CONFIG_SECTION_NAME_PARAMS, "{}_FIRMWARE_REVISION".format(application_str),
                                                    "Revision No:", default_val="0")
    firmwareInfo.revision = int(firmware_revision)

    firmware_build = prompt_and_update_config_option(CONST__CONFIG_SECTION_NAME_PARAMS, "{}_FIRMWARE_BUILD".format(application_str),
                                                    "Build No:", default_val="0")
    firmwareInfo.build = int(firmware_build)


    for item in pyfirmwaremandef.EnumFirmwareReleaseType:
        print("({}) {}".format(item.value,item.name))

    release_type = prompt_and_update_config_option(CONST__CONFIG_SECTION_NAME_PARAMS,"{}_FIRMWARE_RELEASE_TYPE".format(application_str),
                                                           "Fimrware Release Type:", default_val="BETA")

    firmwareInfo.releaseType = pyfirmwaremandef.EnumFirmwareReleaseType[release_type]


    firmware_dateYear = datetime.date.today().year
    firmware_dateMonth = datetime.date.today().month
    firmware_dateDay = datetime.date.today().day

    firmware_dateYear = prompt("Release Year:", default=str(firmware_dateYear), key_bindings=bindings)
    firmware_dateMonth = prompt("Release Month:", default=str(firmware_dateMonth), key_bindings=bindings)
    firmware_dateDay = prompt("Release Day:", default=str(firmware_dateDay), key_bindings=bindings)

    #firmware_dateYear = prompt_and_update_config_option(CONST__CONFIG_SECTION_NAME_PARAMS, "{}_FIRMWARE_DATEYEAR".format(application_str),
    #                                                "Year:", default_val=str(firmware_dateYear))


    firmwareInfo.dateYear = int(firmware_dateYear)
    firmwareInfo.dateMonth = int(firmware_dateMonth)
    firmwareInfo.dateDay = int(firmware_dateDay)
    #firmwareInfo.configId = 1  # // used to distinguish between different configurations of same firmware verison
    # For example for 9600bps; ConfigurationId can be 2;
    # 1 can be count as default configuration

    release_notes_entry = prompt_and_update_config_option(CONST__CONFIG_SECTION_NAME_PARAMS, "{}_FIRMWARE_RELEASE_NOTES".format(application_str),
                                                    "Release Notes(Use ; for new lines):", default_val=str("- Desc1;- Desc2"))

    release_notes = release_notes_entry.replace(";","\n")


    #release_notes = "- Improved RF Stability \n" \
    #                "- Faster start-up\n"

    #release_notes = "test"


    # config sectors (do not include this sectors on checksum calculation) >
    #checksum_excluded_sectors = {30, 31}
    c_checksum_excluded_sectors = (ctypes.c_uint16 * len(checksum_excluded_sectors))(*checksum_excluded_sectors)

    checksum_excluded_sectors_str = ", ".join("{}".format(element) for element in c_checksum_excluded_sectors[:])
    print("Checksum Excluded Sectors:",checksum_excluded_sectors_str)

    excluded_sectors_str = ", ".join("{}".format(element) for element in excluded_sectors_list[:])
    print("Excluded Sectors from writing:",excluded_sectors_str)


    # Wait for input here. We can Excluded Sectors
    r =  input("Continue y/n ?") or "y"
    if r == "n":
        lib.bsp_fwb_freemem()
        quit()

    # Create Upgrade script
    # argtypes ta pointer oldugu belirtilirse, api cagirirken byref yapmadan da calisiyor
    # argtypes belirtilmezse targetDeviceInfo byref(targetDeviceInfo) ile gondermemiz gerekir.
    # lib.comp_fwb_create_upgrade_script.argtypes = (c_uint32*4, c_uint32*4,c_uint32*4,ctypes.POINTER(STRUCT_TARGET_DEVICE_INFO))
    # lib.comp_fwb_create_upgrade_script(keyStatic, keyFirstTime, keyMaster,targetDeviceInfo)

    lib.bsp_fwb_create_upgrade_script_x86_64(keyStatic, keyFirstTime, keyMaster, ctypes.byref(targetDeviceInfo),
                                             ctypes.byref(firmwareInfo), ctypes.c_char_p(release_notes.encode("ascii")),
                                             c_excluded_sectors, len(c_excluded_sectors), c_checksum_excluded_sectors,
                                             len(c_checksum_excluded_sectors))

    # Get simplified Script Output and print it.
    # here we can save the ouput.
    simple_script_out = lib.bsp_fwb_GetSimpleScriptOutput()
    print("\r\n") # C api write checksum information to the log and enter charactwer is missing.
    #print(ctypes.c_char_p(simple_script_out).value.decode("ascii",errors='ignore'))
    f_simple_script_name = f.name
    f_simple_script_name = f_simple_script_name.replace(".hex", ".txt")
    f_simple_script_file = open(f_simple_script_name, "w")
    f_simple_script_file.write(ctypes.c_char_p(simple_script_out).value.decode("ascii", errors='ignore'))
    f_simple_script_file.close()
    print("Simplified output is written to {}".format(f_simple_script_name))

    xml_script_out = lib.bsp_fwb_GetXmlScriptOutput()
    # print(ctypes.c_char_p(xml_script_out).value.decode("ascii",errors='ignore'))

    f_xml_name = f.name
    f_xml_name = f_xml_name.replace(".hex", ".xml")
    f_xml = open(f_xml_name, "w")
    f_xml.write(ctypes.c_char_p(xml_script_out).value.decode("ascii", errors='ignore'))
    f_xml.close()
    print("Xml output is written to {}".format(f_xml_name))

    # Free memory created on heap by the internal C api.
    lib.bsp_fwb_freemem()


menu()