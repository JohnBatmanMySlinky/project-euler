def dec_to_bin(x):
    return int(bin(x)[2:])


def is_palindrome(y):
    y = str(y)
    if len(y)>1:
        left = len(y)/2
        return(y[:left] == y[-left:][::-1])
    else:
        return(True)

def create_palindromes(n):
    palindromes = []
    #1-9
    # 1-9 with 1-9 on left
    # 1-9 with 1-9 on left & right
    # 

create_palindromes(3)


# answer = 0
# for z in range(0,1000001):
#     dec_test = is_palindrome(z)
#     bin_test = is_palindrome(dec_to_bin(z))
#     if dec_test & bin_test:
#         answer = answer + z
#         print(str(z) + ' ' + str(dec_to_bin(z)))
#
# print('answer --> ' + str(answer))
