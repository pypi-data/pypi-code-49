#!/usr/bin/env python3
from sys import argv


def is_start(previous_line, line, case_id):
    return '<!DOCTYPE HTML>' in line.upper() \
           and ('AuditLogFilter - Response' in line or previous_line and 'AuditLogFilter - Response' in previous_line) \
           and (f'[{case_id}]' in line or previous_line and f'[{case_id}]' in previous_line)


def is_stop(previous_line, line):
    return previous_line and '</BODY>' in previous_line.upper() and '</HTML>' in line.upper()


def get_html(log_file, case_id):
    buffer = []
    previous_line = None
    case_file = f'{log_file}_{case_id}.html'

    within = False
    with open(log_file, 'rt', encoding='utf-8') as in_file:
        with open(case_file, 'wt', encoding='utf-8') as out_file:
            for line in in_file:
                if line.strip():
                    original_line = line
                    if is_start(previous_line, line, case_id):
                        buffer = []
                        line = '<!DOCTYPE HTML>'
                        within = True

                    if within:
                        buffer.append(line)

                    if is_stop(previous_line, line):
                        if within:
                            out_file.writelines(buffer)
                            print(''.join(buffer))
                        within = False

                    previous_line = original_line


# if __name__ == '__main__':
#     get_html(argv[1], argv[2])

get_html('/Users/magnus/Downloads/lp_audit.log', '100005')
