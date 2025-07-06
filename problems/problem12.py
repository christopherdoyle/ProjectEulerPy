# Highly Divisible Triangular Number
import math


def count_factors(n: int) -> int:
    n_factors = 0
    i = 1
    n_sqrt = math.isqrt(n)
    while i < n_sqrt:
        n_factors += 2 if n % i == 0 else 0
        i += 1
    n_factors += 1 if i * i == n else 0
    return n_factors


def main():
    i = 0
    i_triangle = 0
    while True:
        i += 1
        i_triangle += i
        factors = count_factors(i_triangle)
        if factors > 500:
            print(f"Triangular number {i}, {i_triangle}, has {factors} factors")
            break


if __name__ == "__main__":
    main()
