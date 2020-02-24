"""
This file converts .xml upgrade file to the smt file (smtester file format)
"""
# X:\hex_repo\A011\upgrade\2-stdMifareV201_AUTO-B-P_Baud19200.xml A0115210

import os
import click
import ctypes
import pathlib
import xml.etree.ElementTree as ET


# Klasör de space varsa tırnak işareti içinde girebiliriz.
# python makebin_upgrade.py "X:\AYEDEK\Software Projects\pysmtesterutils\pysmtesterutils\repo\A092\upgrade\B16V1_0_2Beta_RADF94.xml" A0920000
# python makebin_upgrade.py x:\hex_repo\A092\upgrade\B16V1_0_1Beta_RADF94.xml A0920000


#python makebin_upgrade.py x:\hex_repo\A011\upgrade\1-stdMifareV201_STD-B-P_Baud19200.xml A0115210


@click.command()
@click.argument('xml_file_name')
@click.argument('device_family')
def makebin_upgrade(xml_file_name, device_family):

    #Check if ile exist
    if not os.path.exists(xml_file_name):
        # click.echo(click.style(f"File not found", fg='red'))
        click.echo(click.style(f"File not found {xml_file_name}", fg='bright_red'))
        # print_formatted_text(HTML("<ansired>File not found</ansired>"))
        return


    f_dir = pathlib.Path(xml_file_name).parent
    f_extensions = pathlib.Path(xml_file_name).suffixes
    f_ext = "".join(f_extensions)
    if (f_ext != ".xml"):
        click.echo(click.style(f"Expected .json.enc file", fg='red'))
        #print_formatted_text(HTML("<ansired>Expected .hex.smt file</ansired>"))
        return False

    # Remove all extensions
    f_name_wo_extension = xml_file_name
    for i in range(len(f_extensions)):
        f_name_wo_extension = pathlib.Path(f_name_wo_extension).stem

    # Add extensions
    # f_ext = "".join(f_extensions)
    # pure_f_name = f_name_wo_extension + f_ext

    xml_bin_file_path = str(f_dir) + "\\" + f_name_wo_extension + ".xml.bin"

    root = ET.parse(xml_file_name).getroot()

    binary_upgrade_ba = bytearray()
    # First 4 byte will hold device family infortmation(so application ID) insizde the created bin file
    # so that when upgrading first time, we get device family information( as we need it for first time upgrade) from upgrade bin file.
    device_family_bytes = int(device_family, 16).to_bytes(4, "little")
    binary_upgrade_ba.extend(device_family_bytes)

    for tcommand_tags in root.findall('TCommand'):

        # CMDDesc Not used
        cmd_desc_tag = tcommand_tags[0]

        # CMD
        # Append number(hex)
        cmd_tag = tcommand_tags[1]
        binary_upgrade_ba.append(int(cmd_tag.text, 16))

        # CMDEXC
        # Extend byte array
        cmd_exc_tag = tcommand_tags[2]
        binary_upgrade_ba.extend(bytes.fromhex(cmd_exc_tag.text))


        # PARLN
        # Append number(int) - Not hexadecimal i.e. 524 (524 bytes)
        # LSB First
        parln_tag = tcommand_tags[3]
        parln_tag_value = int(parln_tag.text)
        parln_tag_value_lsb = (parln_tag_value & 0xFF)
        parln_tag_value_msb = (parln_tag_value >> 8)

        binary_upgrade_ba.append(parln_tag_value_lsb)
        binary_upgrade_ba.append(parln_tag_value_msb)


        # PAR
        # Extend byte array
        par_tag = tcommand_tags[4]
        binary_upgrade_ba.extend(bytes.fromhex(par_tag.text))



    f = open(xml_bin_file_path, "wb")
    f.write(binary_upgrade_ba)
    f.close()

    print("Upgrade file is converted to bin. \r\n{}  \r\nTotal {} bytes".format(xml_bin_file_path, len(binary_upgrade_ba)))


if __name__ == '__main__':
    makebin_upgrade()



""""
    for tcommand_tags in root.findall('TCommand'):
         for child in tcommand_tags:
           print(child.tag) #child.attrib
           print(child.text)
"""



