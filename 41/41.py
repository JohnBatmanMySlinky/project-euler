# What is the largest n-digit pandigital prime that exists?

# ideally I have a function that creates list of a n-digit pandigital numbers
# sort that list to be descending
# search for prime
# stop when done!
import sys
sys.path.append('../utils')
from utils import is_prime
from itertools import permutations

answers = []
for x in reversed(range(1,10)):
    universe = [y for y in reversed(range(1,x+1))]
    for z in permutations(universe, x):
        haha = int(''.join([str(a) for a in z]))
        if is_prime(haha):
            print(haha)
            break
    if is_prime(haha):
        break
