# min(odd composite) st != a prime + 2 * n ** 2


# generate some odd composite numbers
    # odd * odd = odd composite

# sqrt((odd composite - a prime)/2) != int
import sys
sys.path.append('../utils')
from utils import Sieve_of_Eratosthenes


upper = 50
print(Sieve_of_Eratosthenes(50))
