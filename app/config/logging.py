from config.settings import (
    LOG_LEVEL,
    LOGS_DIR,
    LOGS_FILENAME
)


def get_logging_config() -> dict:
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simpleFormatter': {
                'class': 'logging.Formatter',
                'format': '%(asctime)s - %(levelname)s: %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'json': {
                'class': 'pythonjsonlogger.jsonlogger.JsonFormatter',
                'format': '%(asctime)s %(levelname)s %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            }
        },
        'handlers': {
            'consoleHandler': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'simpleFormatter',
                'stream': 'ext://sys.stdout'
            },
            'fileHandler': {
                'class': 'logging.FileHandler',
                'level': LOG_LEVEL,
                'formatter': 'json',
                'filename': LOGS_DIR + '/' + LOGS_FILENAME,
                'mode': 'a'
            }
        },
        'loggers': {

        },
        'root': {
            'level': LOG_LEVEL,
            'handlers': [
                'consoleHandler',
                'fileHandler'
            ]
        }
    }
