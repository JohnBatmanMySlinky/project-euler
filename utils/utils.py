def is_prime(n):
    if n <= 3:
        return(n > 1)
    elif (n%2 == 0) | (n%3 == 0):
        return(False)

    i = 5
    while i*i <= n:
        if (n%i == 0) | (n%(i+2) == 0):
            return(False)
        i = i + 6

    return(True)

def is_pandigital(x):
    if ~isinstance(x, str):
        x = str(x)
    return((len(set(x)) == 9) & (x.find('0') == -1))


def Sieve_of_Eratosthenes(n):
    answer = [True for x in range(n+1)]
    answer[0] = False
    answer[1] = False
    x = 2
    while (x*x <= n):
        if answer[x]:
            for i in range(x*2,n+1,x):
                answer[i] = False
        x += 1

    winners = []
    for z in range(n+1):
        if answer[z]:
            winners.append(z)
    return(winners)

def prime_factorization(n):
    i = 2
    factors = []
    if ~is_prime(n):
        while i < n:
            if n % i == 0:
                n = n / i
                factors.append(int(i))
                i = 1
            i = i + 1
    factors.append(int(n))
    return(factors)


if __name__ == "__main__":
    print((Sieve_of_Eratosthenes(50)))
