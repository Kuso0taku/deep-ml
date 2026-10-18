def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	c = []
	for i in range(len(a)):
		s = 0
		for j in range(len(b)):
			try: s += a[i][j]*b[j]
			except IndexError: return -1
		c.append(s)
	return c