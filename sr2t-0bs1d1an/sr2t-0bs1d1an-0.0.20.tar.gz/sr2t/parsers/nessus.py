#!/usr/bin/env python3

""" sr2t Nessus parser"""

import csv
import os
import pkg_resources
import textwrap
import yaml
from prettytable import PrettyTable
# from pprint import pprint


def nessus_portscan_loopy(var1, reporthost, var2):
    """ Specific Nessus loop to add N open ports to the same address """

    for reportitem in reporthost.findall('ReportItem'):
        if reportitem.get('pluginName') == "Nessus SYN scanner":
            if var1 == "addr":
                var2.append(reporthost.get('name'))
            elif var1 == "port":
                var2.append(reportitem.get('port'))


def nessus_tlsscan_loopy(var1, reporthost, tls_obs, var2):
    """ Specific Nessus loop to afind all SSL / TLS related issues """

    for reportitem in reporthost.findall('ReportItem'):
        if int(reportitem.get('pluginID')) in tls_obs.keys():
            if var1 == "addr":
                var2.append(
                    reporthost.get('name') + ":" + reportitem.get('port'))
            elif var1 == "obs":
                var2.append(tls_obs.get(int(reportitem.get('pluginID'))))


def nessus_x509scan_loopy(var1, reporthost, x509_obs, var2):
    """ Specific Nessus loop to find all X.509 certificate issues """

    for reportitem in reporthost.findall('ReportItem'):
        if int(reportitem.get('pluginID')) in x509_obs.keys():
            if var1 == "addr":
                var2.append(
                    reporthost.get('name') + ":" + reportitem.get('port'))
            elif var1 == "obs":
                var2.append(x509_obs.get(int(reportitem.get('pluginID'))))


def nessus_httpscan_loopy(var1, reporthost, http_obs, var2):
    """ Specific Nessus loop to find all HTTP response header issues """

    for reportitem in reporthost.findall('ReportItem'):
        if int(reportitem.get('pluginID')) in http_obs.keys():
            if var1 == "addr":
                var2.append(
                    reporthost.get('name') + ":" + reportitem.get('port'))
            elif var1 == "obs":
                var2.append(http_obs.get(int(reportitem.get('pluginID'))))


def nessus_smbscan_loopy(var1, reporthost, smb_obs, var2):
    """ Specific Nessus loop to find all SMB issues """

    for reportitem in reporthost.findall('ReportItem'):
        if int(reportitem.get('pluginID')) in smb_obs.keys():
            if var1 == "addr":
                var2.append(
                    reporthost.get('name') + ":" + reportitem.get('port'))
            elif var1 == "obs":
                var2.append(smb_obs.get(int(reportitem.get('pluginID'))))


def nessus_rdpscan_loopy(var1, reporthost, rdp_obs, var2):
    """ Specific Nessus loop to find all RDP issues """

    for reportitem in reporthost.findall('ReportItem'):
        if int(reportitem.get('pluginID')) in rdp_obs.keys():
            if var1 == "addr":
                var2.append(
                    reporthost.get('name') + ":" + reportitem.get('port'))
            elif var1 == "obs":
                var2.append(rdp_obs.get(int(reportitem.get('pluginID'))))


def nessus_sshscan_loopy(var1, reporthost, ssh_obs, var2):
    """ Specific Nessus loop to find all SSH issues """

    for reportitem in reporthost.findall('ReportItem'):
        if int(reportitem.get('pluginID')) in ssh_obs.keys():
            if var1 == "addr":
                var2.append(
                    reporthost.get('name') + ":" + reportitem.get('port'))
            elif var1 == "obs":
                var2.append(ssh_obs.get(int(reportitem.get('pluginID'))))


