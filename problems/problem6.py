# Sum Square Difference

def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))


def square_of_sum(n):
    sum_to_n = int((n * (n + 1)) / 2)
    return sum_to_n ** 2


print(abs(sum_of_squares(100) - square_of_sum(100)))
