import sys
sys.path.append('../utils')
sys.path.append('utils')
from utils import Sieve_of_Eratosthenes, is_permutation

# so now we have MIN n/totient & totient(n) = permutation n
# so want to min 1/PROD(1-1/p)
# so we want one big p
# but we know t(prime) = prime - 1, hence primes can't be a permutation
# so we know it can't be prime, hence denom can't have only one term
# so denom of totient formula must have 2 terms then!
# totient(n) = n * (1-1/p1) * (1-1/p2)
# p1 * p2 = n
# algebra gives totient(n) = (p1-1)*(p2-1) and we want primes as big as possible

# sqrt 10,000,000 ~ 3162
# so start guessing around there.
# best case would be 3161^2
u = 4000
l = 2000

search = Sieve_of_Eratosthenes(u)
search = [x for x in search if x > l]

# x & y loops aren't particularly efficient
answer = [0,10**7]
for x in reversed(search):
    for y in reversed(search):
        n = x*y
        if n < 10**7:
            t = (x-1)*(y-1)
            if is_permutation(t,n):
                if n*1.0/t < answer[1]:
                    answer[1] = n*1.0/t
                    answer[0] = n
print(answer)
