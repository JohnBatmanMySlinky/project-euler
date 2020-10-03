# 192 * (1,2,3) = 192, 384, 576 = 192384576 --> pandigital
# x * (1,2,n)==max(pandigital)

# 987654321 is the max 9-pandigital
# how do we get a 9 there --> has to start with 9

# 90 * (1,2,3) = (90, 180, 270, 360) --> never end with 9 digits
# 900 * (1,2,3) = (900, 1800, 2700) --> never end with 9 digits
# 9000 * (1,2) = (9000, 18000) --> gets us 9

# 9876 * (1,2) = (9876, 19752) --> gets us 9
# 9123 * (1,2) = (9123, 18246) --> gets us 9

def is_pandigital(x):
    return((len(set(x)) == 9) & (x.find('0') == -1))

def concatenate_product(left, z):
    right = range(1,z+1)
    return(''.join([str(left*r) for r in right]))

answers = []
for i in range(9123, 9876+1):
    concat_prod = concatenate_product(i, 2)
    if is_pandigital(concat_prod):
        answers.append(concat_prod)


print(max(answers))
