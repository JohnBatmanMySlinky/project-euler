# 1
# +2 +2 +2 +2
# +4 +4 +4 +4 
# +6 +6 +6 +6
import sys
sys.path.append('../utils')
sys.path.append('utils')
from utils import is_prime


diag = 1
current = 1
prime = 0
x = 0
while True:
    x += 1
    for y in range(4):
        current += x*2
        diag += 1
        prime += 1*is_prime(current)
    if prime / diag < .1:
        print(x*2+1)
        break
