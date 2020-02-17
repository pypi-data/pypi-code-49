from mms.base_logger import BaseLogger
from google.cloud.logging.resource import Resource



class AppEngineLogger(BaseLogger):

    def __init__(self, service_name='', trace_id='', project_id='', module_id='', version_id='', local_run=False):
        super().__init__(service_name=service_name,
                         run_id=trace_id,
                         project_id=project_id)
        self.module_id = module_id
        self.version_id = version_id
        self.local_run = local_run

        self.res = Resource(type='gae_app', labels={
            "project_id": super().get_project_id(),
            "module_id": self.module_id,
            "version_id": self.version_id
        })

        self.logger = super().create_logger()

    def update_trace_id(self, new_trace_id):
        super().update_trace_id(new_trace_id=new_trace_id)

    def info(self, message):
        super().do_log(message=message,
                       severity='INFO',
                       res=self.res,
                       local_run=self.local_run,
                       logger=self.logger)

    def warning(self, message):
        super().do_log(message=message,
                       severity='WARNING',
                       res=self.res,
                       local_run=self.local_run,
                       logger=self.logger)

    def error(self, message):
        super().do_log(message=message,
                       severity='ERROR',
                       res=self.res,
                       local_run=self.local_run,
                       logger=self.logger)

    def critical(self, message):
        super().do_log(message=message,
                       severity='CRITICAL',
                       res=self.res,
                       local_run=self.local_run,
                       logger=self.logger)

    def debug(self, message):
        super().do_log(message=message,
                       severity='DEBUG',
                       res=self.res,
                       local_run=self.local_run,
                       logger=self.logger)