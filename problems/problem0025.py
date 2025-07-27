import logging
from problems.lib import cli, main_wrapper
from problems.lib.math_ext import count_digits, fib

logger = logging.getLogger(__name__)


@main_wrapper
def main():
    i = 1
    fib_gen = fib(1, 1)
    while True:
        current_fib, _ = next(fib_gen)
        if count_digits(current_fib) >= 1000:
            break
        i += 1
    return i


if __name__ == "__main__":
    cli()
