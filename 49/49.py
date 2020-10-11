
# arithmetic sequence
# each term is prime
# all numbers are permutations
# numbers are 4 digits




import sys
sys.path.append('../utils')
from utils import is_prime, Sieve_of_Eratosthenes
from itertools import combinations

def is_permutation(j,k):
    return(sorted([int(x) for x in str(j)]) == sorted([int(y) for y in str(k)]))

def has_arith_seq(ls):
    combos = combinations(''.join([str(x) for x in range(0,len(ls))]),3)
    for c in combos:
        test = [int(x) for x in c]
        if ls[test[1]] - ls[test[0]] == ls[test[2]] - ls[test[1]]:
            return([ls[test[z]] for z in range(0,3)])
    return([0,0,0])


primes = Sieve_of_Eratosthenes(10000)
primes = [x for x in primes if x > 1487]

for p in primes:
    permutations = [x for x in primes if is_permutation(x,p)]
    if len(permutations) >3:
        answer = has_arith_seq(permutations)
        if sum(answer) > 0 :
            print(''.join([str(x) for x in answer]))
            assert 5 == 6
            


