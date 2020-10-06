# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

# HA! this is so clever!
# N mod 10 will return last 10 digits of N! --> mind is like kinda blown rn

# so then this becomes useful LOL
# (A * B) mod C = (A mod C * B mod C) mod C

upper = 1000
digits = 10**10

answer = 1
for x in range(2,upper+1):
    z = x
    for y in range(1, x):
        z = ((z%digits) * (x%digits))%digits
    answer = answer + z
print(answer%digits)

