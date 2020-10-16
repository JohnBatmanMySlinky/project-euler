# loop through digit lengths
# loop through ints where nchar(int*6) == nchar(int)
# i guess that's it?
def same_digits(x,y):
    return(sorted([int(a) for a in str(x)]) == sorted([int(b) for b in str(y)]))

arg = 6

for l in range(1,7):
    for x in range(1, int(10**l / arg)):
        if all([same_digits(x,x*y) for y in range(2,arg+1)]):
            print(x)
            assert 5 == 6