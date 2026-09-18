from .. import cc_powmod
from .. import cc_gcd
import math


def SquareDiff1(N):
    i = 1
    while True:
        if math.isqrt(N + i*i) * math.isqrt(N + i*i) == N + i*i:
            p = math.isqrt(N + i*i) - i
            q = math.isqrt(N + i*i) + i
            print(f"p: {p}, q: {q}")
            break
        else:
            i += 1

SquareDiff1(64213)