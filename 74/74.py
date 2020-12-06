# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

# brute force? ok!
import sys
sys.path.append('../utils')
sys.path.append('utils')
from utils import factorial

fact_dict = {0:1}
for k in range(1,10):
    fact_dict[k] = factorial(k)

def digit_wise_factorial(n):
    return(sum([fact_dict[int(x)] for x in str(n)]))

stopping_criteria = {}
stopping_criteria[169] = [363601, 1454]
stopping_criteria[363601] = [1454, 169]
stopping_criteria[1454] = [363601, 169]
stopping_criteria[871] = [45361]
stopping_criteria[45361] = [871]
stopping_criteria[872] = [45362]
stopping_criteria[45362] = [872]

chain_of_60 = 0
for x in range(10,1000000):
    if x % 10000 == 0:
        print('workig on: ' + str(x))
    y = x
    chain = set()
    while y not in chain:
        chain.add(y)
        y = digit_wise_factorial(y)
        if y in stopping_criteria.keys():
            chain.add(y)
            chain.update(stopping_criteria[y])
            break
    if len(chain) == 60:
        chain_of_60 += 1
print('this many chains have length 60: ' + str(chain_of_60))
