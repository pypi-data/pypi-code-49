class BaseLogger(object):

    def __init__(self, service_name='', run_id='', project_id=''):
        self.service_name = service_name
        self.trace_id = run_id
        self.project_id = project_id


    def do_log(self, message, severity, res, local_run, logger):
        message = str(message)
        if local_run is False:
            logger.log_struct({'message': message, 'trace_id': self.trace_id, 'service_name': self.service_name},
                              resource=res, severity=severity)
        else:
            print('{}: {}'.format(severity, message))

    def create_logger(self):
        from google.cloud import logging
        log_client = logging.Client(project=self.project_id)
        logger = log_client.logger(self.service_name)
        return logger

    def update_trace_id(self, new_trace_id):
        self.trace_id = new_trace_id


    def get_project_id(self):
        return self.project_id

    def get_trace_id(self):
        return self.trace_id

    def get_service_name(self):
        return self.service_name