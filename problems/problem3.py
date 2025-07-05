# Largest Prime Factor
import math
from lib.prime import is_prime


N = 600_851_475_143
answer = None
for n in range(math.floor(math.sqrt(N)), 2, -1):
    if (N % n) == 0 and is_prime(n):
        answer = n
        break
print(answer)
