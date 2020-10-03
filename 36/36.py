def dec_to_bin(x):
    return int(bin(x)[2:])


def is_palindrome(y):
    y = str(y)
    if len(y)>1:
        left = len(y)/2
        return(y[:left] == y[-left:][::-1])
    else:
        return(True)

answer = 0
for z in range(1000000):
    dec_test = is_palindrome(z)
    bin_test = is_palindrome(dec_to_bin(z))
    if dec_test & bin_test:
        answer = answer + z
        print(str(z) + ' ' + str(dec_to_bin(z)))

print('answer --> ' + str(answer))
