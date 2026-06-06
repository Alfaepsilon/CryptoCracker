from CryptoCracker.Assymetric.Miscellaneous import cc_powmod
from CryptoCracker.Assymetric.Miscellaneous import cc_gcd
def MillerRabin(n):
    composite = False
    flag = 0
    if n % 2 == 0:
        return True
    for a in [2, 3, 5, 7, 11]: #Could try more Miller-Rabin witnesses but should be enough
        if cc_gcd(a, n) > 1 and cc_gcd(a, n) != n:
            return True
        q = n - 1
        k = 0
        while q % 2 == 0:
            q = q / 2
            k = k + 1
        a = cc_powmod(n, a, q)
        if a % n == 1:
            composite = 0
            continue
        for i in range(0, k - 1):
            if a % n == n - 1:
                flag = 1
                break
            a = cc_powmod(n, a, 2)
        if(flag == 1):
            continue
        composite = True
        return composite
