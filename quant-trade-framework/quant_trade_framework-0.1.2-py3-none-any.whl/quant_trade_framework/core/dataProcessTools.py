from datetime import datetime,timezone,timedelta


class DataProcessTools:
    @classmethod
    def getDateTimeNow(cls):
        utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
        tzutc_8 = timezone(timedelta(hours=8))
        datetime_now = utc_dt.astimezone(tzutc_8)
        return datetime_now

    @classmethod
    def transferLocalDateTimeToChineseTimeZone(cls,input_datetime):
        datetime_now = None
        if isinstance(input_datetime,datetime):
            utc_dt = input_datetime.utcnow().replace(tzinfo=timezone.utc)
            tzutc_8 = timezone(timedelta(hours=8))
            datetime_now = utc_dt.astimezone(tzutc_8)
        return datetime_now