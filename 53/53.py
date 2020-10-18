fact_dict = {1:1}
for x in range(2,101):
    fact_dict[x] = fact_dict[x-1] * x

def nCk(n,k):
    return(fact_dict[n]/(fact_dict[k] * fact_dict[n-k]))

answers = 0
for n in range(1, 101):
    for k in range(4, int(n/2)):
        if nCk(n,k) > 10**6:
            answers += 2*(int(n/2) - k)+ 1 + 1*(n%2!=0)
            break
print(answers)
