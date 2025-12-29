import logging
import os
import sys


def get_base_dir():
    """
    Devuelve la ruta base correcta tanto en desarrollo
    como en ejecutable PyInstaller
    """
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def setup_logger(name="app", filename="launcher.log"):
    log_path = os.path.join(get_base_dir(), filename)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Evitar handlers duplicados
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
