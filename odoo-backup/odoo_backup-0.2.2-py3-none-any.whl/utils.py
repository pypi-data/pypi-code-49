from datetime import datetime


def backup_name_from_datetime(timestamp):
    return timestamp.strftime("%Y%m%d-%H%M%S.zip")

def backup_datetime_from_name(name):
    return datetime.strptime(name, "%Y%m%d-%H%M%S.zip")
