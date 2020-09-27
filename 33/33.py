

# exactly four
# non-trivial
# less than one
# 2 digit in num and denom
def do_split(z):
    return(int(str(z)[0]), int(str(z)[1]))


answer = 1.0
for x in range(11,100):
    for y in range(11,100):
        a, b = do_split(x)
        c, d = do_split(y)

        if (x%10 == 0) | (y%10 == 0):
            continue

        if (b==c) & (a*1.0/d == x*1.0/y) * (b != d):
            print(str(x)+ ' ' + str(y))
            answer = answer * x / y

print(1/answer)
