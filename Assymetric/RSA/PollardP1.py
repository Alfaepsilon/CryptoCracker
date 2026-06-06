from CryptoCracker.Assymetric.Miscellaneous import cc_powmod
from CryptoCracker.Assymetric.Miscellaneous import cc_gcd

def pollardp1(N):
    for a in (2, 50):
        for j in range(2, 50):
            a = cc_powmod(N, a, j)
            d = cc_gcd(N, a - 1)
            if d > 1 and d < N:
                return d
            if d == N:
                break

N = 1739
p = pollardp1(N)
q = N // p
print(p, q)