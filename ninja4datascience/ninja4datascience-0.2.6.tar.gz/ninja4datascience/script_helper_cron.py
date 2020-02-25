"""
Document
"""

import os
import stat
import datetime
import getpass
from crontab import CronTab


def print_header(length, description):
    """
    Document
    """

    dash = "-" * int(length)
    print(dash)
    print()
    print(description)
    print(dash)
    print()


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


def create_new_cron_job(user_name, min, hour, day, month, env_path, command):
    cron = CronTab(user=user_name)
    directory = os.path.dirname(command)
    python_script = os.path.basename(command)
    for job in cron:
        if str(job.command).find('python {}'.format(python_script)) != -1:
            cron.remove(job)
    command = "source {0} ; cd {1}; python {2}; crontab -l | grep -v 'python {2}' | crontab -"
    job = cron.new(
        command=command.format(
            env_path, directory, python_script))
    job.minute.on(min)
    job.hour.on(hour)
    job.day.on(day)
    job.month.on(month)
    cron.write(user=user_name)


def get_date():
    while True:
        start_date = input("Enter start date (dd-mmm-yyyy):")
        try:
            start_date = datetime.datetime.strptime(start_date, '%d-%b-%Y')
            return start_date
        except ValueError:
            pass


def get_time():
    while True:
        start_time = input("Enter start time (hh:mm):")
        try:
            start_time = datetime.datetime.strptime(start_time, "%H:%M")
            return start_time
        except ValueError:
            pass


def get_username():
    # while True:
    #     user_name = input("Please Enter UserName : ")
    #     if user_name.strip() != '':
    #         return user_name.strip()
    username = getpass.getuser().strip()
    return username


def confirm_user_input(start_date, start_time, username):
    while True:
        confirming_final = input(
            "Start Time is [" + str(start_date.strftime("%d-%b-%Y")) + ":" + str(
                start_time.strftime("%H:%M")) + "] and UserName is [" + str(
                username) + "]\n is this correct (YES/NO)? ==>")
        if confirming_final.upper().strip() in ("NO", "N"):
            return False
        elif confirming_final.upper().strip() in ("YES", "Y"):
            return True


if __name__ == "__main__":
    print_header(80, "Hello")
