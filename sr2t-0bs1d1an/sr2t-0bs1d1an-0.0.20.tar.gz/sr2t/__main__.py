#!/usr/bin/env python3

""" sr2t """

import argparse
import json
import xml.etree.ElementTree as ET
import zipfile
import sr2t.parsers.dirble
import sr2t.parsers.fortify
import sr2t.parsers.nessus
import sr2t.parsers.nikto
import sr2t.parsers.nmap
import sr2t.parsers.testssl
import xlsxwriter
# from pprint import pprint


def get_args():
    """ Get arguments """

    parser = argparse.ArgumentParser(
        description='Converting scanning reports to a tabular format')
    input_group = parser.add_argument_group('specify at least one')
    input_group.add_argument(
        '--nessus', type=argparse.FileType('r'), nargs='+',
        help='Specify (multiple) Nessus XML files.')
    input_group.add_argument(
        '--nmap', type=argparse.FileType('r'), nargs='+',
        help='Specify (multiple) Nmap XML files.')
    input_group.add_argument(
        '--nikto', type=argparse.FileType('r'), nargs='+',
        help='Specify (multiple) Nikto XML files.')
    input_group.add_argument(
        '--dirble', type=argparse.FileType('r'), nargs='+',
        help='Specify (multiple) Dirble XML files.')
    input_group.add_argument(
        '--testssl', type=argparse.FileType('r'), nargs='+',
        help='Specify (multiple) Testssl JSON files.')
    input_group.add_argument(
        '--fortify', type=argparse.FileType('r'), nargs='+',
        help='Specify (multiple) HP Fortify FPR files.')
    parser.add_argument(
        '--nmap-state', default="open",
        help='Specify the desired state to filter (e.g. open|filtered).')
    parser.add_argument(
        '--nmap-services', default='store_false', action='store_true',
        help='Specify to ouput a supplemental list of detected services.')
    parser.add_argument(
        '--no-nessus-autoclassify', default='store_true', action='store_false',
        dest='nessus_autoclassify', help='Specify to not autoclassify ' +
        'Nessus results.')
    parser.add_argument(
        '--nessus-autoclassify-file', type=argparse.FileType('r'),
        help='Specify to override a custom Nessus autoclassify YAML file.')
    parser.add_argument(
        '--nessus-tls-file', type=argparse.FileType('r'),
        help='Specify to override a custom Nessus TLS findings YAML file.')
    parser.add_argument(
        '--nessus-x509-file', type=argparse.FileType('r'),
        help='Specify to override a custom Nessus X.509 findings YAML file.')
    parser.add_argument(
        '--nessus-http-file', type=argparse.FileType('r'),
        help='Specify to override a custom Nessus HTTP findings YAML file.')
    parser.add_argument(
        '--nessus-smb-file', type=argparse.FileType('r'),
        help='Specify to override a custom Nessus SMB findings YAML file.')
    parser.add_argument(
        '--nessus-rdp-file', type=argparse.FileType('r'),
        help='Specify to override a custom Nessus RDP findings YAML file.')
    parser.add_argument(
        '--nessus-ssh-file', type=argparse.FileType('r'),
        help='Specify to override a custom Nessus SSH findings YAML file.')
    parser.add_argument(
        '--nessus-min-severity', default=0, type=int,
        help='Specify the minimum severity to output (e.g. 1).')
    parser.add_argument(
        '--nessus-plugin-name-width', default=80, type=int,
        help='Specify the width of the pluginid column (e.g. 30).')
    parser.add_argument(
        '--nessus-sort-by', default='plugin-id',
        help='Specify to sort output by ip-address, port, plugin-id, ' +
        'plugin-name or severity.')
    parser.add_argument(
        '--nikto-description-width', default=80, type=int,
        help='Specify the width of the description column (e.g. 30).')
    parser.add_argument(
        '--fortify-details', action='store_true',
        help='Specify to include the Fortify abstracts, explanations and ' +
        'recommendations for each vulnerability.')
    parser.add_argument(
        '--annotation-width', default=1, type=int,
        help='Specify the width of the annotation column (e.g. 30).')
    parser.add_argument(
        '-oC', '--output-csv',
        help='Specify the output CSV basename (e.g. output).')
    parser.add_argument(
        '-oT', '--output-txt',
        help='Specify the output TXT file (e.g. output.txt).')
    parser.add_argument(
        '-oX', '--output-xlsx',
        help='Specify the output XLSX file (e.g. output.xlsx). Only for ' +
        'Nessus at the moment')
    parser.add_argument(
        '-oA', '--output-all',
        help='Specify the output basename to output to all formats (e.g. ' +
        'output).')

    args = parser.parse_args()
    if not args.nessus and not args.nmap and not args.nikto and not \
            args.dirble and not args.testssl and not args.fortify:
        parser.error(
            'at least one of the arguments --nessus --nmap --nikto --dirble' +
            '--testssl --fortify is required')

    return parser.parse_args()


