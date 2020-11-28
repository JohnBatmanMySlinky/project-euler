# reduced fractions
# denominator <= 1,000,000
# what is the largest fraction < 3/7

# trick is for every d the best n is
# trunc(d * 3 / 7)
# then we need to find the n such that n/d is max

answer = [1,3]
for d in range(1,1000000):
    if d != 7:
        n = d * 3 / 7           # using ints to will trunc naturally
        better_sol_check = 1.0 * n / d > 1.0 * answer[0] / answer[1]
        not_mult_of_check = (n % 3 != 0) | (d % 7 != 0)
        if better_sol_check & not_mult_of_check:
            answer[0] = n
            answer[1] = d
print(answer)
