# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 12,000?

# Farey sequences!
import sys
sys.path.append('../utils')
sys.path.append('utils')
from utils import farey_sequence_length

def farey_sequence_length(n, lower, upper):
    l, a, b, c, d = 0, 0, 1, 1, n
    while (c<=n):
        p = int((n+b)/d)*c-a
        q = int((n+b)/d)*d-b
        a, b, c, d = c, d, p, q
        if lower < 1.0 * p / q < upper:
            l += 1
        if 1.0 * p / q > upper:
            break
    return(l)

print(farey_sequence_length(12000, 1.0/3, 1.0/2))
