# a^b  where a,b < 100, what is the max digital sum?

def dig_sum_inv(n):
    answer = []
    while n > 0:
        answer.append(min(9,n))
        n = n - min(9,n)
    return(int(''.join([str(x) for x in answer])))
