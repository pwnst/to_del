def fack(n):
	if n == 1:
		return n
	else:
		return n * fack(n -1)

print fack(100)