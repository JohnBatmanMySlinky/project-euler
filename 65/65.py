e = [[1], [2]] + [[1,1,x*2] for x in range(2,34)] + [[1]]
e = [y for x in e for y in x]

n = 100
for i,z in enumerate(reversed(e[:(n-1)])):
    if i == 0:
        x = [1,z]
    else:
        x = [x[1], x[0] + z*x[1]]
x = [x[0] + 2*x[1], x[1]]
print('answer = ' + str(sum([int(y) for y in str(x[0])])))
