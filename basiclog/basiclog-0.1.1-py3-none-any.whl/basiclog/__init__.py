import logging
import slack


class Log(object):

    logLevels = {
        "debug": {
            "file_handler": "DEBUG",
            "consol_handler": "DEBUG",
            "slack_handler": "WARNING",
        },
        "test": {
            "file_handler": "INFO",
            "consol_handler": "INFO",
            "slack_handler": "WARNING",
        },
        "prod": {
            "file_handler": "WARNING",
            "consol_handler": "WARNING",
            "slack_handler": "ERROR",
        },
    }

    def __init__(self, level, script_name):
        """
        Basic example:
            import traceback
            import basiclog

            logger = basiclog.log("debug", __file__)

            # for slack error messages
            logger.add_slack_handler(slack_api_toke, slack_channel)
            
            logger.info("Script has been started")
            try:
                main()
            except KeyboardInterrupt:
                logger.info("Script has been stopped manually")
            except:
                e = traceback.format_exc()
                logger.error(e)
        """

        self.script_name = script_name
        self.slack_level = self.logLevels[level]["slack_handler"]

        self.logger = logging.getLogger(self.script_name)
        self.logger.setLevel(logging.DEBUG)

        # create file handler
        file_handler = logging.FileHandler(self.script_name + ".log")
        file_handler.setLevel(
            logging.getLevelName(self.logLevels[level]["file_handler"])
        )

        # create console handler
        consol_handler = logging.StreamHandler()
        consol_handler.setLevel(
            logging.getLevelName(self.logLevels[level]["consol_handler"])
        )

        # create formatter and add it to the handlers
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        consol_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # add the handlers to logger
        self.logger.addHandler(consol_handler)
        self.logger.addHandler(file_handler)

    def add_slack_handler(self, slack_token, slack_channel):
        # create and add custom Slack handler
        sh = SlackHandler(self.script_name, slack_token, slack_channel)
        sh.setLevel(logging.getLevelName(self.slack_level))
        self.logger.addHandler(sh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


class SlackHandler(logging.StreamHandler):
    def __init__(self, script_name, slack_token, slack_channel):

        logging.StreamHandler.__init__(self)
        self.script_name = script_name
        self.slack_token = slack_token
        self.slack_channel = slack_channel

    def emit(self, message):
        message = self.format(message)
        error_message = """:red_circle: *Script failed*
*Name*: {script_name}
*Error Message*:
{traceback}
        """.format(
            script_name=self.script_name, traceback=message
        )

        client = slack.WebClient(token=self.slack_token)
        client.chat_postMessage(
            channel=self.slack_channel, text=error_message,
        )
