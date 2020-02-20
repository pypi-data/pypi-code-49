import os
import stat


def set_file_permission(file_path):
    if os.path.isfile(file_path):
        os.chmod(file_path, stat.S_IRWXG)


def copy_line_from_file_to_another_file(search_string, from_file, to_file):
    record_exists = False
    with open(to_file, 'w') as destination_file_write:
        with open(from_file) as source_file_read:
            for line in source_file_read:
                if search_string in line:
                    record_exists = True
                    destination_file_write.write(line)
    return record_exists


def remove_double_quotes_from_file(file_path):
    with open(file_path, 'r') as file_read:
        lines = file_read.readlines()

    with open(file_path, 'w') as file_write:
        file_write.truncate(0)
        for line in lines:
            file_write.write(line.replace('"', ''))
