# Largest Prime Factor
import math
from problems.lib.prime import is_prime
from problems.lib import cli, main_wrapper


@main_wrapper
def main():
    N = 600_851_475_143
    answer = None
    for n in range(math.floor(math.sqrt(N)), 2, -1):
        if (N % n) == 0 and is_prime(n):
            answer = n
            break
    return answer


if __name__ == "__main__":
    cli()
