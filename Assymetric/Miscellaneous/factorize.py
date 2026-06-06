from math import floor, sqrt
def factorize(p):
    factors = []
    i = 2
    while i < floor(sqrt(p)):
        if p % i == 0:
            factors.append(i)
        while(p % i == 0):
            p = p // i
        i += 1
    factors.append(p)
    return factors