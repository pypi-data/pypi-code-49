import json
import sys


class CloudRunLogger(object):

    def __init__(self, project_id, local_run=False):
        self.project_id = project_id
        self.request = None
        self.trace_id = None
        self.local_run = local_run

    def update_trace_id(self, trace_id):
        self.trace_id = trace_id

    def update_request_header(self, api_request):
        self.request = api_request

    def _do_log(self, severity, message):
        # check if local run = true if yes just print the message
        if self.local_run:
            print(message)
        else:
            # Build structured log messages as an object.
            global_log_fields = {}
            # Add log correlation to nest all log messages
            # beneath request log in Log Viewer.
            trace_header = self.request.headers.get('X-Cloud-Trace-Context')

            if trace_header and self.project_id:
                trace = trace_header.split('/')
                global_log_fields['logging.googleapis.com/trace'] = (
                    f"projects/{self.project_id}/traces/{trace[0]}")

            # Complete a structured log entry.
            entry = dict(severity=severity,
                         message=message,
                         trace_id=self.trace_id,
                         **global_log_fields)

            print(json.dumps(entry))
            sys.stdout.flush()

    def info(self, message):
        self._do_log('INFO', message=message)

    def warning(self, message):
        self._do_log('WARNING', message=message)

    def error(self, message):
        self._do_log('ERROR', message=message)

    def debug(self, message):
        self._do_log('DEBUG', message=message)

















