import logging


class InfoLogsOnlyFilter(logging.Filter):
    """ Filters out logs data to keep only logs with level 'INFO'. """
    def filter(self, record: logging.LogRecord) -> bool:
        """ Keeping only INFO logs. """
        if record.levelname == "INFO":
            return True
        else:
            return False


class ExcludeDjangoLogs(logging.Filter):
    """ Filters excludes Django native logs. """
    MODULES_TO_EXCLUDE = (
        "django",
        "django.db",
        "django.request",
        "django.channels",
        "daphne.server",
        "django.utils"
    )

    def filter(self, record: logging.LogRecord) -> bool:
        """ Checking if log relates to Django and filters it out. """
        return not any(record.name.startswith(logger) for logger in self.MODULES_TO_EXCLUDE)