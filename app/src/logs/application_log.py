from src.helpers.logger import (
    get_logger
)


class ApplicationLog:
    def __init__(self) -> None:
        self.logger = get_logger()

    def info(self, message: str, extra: dict = None) -> None:
        if self.logger is None:
            print(message)
            return None

        self.logger.info(message, extra=extra)

    def warning(self, message: str, extra: dict = None) -> None:
        if self.logger is None:
            print(message)
            return None

        self.logger.warning(message, extra=extra)

    def error(self, message: str, extra: dict = None) -> None:
        if self.logger is None:
            print(message)
            return None

        self.logger.error(message, extra=extra)

    def critical(self, message: str, extra: dict = None) -> None:
        if self.logger is None:
            print(message)
            return None

        self.logger.critical(message, extra=extra)
