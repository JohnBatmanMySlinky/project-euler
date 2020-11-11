# https://projecteuler.net/problem=64
# https://en.wikipedia.org/wiki/Pell%27s_equation#The_smallest_solution_of_Pell_equations
# https://en.wikipedia.org/wiki/Continued_fraction#Infinite_continued_fractions_and_convergents

# need to translate our series of a's from # 64 into h_i / k_i (Pell wiki)
# formula for a --> h/k in continued fraction wikipedia
# x**2 + D * y**2 = 1
# where a_n is continued fraction expansion from sqrt D
# h_n = a_n * h_n-1 + h_n-2
# k_n = a_n * k_n-1 + k_n-2
# h_n, k_n are solutions for x, y
# h/k can be initialized with 0/1 and 1/0

def CF(X):
    n = int(X**.5)
    d = X-n**2
    cf = []
    cf.append(n)
    i = 0
    while (cf[i] != 2*cf[0]) and (int((X**.5 + n)/d) != 0):
        i += 1
        cf.append(int((X**.5 + n)/d))
        n = d*cf[i]-n
        d = (X-n**2)/d
    return(cf)

answer = {}
scale = 20
for D in range(2,1001):
    if D**.5 != int(D**.5):
        h = [0,1]
        k = [1,0]
        cf = CF(D)
        cf = [cf[0]] + cf[1:] * scale
        tst = False
        i = 0
        while tst == False:
            h.append(cf[i] * h[i+1] + h[i])
            k.append(cf[i] * k[i+1] + k[i])
            tst = (h[i+2]**2 - D * (k[i+2] ** 2)) == 1
            i += 1
        answer[D] = h[i+1]
max_val = max(answer.values())
print([k for k,v in answer.items() if v == max_val])
