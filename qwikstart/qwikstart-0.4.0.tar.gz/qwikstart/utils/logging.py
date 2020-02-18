import logging.config


def configure_logger(level: str = "INFO") -> None:
    logging.config.dictConfig(
        {
            "version": 1,
            "formatters": {
                "colored": {
                    "()": "colorlog.ColoredFormatter",
                    "format": "%(log_color)s%(message)s%(reset)s",
                }
            },
            "handlers": {
                "termcolor": {
                    "level": level,
                    "formatter": "colored",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                }
            },
            "loggers": {"qwikstart": {"level": level, "handlers": ["termcolor"]}},
        }
    )
