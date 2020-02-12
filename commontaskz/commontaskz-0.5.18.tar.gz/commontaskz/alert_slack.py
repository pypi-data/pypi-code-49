import slack
import logging

from datamodelz.error import Error
from prefect import Task
from datetime import date, timedelta, datetime
from prefect.utilities.tasks import defaults_from_attrs


def get_field(dct: dict, name):
    """
    Will check & get field via name
    :param dct: dict
    :param name: any key stored in a dictionary
    :return: any value stored in a dictionary
    """
    if type(dct) == dict and name in dct:
        return dct[name]
    return None


def get_errors(errors, i) -> list:
    error_list = get_field(errors[i], "error")
    if type(error_list) == str:
        return [error_list]
    return error_list


def get_service_id(service_ids, i) -> str:
    service_id = ""
    if len(service_ids) > i and "error" not in service_ids[i]:
        service_id = service_ids[i]
    return service_id


class MakeErrorTask(Task):
    def __init__(self, token, titles=None, max_retries=3, retry_delay=timedelta(minutes=1), **kwargs):
        """
        :param titles:
        :param key: Slack Token to be used in slack.WebClient()
        """
        super().__init__(max_retries, retry_delay, **kwargs)
        self.name = "Make Error"
        self.titles = titles
        self.slack_client = slack.WebClient(token=token)

        # set automatically
        self.problems = []
        self.date = str(date.today())
        self.time = str(datetime.now().time())
        self.file = "results.csv"
        self.file_header = "Central Authority ID, Service ID, Errors"
        self.length = 0

    def make_file_name(self, titles: list) -> None:
        """
        Creates file name ex: datasys_kelvin_set_20190803.csv
        :param titles: list of strings
        :return: None
        """
        if titles:
            self.titles = titles
        title = "_".join(self.titles).lower().replace(" ", "_")
        self.file = "{}_{}.csv".format(title, self.date.replace("-", ""))
        return

    def success_alert(self) -> bool:
        """
        :return: bool: ran ok
        """
        response = self.slack_client.chat_postMessage(
            channel='#prefect-data-alerts',
            text=":smile: New Alert from `{}` there are {} errors (out of {})"
                .format(" ".join(self.titles), len(self.problems), self.length),
        )
        return response["ok"]

    def failure_alert(self) -> bool:
        """
        :return: bool: ran ok
        """
        response = self.slack_client.files_upload(
            channels='#prefect-data-alerts',
            file=self.file,
            filename=self.file,
            filetype="csv",
            initial_comment=":frowning: New Alert from `{}` there are {} errors (out of {})"
                .format(" ".join(self.titles), len(self.problems), self.length),
            title=self.file
        )
        return response["ok"]


class MakePivotErrorTask(MakeErrorTask):
    def __init__(self,
                 token,
                 titles=None,
                 max_retries=3,
                 retry_delay=timedelta(minutes=1),
                 header="Timeseries Code, Company, Check, Date, Value, Business Rule, Reference Link, API Call",
                 **kwargs):
        """
        needs to generate excel with 2 tabs and post to slack

        :param titles:
        :param key: Slack Token to be used in slack.WebClient()
        """
        super().__init__(token, titles, max_retries, retry_delay, **kwargs)
        self.name = "Make Pivot Error"
        self.header = header + "\n"
        self.counts = dict()
        self.formatted_counts = ""

    @staticmethod
    def writeable_list(lst, offset=False):
        if not lst:
            return ""
        writeable = ",".join(lst) + '\n'
        if offset:
            writeable = "," + writeable
        return writeable

    @staticmethod
    def flatten_errors(errors: list):
        error_all = []
        for dct_lst in errors:  # per timeseries
            for dct in dct_lst:   # per check list
                err_lst = get_field(dct, "error")
                if err_lst is None or not err_lst or type(err_lst) == str:
                    logging.debug(err_lst)  # TODO add
                    continue
                error_all += err_lst
        return error_all

    def error_ok(self, errors):
        if errors is None or type(errors) not in [str, list, dict]:
            logging.debug("Returning without making error list")
            return False
        return True

    def make_error_list(self, errors: list, flatten=False) -> None:
        # error has type Error
        if not errors:
            return
        self.length = len(errors)
        if flatten:
            if type(errors[0]) == dict:
                errors = [errors]
            errors = self.flatten_errors(errors)
        else:
            errors = get_field(errors, "error")

        for err in errors:
            if err is None:
                continue
            if type(err) == str:  # TODO:fix
                logging.error(err)
                self.problems.append(err)
                continue
            if err.empty():
                continue
            self.problems.append(err.excel_format())
        return

    def make_error_file(self, titles, collapse, aggregate) -> None:
        """
        requires: self.file, self.file_header, self.problems
        :return: None
        """
        if not self.problems:
            return
        with open(self.file, "w+") as csv:
            csv.write("Date, Time, Set Description, Collapse, Aggregate\n")
            csv.write(self.writeable_list([self.date, self.time, ' '.join(titles), collapse, aggregate, '\n']))
            csv.write(self.header)
            for lst in self.problems:
                try:
                    csv.write(lst)
                    csv.write('\n')
                except:
                    logging.error("cannot print problems list {}".format(lst))
                    continue
        return

    @defaults_from_attrs('titles')
    def run(self, titles=None, errors=None, collapse="", aggregate="", flatten=False, **kwargs) -> bool:
        """
        :param flatten:
        :param aggregate:
        :param collapse:
        :param titles:
        :param errors: list of strings
        :return: bool
        """
        self.date = str(date.today())
        self.time = str(datetime.now().time())
        if errors is None or type(errors) not in [list, dict]:
            errors = list()
        self.make_file_name(titles)
        self.make_error_list(errors, flatten)
        if self.problems:
            self.make_error_file(titles, collapse, aggregate)
            self.failure_alert()
            return False
        self.success_alert()
        return True

