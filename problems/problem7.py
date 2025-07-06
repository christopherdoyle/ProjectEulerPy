from problems.lib.prime import nth_prime
from problems.lib import cli, main_wrapper


@main_wrapper
def main():
    return nth_prime(10001)


if __name__ == "__main__":
    cli(main_wrapper(main))
