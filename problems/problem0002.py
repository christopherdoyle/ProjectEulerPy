# Even Fibonacci Numbers
from problems.lib import cli, main_wrapper
from problems.lib.math_ext import fib


@main_wrapper
def main():
    fib_gen = fib(1, 2)
    accumulator = 0

    a, b = next(fib_gen)
    while b < 4_000_000:
        if b % 2 == 0:
            accumulator += b
        a, b = next(fib_gen)

    return accumulator


if __name__ == "__main__":
    cli()
