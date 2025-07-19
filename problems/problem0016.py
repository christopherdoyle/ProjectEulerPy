from problems.lib import cli, main_wrapper
from problems.lib.math_ext import big_sum_digits


@main_wrapper("Power Digit Sum")
def main():
    return big_sum_digits(2**1000)


if __name__ == "__main__":
    cli()
