# Multiples of 3 or 5
from problems.lib import cli, main_wrapper


@main_wrapper
def main():
    total = sum(i for i in range(1, 1000) if (i % 3) == 0 or (i % 5) == 0)
    return total


if __name__ == "__main__":
    cli()
