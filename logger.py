import logging.config


def create_logger(cf):
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s]: %(message)s'
            }
        },
        'handlers': {
            'default': {
                'level': 'INFO',
                'formatter': 'standard',
                'class': 'logging.FileHandler',
                'filename': cf['logger']['info']
            },
            'error': {
                'level': 'ERROR',
                'formatter': 'standard',
                'class': 'logging.FileHandler',
                'filename': cf['logger']['error']
            },
            'debug': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': cf['logger']['debug']
            }

        },
        'loggers': {
            'aiohttp.server': {
                'handlers': ['error'],
                'level': 'ERROR',
                'propagate': False
            },
            'logger': {
                'handlers': ['default'],
                'level': 'INFO',
                'propagate': False
            },
            'aiohttp.access': {
                'handlers': ['debug'],
                'level': 'DEBUG',
                'propagate': False
            }
        }
    }
    logging.config.dictConfig(LOGGING)
    logger = logging.getLogger('logger')
    return logger
