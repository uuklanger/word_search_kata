import os
import logging
import etc.config as config

__author__ = 'Ken Langer'
_LOGGER = None


def format_log(classname='UNKNOWN', method='UNKNOWN', msg=''):
    return f"[{classname}:{method}] {msg}"


def get_logger(filename=None, log_to_console=True):
    method = "get_logger"
    global _LOGGER
    if _LOGGER:
        pass
    else:
        directory = os.path.dirname(filename)
        create_logger_directory(directory)
        log_fh = open(filename, "w", encoding=config.FILE_ENCODING)

        logging.basicConfig(
            level=config.LOG_LEVEL,
            format=config.FORMAT)

        formatter = logging.Formatter(config.FORMAT)
        _log_stream_handler = logging.StreamHandler(log_fh)
        _log_stream_handler.setLevel(config.LOG_LEVEL)
        _log_stream_handler.setFormatter(formatter)

        log = logging.getLogger("MAIN")
        log.addHandler(_log_stream_handler)

        set_log_propagation(log=log, log_to_console=log_to_console)

        _LOGGER = log

        msg = format_log(
            "<log_helper>",
            method=method,
            msg=f"Initialized new Logger {filename} Console={log_to_console}"
        )
        _LOGGER.info(msg)
    return _LOGGER


def set_log_propagation(log=None, log_to_console=True):
    if log_to_console is False:
        log.propagate = False
    else:
        log.propagate = True
    return


def create_logger_directory(directory=None):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return

#
# end of script
#
