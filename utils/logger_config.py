import logging
import sys

def setup_logger(name=__name__):
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)

        console = logging.StreamHandler(sys.stdout)

        logger.addHandler(console)
        logger.propagate = False

    return logger
