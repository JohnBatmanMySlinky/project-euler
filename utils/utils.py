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
    answer = range(1,n+1)
    for x in range(1,int(n**0.5)+1):
        print(x)



if __name__ == "__main__":
    print('ok now what')
