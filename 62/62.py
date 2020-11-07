# 5073^3

import pdb

def is_permuation(x,y):
    return(sorted([int(a) for a in str(x)]) == sorted([int(b) for b in str(y)]))

cube_list = [x**3 for x in range(5000, 10000)]

def recurse(ls, J, a, p):
    ls = [x for x in ls if x > a]
    for each in ls:
        if is_permuation(a,each):
            p += 1
            if p == 5:
                print(J)
                print(J**(1.0/3))
                assert 5 == 6
            else:
                recurse(ls, J, each, p)
    return(False)

for a in cube_list:
    recurse(cube_list, a,  a, 1)







# for a in cube_list:
#     print(a)
#     cube_list.remove(a)
#     p = 1
#     for b in cube_list:
#         if is_permuation(a,p):
#             p += 1
#             cube_list.remove(b)
#
#         if p == 3:
#             print('yeehaw')
#             print(a)
#             assert 5 == 6
