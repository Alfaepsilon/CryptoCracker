from math import ceil, sqrt
from CryptoCracker.Assymetric.Miscellaneous import exeucalgo
from CryptoCracker.Assymetric.Miscellaneous import cc_powmod
def shanks(val, p, g, N):
	#print("Shanks!")
	inverse = exeucalgo(g, p, 1)
	n = int(ceil(sqrt(N)))
	l1 = {cc_powmod(p, g, i): i for i in range(n)}
	for i in range(n):
		j = (val * cc_powmod(p, inverse, i * n)) % p
		if(j in l1):
			return l1[j] + i*n