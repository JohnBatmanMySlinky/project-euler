# it's like #76 but not
# https://en.wikipedia.org/wiki/Partition_(number_theory) points you to
# https://en.wikipedia.org/wiki/Pentagonal_number_theorem
# which gives you a generating function for p(n)
# how this generating function relates to pentagonal numbers is fucking magic
# p(n) = sum k<>0 -1^(k-1) * p(n-g_k)
# where g_k is the kth pentagonal number
# p(n)=0 for n<0
# so p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) ....
# idk if i'm dumb but that -1^(k-1) was not getting me the alternate pairs of signs i needed, as written

import math

# GENERALIZED PENTAGONAL
def pentagonal(N):
    positive = [int((3*x**2-x)/2) for x in range(1,N+1)]
    negative = [int((3*x**2+x)/2) for x in range(1,N+1)]
    return sorted(positive + negative)

def solve(DIV):
    # initialize with p(0) = 1
    partitions = [1]

    # so start iterations at 1
    n = 1

    # sqrt is just a fuckin guess here
    pent = pentagonal(int(math.sqrt(DIV)))

    # while biggest element of partitions is less than our threshold
    while True:
        # p(n) recursive generating function
        p = 0
        k = 0
        while n-pent[k] >= 0:
            p += -(-1)**(k//2-1) * partitions[n-pent[k]]
            p %= DIV
            k += 1
        partitions.append(p)
        n += 1

        if partitions[-1] % DIV == 0:
            return partitions

answer = solve(1000000)

print(len(answer)-1)
