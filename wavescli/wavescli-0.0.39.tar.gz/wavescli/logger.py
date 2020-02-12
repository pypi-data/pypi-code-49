import logging


WAVES_LOGGER_CONFIG = {
    'version': 1,
    'handlers': {
        'default': {
            'level': logging.INFO,
            'formatter': 'standard',
            'class': 'logging.StreamHandler'
        },
        'waves': {
            'level': logging.INFO,
            'formatter': 'waves',
            'class': 'logging.StreamHandler'
        }
    },
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'waves': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: [identifier:%(identifier)s] %(message)s'
        }
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': logging.INFO,
            'propagate': True
        },
        'waves': {
            'handlers': ['waves'],
            'level': logging.INFO,
            'propagate': False
        }
    }
}
