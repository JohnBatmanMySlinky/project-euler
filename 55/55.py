# XY + YX --> palindrome
# XY + YX --> ABC + CBA --> palindrome : two iterations
# 196 never produces a palindrome --> lychrel number
# N < 10,000 if >= 50 iterations then it's a lychrel
# how many lychrel below 10,000?
import sys
sys.path.append('../utils')
sys.path.append('utils')
from utils import is_palindrome

def rev_it(x):
    return(int(''.join(list(reversed([y for y in str(x)])))))

# could be improved with caching.
# if you end up on a number you know goes to palindrome, just stop becuse it ain't lychrel

upper = 10000
lychrel = 0
for x in range(1, 10000):
    iter = 0
    x_orig = x
    while (iter < 50):
        iter += 1
        x = x + rev_it(x)
        if is_palindrome(x) & (len(str(x)) > 2):
            break
    if iter == 50:
        lychrel += 1
        print(str(x_orig) + ' --> ' + str(x) + ' in ' + str(iter) + ' iterations.')
        print('-----------------------')
print('there are ' + str(lychrel) + ' lychrel #s below ' + str(upper))
