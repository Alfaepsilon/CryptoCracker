from cc_powmod import cc_powmod
from cc_gcd import cc_gcd
from math import *
def MillerRabin(n, a):
    if n % 2 == 0:
        return 1
    if cc_gcd(a, n) != 1 and cc_gcd(a, n) != n:
        return 1
    q = n - 1
    k = 0
    while q % 2 == 0:
        q = q / 2
        k = k + 1
    a = cc_powmod(a, q, n)
    if a % n == 1:
        return 0
    for i in range(0, k - 1):
        if a % n == n - 1:
            return 0
        a = cc_powmod(a, 2, n)
    return 1
