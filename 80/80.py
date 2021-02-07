from decimal import *
import re

N = 100
prec = 100

def sum_decimals(x, prec):
    return(sum([int(x) for x in str(x).replace('.', '')[:prec]]))

# to avoid rounding last digit
getcontext().prec = int(N*1.05)
answer = 0
perf_sq = [x**2 for x in range(1,int(N**0.5)+1)]
for x in range(2,100):
    if x not in perf_sq:
        y = Decimal(x).sqrt()
        answer += sum_decimals(y,100)
print(answer)