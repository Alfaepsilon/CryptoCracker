def cc_powmod(modulo, base, exponent):
	a = base
	b = 1
	while (exponent > 0):
		if (exponent % 2 == 1):
			b = (b * a) % modulo
		a = (a * a) % modulo
		exponent = exponent // 2
	return b