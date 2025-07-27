from problems.lib import cli, main_wrapper
from problems.lib.math_ext import big_sum_digits, factorial


@main_wrapper
def main():
    return big_sum_digits(factorial(100))


if __name__ == "__main__":
    cli()
