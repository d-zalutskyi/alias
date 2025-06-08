import logging
import sys

from config import config


class Logger:
    @classmethod
    def setup_logger(cls, name: str = __name__) -> logging.Logger:
        logger = logging.getLogger(name)
        if logger.hasHandlers():
            logger.handlers.clear()

        log_level = logging.DEBUG if getattr(config, "DEBUG", False) else logging.INFO
        logger.setLevel(log_level)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | "
            "%(filename)s:%(lineno)d | %(funcName)s() | %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

        return logger
