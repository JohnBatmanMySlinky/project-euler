# 1-9 --> 9
# 10-99 --> 180
# 100-999 --> 2700
# 1000-9999 --> 36000
# 10000-99999 --> 450000
# 100000-999999 --> 5400000
# the above facts and some interpolating should work nicely

import numpy as np

index = np.cumsum([0] + [9*x*10**(x-1) for x in range(1,7)])
ds = [10**x for x in range(0,7)]

answer = []
for each in ds:
    pos = 7-sum(each < index)
    lookup = each - index[pos-1]
    answer.append(int(''.join([str(x) for x in range(10**(pos-1),10**pos)])[lookup-1]))

print(np.prod(answer))
