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

for j in range(0,6):
    for k in range(0,6):
        answers.append(brahmagupta([answers[j],answers[k]]))
        assert answers[-1][0] != 756872327473.0

print(answers)
