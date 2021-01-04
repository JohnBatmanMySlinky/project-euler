import sys
import math

# GCD of exponents doesn't work on the sample.
# is it as easy as just using the power rule?

dat = [x.strip().split(',') for x in sys.stdin]
dat = [[int(x[0]),int(x[1])] for x in dat]

# init
answer = [0,0]
for i,x in enumerate(dat):
	challenger = x[1] * math.log(x[0])
	if challenger > answer[0]:
		answer[0] = challenger
		answer[1] = i+1
print(answer[1])
