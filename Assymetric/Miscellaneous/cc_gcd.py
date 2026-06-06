def cc_gcd(A, n):
	while (A != n):
		if A > n:
			A = A - n
		else:
			n = n - A
	return A