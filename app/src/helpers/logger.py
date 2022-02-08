import json
import datetime
import logging

from config.settings import (
    LOGS_DIR,
    LOGS_FILENAME
)
try:
    from src.app import create_app
    current_app = create_app()
except (ImportError, Exception) as e:
    current_app = None


def get_logger():
    if current_app is None:
        return None

    return current_app.logger


def get_logs(from_date: str = None,
             to_date: str = None,
             log_level: str = None) -> list:
    file_path = f"{LOGS_DIR}/{LOGS_FILENAME}"

    with open(file_path) as file:
        file_content = file.read().splitlines()

    # Get all logs
    logs = [json.loads(log) for log in file_content]

    # Filter by date
    if from_date and to_date:
        from_date = datetime.datetime.strptime(from_date, '%Y-%m-%d')
        to_date = datetime.datetime.strptime(
            to_date + " 23:59:59", '%Y-%m-%d %H:%M:%S'
        )
        logs = [
            log for log in logs
            if datetime.datetime.strptime(
                log['asctime'], '%Y-%m-%d %H:%M:%S'
            ) >= from_date
            if datetime.datetime.strptime(
                log['asctime'], '%Y-%m-%d %H:%M:%S'
            ) <= to_date
        ]

    # Filter by log level
    if log_level:
        logs = [
            log for log in logs
            if get_log_level_value(log["levelname"])
            >= get_log_level_value(log_level)
        ]

    return logs


def get_log_level_value(log_level: str) -> int:
    return getattr(logging, log_level)


def clear_logs(latest_logs: list) -> None:
    file_path = f"{LOGS_DIR}/{LOGS_FILENAME}"
    open(file_path, 'w').close()

    with open(file_path, 'a') as file:
        for log in latest_logs:
            file.write(json.dumps(log) + "\n")
