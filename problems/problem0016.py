from problems.lib import cli, main_wrapper


def big_sum_digits(x: int) -> int:
    # avoiding str, because.
    def digits(n):
        while n:
            n, r = divmod(n, 10)
            yield r

    return sum(digits(x))


@main_wrapper("Power Digit Sum")
def main():
    return big_sum_digits(2**1000)


if __name__ == "__main__":
    cli()
