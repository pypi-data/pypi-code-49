import os


def get_file_name(logging_file_path, file_path):
    # def get_file_name(logging_file_path, file_path):
    # process_name = (os.path.splitext(os.path.basename(inspect.getfile(inspect.currentframe())))[0])
    # get_job_name_log_file_path(process_name, logging_file_path)
    # log_write(process_name + " started")
    # log_write(process_name + " finished")
    return os.path.splitext(os.path.basename(file_path))[0]


def convert_bytes(num):
    for y in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, y)
        num /= 1024.0


def get_file_size(logging_file_path, file_path):
    # def get_file_size(logging_file_path, file_path):
    # process_name = (os.path.splitext(os.path.basename(inspect.getfile(inspect.currentframe())))[0])
    # get_job_name_log_file_path(process_name, logging_file_path)
    # log_write(process_name + " started")
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        # log_write(process_name + " finished")
        return convert_bytes(file_info.st_size)


def get_file_type(logging_file_path, file_path):
    # def get_file_type(logging_file_path, file_path):
    # process_name = (os.path.splitext(os.path.basename(inspect.getfile(inspect.currentframe())))[0])
    # get_job_name_log_file_path(process_name, logging_file_path)
    # log_write(process_name + " started")
    # log_write(process_name + " finished")
    return os.path.splitext(os.path.basename(file_path))[1]
