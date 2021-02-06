# 10 can be written as a sum of primes 5 ways,
# what is the first number that can be written as a sum of primes  > 5000 ways?

import sys
sys.path.append('../utils')
sys.path.append('utils')
from utils import Sieve_of_Eratosthenes


def solve(start, thresh):
    N = start
    while True:
        primes = Sieve_of_Eratosthenes(N)
        counter = [1] + [0]*N
        for x in range(0,len(primes)):
            for y in range(primes[x], N+1):
                counter[y] += counter[y-primes[x]]
        if counter[-1] < thresh:
            N += 1
        else:
            return N

print(solve(10,5000))

