# min(odd composite) st != a prime + 2 * n ** 2


# generate some odd composite numbers
    # odd * odd = odd composite

# sqrt((odd composite - a prime)/2) != int
import sys
sys.path.append('../utils')
from numpy import sqrt
from utils import Sieve_of_Eratosthenes


upper = 80
OC = [x*y for x in range(3,upper,2) for y in range(1,upper,2)]
OC.sort(reverse = True)
primes = Sieve_of_Eratosthenes(max(OC))

for x in [5777]:
    OK = False
    for y in [i for i in primes if i < x]:
        if sqrt((x-y)/2) == int(sqrt((x-y)/2)):
            OK = True
            break
    
    if OK == False:
        print("AH HAAAAA!")
        print('answer is ' + str(x))
        assert 5 == 6