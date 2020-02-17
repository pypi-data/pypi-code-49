import datetime
import typing


def get_timestamp(to_str: bool = None) -> typing.Union[str, datetime.datetime]:
    now = datetime.datetime.now()
    if to_str:
        return timestamp2str(now)
    return now


def timestamp2str(target_dt: datetime.datetime) -> str:
    return target_dt.strftime("%Y%m%d%H%M%S")
