import datetime


class Config(object):
    debug = False
    URL = "http://cm-0.tepper.cmu.edu:8765/v1/vision_parsing"
    AUTH_URL = "https://soco-doc-parser-gateway.herokuapp.com/v1/auth"


class Eastern(datetime.tzinfo):
    def utcoffset(self, dt):
      return datetime.timedelta(hours=-5)

    def tzname(self, dt):
        return "EST"

    def dst(self, dt):
        return datetime.timedelta(0)
