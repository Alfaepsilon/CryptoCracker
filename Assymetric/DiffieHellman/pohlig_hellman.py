from CryptoCracker.Assymetric.Miscellaneous import cc_powmod
from .shanks import shanks
from CryptoCracker.Assymetric.Miscellaneous import chinese
def pohlig(val, factors, g, p, N):
    print("Pohlig")
    y = []
    mod = []
    for factor in factors:
        order_gi = N
        qe = 1
        while order_gi % factor == 0:
            order_gi = order_gi // factor
            qe = qe * factor
        gi = cc_powmod(p, g, order_gi) #pow(g, order_gi, p) 
        hi = cc_powmod(p, val, order_gi) #pow(val, order_gi, p)
        yi = shanks(hi, p, gi, qe)
        y.append(yi)
        mod.append(qe)
    return chinese(y, mod)