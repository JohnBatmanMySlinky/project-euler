# https://www.mathstat.dal.ca/FQ/Papers1/42-2/quartrippon02_2004.pdf
# this paper cites the fact that you when a_n = 2a_0 you have identified the period length

# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html
# this site spells things out more explicitly


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

answer = 0
for z in range(2,10001):
    if int(z**.5) != z**.5:
        if (len(CF(z))-1) % 2 != 0:
            answer += 1
print(answer)
