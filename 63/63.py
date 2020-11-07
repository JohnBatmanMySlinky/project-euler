answer = 0
for y in range(1,100):
    x = 1
    while len(str(x**y)) <= y:
        if len(str(x**y)) == y:
            print(str(x) + '^' + str(y) + ' = ' + str(x**y))
            answer += 1
        x += 1
print('answer: ' + str(answer))
