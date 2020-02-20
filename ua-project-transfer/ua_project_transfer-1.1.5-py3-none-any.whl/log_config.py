import logging
import datetime

from uagc_tools.log_tools import log_tools

CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "file_formatter": {
            "()": log_tools.FileFormatter,
            "level_formatters": {
                logging.INFO: logging.Formatter(
                    fmt=(
                        "%(levelname)s:  %(message)s, %(asctime)s")),
                logging.ERROR: logging.Formatter(
                    fmt=(
                        "%(levelname)s: %(message)s, %(asctime)s"))
            }
        },
        # Used by warn, error, and critical handlers.
        "email_formatter": {
            "()": log_tools.EmailFormatter
        }
    },
    "handlers": {
        "info_handler": {
            "class": "logging.FileHandler",
            "filename": "project_transfer_log_{}.txt".format(
                datetime.datetime.today().year
            ),
            # Open in append mode to not delete all the previous transfers.
            "mode": "a",
            "formatter": "file_formatter",
            "filters": ["info_filter"],
        },
        "warn_handler": {
            "()": log_tools.HTMLHandler,
            "mailhost": ("smtpgate.email.arizona.edu", 25),
            "fromaddr": "RDI_NoReply@email.arizona.edu",
            "toaddrs": "sterns1@email.arizona.edu",
            "subject": "A project for your service requires your attention",
            "formatter": "email_formatter",
            "filters": ["warn_filter"],
        },
        "error_handler": {
            "()": log_tools.HTMLHandler,
            "mailhost": ("smtpgate.email.arizona.edu", 25),
            "fromaddr": "RDI_NoReply@email.arizona.edu",
            "toaddrs": "sterns1@email.arizona.edu",
            "subject": "Could Not Transfer Project",
            "formatter": "email_formatter",
            "filters": ["err_crit_filter"]
        },
        "critical_handler": {
            "()": log_tools.HTMLHandler,
            "mailhost": ("smtpgate.email.arizona.edu", 25),
            "fromaddr": "RDI_NoReply@email.arizona.edu",
            "toaddrs": "sterns1@email.arizona.edu",
            "subject": "Project Creation Failed :(",
            "formatter": "email_formatter",
            "filters": ["err_crit_filter"]
        },
        "email_handler": {
            "()": log_tools.HTMLHandler,
            "mailhost": ("smtpgate.email.arizona.edu", 25),
            "fromaddr": "RDI_NoReply@email.arizona.edu",
            "toaddrs": "sterns1@email.arizona.edu",
            "subject": "Project Cannot Be Routed",
            "formatter": "email_formatter",
            "filters": ["warn_filter"],
        },
        "null_handler": {
            "class": "logging.NullHandler",
            "filters": ["warn_filter"],
        }
    },
    "filters": {
        "info_filter": {
            "()": log_tools.LevelFilter,
            "levels": [logging.INFO, logging.ERROR]
        },
        "warn_filter": {
            "()": log_tools.LevelFilter,
            "levels": [logging.WARNING]
        },
        "err_crit_filter": {
            "()": log_tools.LevelFilter,
            "levels": [logging.ERROR, logging.CRITICAL]
        }
    },
    "loggers": {
        "__main__": {
            "propogate": False,
            "level": logging.DEBUG,
            "handlers": [
                "info_handler",
                "warn_handler",
                "error_handler",
                "critical_handler"
            ]
        },
        "__main__.next_steps": {
            "propogate": True,
            "level": logging.DEBUG,
            "handlers": ["email_handler"]
        },
        "__main__.project_lims_tools": {
            "propogate": True,
            "level": logging.DEBUG,
            "handlers": ["null_handler"]
        },
    }
}
