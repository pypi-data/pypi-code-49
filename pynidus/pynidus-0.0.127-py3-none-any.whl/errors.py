import logging
import bugsnag

class ErrorLogger:

    def __init__(self, config):

        self.api_key=config.get('API_KEY')
        self.release_stage=config.get('RELEASE_STAGE')
            
        bugsnag.configure(
            api_key=self.api_key,
            release_stage=self.release_stage
        )
        
        self.logger = logging.getLogger('bugsnag')
        
        handler = bugsnag.handlers.BugsnagHandler()
        handler.setLevel(logging.ERROR)

        self.logger.addHandler(handler)

    def notify(self, e):
        bugsnag.notify(e)
        self.logger.error(e)