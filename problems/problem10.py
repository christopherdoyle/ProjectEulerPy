# Summation of Primes
from problems.lib import prime
from problems.lib import cli, main_wrapper


@main_wrapper
def main():
    return sum(prime.sieve_of_eratosthenes(2_000_000))


if __name__ == "__main__":
    cli()
