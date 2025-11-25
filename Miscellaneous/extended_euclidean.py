def exeucalgo(a, b, inverse):
	u = 1
	x = 0
	g = a
	if (b == 0):
		return [g, u, 0]
	y = b
	while (y > 0):
		t = g % y
		q = g // y
		s = u - (q * x)
		u = x
		g = y
		x = s
		y = t
	v = (g - a * u) // b
	while (u < 0):
		u = u + b//g
		v = v - a//g
	if(inverse == 1):
		return u
	return [g, u, v]