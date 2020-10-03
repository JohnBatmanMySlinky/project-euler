from math import factorial

upper = 50000
fact_dict = {}

fact_dict[upper] = factorial(upper)
for x in reversed(range(0,upper)):
    fact_dict[x] = fact_dict[x+1]/(x+1)


# print(sum([(fact_dict[int(x)]) for x in list(str(145))]) == 145)

answer = 0
for each in range(3,upper):
    if sum([fact_dict[int(x)] for x in list(str(each))]) == each:
        answer = answer + each
        print(each)


print('answer --> ' + str(answer))
