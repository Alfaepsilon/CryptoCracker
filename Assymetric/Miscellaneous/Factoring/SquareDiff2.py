from .. import cc_powmod
from .. import cc_gcd
import math


def SquareDiff1(N, k, b):
    while True:
        if math.isqrt(k*N + b*b) * math.isqrt(k*N + b*b) == k*N + b*b:
            p = math.isqrt(k*N + b*b) - b
            q = math.isqrt(k*N + b*b) + b
            p = cc_gcd(N, p)
            q = cc_gcd(N, q)
            print(f"p: {p}, q: {q}")
            break
        else:
            b += 1

SquareDiff1(2510839, 21, 90)