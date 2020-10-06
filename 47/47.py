import sys
sys.path.append('../utils')
from utils import is_prime, prime_factorization

for x in range(10,200000):
    a = prime_factorization(x)
    if len(set(a)) == 4:
        b = prime_factorization(x+1)
        if len(set(b)) == 4:
            c = prime_factorization(x+2)
            if len(set(c)) == 4:
                d = prime_factorization(x+3)
                if len(set(d)) == 4:
                    print(str(x) + ': [%s]' % ', '.join(map(str, a)))
                    print(str(x+1) + ': [%s]' % ', '.join(map(str, b)))
                    print(str(x+2) + ': [%s]' % ', '.join(map(str, c)))
                    print(str(x+3) + ': [%s]' % ', '.join(map(str, d)))
                    assert 5 == 6

