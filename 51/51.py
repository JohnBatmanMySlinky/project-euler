import sys
sys.path.append('../utils')
sys.path.append('utils')
from utils import is_prime, Sieve_of_Eratosthenes
from itertools import combinations, permutations

primes = Sieve_of_Eratosthenes(1000000)

primes = [x for x in primes if x > 100000]
# so we know that the the solution is a family of 8
# so it has to have a 0, 1 or 2.
# we don't know how many of them tho...


# guess n check with d and c ranges
for d in [6]:
    for c in range(3,d):
        print(c)
        combos = combinations([x for x in range(d)],c)
        for each in combos:
            print(each)
            for p in primes:
                if (sum([1*(str(p)[x]=='0') for x in each]) == c) | (sum([1*(str(p)[x]=='1') for x in each]) == c) | (sum([1*(str(p)[x]=='2') for x in each]) == c):
                    test = 0
                    for t in range(0,10):
                        to_be_tested = int(''.join([str(p)[z] if z not in each else str(t) for z in range(d)]))
                        test += 1*is_prime(to_be_tested)*(to_be_tested >= p)
                    if test == 8:
                        print(p)
                        assert 5 == 6
