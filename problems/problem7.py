from problems.lib.prime import sieve_of_eratosthenes


primes = sieve_of_eratosthenes(1_000_000)
print(primes[10000])
