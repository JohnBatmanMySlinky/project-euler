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

# transform diophantine eq into a pell eq
    # via find_DN
# find 2 initial solutions
    # via brute force
# transform those two solutions into many solutions
    # via brahmagupta
# transform pell solutions back to diophatine
    # via A & B from transformation_to_DN
# find first solution pair that red+blue > 10**12

from sympy.solvers.diophantine import transformation_to_DN, diophantine, find_DN
from sympy import *

x, y = symbols("x, y", integer = True)
s = diophantine(x**2 -2*x*y - y**2 - x + y)
A, B = transformation_to_DN(s)
D, N = find_DN(s)

def pell(y, D, N):
    return((D*y**2+N)**.5)

answers = []
y = 0
while len(answers) < 2:
    y += 1
    if pell(y).is_integer():
        answers.append([pell(y, D, N), y])

def brahmagupta(z):
    x_tmp = z[0][0] * z[1][0] + 8 * z[0][1] * z[1][1]
    y_tmp = z[0][0] * z[1][1] + z[0][1] * z[1][0]
    return([x_tmp, y_tmp])


for i in range(0,100):
    print(str(i) + 'th solution')
    answers.append(brahmagupta([answers[0],answers[i]]))
    pls = A*Matrix(answers[-1]) + B
    if pls[0]+pls[1]>10**12:
        print(pls[0])
        break
