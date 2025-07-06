import logging
import time

from functools import wraps

logger = logging.getLogger(__name__)

REGISTERED_MAINS = {}


def _wrap_main_fn(fn, description):
    @wraps(fn)
    def fn_(*a, **kw):
        t_start = time.time()
        if description is not None:
            logger.info(f"Running problem: '{description}'")
        result = fn(*a, **kw)
        t_end = time.time()
        total_time = t_end - t_start
        logger.debug(f"Main function '{fn.__name__}' took {total_time:.2f} seconds")
        if result is not None:
            logger.info(f"Result: {result}")
        return result

    return fn_


def main_wrapper(arg):
    if callable(arg):
        # If the argument is a callable, treat it as the main function
        description = None
        fn = arg
        fn_ = _wrap_main_fn(fn, description)
        REGISTERED_MAINS[fn.__module__] = fn_
        return fn_
    else:
        # Otherwise, treat it as a description for the main function
        description = arg

        def decorator(fn):
            fn_ = _wrap_main_fn(fn, description)
            REGISTERED_MAINS[fn.__module__] = fn_
            return fn_

        return decorator


class ColorFormatter(logging.Formatter):
    colors = {
        "DEBUG": "\033[90m",  # Grey
        "INFO": "\033[0m",  # Default (no color)
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[95m",  # Magenta
        "RESET": "\033[0m",  # Reset to default
    }

    def format(self, record):
        reset = self.colors["RESET"]
        log_color = self.colors.get(record.levelname, reset)
        formatted_msg = super().format(record)
        return f"{log_color}{formatted_msg}{reset}"


def setup_logger(name=None, level=logging.DEBUG):
    formatter = ColorFormatter(
        fmt="[{asctime}] [{levelname:<8s}] {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.propagate = False

    return logger


def cli(fn=None):
    setup_logger()
    if fn is not None:
        if isinstance(fn, str):
            if fn in REGISTERED_MAINS:
                fn = REGISTERED_MAINS[fn]
            else:
                raise ValueError(f"Function '{fn}' not registered.")
    else:
        fn = REGISTERED_MAINS["__main__"]

    fn()
