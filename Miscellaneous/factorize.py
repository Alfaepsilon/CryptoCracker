from math import floor
import gmpy2
def factorize(p):
    factors = []
    i = 2
    while i < floor(gmpy2.sqrt(p)):
        if p % i == 0:
            factors.append(i)
        while(p % i == 0):
            p = p // i
        i += 1
    factors.append(p)
    return factors