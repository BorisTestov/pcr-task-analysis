import logging
import os
from datetime import datetime

from .settings import log_settings


def setup_logging():
    formatter = logging.Formatter(
        "%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s"
    )
    os.makedirs(log_settings.directory, exist_ok=True)

    log_filename = os.path.join(
        log_settings.directory,
        f"{log_settings.base_filename}_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')}.log",
    )

    file_handler = logging.FileHandler(log_filename, mode="w")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logging.basicConfig(
        level=log_settings.level, handlers=[file_handler, stream_handler]
    )

    rotate_logs(
        log_settings.directory,
        log_settings.base_filename,
        log_settings.rotation_value,
    )


def rotate_logs(log_directory, file_prefix, rotation_value):
    log_files = sorted(
        [f for f in os.listdir(log_directory) if f.startswith(file_prefix)],
        key=lambda f: os.path.getctime(os.path.join(log_directory, f)),
    )

    while len(log_files) > rotation_value:
        oldest_file = log_files.pop(0)
        os.remove(os.path.join(log_directory, oldest_file))


def get_logger(name):
    return logging.getLogger(name)


setup_logging()
