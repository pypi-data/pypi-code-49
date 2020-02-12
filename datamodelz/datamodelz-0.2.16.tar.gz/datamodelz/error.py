from datetime import datetime


class Error:
    def __init__(self,
                 timeseries_code: str = "",
                 company: str = "",
                 check_name: str = "",
                 date: datetime = None,
                 value=None,
                 business_rule=None,
                 reference: str = "",
                 api_call: str = ""):
        self.timeseries_code = timeseries_code
        self.company = company
        self.check_name = check_name
        self.date = date  # filled in by error function
        self.value = value  # filled in by error function
        self.business_rule = business_rule  # filled in by error function
        self.reference = reference
        self.api_call = api_call
        self.fields = [self.timeseries_code, self.company, self.check_name, self.date, self.value, self.business_rule,
                       self.reference, self.api_call]

    def __repr__(self):
        return self.excel_format()

    def empty(self):
        if self.timeseries_code == "" and \
                self.company == "" and \
                self.check_name == "" and \
                self.value is None and \
                self.business_rule is None and \
                self.reference == "":
            return True
        return False

    def excel_format(self):
        lst = list()
        for field in self.fields:
            if field is None:
                to_add = ""
            elif field == self.date:
                to_add = self.date.strftime("%a %b %d %H:%M:%S")
            else:
                to_add = str(field)
            lst.append(to_add)
        return ",".join(lst)