def nessus_parser(args, root, data_nessus, workbook):
    """ Nessus parser """

    if not args.nessus_autoclassify_file:
        autoclassify_file = pkg_resources.resource_string(
            __name__, '../data/nessus_autoclassify.yaml')
    if args.nessus_autoclassify_file:
        autoclassify_file = args.nessus_autoclassify_file
    autoclassify = yaml.load(autoclassify_file, Loader=yaml.FullLoader)

    if not args.nessus_tls_file:
        tls_file = pkg_resources.resource_string(
            __name__, '../data/nessus_tls.yaml')
    if args.nessus_tls_file:
        tls_file = args.nessus_tls_file
    tls_obs = yaml.load(tls_file, Loader=yaml.FullLoader)

    if not args.nessus_x509_file:
        x509_file = pkg_resources.resource_string(
            __name__, '../data/nessus_x509.yaml')
    if args.nessus_x509_file:
        x509_file = args.nessus_x509_file
    x509_obs = yaml.load(x509_file, Loader=yaml.FullLoader)

    if not args.nessus_http_file:
        http_file = pkg_resources.resource_string(
            __name__, '../data/nessus_http.yaml')
    if args.nessus_http_file:
        http_file = args.nessus_http_file
    http_obs = yaml.load(http_file, Loader=yaml.FullLoader)

    if not args.nessus_smb_file:
        smb_file = pkg_resources.resource_string(
            __name__, '../data/nessus_smb.yaml')
    if args.nessus_smb_file:
        smb_file = args.nessus_smb_file
    smb_obs = yaml.load(smb_file, Loader=yaml.FullLoader)

    if not args.nessus_rdp_file:
        rdp_file = pkg_resources.resource_string(
            __name__, '../data/nessus_rdp.yaml')
    if args.nessus_rdp_file:
        rdp_file = args.nessus_rdp_file
    rdp_obs = yaml.load(rdp_file, Loader=yaml.FullLoader)

    if not args.nessus_ssh_file:
        ssh_file = pkg_resources.resource_string(
            __name__, '../data/nessus_ssh.yaml')
    if args.nessus_ssh_file:
        ssh_file = args.nessus_ssh_file
    ssh_obs = yaml.load(ssh_file, Loader=yaml.FullLoader)

    portscan = []
    tlsscan = []
    x509scan = []
    httpscan = []
    smbscan = []
    rdpscan = []
    sshscan = []

    for element in root:
        for reporthost in element.findall('Report/ReportHost'):
            for reportitem in reporthost.findall('ReportItem'):
                if int(reportitem.get('severity')) >= args.nessus_min_severity:
                    data_nessus.append([
                        reporthost.get('name'),
                        reportitem.get('port'),
                        reportitem.get('pluginID'),
                        textwrap.fill(
                            reportitem.get('pluginName'),
                            width=args.nessus_plugin_name_width),
                        reportitem.findtext('plugin_output'),
                        reportitem.get('severity')
                    ])

            portscan_addr = []
            portscan_port = []
            nessus_portscan_loopy("addr", reporthost, portscan_addr)
            nessus_portscan_loopy("port", reporthost, portscan_port)
            if portscan_addr:
                portscan.append([portscan_addr[0], portscan_port])

            tlsscan_addr = []
            tlsscan_obs = []
            nessus_tlsscan_loopy("addr", reporthost, tls_obs, tlsscan_addr)
            nessus_tlsscan_loopy("obs", reporthost, tls_obs, tlsscan_obs)
            if tlsscan_addr:
                tlsscan.append([tlsscan_addr[0], tlsscan_obs])

            x509scan_addr = []
            x509scan_obs = []
            nessus_x509scan_loopy("addr", reporthost, x509_obs, x509scan_addr)
            nessus_x509scan_loopy("obs", reporthost, x509_obs, x509scan_obs)
            if x509scan_addr:
                x509scan.append([x509scan_addr[0], x509scan_obs])

            httpscan_addr = []
            httpscan_obs = []
            nessus_httpscan_loopy("addr", reporthost, http_obs, httpscan_addr)
            nessus_httpscan_loopy("obs", reporthost, http_obs, httpscan_obs)
            if httpscan_addr:
                httpscan.append([httpscan_addr[0], httpscan_obs])

            smbscan_addr = []
            smbscan_obs = []
            nessus_smbscan_loopy("addr", reporthost, smb_obs, smbscan_addr)
            nessus_smbscan_loopy("obs", reporthost, smb_obs, smbscan_obs)
            if smbscan_addr:
                smbscan.append([smbscan_addr[0], smbscan_obs])

            rdpscan_addr = []
            rdpscan_obs = []
            nessus_rdpscan_loopy("addr", reporthost, rdp_obs, rdpscan_addr)
            nessus_rdpscan_loopy("obs", reporthost, rdp_obs, rdpscan_obs)
            if rdpscan_addr:
                rdpscan.append([rdpscan_addr[0], rdpscan_obs])

            sshscan_addr = []
            sshscan_obs = []
            nessus_sshscan_loopy("addr", reporthost, ssh_obs, sshscan_addr)
            nessus_sshscan_loopy("obs", reporthost, ssh_obs, sshscan_obs)
            if sshscan_addr:
                sshscan.append([sshscan_addr[0], sshscan_obs])

    my_nessus_table = PrettyTable()
    csv_array = []
    header = ['host', 'port', 'plugin id', 'plugin name']
    header.extend(['plugin output'])
    header.extend(['severity'])
    header.extend(['annotations'.ljust(args.annotation_width)])
    my_nessus_table.field_names = header
    my_nessus_table.align["host"] = "l"
    my_nessus_table.align["port"] = "l"
    my_nessus_table.align["plugin id"] = "l"
    my_nessus_table.align["plugin name"] = "l"
    my_nessus_table.align["plugin output"] = "l"
    my_nessus_table.align["annotations"] = "l"

    def sortf(data_nessus):
        """ Sort function """
        if args.nessus_sort_by == 'ip-address':
            sorted_result = sorted(data_nessus, key=lambda x: x[0])
        elif args.nessus_sort_by == 'port':
            sorted_result = sorted(data_nessus, key=lambda x: x[1])
        elif args.nessus_sort_by == 'plugin-id':
            sorted_result = sorted(data_nessus, key=lambda x: x[2])
        elif args.nessus_sort_by == 'plugin-name':
            sorted_result = sorted(data_nessus, key=lambda x: x[3])
        elif args.nessus_sort_by == 'severity':
            sorted_result = sorted(
                data_nessus, key=lambda x: x[4], reverse=True)
        return sorted_result

    for (host, port, plugin_id, plugin_name, severity,
         plugin_output) in sortf(data_nessus):
        row = [host, port, plugin_id, plugin_name, severity]
        row.extend([plugin_output])
        if int(plugin_id) in autoclassify.keys():
            for key, value in autoclassify[int(plugin_id)].items():
                if key == "stdobs_title":
                    row.extend([value])
        else:
            row.extend(['X'])
        my_nessus_table.add_row(row)
        csv_array.append(row)

    ports = sorted(
        set([int(port) for _, open_ports in portscan for port in open_ports])
    )

    tls_observations = sorted(
        set([obs for _, all_obs in tlsscan for obs in all_obs])
    )

    x509_observations = sorted(
        set([obs for _, all_obs in x509scan for obs in all_obs])
    )

    http_observations = sorted(
        set([obs for _, all_obs in httpscan for obs in all_obs])
    )

    smb_observations = sorted(
        set([obs for _, all_obs in smbscan for obs in all_obs])
    )

    rdp_observations = sorted(
        set([obs for _, all_obs in rdpscan for obs in all_obs])
    )

    ssh_observations = sorted(
        set([obs for _, all_obs in sshscan for obs in all_obs])
    )

    nessus_portscan_table = PrettyTable()
    portscan_csv_array = []
    portscan_header = ['ip address', ]
    portscan_header.extend(ports)
    nessus_portscan_table.field_names = portscan_header
    for ip_address, open_ports in portscan:
        row = [ip_address]
        row.extend('X' if str(port) in open_ports else '' for port in ports)
        nessus_portscan_table.add_row(row)
        portscan_csv_array.append(row)
    nessus_portscan_table.align["ip address"] = "l"

    nessus_tlsscan_table = PrettyTable()
    tlsscan_csv_array = []
    tlsscan_header = ['ip address', ]
    tlsscan_header.extend(tls_observations)
    nessus_tlsscan_table.field_names = tlsscan_header
    for ip_address, all_obs in tlsscan:
        row = [ip_address]
        row.extend(
            'X' if str(obs) in all_obs else '' for obs in tls_observations)
        nessus_tlsscan_table.add_row(row)
        tlsscan_csv_array.append(row)
    nessus_tlsscan_table.align["ip address"] = "l"

    nessus_x509scan_table = PrettyTable()
    x509scan_csv_array = []
    x509scan_header = ['ip address', ]
    x509scan_header.extend(x509_observations)
    nessus_x509scan_table.field_names = x509scan_header
    for ip_address, all_obs in x509scan:
        row = [ip_address]
        row.extend(
            'X' if str(obs) in all_obs else '' for obs in x509_observations)
        nessus_x509scan_table.add_row(row)
        x509scan_csv_array.append(row)
    nessus_x509scan_table.align["ip address"] = "l"

    nessus_httpscan_table = PrettyTable()
    httpscan_csv_array = []
    httpscan_header = ['ip address', ]
    httpscan_header.extend(http_observations)
    nessus_httpscan_table.field_names = httpscan_header
    for ip_address, all_obs in httpscan:
        row = [ip_address]
        row.extend(
            'X' if str(obs) in all_obs else '' for obs in http_observations)
        nessus_httpscan_table.add_row(row)
        httpscan_csv_array.append(row)
    nessus_httpscan_table.align["ip address"] = "l"

    nessus_smbscan_table = PrettyTable()
    smbscan_csv_array = []
    smbscan_header = ['ip address', ]
    smbscan_header.extend(smb_observations)
    nessus_smbscan_table.field_names = smbscan_header
    for ip_address, all_obs in smbscan:
        row = [ip_address]
        row.extend(
            'X' if str(obs) in all_obs else '' for obs in smb_observations)
        nessus_smbscan_table.add_row(row)
        smbscan_csv_array.append(row)
    nessus_smbscan_table.align["ip address"] = "l"

    nessus_rdpscan_table = PrettyTable()
    rdpscan_csv_array = []
    rdpscan_header = ['ip address', ]
    rdpscan_header.extend(rdp_observations)
    nessus_rdpscan_table.field_names = rdpscan_header
    for ip_address, all_obs in rdpscan:
        row = [ip_address]
        row.extend(
            'X' if str(obs) in all_obs else '' for obs in rdp_observations)
        nessus_rdpscan_table.add_row(row)
        rdpscan_csv_array.append(row)
    nessus_rdpscan_table.align["ip address"] = "l"

    nessus_sshscan_table = PrettyTable()
    sshscan_csv_array = []
    sshscan_header = ['ip address', ]
    sshscan_header.extend(ssh_observations)
    nessus_sshscan_table.field_names = sshscan_header
    for ip_address, all_obs in sshscan:
        row = [ip_address]
        row.extend(
            'X' if str(obs) in all_obs else '' for obs in ssh_observations)
        nessus_sshscan_table.add_row(row)
        sshscan_csv_array.append(row)
    nessus_sshscan_table.align["ip address"] = "l"

    if args.output_csv:
        with open(
            os.path.splitext(args.output_csv)[0] + "_nessus.csv", 'w'
        ) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(header)
            for row in csv_array:
                csvwriter.writerow(row)
        with open(
            os.path.splitext(args.output_csv)[0] + "_nessus_portscan.csv", 'w'
        ) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([''] + ports)
            for row in portscan_csv_array:
                csvwriter.writerow(row)
        with open(
            os.path.splitext(args.output_csv)[0] + "_nessus_tls.csv", 'w'
        ) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([''] + ports)
            for row in tlsscan_csv_array:
                csvwriter.writerow(row)
        with open(
            os.path.splitext(args.output_csv)[0] + "_nessus_x509.csv", 'w'
        ) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([''] + ports)
            for row in x509scan_csv_array:
                csvwriter.writerow(row)
        with open(
            os.path.splitext(args.output_csv)[0] + "_nessus_http.csv", 'w'
        ) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([''] + ports)
            for row in httpscan_csv_array:
                csvwriter.writerow(row)
        with open(
            os.path.splitext(args.output_csv)[0] + "_nessus_smb.csv", 'w'
        ) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([''] + ports)
            for row in smbscan_csv_array:
                csvwriter.writerow(row)
        with open(
            os.path.splitext(args.output_csv)[0] + "_nessus_rdp.csv", 'w'
        ) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([''] + ports)
            for row in rdpscan_csv_array:
                csvwriter.writerow(row)
        with open(
            os.path.splitext(args.output_csv)[0] + "_nessus_ssh.csv", 'w'
        ) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([''] + ports)
            for row in sshscan_csv_array:
                csvwriter.writerow(row)

    if args.output_xlsx:

        # Defining cell formats
        bold = workbook.add_format({'bold': True})
        bold.set_text_wrap()
        wrap = workbook.add_format()
        wrap.set_text_wrap()
        bad_cell = workbook.add_format()
        bad_cell.set_text_wrap()
        bad_cell.set_bg_color('#c00000')
        bad_cell.set_font_color('#ffffff')
        good_cell = workbook.add_format()
        good_cell.set_text_wrap()
        good_cell.set_bg_color('#046a38')
        good_cell.set_font_color('#ffffff')
        tls_bad_cell = workbook.add_format()

        # Dunno why this one doesn't work >:c
        tls_bad_cell.set_align('center')

        tls_bad_cell.set_bg_color('#c00000')
        tls_bad_cell.set_font_color('#ffffff')
        tls_bad_cell.set_border(1)
        tls_bad_cell.set_border_color('#ffffff')
        tls_good_cell = workbook.add_format()

        # Dunno why this one doesn't work >:c
        tls_good_cell.set_align('center')

        tls_good_cell.set_bg_color('#046a38')
        tls_good_cell.set_font_color('#ffffff')
        tls_good_cell.set_border(1)
        tls_good_cell.set_border_color('#ffffff')

        # Create all worksheets
        worksheet_summary = workbook.add_worksheet('Summary')
        worksheet_summary.write_rich_string(0, 0, bold, 'Summary')
        worksheet_critical = workbook.add_worksheet('Critical')
        worksheet_critical.set_tab_color('red')
        worksheet_high = workbook.add_worksheet('High')
        worksheet_high.set_tab_color('orange')
        worksheet_medium = workbook.add_worksheet('Medium')
        worksheet_medium.set_tab_color('yellow')
        worksheet_low = workbook.add_worksheet('Low')
        worksheet_low.set_tab_color('green')
        worksheet_info = workbook.add_worksheet('Info')
        worksheet_info.set_tab_color('blue')
        worksheet_portscan = workbook.add_worksheet('SYN')
        worksheet_portscan.set_tab_color('black')
        worksheet_portscan.set_column(0, 0, 15)
        worksheet_portscan.write_row(0, 0, portscan_header)

        if tlsscan_csv_array:
            worksheet_tlsscan = workbook.add_worksheet('TLS')
            worksheet_tlsscan.set_tab_color('black')
            worksheet_tlsscan.set_column(0, 0, 20)
            worksheet_tlsscan.write_row(0, 0, tlsscan_header)

        if x509scan_csv_array:
            worksheet_x509scan = workbook.add_worksheet('X.509')
            worksheet_x509scan.set_tab_color('black')
            worksheet_x509scan.set_column(0, 0, 20)
            worksheet_x509scan.write_row(0, 0, x509scan_header)

        if httpscan_csv_array:
            worksheet_httpscan = workbook.add_worksheet('HTTP')
            worksheet_httpscan.set_tab_color('black')
            worksheet_httpscan.set_column(0, 0, 20)
            worksheet_httpscan.write_row(0, 0, httpscan_header)

        if smbscan_csv_array:
            worksheet_smbscan = workbook.add_worksheet('SMB')
            worksheet_smbscan.set_tab_color('black')
            worksheet_smbscan.set_column(0, 0, 20)
            worksheet_smbscan.write_row(0, 0, smbscan_header)

        if rdpscan_csv_array:
            worksheet_rdpscan = workbook.add_worksheet('RDP')
            worksheet_rdpscan.set_tab_color('black')
            worksheet_rdpscan.set_column(0, 0, 20)
            worksheet_rdpscan.write_row(0, 0, rdpscan_header)

        if sshscan_csv_array:
            worksheet_sshscan = workbook.add_worksheet('SSH')
            worksheet_sshscan.set_tab_color('black')
            worksheet_sshscan.set_column(0, 0, 20)
            worksheet_sshscan.write_row(0, 0, sshscan_header)

        # Set colums and row sizes for the observation worksheets
        observation_worksheets = [
            worksheet_critical,
            worksheet_high,
            worksheet_medium,
            worksheet_low,
            worksheet_info]
        for worksheet_select in observation_worksheets:
            worksheet_select.set_column(0, 0, 15)
            worksheet_select.set_column(1, 1, 8)
            worksheet_select.set_column(2, 2, 11)
            worksheet_select.set_column(3, 3, 50)
            worksheet_select.set_column(4, 4, 50)
            worksheet_select.set_column(5, 5, 11)
            worksheet_select.set_column(6, 6, 30)

        # Fill observation worksheets
        col = 0
        row_critical = 1
        row_high = 1
        row_medium = 1
        row_low = 1
        row_info = 1

        for item in csv_array:
            if item[5] == '4':
                worksheet_select = worksheet_critical
                row = row_critical
            elif item[5] == '3':
                worksheet_select = worksheet_high
                row = row_high
            elif item[5] == '2':
                worksheet_select = worksheet_medium
                row = row_medium
            elif item[5] == '1':
                worksheet_select = worksheet_low
                row = row_low
            elif item[5] == '0':
                worksheet_select = worksheet_info
                row = row_info
                if args.nessus_autoclassify:
                    format_cell = good_cell
            if int(item[2]) in autoclassify and args.nessus_autoclassify:
                format_cell = bad_cell
            elif not item[5] == '0':
                format_cell = wrap
            worksheet_select.write_row(row, col, item, format_cell)
            worksheet_select.set_row(row, 30)
            if item[5] == '4':
                row_critical += 1
            if item[5] == '3':
                row_high += 1
            if item[5] == '2':
                row_medium += 1
            if item[5] == '1':
                row_low += 1
            if item[5] == '0':
                row_info += 1

        for worksheet_select in observation_worksheets:
            if worksheet_select == worksheet_critical:
                row = row_critical
            elif worksheet_select == worksheet_high:
                row = row_high
            elif worksheet_select == worksheet_medium:
                row = row_medium
            elif worksheet_select == worksheet_low:
                row = row_low
            elif worksheet_select == worksheet_info:
                row = row_info
            worksheet_select.add_table(0, 0, row - 1, 6, {
                'style':
                'Table Style Light 9',
                'header_row': True,
                'columns': [
                    {'header_format': bold, 'header': 'ip address'},
                    {'header_format': bold, 'header': 'port'},
                    {'header_format': bold, 'header': 'plugin id'},
                    {'header_format': bold, 'header': 'plugin name'},
                    {'header_format': bold, 'header': 'plugin output'},
                    {'header_format': bold, 'header': 'severity'},
                    {'header_format': bold, 'header': 'annotations'}
                ]})
            worksheet_select.set_row(0, 30)

        # Fill summary sheet
        worksheet_summary.set_row(0, 30)
        worksheet_summary.write(1, 0, 'Critical')
        worksheet_summary.write(1, 1, row_critical - 1)
        worksheet_summary.write(2, 0, 'High')
        worksheet_summary.write(2, 1, row_high - 1)
        worksheet_summary.write(3, 0, 'Medium')
        worksheet_summary.write(3, 1, row_medium - 1)
        worksheet_summary.write(4, 0, 'Low')
        worksheet_summary.write(4, 1, row_low - 1)
        worksheet_summary.write(5, 0, 'Info')
        worksheet_summary.write(5, 1, row_info - 1)

        # Fill portscan sheet
        xlsx_portscan_header = [
            {'header_format': bold, 'header': '{}'.format(title)} for title
            in portscan_header]
        worksheet_portscan.add_table(
            0, 0, len(portscan_csv_array), len(portscan_csv_array[0]) - 1, {
                'data': portscan_csv_array,
                'style': 'Table Style Light 9',
                'header_row': True,
                'columns': xlsx_portscan_header
            })
        worksheet_portscan.freeze_panes(0, 1)

        # Fill TLS scan sheet
        if tlsscan_csv_array:
            xlsx_tlsscan_header = [
                {'header_format': bold, 'header': '{}'.format(title)} for title
                in tlsscan_header]
            worksheet_tlsscan.add_table(
                0, 0, len(tlsscan_csv_array), len(tlsscan_csv_array[0]) - 1, {
                    'data': tlsscan_csv_array,
                    'style': 'Table Style Light 9',
                    'header_row': True,
                    'columns': xlsx_tlsscan_header
                })
            worksheet_tlsscan.set_row(0, 45)
            worksheet_tlsscan.set_column(1, len(xlsx_tlsscan_header) - 1, 11)
            worksheet_tlsscan.conditional_format(
                0, 1, len(tlsscan_csv_array), len(tlsscan_csv_array[0]) - 1, {
                    'type': 'cell',
                    'criteria': '==',
                    'value': '"X"',
                    'format': tls_bad_cell})
            worksheet_tlsscan.conditional_format(
                0, 1, len(tlsscan_csv_array), len(tlsscan_csv_array[0]) - 1, {
                    'type': 'cell',
                    'criteria': '==',
                    'value': '""',
                    'format': tls_good_cell})

        # Fill X.509 scan sheet
        if x509scan_csv_array:
            xlsx_x509scan_header = [
                {'header_format': bold, 'header': '{}'.format(title)} for title
                in x509scan_header]
            worksheet_x509scan.add_table(
                0, 0, len(x509scan_csv_array),
                len(x509scan_csv_array[0]) - 1, {
                    'data': x509scan_csv_array,
                    'style': 'Table Style Light 9',
                    'header_row': True,
                    'columns': xlsx_x509scan_header
                })
            worksheet_x509scan.set_row(0, 45)
            worksheet_x509scan.set_column(1, len(xlsx_x509scan_header) - 1, 11)
            worksheet_x509scan.conditional_format(
                0, 1, len(x509scan_csv_array),
                len(x509scan_csv_array[0]) - 1, {
                    'type': 'cell',
                    'criteria': '==',
                    'value': '"X"',
                    'format': tls_bad_cell})
            worksheet_x509scan.conditional_format(
                0, 1, len(x509scan_csv_array),
                len(x509scan_csv_array[0]) - 1, {
                    'type': 'cell',
                    'criteria': '==',
                    'value': '""',
                    'format': tls_good_cell})

        # Fill HTTP scan sheet
        if httpscan_csv_array:
            xlsx_httpscan_header = [
                {'header_format': bold, 'header': '{}'.format(title)} for title
                in httpscan_header]
            worksheet_httpscan.add_table(
                0, 0, len(httpscan_csv_array),
                len(httpscan_csv_array[0]) - 1, {
                    'data': httpscan_csv_array,
                    'style': 'Table Style Light 9',
                    'header_row': True,
                    'columns': xlsx_httpscan_header
                })
            worksheet_httpscan.set_row(0, 45)
            worksheet_httpscan.set_column(1, len(xlsx_httpscan_header) - 1, 11)
            worksheet_httpscan.conditional_format(
                0, 1, len(httpscan_csv_array),
                len(httpscan_csv_array[0]) - 1, {
                    'type': 'cell',
                    'criteria': '==',
                    'value': '"X"',
                    'format': tls_bad_cell})
            worksheet_httpscan.conditional_format(
                0, 1, len(httpscan_csv_array),
                len(httpscan_csv_array[0]) - 1, {
                    'type': 'cell',
                    'criteria': '==',
                    'value': '""',
                    'format': tls_good_cell})

        # Fill SMB scan sheet
        if smbscan_csv_array:
            xlsx_smbscan_header = [
                {'header_format': bold, 'header': '{}'.format(title)} for title
                in smbscan_header]
            worksheet_smbscan.add_table(
                0, 0, len(smbscan_csv_array), len(smbscan_csv_array[0]) - 1, {
                    'data': smbscan_csv_array,
                    'style': 'Table Style Light 9',
                    'header_row': True,
                    'columns': xlsx_smbscan_header
                })
            worksheet_smbscan.set_row(0, 45)
            worksheet_smbscan.set_column(1, len(xlsx_smbscan_header) - 1, 11)
            worksheet_smbscan.conditional_format(
                0, 1, len(smbscan_csv_array), len(smbscan_csv_array[0]) - 1, {
                    'type': 'cell',
                    'criteria': '==',
                    'value': '"X"',
                    'format': tls_bad_cell})
            worksheet_smbscan.conditional_format(
                0, 1, len(smbscan_csv_array), len(smbscan_csv_array[0]) - 1, {
                    'type': 'cell',
                    'criteria': '==',
                    'value': '""',
                    'format': tls_good_cell})

        # Fill RDP scan sheet
        if rdpscan_csv_array:
            xlsx_rdpscan_header = [
                {'header_format': bold, 'header': '{}'.format(title)} for title
                in rdpscan_header]
            worksheet_rdpscan.add_table(
                0, 0, len(rdpscan_csv_array), len(rdpscan_csv_array[0]) - 1, {
                    'data': rdpscan_csv_array,
                    'style': 'Table Style Light 9',
                    'header_row': True,
                    'columns': xlsx_rdpscan_header
                })
            worksheet_rdpscan.set_row(0, 45)
            worksheet_rdpscan.set_column(1, len(xlsx_rdpscan_header) - 1, 11)
            worksheet_rdpscan.conditional_format(
                0, 1, len(rdpscan_csv_array), len(rdpscan_csv_array[0]) - 1, {
                    'type': 'cell',
                    'criteria': '==',
                    'value': '"X"',
                    'format': tls_bad_cell})
            worksheet_rdpscan.conditional_format(
                0, 1, len(rdpscan_csv_array), len(rdpscan_csv_array[0]) - 1, {
                    'type': 'cell',
                    'criteria': '==',
                    'value': '""',
                    'format': tls_good_cell})

        # Fill SSH scan sheet
        if sshscan_csv_array:
            xlsx_sshscan_header = [
                {'header_format': bold, 'header': '{}'.format(title)} for title
                in sshscan_header]
            worksheet_sshscan.add_table(
                0, 0, len(sshscan_csv_array), len(sshscan_csv_array[0]) - 1, {
                    'data': sshscan_csv_array,
                    'style': 'Table Style Light 9',
                    'header_row': True,
                    'columns': xlsx_sshscan_header
                })
            worksheet_sshscan.set_row(0, 45)
            worksheet_sshscan.set_column(1, len(xlsx_sshscan_header) - 1, 11)
            worksheet_sshscan.conditional_format(
                0, 1, len(sshscan_csv_array), len(sshscan_csv_array[0]) - 1, {
                    'type': 'cell',
                    'criteria': '==',
                    'value': '"X"',
                    'format': tls_bad_cell})
            worksheet_sshscan.conditional_format(
                0, 1, len(sshscan_csv_array), len(sshscan_csv_array[0]) - 1, {
                    'type': 'cell',
                    'criteria': '==',
                    'value': '""',
                    'format': tls_good_cell})

    return my_nessus_table, nessus_portscan_table, nessus_tlsscan_table, \
        nessus_x509scan_table, nessus_httpscan_table, nessus_smbscan_table, \
        nessus_rdpscan_table, nessus_sshscan_table, csv_array, header, workbook
