from extended_euclidean import exeucalgo
def chinese(y_list, mods):
	answers = y_list[0]
	mod = mods[0]
	for i in range(1, len(y_list)):
		y = ((y_list[i] - answers) * exeucalgo(mod, mods[i],  1)) % mods[i]
		x = (answers + mod * y) % (mod * mods[i])
		answers = x
		mod = (mod * mods[i])
	return x