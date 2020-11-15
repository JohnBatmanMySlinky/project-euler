import wget
import pandas as pd

# wget.download('https://projecteuler.net/project/resources/p067_triangle.txt')

# create left shifted triangle
triangle = []
f = open('p067_triangle.txt')
for i,r in enumerate(f):
    triangle.append([int(x) for x in r.strip().split(' ')] + [0]*(99-i))

# given left shifted triangle, return max path sum
def MaxPathSum(t):
    for i in range(len(t)-2,-1,-1):     # iterate through rows, bottom up
        for j in range(i, -1, -1):      # iterate through rows, right --> left
            t[i][j] += max(t[i+1][j+1], t[i+1][j])   # update with largest leaf
    return(t[0][0])

print(MaxPathSum(triangle))
