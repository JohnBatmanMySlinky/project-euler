import sys
sys.path.append('/home/jmyslinski/personnal/project-euler/utils')
from utils import is_prime, Sieve_of_Eratosthenes
from itertools import combinations


# any 2 out of 5 concatnate (both ways) to be prime
# min(sum of 5) == ?

upper_bound = 10000

primes = Sieve_of_Eratosthenes(upper_bound)

def concat_prime_test(a,b):
    return(is_prime(int(str(a)+str(b)))&is_prime(int(str(b)+str(a))))

for a in primes:
    for b in primes:
        if concat_prime_test(a,b):
            for c in primes:
                if concat_prime_test(a,c):
                    if concat_prime_test(b,c):
                        for d in primes:
                            if concat_prime_test(a,d):
                                if concat_prime_test(b,d):
                                    if concat_prime_test(c,d):
                                        for e in primes:
                                            if concat_prime_test(a,e):
                                                if concat_prime_test(b,e):
                                                    if concat_prime_test(c,e):
                                                        if concat_prime_test(d,e):
                                                            print(','.join([str(x) for x in [a,b,c,d,e]]))
                                                            print(a+b+c+d+e)
                                                            assert 5 == 6
