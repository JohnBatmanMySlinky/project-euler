import sys
sys.path.append('../utils')
sys.path.append('utils')
from utils import Sieve_of_Eratosthenes

# thanks wikipedia
# we want to max
# n/(n * PROD (1-1/p))
# we want small denominator, min PROD(1-1/p)
# we want many small prime factors
# so the number below 1,000,000 with the most prime factors.
# will be the product of consecutive primes.
# no totients needed :)

search = Sieve_of_Eratosthenes(100)
i = 0
winner = 1
while winner <= 1000000:
    winner *= search[i]
    i += 1
print(winner/search[i-1])
