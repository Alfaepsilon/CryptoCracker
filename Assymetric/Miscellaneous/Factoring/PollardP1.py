from .. import cc_powmod
from .. import cc_gcd


def PollardP1(N):
    for a in (2, 50):
        for j in range(2, 50):
            a = cc_powmod(N, a, j)
            d = cc_gcd(N, a - 1)
            if d > 1 and d < N:
                print(j)
                return d
            if d == N:
                break

# p = PollardP1()
# print(p)
# q = N // p
# print(p, q)