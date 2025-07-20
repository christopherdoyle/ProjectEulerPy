import math

from problems.lib import cli, main_wrapper


def find_divisors(x: int) -> list[int]:
    divisors = [1]
    for i in range(2, math.isqrt(x)):
        quot, rem = divmod(x, i)
        if rem == 0:
            divisors.append(i)
            divisors.append(quot)
    return divisors


def find_sum_of_divisors(x: int) -> int:
    return sum(find_divisors(x))


@main_wrapper
def main():
    dns = {}
    amicable_pairs = []
    for a in range(1, 10000 + 1):
        da = find_sum_of_divisors(a)
        if dns.get(da) == a:
            # amicable boy
            amicable_pairs.append((a, da))
            del dns[da]
            continue
        dns[a] = da

    return sum(map(sum, amicable_pairs))


if __name__ == "__main__":
    cli()
