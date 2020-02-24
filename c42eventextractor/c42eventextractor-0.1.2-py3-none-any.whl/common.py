from datetime import datetime


class FileEventHandlers(object):
    def handle_response(self, response):
        print(response.text)

    def handle_error(self, exception):
        print(repr(exception))

    def get_cursor_position(self):
        pass

    def record_cursor_position(self, cursor):
        pass


def convert_datetime_to_timestamp(date):
    return (date - datetime.utcfromtimestamp(0)).total_seconds()
