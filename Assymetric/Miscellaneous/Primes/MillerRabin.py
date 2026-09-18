from CryptoCracker.Assymetric.Miscellaneous import cc_powmod
from CryptoCracker.Assymetric.Miscellaneous import cc_gcd
def MillerRabin(X):
    witnesses = [2, 3, 5, 7, 11, 13]  # Can try more witnesses if desired

    # Small primes
    if X in witnesses:
        return False

    # Even numbers are composite
    if X % 2 == 0:
        return True

    q = X - 1
    Xphi = X - 1  # -1 mod X

    k = 0
    while q % 2 == 0:
        q //= 2
        k += 1

    for a in witnesses:
        if X < a:
            break

        gcd = cc_gcd(X, a)

        # If gcd(a, X) > 1, then X is composite
        if gcd > 1 and gcd != X:
            return True

        modX = cc_powmod(X, a, q)

        if modX == 1:
            continue
        if modX == Xphi:
            continue

        flag = False
        for _ in range(k):
            modX = cc_powmod(X, modX, 2)
            if modX == Xphi:
                flag = True
                break

        if flag:
            continue

        return True

    return False