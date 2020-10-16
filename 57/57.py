x = [1,2]
winners = 0
for z in range(0,1000):
    x = [x[1],x[0]+2*x[1]]
    winners += 1*(len(str(x[0]+x[1])) > len(str(x[1])))
print(winners)