def main():
    """ Main function """

    args = get_args()

    data_nessus = []
    data_nikto = []
    data_dirble = []
    data_testssl = []
    data_fortify = []

    # needs to be known before eval
    nessus_portscan_table = ''
    nessus_tlsscan_table = ''

    if args.output_all:
        args.output_csv = args.output_all
        args.output_txt = args.output_all + ".txt"
        args.output_xlsx = args.output_all + ".xlsx"

    if args.output_xlsx:
        workbook = xlsxwriter.Workbook(
            args.output_xlsx, {'strings_to_urls': False})
    else:
        workbook = False

    if args.nessus:
        root = []
        for file in args.nessus:
            root.append(ET.parse(file).getroot())
        my_nessus_table, nessus_portscan_table, nessus_tlsscan_table, \
            nessus_x509scan_table, nessus_httpscan_table, \
            nessus_smbscan_table, nessus_rdpscan_table, nessus_sshscan_table, \
            csv_array, header, workbook = sr2t.parsers.nessus.nessus_parser(
                args, root, data_nessus, workbook)
    if args.nmap:
        root = []
        for file in args.nmap:
            root.append(ET.parse(file).getroot())
        my_nmap_tcp_table, my_nmap_udp_table, my_nmap_services_table, \
            workbook = sr2t.parsers.nmap.nmap_parser(
                args, root, workbook)
    if args.nikto:
        root = []
        for file in args.nikto:
            root.append(ET.parse(file).getroot())
        my_nikto_table, csv_array, header, workbook = \
            sr2t.parsers.nikto.nikto_parser(
                args, root, data_nikto, workbook)
    if args.dirble:
        root = []
        for file in args.dirble:
            root.append(ET.parse(file).getroot())
        my_dirble_table, csv_array, header, workbook = \
            sr2t.parsers.dirble.dirble_parser(
                args, root, data_dirble, workbook)
    if args.testssl:
        root = []
        for file in args.testssl:
            root.append(json.load(file))
        my_testssl_table, workbook = \
            sr2t.parsers.testssl.testssl_parser(
                args, root, data_testssl, workbook)
    if args.fortify:
        root = []
        for fprfile in args.fortify:
            zfpr = zipfile.ZipFile(fprfile.name)
            fvdl = zfpr.open('audit.fvdl')
            root.append(ET.parse(fvdl).getroot())
        my_fortify_table, csv_array, header, workbook = \
            sr2t.parsers.fortify.fortify_parser(
                args, root, data_fortify, workbook)

    if args.output_txt:
        with open(args.output_txt, 'w') as txtfile:
            if args.nessus:
                print(my_nessus_table, file=txtfile)
                if nessus_portscan_table:
                    print("Nessus SYN scan table:")
                    print(nessus_portscan_table, "\n", file=txtfile)
                if nessus_tlsscan_table:
                    print("Nessus TLS table:")
                    print(nessus_tlsscan_table, "\n", file=txtfile)
                if nessus_x509scan_table:
                    print("Nessus X.509 table")
                    print(nessus_x509scan_table, "\n", file=txtfile)
                if nessus_httpscan_table:
                    print("Nessus HTTP table:")
                    print(nessus_httpscan_table, "\n", file=txtfile)
                if nessus_smbscan_table:
                    print("Nessus SMB table:")
                    print(nessus_smbscan_table, "\n", file=txtfile)
                if nessus_rdpscan_table:
                    print("Nessus RDP table:")
                    print(nessus_rdpscan_table, "\n", file=txtfile)
                if nessus_sshscan_table:
                    print("Nessus SSH table:")
                    print(nessus_rdpscan_table, "\n", file=txtfile)
            if args.nmap:
                if my_nmap_tcp_table:
                    print("Nmap TCP:")
                    print(my_nmap_tcp_table, "\n", file=txtfile)
                if my_nmap_udp_table:
                    print("Nmap UDP:")
                    print(my_nmap_udp_table, "\n", file=txtfile)
                if my_nmap_services_table and args.nmap_services == 1:
                    print("Nmap Services:")
                    print(my_nmap_services_table, "\n", file=txtfile)
            if args.nitko:
                print(my_nikto_table, "\n", file=txtfile)
            if args.dirble:
                print(my_dirble_table, "\n", file=txtfile)
            if args.testssl:
                print(my_testssl_table, "\n", file=txtfile)
            if args.fortify:
                print(my_fortify_table, "\n", file=txtfile)

    if not args.output_csv and not args.output_txt and not args.output_xlsx \
       and not args.output_all:
        if args.nessus:
            print(my_nessus_table)
            if nessus_portscan_table:
                print("Nessus SYN scan table:")
                print(nessus_portscan_table, "\n")
            if nessus_tlsscan_table:
                print("Nessus TLS table:")
                print(nessus_tlsscan_table, "\n")
            if nessus_x509scan_table:
                print("Nessus X.509 table")
                print(nessus_x509scan_table, "\n")
            if nessus_httpscan_table:
                print("Nessus HTTP table:")
                print(nessus_httpscan_table, "\n")
            if nessus_smbscan_table:
                print("Nessus SMB table:")
                print(nessus_smbscan_table, "\n")
            if nessus_rdpscan_table:
                print("Nessus RDP table:")
                print(nessus_rdpscan_table, "\n")
            if nessus_sshscan_table:
                print("Nessus SSH table:")
                print(nessus_rdpscan_table, "\n")
        if args.nmap:
            if my_nmap_tcp_table:
                print("Nmap TCP:")
                print(my_nmap_tcp_table, "\n")
            if my_nmap_udp_table:
                print("Nmap UDP:")
                print(my_nmap_udp_table, "\n")
            if my_nmap_services_table and args.nmap_services == 1:
                print("Nmap Services:")
                print(my_nmap_services_table, "\n")
        if args.nikto:
            print(my_nikto_table, "\n")
        if args.dirble:
            print(my_dirble_table, "\n")
        if args.testssl:
            print(my_testssl_table, "\n")
        if args.fortify:
            print(my_fortify_table, "\n")

    if args.output_xlsx:
        workbook.close()


if __name__ == '__main__':
    main()
