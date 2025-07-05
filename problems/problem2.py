# Even Fibonacci Numbers

def fib(a, b):
    yield a, b
    yield from fib(b, a + b)


def main():
    fib_gen = fib(1, 2)
    accumulator = 0

    a, b = next(fib_gen)
    while b < 4_000_000:
        if b % 2 == 0:
            accumulator += b
        a, b = next(fib_gen)

    print(accumulator)


if __name__ == "__main__":
    main()
