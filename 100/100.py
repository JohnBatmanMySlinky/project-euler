# min (x+y) such that
# x + y >= 10^12
# x / (x+y) * (x-1) / (x+y-1) == .5
# x and y are natural numbers

# I tried using some algebra on the above equality
# i could determine the line that the answer lied on
# and I could brute force search for integer solutions on that line but
# the answer lied too far above the 10**12 threshold for my code to run in
# a reasonable amount of time

# so
# today we learn about diophantine equations
# i did a decent amount of reverse engineering and using sympy but
# I learned alot so that's nice

from sympy.solvers.diophantine import transformation_to_DN, diophantine, diop_DN, find_DN
from sympy import *

x, y = symbols("x, y", integer = True)
A, B = transformation_to_DN(x**2 -2*x*y - y**2 - x + y)
D, N = find_DN(x**2 -2*x*y - y**2 - x + y)

def pell(y):
    return((8*y**2+1)**.5)

answers = []
y = 0
while len(answers) < 2:
    y += 1
    if pell(y).is_integer():
        answers.append([pell(y),y])

def brahmagupta(z):
    x_tmp = z[0][0] * z[1][0] + 8 * z[0][1] * z[1][1]
    y_tmp = z[0][0] * z[1][1] + z[0][1] * z[1][0]
    return([x_tmp, y_tmp])


for i in range(0,100):
    answers.append(brahmagupta([answers[0],answers[i]]))

pls = [A*Matrix(x)+B for x in answers]
for each in pls:
    if each[0]+each[1]>10**12:
        print(each[0])
        break
