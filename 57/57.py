x = [1,2]; i = 0; winners = 0
while i < 999:
    x = [x[1],x[0]+2*x[1]]
    i += 1
    if len(str(x[0]+x[1])) > len(str(x[1])):
        winners += 1
print(winners)
