import re
from datetime import datetime

from datamodelz.error import Error
from .field import Field, URLField, StringField, TickerField, HttpsField
from . import rule


def matches_url(field, url):
    return len(re.findall(r"https://(www\.)?{name}\.com.*".format(name=field.name), str(url))) > 0


def matches(field, sample):
    return len(re.findall(r".*{name}.*".format(name=field.name), str(sample))) > 0


class CAResponseField(Field):
    def __init__(self):
        super().__init__()
        self.name = "response"
        self.value = {}

        self.biids = BiidsField("biids")
        self.mainDomains = MainDomainField("mainDomains")
        self.urls = UrlsField("URLs")
        self.rules = [
            rule.no_error,
            rule.has_field(self.biids.name),
            rule.has_field(self.mainDomains.name),
            rule.has_field(self.urls.name)
        ]
        self.fields = [self.biids, self.mainDomains, self.urls]

    def set(self, value):
        self.value = value
        self.run_rules()  # checks that names exist in dictionary
        self.set_fields(self.fields)  # goes through fields & sets them
        return self.errors

    def validate(self):
        # does not re-run rules
        self.validate_fields(self.fields)
        if not self.errors:
            self.valid = True
        return self.errors


class CAResponseSubField(Field):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.found = {}

    def was_found(self, field, value):
        if field.name in self.found:
            old_value = self.found[field.name]
            self.error(Error(check_name="Duplicate URL",
                             value="{} and {}".format(old_value, value),
                             business_rule="Only 1 {} url".format(field.name),
                             date=datetime.now()))
            return True
        self.found[field.name] = value
        return False


class BiidsField(CAResponseSubField):
    def __init__(self, name):
        super().__init__(name)
        self.datasys_id = StringField("datasys")
        self.timeseries_id = StringField("timeseries")
        self.ticker = TickerField("ticker")
        self.exchange = StringField("exchange")  # Todo: update to be more specific
        self.eod = TickerField("eod")
        self.fields = [self.datasys_id, self.timeseries_id, self.ticker, self.exchange, self.eod]

    def set(self, value):
        self.value = value
        for obj in self.value:
            value = obj["value"]
            service = obj["service"]
            if matches(self.datasys_id, service):
                if not self.was_found(self.datasys_id, value):
                    self.set_field(self.datasys_id, value)
            elif matches(self.timeseries_id, service):
                if not self.was_found(self.timeseries_id, value):
                    self.set_field(self.timeseries_id, value)
            elif matches(self.eod, service):
                if not self.was_found(self.eod, value):
                    self.set_field(self.eod, value)
            elif matches(self.exchange, service):  # Note: not limited to 1
                self.set_field(self.exchange, service)
                self.set_field(self.ticker, value)
        return self.errors


class MainDomainField(CAResponseSubField):
    def __init__(self, name):
        super().__init__(name)
        self.domain = StringField("mainDomain")  # TODO: is this right?
        self.fields = [self.domain]

    def set(self, value):
        self.value = value
        for obj in self.value:
            if not self.was_found(self.domain, obj["value"]):
                self.set_field(self.domain, obj["value"])
        return self.errors

class UrlsField(CAResponseSubField):
    def __init__(self, name):
        super().__init__(name)
        self.linkedin = URLField("linkedin")
        self.indeed = URLField("indeed")
        self.comparably = URLField("comparably")
        self.marketbeat = URLField("marketbeat")
        self.yahoo = HttpsField("finance.yahoo")
        self.twitter = HttpsField("twitter")
        self.facebook = URLField("facebook")
        self.fields = [self.linkedin, self.indeed, self.comparably, self.marketbeat, self.yahoo, self.twitter, self.facebook]

    def set(self, value):
        self.value = value
        for obj in self.value:
            url = obj["value"]
            for field in self.fields:
                if matches_url(field, url):
                    if not self.was_found(field, url):
                        self.set_field(field, url)
                    break
            else:
                self.error(Error(check_name="Extra URL", value=url, date=datetime.now()))
        return self.errors
