# Largest Palindrome Product

def is_palindrome(x: int) -> bool:
    s = str(x)
    return s == s[::-1]


largest_pal = 0

for a in range(999, 99, -1):
    for b in range(999, 99, -1):
        product = a * b
        if is_palindrome(product):
            if product > largest_pal:
                largest_pal = product
            # we have found the largest for the given a, therefore break
            break

print(largest_pal)
