import math

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


def is_permutation(j,k):
    return(sorted([int(x) for x in str(j)]) == sorted([int(y) for y in str(k)]))

def is_palindrome(x):
    if ~isinstance(x, str):
        x = str(x)
    cut = int(len(x)/2)
    return(x[:cut] == ''.join(list(reversed(x[-cut:]))))

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
    res = []
    # iterate over all even numbers first.
    while n % 2 == 0:
        res.append(2)
        n //= 2
    # try odd numbers up to sqrt(n)
    limit = math.sqrt(n+1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n //= i
            limit = math.sqrt(n+i)
        else:
            i += 2
    if n != 1:
        res.append(n)
    return res


def totient(n):
    for each in list(set(prime_factorization(n))):
        n *= (1-1.0/each)
    return(int(n))

def GCD(a,b):
    while b:
        a, b = b, a%b
    return(a)

def farey_sequence_length(n):
    l, a, b, c, d = 0, 0, 1, 1, n
    while (c<=n):
        p = int((n+b)/d)*c-a
        q = int((n+b)/d)*d-b
        a, b, c, d = c, d, p, q
        l += 1
    return(l+1)

if __name__ == "__main__":
    print((Sieve_of_Eratosthenes(50)))
