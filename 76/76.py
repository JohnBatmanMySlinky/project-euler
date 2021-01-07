#Project Euler Problem 76

N = 100
counter = [1] + [0]*N

for x in range(1,N):
    for y in range(x, N+1):
        counter[y] += counter[y-x]
print(counter[N])
