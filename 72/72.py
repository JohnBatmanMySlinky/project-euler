import sys
sys.path.append('../utils')
sys.path.append('utils')
from utils import totient

# how many reduced fractions are there for d <= 1,000,000
# when d <= 8, there are 21s

N = 10**6
answer = 0
for n in range(2,N+1):
    answer += totient(n)
print(answer)
