import logging

FTM = "%(asctime)s - %(message)s"
FORMATS = {
    logging.DEBUG: FTM,
    logging.INFO: f"\x1B[32m{FTM}\x1B[0m",
    logging.ERROR: f"\x1B[31m{FTM}\x1B[0m"
}


class CustomLoggingFormatter(logging.Formatter):
    def format(self, record):
        log_ftm = FORMATS[record.levelno]
        formatter = logging.Formatter(log_ftm)
        return formatter.format(record)
