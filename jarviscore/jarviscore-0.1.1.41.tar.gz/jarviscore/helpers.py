from datetime import datetime, timedelta





class Helpers():
    def get_timestamp_from_datetime(self, timestamp: datetime):
        """return a formatted date string for a given timestamp"""
        return self.__generate_timestamp(timestamp)
        
    def get_timestamp(self):
        return self.__generate_timestamp(datetime.now())
    
    def get_utc_timestamp(self):
        return self.__generate_timestamp(datetime.utcnow())

    def __generate_timestamp(self, provided_time: datetime):
        return provided_time.strftime("%Y-%m-%d %H:%M:%S.%f")

    def utc_from_timestamp(self, utc_timestamp):
        utc = datetime.datetime.strptime(utc_timestamp,"%Y-%m-%dT%H:%M:%SZ")
        return self.__generate_timestamp(utc)

    def utc_from_timestamp_to_localtime_timestamp(self, utc_timestamp: str):
        if datetime.localtime().tm_isdst == 1:
            dst = 11
        else:
            dst = 10
        utc = datetime.datetime.strptime(utc_timestamp,"%Y-%m-%dT%H:%M:%SZ")
        return self.__generate_timestamp(utc-timedelta(hours=-dst))
    
