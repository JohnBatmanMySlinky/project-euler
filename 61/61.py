# set of 6 4 digit numbers
# last two digits of x_i == first two digits of x_i+1 (including the last --> first)
# one is triangle, one is square, one is pentagonal etc...

# (-b +/- sqrt(b^2-4ac))/2a
import time
start = time.time()
func_dict = {
    'triangle': [0.5, 0.5, 0],
    'square': [1, 0, 0],
    'pentagonal': [1.5, -.5, 0],
    'hexagonal': [2, -1, 0],
    'heptagonal': [2.5, -1.5, 0],
    'octagonal': [3, -2, 0]
}

def is_a_func(x, func):
    a = func_dict[func][0]
    b = func_dict[func][1]
    c = func_dict[func][2] - x
    test = (-b+(b**2-4*a*c)**0.5)/(2*a)
    return([int(test) == test, test])


space = sorted(list(set([x for x in range(1000, 10000) for y in func_dict.keys() if is_a_func(x,y)[0]])))

i = 0
for a in space:
    for b in [z for z in space if (str(z)[:2] == str(a)[-2:]) & (z not in [a])]:
        for c in [z for z in space if (str(z)[:2] == str(b)[-2:]) & (z not in [a,b])]:
            for d in [z for z in space if (str(z)[:2] == str(c)[-2:]) & (z not in [a,b,c])]:
                for e in [z for z in space if (str(z)[:2] == str(d)[-2:]) & (z not in [a,b,c,d])]:
                    for f in [z for z in space if (str(z)[:2] == str(e)[-2:]) & (z not in [a,b,c,d,e]) & (str(z)[-2:] == str(a)[:2])]:
                        answer = [[x,y] for x in func_dict.keys() for y in [a,b,c,d,e,f] if is_a_func(y,x)[0]]


                        check_list = []
                        for each in answer:
                            check_list.append(each[0])
                        #make sure each function is at least used once
                        if len(set(check_list))==6:
                            # figure out which function is duplicated
                            dupe = list(set([x for x in check_list if check_list.count(x)>1]))

                            # solution is where a duplicate function has a duplicate numbers
                            # this gets numbers associated with dupe functions
                            check_for = []
                            for each in answer:
                                if each[0] == dupe[0]:
                                    check_for.append(each[1])

                            # all values in answer
                            vals = []
                            for each in answer:
                                vals.append(each[1])

                            # for each value of a duplicate check for duplicate values
                            for each in check_for:
                                if vals.count(each) >1:
                                    print(a+b+c+d+e+f)
                                    print(time.time()-start)
                                    assert 5 == 6







                                #
                                # print(a+b+c+d+e+f)
                                # assert 5 == 6
