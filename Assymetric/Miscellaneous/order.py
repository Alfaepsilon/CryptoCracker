#from sympy import primefactors
from .factorize import factorize
from .cc_powmod import cc_powmod
def order(g, p):
    factors = factorize(p)
    modulo = p + 1
    for factor in factors:
        while cc_powmod(modulo, g, p // factor) == 1:
            p = p // factor
    order = p
    print(order)
    return order