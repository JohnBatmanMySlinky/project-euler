from math import factorial


fact_dict = {}
fact_dict[9] = factorial(9)
for x in reversed(range(0,9)):
    fact_dict[x] = fact_dict[x+1]/(x+1)


upper = 50000
answer = 0
for each in range(3,upper):
    if sum([fact_dict[int(x)] for x in list(str(each))]) == each:
        answer = answer + each
        print(each)


print('answer --> ' + str(answer))
