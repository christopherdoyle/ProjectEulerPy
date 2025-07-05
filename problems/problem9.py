

def is_pythagorean_triplet(a, b, c):
    return (a ** 2) + (b ** 2) == c ** 2

# (a + b) ** 2 = a**2 + b**2 + 2ab
# a**2 + b**2 = c**2
# therefore (a + b) ** 2 < c**2

def find():
    for a in range(1, 999):
        for b in range(1, 999):
            c = 1000 - a - b
            if is_pythagorean_triplet(a, b, c):
                return a, b, c


a, b, c = find()
print(a, b, c)
print(a * b * c)
