import datetime


def format_date_time(time_format="24"):
    d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")  # yyyy-MM-dd HH:mm
    if time_format == "24":
        return d
    else:
        return datetime.datetime.strptime(d, "%Y-%m-%d %H:%M").strftime("%Y-%m-%d %I:%M %p")  # yyyy-MM-dd HH:mm tt

